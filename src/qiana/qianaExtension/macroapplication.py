
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
        processed_line = _apply_macro_transformation(line)
        processed_lines.append(processed_line)
    
    return '\n'.join(processed_lines)

def _quote(text: str) -> str:
    """
    Take as input a formula or term and returns it qiana quotation.
    """
    


def _apply_macro_transformation(line: str) -> str:
    """
    Apply macro transformation to a single line, working from inside out.
    Transforms !name(x,y) to ist(name(x),{_quote(y)})
    """
    import re
    
    # Pattern to match !name(args) where name is an identifier and args can contain nested parentheses
    # We need to work from inside out, so we'll use a loop until no more matches are found
    
    while True:
        # Find the innermost !name(x,y) pattern
        # This regex looks for ! followed by identifier, then parentheses with content
        pattern = r'!([a-zA-Z_][a-zA-Z0-9_]*)\(([^()]*(?:\([^()]*\)[^()]*)*)\)'
        
        match = re.search(pattern, line)
        if not match:
            break
            
        full_match = match.group(0)
        name = match.group(1)
        args = match.group(2)
        
        # Split arguments by comma, but be careful with nested structures
        args_list = _split_arguments(args)
        
        if len(args_list) >= 2:
            # Take first argument as x, and the rest as y (joined by comma if multiple)
            x = args_list[0].strip()
            y = ', '.join(args_list[1:]).strip()
            
            replacement = f"ist({name}({x}), {_quote(y)}))"
            line = line.replace(full_match, replacement)
        else:
            # If not enough arguments, leave as is and break to avoid infinite loop
            break
    
    return line


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