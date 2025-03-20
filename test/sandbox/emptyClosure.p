fof(schema_6,axiom,(! [Tc, T1, T2]: (ist(Tc, q_And(T1, T2)) => ist(Tc, T1)))).
fof(schema_7,axiom,(! [Tc, T1, T2]: (ist(Tc, q_And(T1, T2)) <=> ist(Tc, q_And(T2, T1))))).
fof(schema_8,axiom,(! [Tc, T1]: (ist(Tc, q_Not(q_Not(T1))) <=> ist(Tc, T1)))).
fof(schema_9,axiom,(! [Tc, T1, T2, T3]: (ist(Tc, q_And(q_And(T1, T2), T3)) <=> ist(Tc, q_And(T1, q_And(T2, T3)))))).
fof(schema_10,axiom,(! [Tc, T1, T2, T3]: (ist(Tc, q_Or(q_And(T1, T2), T3)) <=> ist(Tc, q_And(q_Or(T1, T3), q_Or(T2, T3)))))).
fof(schema_11,axiom,(! [Tc, T1, T2]: ((ist(Tc, q_Or(T1, T2)) & ist(C, q_Not(T1))) => ist(C, T2)))).
fof(schema_29,axiom,(! [X]: equals(X, X))).
fof(schema_30,axiom,(! [X, Y, Z]: ((equals(X, Y) & equals(Y, Z)) => equals(X, Z)))).
fof(schema_31,axiom,(! [X, Y]: (equals(X, Y) => equals(Y, X)))).
fof(schema_35,axiom,(! [T]: (reach(T) => equals(eval(quote(T)), T)))).
fof(schema_38,axiom,(! [T1, T2]: equals(eval(q_And(T1, T2)), q_And(T1, T2)))).
fof(schema_39,axiom,(! [T1, T2]: equals(eval(q_Forall(T1, T2)), q_Forall(T1, T2)))).
fof(schema_40,axiom,(! [T]: equals(eval(q_Not(T)), q_Not(T)))).
fof(schema_42_q_VAR_2,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_2, T, q_VAR_2), T)))).
fof(schema_42_q_VAR_1,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_1, T, q_VAR_1), T)))).
fof(schema_42_q_VAR_0,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_0, T, q_VAR_0), T)))).
fof(schema_43_q_VAR_2_q_VAR_1,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_2, T, q_VAR_1), q_VAR_1)))).
fof(schema_43_q_VAR_2_q_VAR_0,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_2, T, q_VAR_0), q_VAR_0)))).
fof(schema_43_q_VAR_1_q_VAR_2,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_1, T, q_VAR_2), q_VAR_2)))).
fof(schema_43_q_VAR_1_q_VAR_0,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_1, T, q_VAR_0), q_VAR_0)))).
fof(schema_43_q_VAR_0_q_VAR_2,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_0, T, q_VAR_2), q_VAR_2)))).
fof(schema_43_q_VAR_0_q_VAR_1,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_0, T, q_VAR_1), q_VAR_1)))).
fof(schema_47_q_VAR_2,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_VAR_0, T1, q_Forall(q_VAR_0, T2)), q_Forall(q_VAR_0, T2))))).
fof(schema_47_q_VAR_1,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_VAR_0, T1, q_Forall(q_VAR_0, T2)), q_Forall(q_VAR_0, T2))))).
fof(schema_47_q_VAR_0,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_VAR_0, T1, q_Forall(q_VAR_0, T2)), q_Forall(q_VAR_0, T2))))).
fof(schema_48_q_VAR_2_q_VAR_1,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_VAR_2, T1, q_Forall(q_VAR_1, T2)), q_Forall(q_VAR_1, sub(q_VAR_2, T1, T2)))))).
fof(schema_48_q_VAR_2_q_VAR_0,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_VAR_2, T1, q_Forall(q_VAR_0, T2)), q_Forall(q_VAR_0, sub(q_VAR_2, T1, T2)))))).
fof(schema_48_q_VAR_1_q_VAR_2,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_VAR_1, T1, q_Forall(q_VAR_2, T2)), q_Forall(q_VAR_2, sub(q_VAR_1, T1, T2)))))).
fof(schema_48_q_VAR_1_q_VAR_0,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_VAR_1, T1, q_Forall(q_VAR_0, T2)), q_Forall(q_VAR_0, sub(q_VAR_1, T1, T2)))))).
fof(schema_48_q_VAR_0_q_VAR_2,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_VAR_0, T1, q_Forall(q_VAR_2, T2)), q_Forall(q_VAR_2, sub(q_VAR_0, T1, T2)))))).
fof(schema_48_q_VAR_0_q_VAR_1,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_VAR_0, T1, q_Forall(q_VAR_1, T2)), q_Forall(q_VAR_1, sub(q_VAR_0, T1, T2)))))).
fof(schema_49_q_VAR_2,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_VAR_2, T1, quote(T2)), quote(T2))))).
fof(schema_49_q_VAR_1,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_VAR_1, T1, quote(T2)), quote(T2))))).
fof(schema_49_q_VAR_0,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_VAR_0, T1, quote(T2)), quote(T2))))).
fof(schema_52,axiom,(! [X]: reach(quote(X)))).
fof(schema_55,axiom,(! [X]: wft(quote(X)))).
fof(schema_57_q_VAR_2,axiom,wft(q_VAR_2)).
fof(schema_57_q_VAR_1,axiom,wft(q_VAR_1)).
fof(schema_57_q_VAR_0,axiom,wft(q_VAR_0)).
fof(schema_60,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => (truthPredicate(q_And(T1, T2)) <=> (truthPredicate(T1) & truthPredicate(T2)))))).
fof(schema_61,axiom,(! [T1]: (reach(T1) => (truthPredicate(q_Not(T1)) <=> (truthPredicate(T1)))))).
fof(schema_62_q_VAR_2,axiom,(! [T1]: (reach(T1) => (truthPredicate(q_Forall(q_VAR_2, T1)) <=> (! [X]: truthPredicate(sub(q_VAR_2, quote(X), T1))))))).
fof(schema_62_q_VAR_1,axiom,(! [T1]: (reach(T1) => (truthPredicate(q_Forall(q_VAR_1, T1)) <=> (! [X]: truthPredicate(sub(q_VAR_1, quote(X), T1))))))).
fof(schema_62_q_VAR_0,axiom,(! [T1]: (reach(T1) => (truthPredicate(q_Forall(q_VAR_0, T1)) <=> (! [X]: truthPredicate(sub(q_VAR_0, quote(X), T1))))))).