"""   Qiana Schemes

Enumerates the schemes of Qiana
"""

from typing import Callable, List
import typing

import qianaExtension.Formulas as Formulas
from qianaExtension.SchemeFactory import SchemeFactory
from qianaExtension.FormulaParser import parse



def outputSchemes(output: Callable[[str, Formulas.Formula], typing.Any], signature : Formulas.Signature):
    """Calls the output function for all schemes generated from the signature"""
    
    # ===============================================
    # Convenience shorthands for use of SchemeFactory
    argumentList = SchemeFactory.ExtensionModes.argumentList
    predicateAND = SchemeFactory.ExtensionModes.predicateAND
    def reachFromIndice(i : int) -> str:
        return f"reach(t{i})"
    def quotedFunArg(i : int) -> str:
        return f"t{i}"
    def evalFunArg(i : int) -> str:
        return f"eval(t{i})"

    # ===============================================
    # Schemes

    output("schema_6", parse("∀tc, t1, t2. ist(tc, t1∧t2) → ist(tc, t1)"))
    output("schema_7", parse("∀tc, t1, t2. ist(tc, t1∧t2) ↔ ist(tc, t2∧t1)"))
    output("schema_8", parse("∀tc, t1. ist(tc, ¬¬t1) ↔ ist(tc, t1)"))
    output(
        "schema_9", parse("∀tc, t1, t2, t3. ist(tc, (t1∧t2)∧t3) ↔ ist(tc, t1∧(t2∧t3))")
    )
    output(
        "schema_10",
        parse("∀tc, t1, t2, t3. ist(tc, (t1∧t2)∨t3) ↔ ist(tc, (t1∨t3)∧(t2∨t3))"),
    )
    output("schema_11", parse("∀tc, t1, t2. ist(tc, t1∨t2) ∧ ist(c, ¬t1) → ist(c, t2)"))

    output("schema_29", parse("∀x. equals(x, x)"))
    output("schema_30", parse("∀x, y, z. equals(x, y) ∧ equals(y, z) → equals(x, z)"))
    output("schema_31", parse("∀x, y. equals(x, y) → equals(y, x)"))

    # Syntax:
    #    p(xn)        ~~~~>   p(x1, ..., xn)
    #    ∀ xn         ~~~~>   ∀ x1, ..., xn
    #    p(x_AND)     ~~~~>   p(x1) & ... & p(xn)
    #    f(p(x_TERM)) ~~~~>   f(p(x1), p(x2),...,p(xn))

    # Schema 32
    for f in signature.functions:
        output(
            "schema_32_" + f,
            parse(f"∀ xn, yn. equals(x_AND, y_AND) → equals({f}(xn), {f}(yn))").expand(
                signature.functions[f]
            ),
        )

    # Schema (33):
    for p in signature.predicates:
        if signature.predicates[p] > 0:
            output(
                "schema_33_" + p,
                parse(f"∀ xn, yn. equals(x_AND, y_AND) → ({p}(xn) ↔ {p}(yn))").expand(
                    signature.predicates[p]
                ),
            )
    # Schema (34):
    for c in signature.constants:
        output("schema_34_" + c, parse(f"equals(eval({Formulas.quote(c)}), {c})"))

    output("schema_35", parse(f"∀t. reach(t) → equals(eval(quote(t)), t)"))

    # Schema (36):
    for f in signature.functions:
        quoted_f : str = Formulas.quote(f)
        def schema_36_instance(quotedFunArgsReach : str, quotedFunArgs : str, evalFunArgs : str) -> str:
            return f"∀{quotedFunArgs}.({quotedFunArgsReach}) → equals(eval({quoted_f}({quotedFunArgs})), {f}({evalFunArgs}))"
        indicesToStrings = [reachFromIndice, quotedFunArg, evalFunArg]
        maxIndices : List[int] = [signature.functions[f] for _ in range(3)]
        modes = [predicateAND, argumentList, argumentList]
        output(f"schema_36_{f}",parse(SchemeFactory.generateSchemeInstance(schema_36_instance, indicesToStrings, maxIndices, modes)))

    # # OLD SCHEMA 36
    # for f in signature.functions:
    #     output(
    #         "schema_36_" + f,
    #         parse(
    #             f"∀tn.(reach(t_AND)) → equals(eval({Formulas.quote(f)}(t_TERM)), {f}(eval(t_TERM)))"
    #         ).expand(signature.functions[f]),
    #     )

    # Schema (37):
    for p in signature.predicates:
        quoted_p : str = Formulas.quote(p)
        def schema_37_instance(quotedFunArgs, quotedFunArgsReach) -> str:
            return f"∀{quotedFunArgs}.({quotedFunArgsReach}) → equals(eval({quoted_p}({quotedFunArgs})), {quoted_p}({quotedFunArgs}))"
        indicesToStrings = [quotedFunArg, reachFromIndice]
        maxIndices : List[int] = [signature.predicates[p] for _ in range(2)]
        modes = [argumentList, predicateAND]
        output(f"schema_37_{p}",parse(SchemeFactory.generateSchemeInstance(schema_37_instance, indicesToStrings, maxIndices, modes)))
    
    # # OLD SCHEMA 37
    # for p in signature.predicates:
    #     output(
    #         "schema_37_" + p,
    #         parse(
    #             f"∀tn.(reach(t_AND)) → equals(eval({Formulas.quote(p)}(t_TERM)), {Formulas.quote(p)}(t_TERM))"
    #         ).expand(signature.predicates[p]),
    #     )
    output("schema_38", parse(f"∀t1, t2. equals(eval(q_And(t1, t2)), q_And(t1, t2))"))
    output(
        "schema_39", parse(f"∀t1, t2. equals(eval(q_Forall(t1, t2)), q_Forall(t1, t2))")
    )
    output("schema_40", parse(f"∀t. equals(eval(q_Not(t)), q_Not(t))"))

    # Schema (41):
    for c in signature.quotedVariables:
        output("schema_41_" + c, parse(f"equals(eval({c}), {c})"))
    # Schema (42):
    for c in signature.quotedVariables:
        output("schema_42_" + c, parse(f"∀t. reach(t) → equals(sub({c}, t, {c}), t)"))

    # Schema (43): ∀t. reach(t) → sub(cx, t, cy ) = cy
    for cx in signature.quotedVariables:
        for cy in signature.quotedVariables:
            if cx == cy:
                continue
            output(
                "schema_43_" + cx + "_" + cy,
                parse(f"∀t. reach(t) → equals(sub({cx}, t, {cy} ), {cy})"),
            )

    # Schema (44): ∀t. reach(t) → sub(cx, t, qc) = c
    for cx in signature.quotedVariables:
        for c in signature.constants:
            output(
                "schema_43_" + cx + "_" + c,
                parse(f"∀t. reach(t) → equals(sub({cx}, t, {Formulas.quote(c)}), {c})"),
            )

    # Schema 45 TODO: check paper for 45 and 46
    for cx in signature.quotedVariables:
        for f in signature.quotedFunctions:
            output(
                "schema_45_" + cx + "_" + f,
                parse(
                    f"∀ tn. reach(t_AND) → equals(sub({cx}, t, {f}(tn)), {f}(sub({cx}, t, t_TERM)))"
                ).expand(signature.quotedFunctions[f]),
            )

    # Schema (47):
    for c in signature.quotedVariables:
        output(
            "schema_47_" + c,
            parse(
                f"∀t1, t2. (reach(t1) ∧ reach(t2)) → equals(sub({cx}, t1, q_Forall({cx}, t2)), q_Forall({cx}, t2)))"
            ),
        )

    # Schema 48:
    for cx in signature.quotedVariables:
        for cy in signature.quotedVariables:
            if cx == cy:
                continue
            output(
                "schema_48_" + cx + "_" + cy,
                parse(
                    f"∀t1, t2. (reach(t1) ∧ reach(t2)) → equals(sub({cx}, t1, q_Forall({cy}, t2)), q_Forall({cy}, sub({cx}, t1, q_Forall({cy} , t2))))"
                ),
            )

    # Schema 49:
    for cx in signature.quotedVariables:
        output(
            "schema_49_" + cx,
            parse(
                f"∀t1, t2. (reach(t1) ∧ reach(t2)) → equals(sub({cx}, t1, quote(t2)), quote(t2))"
            ),
        )

    # Schema 50 is a typo and does not exist. I will remove it at the last possible time to avoid confusing the naming scheme

    # Schema (52):
    output("schema_52", parse("∀x. reach(quote(x))"))

    # Schema (53):
    for c in signature.constants:
        output("schema_53_" + c, parse(f"reach({c})"))

    # Schema (54):
    for f in signature.functions:
        output(
            "schema_54",
            parse(f"∀ tn. (reach(t_AND)) → reach({f}(tn))").expand(
                signature.functions[f]
            ),
        )

    # Schema (55):
    output("schema_55", parse(f"∀x. wft(quote(x))"))

    # Schema (56):
    for c in signature.quotedConstants:
        output("schema_56", parse(f"wft({c})"))

    # Schema (57):
    for cx in signature.quotedVariables:
        output("schema_57_" + cx, parse(f"wft({cx})"))

    # Schema (58):
    for f in signature.functions:
        output(
            "schema_58",
            parse(f"∀ tn. (wft(t_AND)) → wft({f}(tn))").expand(signature.functions[f]),
        )

    # Schema (59):
    for p in signature.predicates:
        output(
            "schema_59_" + p,
            parse(
                f"∀tn. (wft(t_AND)) → truthPredicate({Formulas.quote(p)}(tn)) ↔ {p}(eval(t_TERM))"
            ).expand(signature.predicates[p]),
        )

    # Schema (60):
    output(
        "schema_60",
        parse(
            "∀ t1, t2. (reach(t1) ∧ reach(t2)) → truthPredicate(q_And(t1, t2)) ↔ (truthPredicate(t1) ∧ truthPredicate(t2))"
        ),
    )

    # Schema (61):
    output(
        "schema_61",
        parse("∀ t1. reach(t1) → truthPredicate(q_Not(t1)) ↔ (¬truthPredicate(t1))"),
    )

    # Schema (62):
    for cx in signature.quotedVariables:
        output(
            "schema_62_" + cx,
            parse(
                f"∀ t1. reach(t1) → truthPredicate(q_Forall({cx}, t1)) ↔ (∀x. truthPredicate(sub({cx}, quote(x), t1)))"
            ),
        )
