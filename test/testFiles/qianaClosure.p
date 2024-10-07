fof(axiom_1,axiom,(! [X]: (ist(say(friar), X) => truthPredicate(X)))).

fof(axiom_2,axiom,(! [X, Y]: ((madLove(X, Y) & ist(bel(X), q_dead(q_quote(Y)))) => dead(X)))).

fof(axiom_3,axiom,madLove(romeo, juliet)).

fof(axiom_4,axiom,madLove(juliet, romeo)).

fof(axiom_5,axiom,ist(say(friar), q_Forall(q_x0, q_Not(q_And(q_drinkPotion(q_x0), q_Not(q_appearDead(q_x0))))))).

fof(axiom_6,axiom,drinkPotion(juliet)).

fof(axiom_7,axiom,(! [X, Y]: (appearDead(X) => ist(Y, q_appearDead(q_quote(X)))))).

fof(axiom_8,axiom,(! [X, Y]: (dead(X) => ist(Y, q_dead(q_quote(X)))))).

fof(axiom_9,axiom,(! [X]: ist(bel(romeo), q_Not(q_And(q_appearDead(q_quote(X)), q_Not(q_dead(q_quote(X)))))))).

fof(axiom_10,conjecture,dead(juliet)).

fof(schema_6,axiom,(! [Tc, T1, T2]: (ist(Tc, q_And(T1, T2)) => ist(Tc, T1)))).
fof(schema_7,axiom,(! [Tc, T1, T2]: (ist(Tc, q_And(T1, T2)) <=> ist(Tc, q_And(T2, T1))))).
fof(schema_8,axiom,(! [Tc, T1]: (ist(Tc, q_Not(q_Not(T1))) <=> ist(Tc, T1)))).
fof(schema_9,axiom,(! [Tc, T1, T2, T3]: (ist(Tc, q_And(q_And(T1, T2), T3)) <=> ist(Tc, q_And(T1, q_And(T2, T3)))))).
fof(schema_10,axiom,(! [Tc, T1, T2, T3]: (ist(Tc, q_Or(q_And(T1, T2), T3)) <=> ist(Tc, q_And(q_Or(T1, T3), q_Or(T2, T3)))))).
fof(schema_11,axiom,(! [Tc, T1, T2]: (ist(Tc, q_Or(T1, T2)) & (ist(C, q_Not(T1)) => ist(C, T2))))).
fof(schema_29,axiom,(! [X]: equals(X, X))).
fof(schema_30,axiom,(! [X, Y, Z]: (equals(X, Y) & (equals(Y, Z) => equals(X, Z))))).
fof(schema_31,axiom,(! [X, Y]: (equals(X, Y) => equals(Y, X)))).
fof(schema_32_say,axiom,(! [X_1, Y_1]: ((equals(X_1, Y_1)) => equals(say(X_1), say(Y_1))))).
fof(schema_32_bel,axiom,(! [X_1, Y_1]: ((equals(X_1, Y_1)) => equals(bel(X_1), bel(Y_1))))).
fof(schema_33_madLove,axiom,(! [X_1, X_2, Y_1, Y_2]: ((equals(X_1, Y_1) & equals(X_2, Y_2)) => (madLove(X_1, X_2) <=> madLove(Y_1, Y_2))))).
fof(schema_33_dead,axiom,(! [X_1, Y_1]: ((equals(X_1, Y_1)) => (dead(X_1) <=> dead(Y_1))))).
fof(schema_33_drinkPotion,axiom,(! [X_1, Y_1]: ((equals(X_1, Y_1)) => (drinkPotion(X_1) <=> drinkPotion(Y_1))))).
fof(schema_33_appearDead,axiom,(! [X_1, Y_1]: ((equals(X_1, Y_1)) => (appearDead(X_1) <=> appearDead(Y_1))))).
fof(schema_34_romeo,axiom,equals(eval(q_romeo), romeo)).
fof(schema_34_juliet,axiom,equals(eval(q_juliet), juliet)).
fof(schema_34_friar,axiom,equals(eval(q_friar), friar)).
fof(schema_35,axiom,(! [T]: (reach(T) => equals(eval(quote(T)), T)))).
fof(schema_36_say,axiom,(! [T_1]: ((reach(T_1)) => equals(eval(q_say(T_1)), say(eval(T_1)))))).
fof(schema_36_bel,axiom,(! [T_1]: ((reach(T_1)) => equals(eval(q_bel(T_1)), bel(eval(T_1)))))).
fof(schema_37_madLove,axiom,(! [T_1, T_2]: ((reach(T_1) & reach(T_2)) => equals(eval(q_madLove(T_1), q_madLove(T_2)), q_madLove(T_1), q_madLove(T_2))))).
fof(schema_37_dead,axiom,(! [T_1]: ((reach(T_1)) => equals(eval(q_dead(T_1)), q_dead(T_1))))).
fof(schema_37_drinkPotion,axiom,(! [T_1]: ((reach(T_1)) => equals(eval(q_drinkPotion(T_1)), q_drinkPotion(T_1))))).
fof(schema_37_appearDead,axiom,(! [T_1]: ((reach(T_1)) => equals(eval(q_appearDead(T_1)), q_appearDead(T_1))))).
fof(schema_38,axiom,(! [T1, T2]: equals(eval(q_And(T1, T2)), q_And(T1, T2)))).
fof(schema_39,axiom,(! [T1, T2]: equals(eval(q_Forall(T1, T2)), q_Forall(T1, T2)))).
fof(schema_40,axiom,(! [T]: equals(eval(q_Not(T)), q_Not(T)))).
fof(schema_41_q_VAR_0,axiom,equals(eval(q_VAR_0), q_VAR_0)).
fof(schema_41_q_VAR_2,axiom,equals(eval(q_VAR_2), q_VAR_2)).
fof(schema_41_q_VAR_1,axiom,equals(eval(q_VAR_1), q_VAR_1)).
fof(schema_41_q_x0,axiom,equals(eval(q_x0), q_x0)).
fof(schema_42_q_VAR_0,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_0, T, q_VAR_0), T)))).
fof(schema_42_q_VAR_2,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_2, T, q_VAR_2), T)))).
fof(schema_42_q_VAR_1,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_1, T, q_VAR_1), T)))).
fof(schema_42_q_x0,axiom,(! [T]: (reach(T) => equals(sub(q_x0, T, q_x0), T)))).
fof(schema_43_q_VAR_0_q_VAR_2,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_0, T, q_VAR_2), q_VAR_2)))).
fof(schema_43_q_VAR_0_q_VAR_1,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_0, T, q_VAR_1), q_VAR_1)))).
fof(schema_43_q_VAR_0_q_x0,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_0, T, q_x0), q_x0)))).
fof(schema_43_q_VAR_2_q_VAR_0,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_2, T, q_VAR_0), q_VAR_0)))).
fof(schema_43_q_VAR_2_q_VAR_1,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_2, T, q_VAR_1), q_VAR_1)))).
fof(schema_43_q_VAR_2_q_x0,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_2, T, q_x0), q_x0)))).
fof(schema_43_q_VAR_1_q_VAR_0,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_1, T, q_VAR_0), q_VAR_0)))).
fof(schema_43_q_VAR_1_q_VAR_2,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_1, T, q_VAR_2), q_VAR_2)))).
fof(schema_43_q_VAR_1_q_x0,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_1, T, q_x0), q_x0)))).
fof(schema_43_q_x0_q_VAR_0,axiom,(! [T]: (reach(T) => equals(sub(q_x0, T, q_VAR_0), q_VAR_0)))).
fof(schema_43_q_x0_q_VAR_2,axiom,(! [T]: (reach(T) => equals(sub(q_x0, T, q_VAR_2), q_VAR_2)))).
fof(schema_43_q_x0_q_VAR_1,axiom,(! [T]: (reach(T) => equals(sub(q_x0, T, q_VAR_1), q_VAR_1)))).
fof(schema_43_q_VAR_0_romeo,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_0, T, q_romeo), romeo)))).
fof(schema_43_q_VAR_0_juliet,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_0, T, q_juliet), juliet)))).
fof(schema_43_q_VAR_0_friar,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_0, T, q_friar), friar)))).
fof(schema_43_q_VAR_2_romeo,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_2, T, q_romeo), romeo)))).
fof(schema_43_q_VAR_2_juliet,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_2, T, q_juliet), juliet)))).
fof(schema_43_q_VAR_2_friar,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_2, T, q_friar), friar)))).
fof(schema_43_q_VAR_1_romeo,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_1, T, q_romeo), romeo)))).
fof(schema_43_q_VAR_1_juliet,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_1, T, q_juliet), juliet)))).
fof(schema_43_q_VAR_1_friar,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_1, T, q_friar), friar)))).
fof(schema_43_q_x0_romeo,axiom,(! [T]: (reach(T) => equals(sub(q_x0, T, q_romeo), romeo)))).
fof(schema_43_q_x0_juliet,axiom,(! [T]: (reach(T) => equals(sub(q_x0, T, q_juliet), juliet)))).
fof(schema_43_q_x0_friar,axiom,(! [T]: (reach(T) => equals(sub(q_x0, T, q_friar), friar)))).
fof(schema_45_q_VAR_0_q_quote,axiom,(! [T_1]: ((reach(T_1)) => equals(sub(q_VAR_0, T, q_quote(T_1)), q_quote(sub(q_VAR_0, T, T_1)))))).
fof(schema_45_q_VAR_0_q_dead,axiom,(! [T_1]: ((reach(T_1)) => equals(sub(q_VAR_0, T, q_dead(T_1)), q_dead(sub(q_VAR_0, T, T_1)))))).
fof(schema_45_q_VAR_0_q_appearDead,axiom,(! [T_1]: ((reach(T_1)) => equals(sub(q_VAR_0, T, q_appearDead(T_1)), q_appearDead(sub(q_VAR_0, T, T_1)))))).
fof(schema_45_q_VAR_0_q_drinkPotion,axiom,(! [T_1]: ((reach(T_1)) => equals(sub(q_VAR_0, T, q_drinkPotion(T_1)), q_drinkPotion(sub(q_VAR_0, T, T_1)))))).
fof(schema_45_q_VAR_2_q_quote,axiom,(! [T_1]: ((reach(T_1)) => equals(sub(q_VAR_2, T, q_quote(T_1)), q_quote(sub(q_VAR_2, T, T_1)))))).
fof(schema_45_q_VAR_2_q_dead,axiom,(! [T_1]: ((reach(T_1)) => equals(sub(q_VAR_2, T, q_dead(T_1)), q_dead(sub(q_VAR_2, T, T_1)))))).
fof(schema_45_q_VAR_2_q_appearDead,axiom,(! [T_1]: ((reach(T_1)) => equals(sub(q_VAR_2, T, q_appearDead(T_1)), q_appearDead(sub(q_VAR_2, T, T_1)))))).
fof(schema_45_q_VAR_2_q_drinkPotion,axiom,(! [T_1]: ((reach(T_1)) => equals(sub(q_VAR_2, T, q_drinkPotion(T_1)), q_drinkPotion(sub(q_VAR_2, T, T_1)))))).
fof(schema_45_q_VAR_1_q_quote,axiom,(! [T_1]: ((reach(T_1)) => equals(sub(q_VAR_1, T, q_quote(T_1)), q_quote(sub(q_VAR_1, T, T_1)))))).
fof(schema_45_q_VAR_1_q_dead,axiom,(! [T_1]: ((reach(T_1)) => equals(sub(q_VAR_1, T, q_dead(T_1)), q_dead(sub(q_VAR_1, T, T_1)))))).
fof(schema_45_q_VAR_1_q_appearDead,axiom,(! [T_1]: ((reach(T_1)) => equals(sub(q_VAR_1, T, q_appearDead(T_1)), q_appearDead(sub(q_VAR_1, T, T_1)))))).
fof(schema_45_q_VAR_1_q_drinkPotion,axiom,(! [T_1]: ((reach(T_1)) => equals(sub(q_VAR_1, T, q_drinkPotion(T_1)), q_drinkPotion(sub(q_VAR_1, T, T_1)))))).
fof(schema_45_q_x0_q_quote,axiom,(! [T_1]: ((reach(T_1)) => equals(sub(q_x0, T, q_quote(T_1)), q_quote(sub(q_x0, T, T_1)))))).
fof(schema_45_q_x0_q_dead,axiom,(! [T_1]: ((reach(T_1)) => equals(sub(q_x0, T, q_dead(T_1)), q_dead(sub(q_x0, T, T_1)))))).
fof(schema_45_q_x0_q_appearDead,axiom,(! [T_1]: ((reach(T_1)) => equals(sub(q_x0, T, q_appearDead(T_1)), q_appearDead(sub(q_x0, T, T_1)))))).
fof(schema_45_q_x0_q_drinkPotion,axiom,(! [T_1]: ((reach(T_1)) => equals(sub(q_x0, T, q_drinkPotion(T_1)), q_drinkPotion(sub(q_x0, T, T_1)))))).
fof(schema_47_q_VAR_0,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_x0, T1, q_Forall(q_x0, T2)), q_Forall(q_x0, T2))))).
fof(schema_47_q_VAR_2,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_x0, T1, q_Forall(q_x0, T2)), q_Forall(q_x0, T2))))).
fof(schema_47_q_VAR_1,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_x0, T1, q_Forall(q_x0, T2)), q_Forall(q_x0, T2))))).
fof(schema_47_q_x0,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_x0, T1, q_Forall(q_x0, T2)), q_Forall(q_x0, T2))))).
fof(schema_48_q_VAR_0_q_VAR_2,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_VAR_0, T1, q_Forall(q_VAR_2, T2)), q_Forall(q_VAR_2, sub(q_VAR_0, T1, q_Forall(q_VAR_2, T2))))))).
fof(schema_48_q_VAR_0_q_VAR_1,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_VAR_0, T1, q_Forall(q_VAR_1, T2)), q_Forall(q_VAR_1, sub(q_VAR_0, T1, q_Forall(q_VAR_1, T2))))))).
fof(schema_48_q_VAR_0_q_x0,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_VAR_0, T1, q_Forall(q_x0, T2)), q_Forall(q_x0, sub(q_VAR_0, T1, q_Forall(q_x0, T2))))))).
fof(schema_48_q_VAR_2_q_VAR_0,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_VAR_2, T1, q_Forall(q_VAR_0, T2)), q_Forall(q_VAR_0, sub(q_VAR_2, T1, q_Forall(q_VAR_0, T2))))))).
fof(schema_48_q_VAR_2_q_VAR_1,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_VAR_2, T1, q_Forall(q_VAR_1, T2)), q_Forall(q_VAR_1, sub(q_VAR_2, T1, q_Forall(q_VAR_1, T2))))))).
fof(schema_48_q_VAR_2_q_x0,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_VAR_2, T1, q_Forall(q_x0, T2)), q_Forall(q_x0, sub(q_VAR_2, T1, q_Forall(q_x0, T2))))))).
fof(schema_48_q_VAR_1_q_VAR_0,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_VAR_1, T1, q_Forall(q_VAR_0, T2)), q_Forall(q_VAR_0, sub(q_VAR_1, T1, q_Forall(q_VAR_0, T2))))))).
fof(schema_48_q_VAR_1_q_VAR_2,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_VAR_1, T1, q_Forall(q_VAR_2, T2)), q_Forall(q_VAR_2, sub(q_VAR_1, T1, q_Forall(q_VAR_2, T2))))))).
fof(schema_48_q_VAR_1_q_x0,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_VAR_1, T1, q_Forall(q_x0, T2)), q_Forall(q_x0, sub(q_VAR_1, T1, q_Forall(q_x0, T2))))))).
fof(schema_48_q_x0_q_VAR_0,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_x0, T1, q_Forall(q_VAR_0, T2)), q_Forall(q_VAR_0, sub(q_x0, T1, q_Forall(q_VAR_0, T2))))))).
fof(schema_48_q_x0_q_VAR_2,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_x0, T1, q_Forall(q_VAR_2, T2)), q_Forall(q_VAR_2, sub(q_x0, T1, q_Forall(q_VAR_2, T2))))))).
fof(schema_48_q_x0_q_VAR_1,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_x0, T1, q_Forall(q_VAR_1, T2)), q_Forall(q_VAR_1, sub(q_x0, T1, q_Forall(q_VAR_1, T2))))))).
fof(schema_49_q_VAR_0,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_VAR_0, T1, quote(T2)), quote(T2))))).
fof(schema_49_q_VAR_2,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_VAR_2, T1, quote(T2)), quote(T2))))).
fof(schema_49_q_VAR_1,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_VAR_1, T1, quote(T2)), quote(T2))))).
fof(schema_49_q_x0,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_x0, T1, quote(T2)), quote(T2))))).
fof(schema_52,axiom,(! [X]: reach(quote(X)))).
fof(schema_53_romeo,axiom,reach(romeo)).
fof(schema_53_juliet,axiom,reach(juliet)).
fof(schema_53_friar,axiom,reach(friar)).
fof(schema_54,axiom,(! [T_1]: ((reach(T_1)) => reach(say(T_1))))).
fof(schema_54,axiom,(! [T_1]: ((reach(T_1)) => reach(bel(T_1))))).
fof(schema_55,axiom,(! [X]: wft(quote(X)))).
fof(schema_57_q_VAR_0,axiom,wft(q_VAR_0)).
fof(schema_57_q_VAR_2,axiom,wft(q_VAR_2)).
fof(schema_57_q_VAR_1,axiom,wft(q_VAR_1)).
fof(schema_57_q_x0,axiom,wft(q_x0)).
fof(schema_58,axiom,(! [T_1]: ((wft(T_1)) => wft(say(T_1))))).
fof(schema_58,axiom,(! [T_1]: ((wft(T_1)) => wft(bel(T_1))))).
fof(schema_59_madLove,axiom,(! [T_1, T_2]: ((wft(T_1) & wft(T_2)) => (truthPredicate(q_madLove(T_1, T_2)) <=> madLove(eval(T_1), eval(T_2)))))).
fof(schema_59_dead,axiom,(! [T_1]: ((wft(T_1)) => (truthPredicate(q_dead(T_1)) <=> dead(eval(T_1)))))).
fof(schema_59_drinkPotion,axiom,(! [T_1]: ((wft(T_1)) => (truthPredicate(q_drinkPotion(T_1)) <=> drinkPotion(eval(T_1)))))).
fof(schema_59_appearDead,axiom,(! [T_1]: ((wft(T_1)) => (truthPredicate(q_appearDead(T_1)) <=> appearDead(eval(T_1)))))).
fof(schema_60,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => (truthPredicate(q_And(T1, T2)) <=> (truthPredicate(T1) & truthPredicate(T2)))))).
fof(schema_61,axiom,(! [T1]: (reach(T1) => (truthPredicate(q_Not(T1)) <=> (truthPredicate(T1)))))).
fof(schema_62_q_VAR_0,axiom,(! [T1]: (reach(T1) => (truthPredicate(q_Forall(q_VAR_0, T1)) <=> (! [X]: truthPredicate(sub(q_VAR_0, quote(X), T1))))))).
fof(schema_62_q_VAR_2,axiom,(! [T1]: (reach(T1) => (truthPredicate(q_Forall(q_VAR_2, T1)) <=> (! [X]: truthPredicate(sub(q_VAR_2, quote(X), T1))))))).
fof(schema_62_q_VAR_1,axiom,(! [T1]: (reach(T1) => (truthPredicate(q_Forall(q_VAR_1, T1)) <=> (! [X]: truthPredicate(sub(q_VAR_1, quote(X), T1))))))).
fof(schema_62_q_x0,axiom,(! [T1]: (reach(T1) => (truthPredicate(q_Forall(q_x0, T1)) <=> (! [X]: truthPredicate(sub(q_x0, quote(X), T1))))))).