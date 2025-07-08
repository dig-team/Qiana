# Testing
The tests are meant to be run with Pytest. Give the `test` directory as input to pytest and ensure the `qiana` package located in `src/qiana` can be imported (this can be done by installing the package or setting the current working directory to `src`).

# Writting new schemes
The scheme language used to generate all the axioms of Qiana on a given signature is described bellow. For a real example, see ```src/qianaExtension/qianaAxio.schemes```

## Defining new symbols
PREDICATE [name] OF ARITY [number] - Declares a predicate with specific arity, it will be a member of BASE_PREDICATE
FUNCTION [name] OF ARITY [number] - Declares a function with specific arity, it will be a member of BASE_FUNCTION

## Axiom Definition:
Each axiom starts with FORMULA [name]
Followed by BODY [formula expression]

The formula expression is the body of a TPTP formula, except it can contain the folllowing macro patterns:

1. **swap Patterns**: 
   - `$f`, `$p` - Pattern variables that will be replaced with concrete symbols
   - The `RANGE` directive specifies which set of symbols to use for substitution. The valid targets are BASE_FUNCTION, BASE_PREDICATE, QIANA_FUNCTION, ANY_PREDICATE, and QUOTED_VARIABLE. These correspond to the sets $F_b$, $P_b$, $F$, $P$, and the quotation of $V$ as defined in the formalization of Qiana. Is is also possible to assign a range of possible arities to the symbols. Examples:
     - `RANGE $p IN ANY_PREDICATE`
     - `RANGE $f IN BASE_FUNCTION`
     - `RANGE $f[1;-1] IN BASE_FUNCTION` note the use of `-1` to designate positive infinity. This is equivalent to excluding functions of arity 0 (constants).

Remark that QIANA_FUNCTION does not span over the symbols added in the finite axiomattization of Qiana and instead rangers only over all functions of the general semantic of Qiana.

2. **Dots Pattern**:
   - `X1,...,X#` - Represents a variable-length list of parameters. The symbol "," at each end of the end can be replaced with other desired symbols. The # indicates where the counter number substitution will be done to range on the list.
   - The `DOT_ARITIES` directive specifies the length to substitute. Swap pattern targets (like $f) can be used to specify the arity of the symbol in question will be used for the dot pattern; linking a swap pattern and a dot pattern.

3. **Quoting Mechanism**:
   - `WITH $qp QUOTING $p` - Creates a quoted version of symbol `$p` named `$qp`, used in swap patterns.

4. **Distinct symbols**
   - `DISTINCT $f $g` excludes instance of the scheme where the symbol variables $f and $g are assigned the same values.

## Example
```
FORMULA axiom24
BODY ![X1,...,X#] :((term(X1)&...&term(X#)) => eval($qp(X1,...,X#)) = $qp(X1,...,X#))
RANGE $p IN BASE_PREDICATE
WITH $qp QUOTING $p
DOT_ARITIES $p $p $p $p
```
This would expand to multiple formulas, one for each predicate in BASE_PREDICATE, with the appropriate number of arguments based on each predicate`s arity.

For example if there is a predicate p of arity 2 in the base predicates this will generate:
```
fof(axiom24_p, axiom, ![X1,X2] :((term(X1)&term(X2)) => eval(q_p(X1,X2)) = q_p(X1,X2))).
```