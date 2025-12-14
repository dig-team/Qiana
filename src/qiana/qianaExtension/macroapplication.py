from typing import List, Dict, Tuple
import re

from qiana.qianaExtension.tptpUtils import isQuoted, quoteSymbol, get_special_function, next_quoted_var
from qiana.qianaExtension.tptpParsing import parseStruct

def applyMacros(text: str) -> str:
    """
    Take as input a text corresponding to many formulas and returns it with macros applied. Does not apply to comments (lines starting with %).
    """
    import re
    
    lines = text.split('\n')
    processed_lines = []
    
    for line in lines:
        # Skip comment lines (starting with %)
        if line.strip().startswith('%'):
            processed_lines.append(line)
            continue
        
        # Apply macro transformation to non-comment lines
        processed_line = _apply_macro_transformations(line)
        processed_lines.append(processed_line)
    
    return '\n'.join(processed_lines)

def _apply_macro_transformations(line: str) -> str:
    """
    Apply all macro transformations to a single line, working from inside out.
    Replaces all instance of a "bang macro" with its extended form, where a bang macro is of the form !name(x,y), name being an identifier, x being a term, and y being a formula.
    No verification is performed to ensure the nature of x and y.
    All instances of this form are replaced by ist(name(x), z), with z being the quotation of y.

    Nested macros are handled correctly by working from inside out. 
    However quantification accross levels of quotation is not supported.

    Examples:

    >>> _apply_macro_transformations("!believes(alice,p(c,d)))")
    "ist(believes(alice),q_p(q_c,q_d))"
    """
    import re
    
    # Pattern to match !name(args) where name is an identifier and args can contain nested parentheses
    # We need to work from inside out, so we'll use a loop until no more matches are found
    
    while True:
        # Find the rightmost !name(x,y) pattern
        pattern_match = _find_bang_pattern(line)
        if not pattern_match: 
            break # No more patterns to replace
        full_match, name, args = pattern_match
        
        # Split arguments by comma, but be careful with nested structures
        args_list = _split_arguments(args)
        
        if len(args_list) >= 2:
            # Take first argument as x, and the rest as y (joined by commas if multiple)
            x = args_list[0].strip()
            y = ', '.join(args_list[1:]).strip()
            
            replacement = f"ist({name}({x}), {_quote(y)})"
            line = line.replace(full_match, replacement)
        else:
            # If not enough arguments, leave as is and break to avoid infinite loop
            break
    
    return line

def _find_bang_pattern(line: str) -> Tuple[str, str, str] | None:
    """
    Find the rightmost pattern of the form !name(x,y) in the line.
    Returns a tuple of (full_match, name, args_list) or None if no match.

    Example:
        >>> "fof(test,axiom, !believes(alice,p(c,d))) i
        ("!believes(alice,p(c,d))", "believes", "alice,p(c,d)")
    """
    pattern = r'!([a-zA-Z_][a-zA-Z0-9_]*)'  # Match ! followed by an identifier.
    matches = list(re.finditer(pattern, line))
    if not matches: return None
    match =  matches[-1]  # Return the rightmost match

    name = match.group(1)
    start_args_index = match.end()
    paren_depth = 0
    for i in range(start_args_index, len(line)):
        char = line[i]
        if char == '(':
            paren_depth += 1
        elif char == ')':
            paren_depth -= 1
            if paren_depth == 0:
                end_args_index = i+1
                break
    else:
        raise ValueError(f"Unmatched parentheses after {name} in line: {line}")
    args_str = line[start_args_index:end_args_index][1:-1]

    full_match = line[match.start():end_args_index]
    return (full_match, name, args_str)

