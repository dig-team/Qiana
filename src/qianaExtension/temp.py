from typing import List, Tuple
    def extendFromTptp(self, tptpFormula: str) -> None:
        """
        Read the body of a TPTP formula and extend the signature with the functions and predicates found in the formula.
        @param tptpFormula: The body of a TPTP formula, example : "![X1] p(f(X1),X1)"
        """
        for symbol, arity, isFunction in Signature._parseFormula(tptpFormula):
            if isFunction:
                self.addFunction(symbol, arity)
            else:
                self.addPredicate(symbol, arity)

    def _parseFormula(formula : str, formulasNext : bool = False) -> List[Tuple[str, int, bool]]:
        """
        Take a formula (for example "![X1] p(f(X1))") and returns a list of tuple containing each symbol along with its arity and a isAFunction boolean
        """
        def _parseTopLevel(formula : str) -> Tuple[str, List[str]]:
            """
            Read a formula of the form $f(a1, a2, ..., an)$ and return the function name and the arguments
            """
            name_end = formula.find('(')
            if name_end == -1:
                return formula.strip(), []
            
            name = formula[:name_end].strip()
            
            if not formula.endswith(')'):
                raise ValueError(f"Formula missing closing parenthesis: {formula}")
            
            arg_string = formula[name_end + 1:-1]
            
            args = []
            if arg_string.strip():
                current_arg = ""
                paren_level = 0
                for char in arg_string:
                    if char == '(' and paren_level == 0:
                        current_arg += char
                        paren_level += 1
                    elif char == '(' and paren_level > 0:
                        current_arg += char
                        paren_level += 1
                    elif char == ')' and paren_level > 1:
                        current_arg += char
                        paren_level -= 1
                    elif char == ')' and paren_level == 1:
                        current_arg += char
                        paren_level -= 1
                    elif char == ',' and paren_level == 0:
                        args.append(current_arg.strip())
                        current_arg = ""
                    else:
                        current_arg += char
                
                if current_arg:
                    args.append(current_arg.strip())
            
            return name, args

        # Handle logical connectives by splitting the formula
        logical_connectives = ["&", "=>", "<=>", "|", "~"]
        
        # First handle quantifiers
        if "]" in formula: 
            formula = formula.split("]", 1)[1].strip()
        if not formula: 
            return []
            
        # Remove outer parentheses if they exist
        if formula[0] == "(" and formula[-1] == ")": 
            formula = formula[1:-1].strip()
            
        # Try to split by logical connectives
        result = []
        
        # Check if we have any logical connectives at the top level
        split_positions = []
        paren_level = 0
        for i, char in enumerate(formula):
            if char == '(':
                paren_level += 1
            elif char == ')':
                paren_level -= 1
            # Only consider connectives at the top level (outside of any parentheses)
            elif paren_level == 0:
                for conn in logical_connectives:
                    if formula[i:].startswith(conn):
                        split_positions.append(i)
        
        # If we found logical connectives, split and process each part
        if split_positions:
            # Add the start position to make splitting easier
            split_positions = [0] + split_positions + [len(formula)]
            
            # Process each part between split positions
            for i in range(len(split_positions)-1):
                start = split_positions[i]
                end = split_positions[i+1]
                
                # Skip connectives themselves
                part = formula[start:end].strip()
                if part and not any(part == conn for conn in logical_connectives):
                    # For parts that contain logical connectives, recursively process them
                    result.extend(Signature._parseFormula(part, formulasNext))
        else:
            # If no connectives found, process normally
            try:
                symbol, arguments = _parseTopLevel(formula)
                
                # Only variables start with an uppercase char
                if not symbol[0].islower():
                    assert not arguments
                    return []
                
                result = [(symbol, len(arguments), formulasNext)]
                # Process arguments recursively
                for arg in arguments:
                    result.extend(Signature._parseFormula(arg, True))
            except ValueError:
                # If we can't parse the formula as a predicate/function, return empty
                pass
                
        return result