"""   Qiana Schemes

Enumerates the schemes of Qiana
"""

from typing import Callable, List
import typing

import qianaExtension.Formulas as Formulas
from qianaExtension.Formulas import Formula
from qianaExtension.SchemeFactory import SchemeFactory
from qianaExtension.SchemeFactory import SchemeFactory as SF
from qianaExtension.FormulaParser import parse
from qianaExtension.Signatures import Signature


def outputSchemes(output: Callable[[str, Formulas.Formula], typing.Any], signature : Signature):
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

    # Schema A1fin
    for p in signature.predicates:
        output(
            "schema_A1fin_" + p,
            parse(
                f"∀tn. (wft(t_AND)) → truthPredicate({Formula.quoteStr(p)}(tn)) ↔ {p}(eval(t_TERM))"
            ).expand(signature.predicates[p]),
        )
    
    # Schema A2fin
    output(
        "schema_A2fin",
        parse(
            "∀ t1, t2. (reach(t1) ∧ reach(t2)) → truthPredicate(q_And(t1, t2)) ↔ (truthPredicate(t1) ∧ truthPredicate(t2))"
        ),
    )

    # Schema A3fin
    output(
        "schema_A3fin",
        parse("∀ t1. reach(t1) → (truthPredicate(q_Not(t1)) ↔ (~truthPredicate(t1)))"),
    )

    # Schema A4fin
    for cx in signature.quotedVariables:
        output(
            "schema_A4fin_" + cx,
            parse(
                f"∀ t1. reach(t1) → (truthPredicate(q_Forall({cx}, t1)) ↔ (∀x. truthPredicate(sub({cx}, quote(x), t1))))"
            ),
        )

    # Schema A5 
    output("schema_A5", SF.genParsedScheme("∀tc, t1, t2. ist(tc, t1\\!∧t2) → ist(tc, t1)"))

    # Schema A6 
    output("schema_A6", SF.genParsedScheme("∀tc, t1, t2. ist(tc, t1\\!∧t2) ↔ ist(tc, t2\\!∧t1)"))
    
    # Schema A7 
    output("schema_A7", SF.genParsedScheme("∀tc, t1. ist(tc, qNot(qNot(t1))) ↔ ist(tc, t1)"))

    # Schema A8 
    output(
        "schema_A8", parse("∀tc, t1, t2, t3. ist(tc,qAnd(qAnd(t1, t2), t3)) ↔ ist(tc,qAnd(t1,qAnd(t2, t3)))"))
    
    # Schema A9 
    output(
        "schema_A9",
        parse("∀tc, t1, t2, t3. ist(tc, qOr(qAnd(t1,t2),t3)) ↔ ist(tc, qAnd(qOr(t1,t3),qOr(t2,t3)))"),
    )
    
    # Schema A10
    output("schema_A10", parse("∀tc, t1, t2. (ist(tc, qOr(t1,t2)) ∧ ist(tc, qNot(t1))) → ist(tc, t2)"))

    # Schema A11fin TODO

    # Schema A12
    output("schema_A12", parse("∀x. equals(x, x)"))

    # Schema A13
    output("schema_A13", parse("∀x, y. equals(x, y) → equals(y, x)"))
    
    # Schema A14
    output("schema_A14", parse("∀x, y, z. ((equals(x, y) ∧ equals(y, z)) → equals(x, z))"))

    # Syntax:
    #    p(xn)        ~~~~>   p(x1, ..., xn)
    #    ∀ xn         ~~~~>   ∀ x1, ..., xn
    #    p(x_AND)     ~~~~>   p(x1) & ... & p(xn)
    #    f(p(x_TERM)) ~~~~>   f(p(x1), p(x2),...,p(xn))

    # Schema A15
    for f in signature.functions:
        output(
            "schema_A15_" + f,
            parse(f"∀ xn, yn. equals(x_AND, y_AND) → equals({f}(xn), {f}(yn))").expand(
                signature.functions[f]
            ),
        )

    # Schema A16
    for p in signature.predicates:
        if signature.predicates[p] > 0:
            output(
                "schema_A16_" + p,
                parse(f"∀ xn, yn. equals(x_AND, y_AND) → ({p}(xn) ↔ {p}(yn))").expand(
                    signature.predicates[p]
                ),
            )

    # Schema A17:
    output("schema_A17", parse("∀x. reach(quote(x))"))

    # Schema A18
    for f in signature.functions:
        output(
            "schema_A18_"+f,
            parse(f"∀ tn. (reach(t_AND)) → reach({f}(tn))").expand(
                signature.functions[f]
            ),
        )
    for c in signature.constants:
        output("schema_A18_" + c, parse(f"reach({c})"))

    # Schema A19
    output("schema_A19", parse(f"∀x. wft(quote(x))"))

    # Schema A20
    for cx in signature.quotedVariables:
        output("schema_A20_" + cx, parse(f"wft({cx})"))

    # Schema A21 
    for c in signature.quotedConstants:
        output("schema_A21_" + c, parse(f"wft({c})"))

    for f, arity in signature.functions.items():
        fq = Formula.quoteStr(f)
        output(
            "schema_A21_" + fq,
            parse(f"∀ tn. (wft(t_AND)) → wft({fq}(tn))").expand(arity),
        )

    # Schema A22
    output("schema_A22", parse(f"∀t. reach(t) → equals(eval(quote(t)), t)"))

    # Schema A23 
    for f, arity in signature.functions.items():
        qf = Formula.quoteStr(f)
        output(f"schema_A23_{f}",SF.genParsedScheme(f"∀\\![T_$;,].(\\![reach(T_$);∧]) → equals(eval({qf}(\\![T_$;,])), {f}(\\![eval(T_$);,])))", 4*[arity]))

    for c in signature.constants:
        output("schema_A23_" + c, parse(f"equals(eval({Formula.quoteStr(c)}), {c})"))

    # Schema A24
    for p, arity in signature.predicates.items():
        qp = Formula.quoteStr(p)
        output(f"schema_A24_{p}",SF.genParsedScheme(f"∀\\![T_$;,].(\\![reach(T_$);∧]) → equals(eval({qp}(\\![T_$;,])), {qp}(\\![T_$;,]))", 4*[arity]))

    # Schema A25
    output("schema_A25", parse(f"∀t1, t2. equals(eval(q_And(t1, t2)), q_And(t1, t2))"))

    # Schema A26
    output(
        "schema_A26", parse(f"∀t1, t2. equals(eval(q_Forall(t1, t2)), q_Forall(t1, t2))")
    )
    
    # Schema A27
    output("schema_A27", parse(f"∀t. equals(eval(q_Not(t)), q_Not(t))"))

    # Schema A28
    for qv in signature.quotedVariables:
        output("schema_A28"+qv, parse(f"equals(eval({qv}), {qv})"))

    # Schema A29
    for c in signature.quotedVariables:
        output("schema_A29_" + c, parse(f"∀t. reach(t) → equals(sub({c}, t, {c}), t)"))

    # Schema A30: ∀t. reach(t) → sub(cx, t, cy ) = cy
    for cx in signature.quotedVariables:
        for cy in signature.quotedVariables:
            if cx == cy:
                continue
            output(
                "schema_A30_" + cx + "_" + cy,
                parse(f"∀t. reach(t) → equals(sub({cx}, t, {cy} ), {cy})"),
            )

    # Schema A31 TODO + Bad 
    # Handles both quoted functions and quoted predicates
    for cx in signature.quotedVariables:
        for f in signature.quotedFunctions:
            output(
                "schema_A31_" + cx + "_" + f,
                parse(
                    f"∀ tn. reach(t_AND) → equals(sub({cx}, t, {f}(tn)), {f}(sub({cx}, t, t_TERM)))"
                ).expand(signature.quotedFunctions[f]),
            )
    # Schema (44): ∀t. reach(t) → sub(cx, t, qc) = c
    for cx in signature.quotedVariables:
        for c in signature.constants:
            output(
                "schema_43_" + cx + "_" + c,
                parse(f"∀t. reach(t) → equals(sub({cx}, t, {Formula.quoteStr(c)}), {Formula.quoteStr(c)})"),
            )

    # Schema A32
    for c in signature.quotedVariables:
        output(
            "schema_A32_" + c,
            parse(
                f"∀t1, t2. (reach(t1) ∧ reach(t2)) → equals(sub({cx}, t1, q_Forall({cx}, t2)), q_Forall({cx}, t2)))"
            ),
        )

    # Schema A33
    for cx in signature.quotedVariables:
        for cy in signature.quotedVariables:
            if cx == cy:
                continue
            output(
                "schema_A33_" + cx + "_" + cy,
                parse(
                    f"∀t1, t2. (reach(t1) ∧ reach(t2)) → equals(sub({cx}, t1, q_Forall({cy}, t2)), q_Forall({cy}, sub({cx}, t1, t2)))"
                ),
            )

    # Schema A34
    for cx in signature.quotedVariables:
        output(
            "schema_A34_" + cx,
            parse(
                f"∀t1, t2. (reach(t1) ∧ reach(t2)) → equals(sub({cx}, t1, quote(t2)), quote(t2))"
            ),
        )



    # Schema 50 is a typo and does not exist. I will remove it at the last possible time to avoid confusing the naming scheme

    # Schema (53): # TODO where should this go?



    # Schema (60):
    

    # Schema (61):
    




    # # OLD Schema (36):
    # for f in signature.functions:
    #     quoted_f : str = Formula.quoteStr(f)
    #     def schema_36_instance(quotedFunArgsReach : str, quotedFunArgs : str, evalFunArgs : str) -> str:
    #         return f"∀{quotedFunArgs}.({quotedFunArgsReach}) → equals(eval({quoted_f}({quotedFunArgs})), {f}({evalFunArgs}))"
    #     indicesToStrings = [reachFromIndice, quotedFunArg, evalFunArg]
    #     maxIndices : List[int] = [signature.functions[f] for _ in range(3)]
    #     modes = [predicateAND, argumentList, argumentList]
    #     output(f"schema_36_old_{f}",parse(SchemeFactory.generateSchemeInstance(schema_36_instance, indicesToStrings, maxIndices, modes)))

    # # OLDER SCHEMA 36
    # for f in signature.functions:
    #     output(
    #         "schema_36_" + f,
    #         parse(
    #             f"∀tn.(reach(t_AND)) → equals(eval({Formulas.quote(f)}(t_TERM)), {f}(eval(t_TERM)))"
    #         ).expand(signature.functions[f]),
    #     )

    # # OLD Schema (37):
    # for p in signature.predicates:
    #     quoted_p : str = Formula.quoteStr(p)
    #     def schema_37_instance(quotedFunArgs, quotedFunArgsReach) -> str:
    #         return f"∀{quotedFunArgs}.({quotedFunArgsReach}) → equals(eval({quoted_p}({quotedFunArgs})), {quoted_p}({quotedFunArgs}))"
    #     indicesToStrings = [quotedFunArg, reachFromIndice]
    #     maxIndices : List[int] = [signature.predicates[p] for _ in range(2)]
    #     modes = [argumentList, predicateAND]
    #     output(f"schema_37_OLD_{p}",parse(SchemeFactory.generateSchemeInstance(schema_37_instance, indicesToStrings, maxIndices, modes)))
    
    # # OLDER SCHEMA 37
    # for p in signature.predicates:
    #     output(
    #         "schema_37_" + p,
    #         parse(
    #             f"∀tn.(reach(t_AND)) → equals(eval({Formulas.quote(p)}(t_TERM)), {Formulas.quote(p)}(t_TERM))"
    #         ).expand(signature.predicates[p]),
    #     )