def _split_arguments(args_str: str) -> list:
    """
    Split arguments by comma, respecting nested parentheses.
    """
    if not args_str.strip():
        return []
    
    args = []
    current_arg = ""
    paren_depth = 0
    
    for char in args_str:
        if char == '(' :
            paren_depth += 1
            current_arg += char
        elif char == ')':
            paren_depth -= 1
            current_arg += char
        elif char == ',' and paren_depth == 0:
            args.append(current_arg.strip())
            current_arg = ""
        else:
            current_arg += char
    
    if current_arg.strip():
        args.append(current_arg.strip())
    
    return args

def _quote(text: str) -> str:
    """
    Take as input a formula or q_Term and returns it qiana quotation.
    """
    return _quote_from_struct(parseStruct(text), {})

def _formula_from_struct(struct : List[str | List]) -> str:
    """
    Take as input a formula represented as a nested list of lists and strings (as produced by tptpParsing.parseStruct) and outputs a matching TPTP formula.
    See tptpParsing.parseStruct for more details on the input format.

    Example: 
        >>> ["f", "a", "b"] 
        "f(a,b)"
    """
    assert len(struct) > 0, "Input structure cannot be empty" 
    assert isinstance(struct[0], str), "First element of structure must be a string representing the symbol"

    symbol = struct[0]

    # Leaf case
    if len(struct) == 1: return symbol

    # List of variables
    if symbol == ",":
        assert len(struct) > 1, "Comma must have at least one argument"
        assert all(isinstance(arg, str) for arg in struct[1:]), "All arguments after comma must be strings"
        return ', '.join(struct[1:])

    # Quantification
    if symbol in ["!", "?"]:
        assert len(struct) == 3
        symbol, variables, body = struct
        return f"{symbol}[{_formula_from_struct(variables)}] : ({_formula_from_struct(body)})"

    # Binary operators and logical connectives
    if symbol in ["=>", "<=>", "=", "&", "|"]:
        assert len(struct) == 3, f"Binary operator {symbol} must have exactly two arguments"
        return f"({_formula_from_struct(struct[1])} {symbol} {_formula_from_struct(struct[2])})"
    
    # Negation
    if symbol == "~":
        assert len(struct) == 2, "Negation must have exactly one argument"
        return f"~{_formula_from_struct(struct[1])}"
    
    # Function or predicate application
    assert re.match(r'\w*$', symbol), f"Symbol '{symbol}' must contain only alphanumeric characters and underscores"

    return f"{symbol}({', '.join(_formula_from_struct(arg) for arg in struct[1:])})" # We know that struct[1:] is not empty here because we handled the leaf case above
    
def _quote_from_struct(struct : List, var_to_qvar : Dict[str, str]) -> str:
    """Convert a parsed structure to its quoted representation.
    See tptpParsing.parseStruct for more details on the input format.

    Args:
        struct: A parsed structure representing a formula.
        var_to_qvar: Dict mapping variable names to their quoted versions. This is increased when entering quantifications, hence the variables within the scope of a quantification will have their mapping here. Variables not in this dict are considered free variables from a higher scope.

    Returns:
        The quoted string representation of the structure.
    """
    if var_to_qvar is None : var_to_qvar = {}
    assert len(struct) > 0, "Input structure cannot be empty"
    assert isinstance(struct[0], str), "First element of structure must be a string representing the symbol"

    symbol = struct[0]

    # If the symbol is quoted, we use apply q_Quote and assume everything beyond is already quoted
    # TODO : this relies on implicit assumptions that everything beyond is also already quoted and does not react well to special symbols
    # It would be nice if we could handle quotation of free variables, but that would require more complex macros
    if isQuoted(symbol):
        q_Quote = get_special_function("q_Quote")
        return f"{q_Quote}({_formula_from_struct(struct)})"

    # Leaf cases
    ## Variable case
    if len(struct) == 1 and re.match(r'^[A-Z]\w*$', symbol):
        if symbol not in var_to_qvar:
            # It is not quantified in this scope, we treat is as a free variable from a higher scope
            q_Quote = get_special_function("q_Quote")
            return f"{q_Quote}({symbol})"
        return var_to_qvar[symbol] # If it is mapped then it was quantified above. Return its quoted version.
    
    ## Function or predicate with no arguments case
    if len(struct) == 1 and re.match(r'^[a-z_]\w*$', symbol):
        quoted_symbol = quoteSymbol(symbol)
        return f"{quoted_symbol}"
        
    # Quantification
    ## Lazy (codewise) way to flatten the structure when the quantification has more than one variable
    if symbol in ["!", "?"] and len(struct) == 3 and len(struct[1]) > 1:
        assert len(struct) == 3, f"Quantification {symbol} must have exactly two arguments"
        assert isinstance(struct[1], list), "Quantification variables must be a list"
        assert all(isinstance(var, str) for var in struct[1]), "All quantification variables must be strings"
        _, variables, body = struct

        assert variables[0] == ","
        variables = variables[1:]

        top_var, other_vars = variables[0], variables[1:]
        flatter_struct = [symbol, [top_var], [symbol, other_vars, body]]
        return _quote_from_struct(flatter_struct, var_to_qvar)
    
    ## Universal quantification with a single variable
    if symbol == "!":
        assert len(struct) == 3, f"Quantification {symbol} must have exactly two arguments"
        _, variable, body = struct
        quoted_symbol = get_special_function("q_Forall") 
        fresh_var = next_quoted_var(var_to_qvar.keys())
        var_to_qvar[variable[0]] = fresh_var
        variable = _quote_from_struct(variable, var_to_qvar)
        body = _quote_from_struct(body, var_to_qvar)
        return f"{quoted_symbol}({variable}, {body})"
    
    ## Existential quantification with a single variable
    if symbol == "?":
        assert len(struct) == 3, f"Quantification {symbol} must have exactly two arguments"
        _, variable, body = struct
        quoted_symbol = get_special_function("q_Forall") 
        fresh_var = next_quoted_var(var_to_qvar.keys())
        var_to_qvar[variable[0]] = fresh_var
        neg_symbol = get_special_function("q_Neg")
        body = _quote_from_struct(body, var_to_qvar)
        variable = _quote_from_struct(variable, var_to_qvar)
        return f"{neg_symbol}({quoted_symbol}({variable}, {neg_symbol}({body})))"
 
    # Binary operators and logical connectives
    if symbol in ["&", "|"]:
        assert len(struct) == 3, f"Binary operator {symbol} must have exactly two arguments"
        left = _quote_from_struct(struct[1], var_to_qvar)
        right = _quote_from_struct(struct[2], var_to_qvar)
        quoted_symbol = get_special_function("q_And") if symbol == "&" else get_special_function("q_Or")
        return f"{quoted_symbol}({left}, {right})"
    
    if symbol in ["=>", "<=>"]:
        assert len(struct) == 3, f"Binary operator {symbol} must have exactly two arguments"
        left = struct[1]
        right = struct[2]
        if symbol == "=>":
            new_struct = ["|", ["~", left], right]
        else:
            new_struct = ["&", ["=>", left, right], ["=>", right, left]]
        return _quote_from_struct(new_struct, var_to_qvar)
    
    # Negation
    if symbol == "~":
        assert len(struct) == 2, "Negation must have exactly one argument"
        body = _quote_from_struct(struct[1], var_to_qvar)
        quoted_symbol = get_special_function("q_Neg")
        return f"{quoted_symbol}({body})"
    

    if symbol == ",":
        raise ValueError("Comma is not a valid symbol in this context, it should be handled separately")

    
    # Function or predicate application
    assert re.match(r'^[a-z_]\w*$', symbol), f"Symbol '{symbol}' must contain only lowercase alphanumeric characters and underscores"
    quoted_symbol = quoteSymbol(symbol)
    return f"{quoted_symbol}({', '.join(_quote_from_struct(arg, var_to_qvar) for arg in struct[1:])})" # We know that struct[1:] is not empty here because we handled the leaf case above