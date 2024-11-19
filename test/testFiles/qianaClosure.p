fof(axiom_1,axiom,(! [X]: (ist(say(friar), X) => truthPredicate(X)))).

fof(axiom_2,axiom,(! [X, Y]: ((madLove(X, Y) & ist(bel(X), q_dead(quote(Y)))) => dead(X)))).

fof(axiom_3,axiom,madLove(romeo, juliet)).

fof(axiom_4,axiom,madLove(juliet, romeo)).

fof(axiom_5,axiom,ist(say(friar), q_Forall(q_x0, q_Not(q_And(q_drinkPotion(q_x0), q_Not(q_appearDead(q_x0))))))).

fof(axiom_6,axiom,drinkPotion(juliet)).

fof(axiom_7,axiom,(! [X, Y]: (appearDead(X) => ist(Y, q_appearDead(quote(X)))))).

fof(axiom_8,axiom,(! [X, Y]: (dead(X) => ist(Y, q_dead(quote(X)))))).

fof(axiom_9,axiom,(! [X]: ist(bel(romeo), q_Not(q_And(q_appearDead(quote(X)), q_Not(q_dead(quote(X)))))))).

fof(axiom_10,conjecture,dead(juliet)).

fof(schema_A1fin_madLove,axiom,(! [T_1, T_2]: ((wft(T_1) & wft(T_2)) => (truthPredicate(q_madLove(T_1, T_2)) <=> madLove(eval(T_1), eval(T_2)))))).
fof(schema_A1fin_dead,axiom,(! [T_1]: ((wft(T_1)) => (truthPredicate(q_dead(T_1)) <=> dead(eval(T_1)))))).
fof(schema_A1fin_drinkPotion,axiom,(! [T_1]: ((wft(T_1)) => (truthPredicate(q_drinkPotion(T_1)) <=> drinkPotion(eval(T_1)))))).
fof(schema_A1fin_appearDead,axiom,(! [T_1]: ((wft(T_1)) => (truthPredicate(q_appearDead(T_1)) <=> appearDead(eval(T_1)))))).
fof(schema_A1fin_ist,axiom,(! [T_1, T_2]: ((wft(T_1) & wft(T_2)) => (truthPredicate(q_ist(T_1, T_2)) <=> ist(eval(T_1), eval(T_2)))))).
fof(schema_A2fin,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => (truthPredicate(q_And(T1, T2)) <=> (truthPredicate(T1) & truthPredicate(T2)))))).
fof(schema_A3fin,axiom,(! [T1]: (reach(T1) => (truthPredicate(q_Not(T1)) <=> ~truthPredicate(T1))))).
fof(schema_A4fin_q_VAR_0,axiom,(! [T1]: (reach(T1) => (truthPredicate(q_Forall(q_VAR_0, T1)) <=> (! [X]: truthPredicate(sub(q_VAR_0, quote(X), T1))))))).
fof(schema_A4fin_q_Y,axiom,(! [T1]: (reach(T1) => (truthPredicate(q_Forall(q_Y, T1)) <=> (! [X]: truthPredicate(sub(q_Y, quote(X), T1))))))).
fof(schema_A4fin_q_VAR_2,axiom,(! [T1]: (reach(T1) => (truthPredicate(q_Forall(q_VAR_2, T1)) <=> (! [X]: truthPredicate(sub(q_VAR_2, quote(X), T1))))))).
fof(schema_A4fin_q_x0,axiom,(! [T1]: (reach(T1) => (truthPredicate(q_Forall(q_x0, T1)) <=> (! [X]: truthPredicate(sub(q_x0, quote(X), T1))))))).
fof(schema_A4fin_q_VAR_1,axiom,(! [T1]: (reach(T1) => (truthPredicate(q_Forall(q_VAR_1, T1)) <=> (! [X]: truthPredicate(sub(q_VAR_1, quote(X), T1))))))).
fof(schema_A4fin_q_X,axiom,(! [T1]: (reach(T1) => (truthPredicate(q_Forall(q_X, T1)) <=> (! [X]: truthPredicate(sub(q_X, quote(X), T1))))))).
fof(schema_A5,axiom,(! [Tc, T1, T2]: (ist(Tc, qAnd(T1, T2)) => ist(Tc, T1)))).
fof(schema_A6,axiom,(! [Tc, T1, T2]: (ist(Tc, qAnd(T1, T2)) <=> ist(Tc, qAnd(T2, T1))))).
fof(schema_A7,axiom,(! [Tc, T1]: (ist(Tc, qNot(qNot(T1))) <=> ist(Tc, T1)))).
fof(schema_A8,axiom,(! [Tc, T1, T2, T3]: (ist(Tc, qAnd(qAnd(T1, T2), T3)) <=> ist(Tc, qAnd(T1, qAnd(T2, T3)))))).
fof(schema_A9,axiom,(! [Tc, T1, T2, T3]: (ist(Tc, qOr(qAnd(T1, T2), T3)) <=> ist(Tc, qAnd(qOr(T1, T3), qOr(T2, T3)))))).
fof(schema_A10,axiom,(! [Tc, T1, T2]: ((ist(Tc, qOr(T1, T2)) & ist(Tc, qNot(T1))) => ist(Tc, T2)))).
fof(schema_A11fin,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => (ist(T2, q_Forall(q_VAR_0, T1)) => (! [X]: ist(T2, sub(T1, q_VAR_0, quote(X)))))))).
fof(schema_A11fin,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => (ist(T2, q_Forall(q_Y, T1)) => (! [X]: ist(T2, sub(T1, q_Y, quote(X)))))))).
fof(schema_A11fin,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => (ist(T2, q_Forall(q_VAR_2, T1)) => (! [X]: ist(T2, sub(T1, q_VAR_2, quote(X)))))))).
fof(schema_A11fin,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => (ist(T2, q_Forall(q_x0, T1)) => (! [X]: ist(T2, sub(T1, q_x0, quote(X)))))))).
fof(schema_A11fin,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => (ist(T2, q_Forall(q_VAR_1, T1)) => (! [X]: ist(T2, sub(T1, q_VAR_1, quote(X)))))))).
fof(schema_A11fin,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => (ist(T2, q_Forall(q_X, T1)) => (! [X]: ist(T2, sub(T1, q_X, quote(X)))))))).
fof(schema_A12,axiom,(! [X]: equals(X, X))).
fof(schema_A13,axiom,(! [X, Y]: (equals(X, Y) => equals(Y, X)))).
fof(schema_A14,axiom,(! [X, Y, Z]: ((equals(X, Y) & equals(Y, Z)) => equals(X, Z)))).
fof(schema_A15_say,axiom,(! [X_1, Y_1]: ((equals(X_1, Y_1)) => equals(say(X_1), say(Y_1))))).
fof(schema_A15_bel,axiom,(! [X_1, Y_1]: ((equals(X_1, Y_1)) => equals(bel(X_1), bel(Y_1))))).
fof(schema_A16_madLove,axiom,(! [X_1, X_2, Y_1, Y_2]: ((equals(X_1, Y_1) & equals(X_2, Y_2)) => (madLove(X_1, X_2) <=> madLove(Y_1, Y_2))))).
fof(schema_A16_dead,axiom,(! [X_1, Y_1]: ((equals(X_1, Y_1)) => (dead(X_1) <=> dead(Y_1))))).
fof(schema_A16_drinkPotion,axiom,(! [X_1, Y_1]: ((equals(X_1, Y_1)) => (drinkPotion(X_1) <=> drinkPotion(Y_1))))).
fof(schema_A16_appearDead,axiom,(! [X_1, Y_1]: ((equals(X_1, Y_1)) => (appearDead(X_1) <=> appearDead(Y_1))))).
fof(schema_A16_ist,axiom,(! [X_1, X_2, Y_1, Y_2]: ((equals(X_1, Y_1) & equals(X_2, Y_2)) => (ist(X_1, X_2) <=> ist(Y_1, Y_2))))).
fof(schema_A17,axiom,(! [X]: reach(quote(X)))).
fof(schema_A18_say,axiom,(! [T_1]: ((reach(T_1)) => reach(say(T_1))))).
fof(schema_A18_bel,axiom,(! [T_1]: ((reach(T_1)) => reach(bel(T_1))))).
fof(schema_A18_friar,axiom,reach(friar)).
fof(schema_A18_romeo,axiom,reach(romeo)).
fof(schema_A18_juliet,axiom,reach(juliet)).
fof(schema_A19,axiom,(! [X]: wft(quote(X)))).
fof(schema_A20_q_VAR_0,axiom,wft(q_VAR_0)).
fof(schema_A20_q_Y,axiom,wft(q_Y)).
fof(schema_A20_q_VAR_2,axiom,wft(q_VAR_2)).
fof(schema_A20_q_x0,axiom,wft(q_x0)).
fof(schema_A20_q_VAR_1,axiom,wft(q_VAR_1)).
fof(schema_A20_q_X,axiom,wft(q_X)).
fof(schema_A21_q_romeo,axiom,wft(q_romeo)).
fof(schema_A21_q_juliet,axiom,wft(q_juliet)).
fof(schema_A21_q_friar,axiom,wft(q_friar)).
fof(schema_A21_q_say,axiom,(! [T_1]: ((wft(T_1)) => wft(q_say(T_1))))).
fof(schema_A21_q_bel,axiom,(! [T_1]: ((wft(T_1)) => wft(q_bel(T_1))))).
fof(schema_A22,axiom,(! [T]: (reach(T) => equals(eval(quote(T)), T)))).
fof(schema_A23_say,axiom,(! [T_1]: (reach(T_1) => equals(eval(q_say(T_1)), say(eval(T_1)))))).
fof(schema_A23_bel,axiom,(! [T_1]: (reach(T_1) => equals(eval(q_bel(T_1)), bel(eval(T_1)))))).
fof(schema_A23_friar,axiom,equals(eval(q_friar), friar)).
fof(schema_A23_romeo,axiom,equals(eval(q_romeo), romeo)).
fof(schema_A23_juliet,axiom,equals(eval(q_juliet), juliet)).
fof(schema_A24_madLove,axiom,(! [T_1, T_2]: ((reach(T_1) & reach(T_2)) => equals(eval(q_madLove(T_1, T_2)), q_madLove(T_1, T_2))))).
fof(schema_A24_dead,axiom,(! [T_1]: (reach(T_1) => equals(eval(q_dead(T_1)), q_dead(T_1))))).
fof(schema_A24_drinkPotion,axiom,(! [T_1]: (reach(T_1) => equals(eval(q_drinkPotion(T_1)), q_drinkPotion(T_1))))).
fof(schema_A24_appearDead,axiom,(! [T_1]: (reach(T_1) => equals(eval(q_appearDead(T_1)), q_appearDead(T_1))))).
fof(schema_A24_ist,axiom,(! [T_1, T_2]: ((reach(T_1) & reach(T_2)) => equals(eval(q_ist(T_1, T_2)), q_ist(T_1, T_2))))).
fof(schema_A25,axiom,(! [T1, T2]: equals(eval(q_And(T1, T2)), q_And(T1, T2)))).
fof(schema_A26,axiom,(! [T1, T2]: equals(eval(q_Forall(T1, T2)), q_Forall(T1, T2)))).
fof(schema_A27,axiom,(! [T]: equals(eval(q_Not(T)), q_Not(T)))).
fof(schema_A28q_VAR_0,axiom,equals(eval(q_VAR_0), q_VAR_0)).
fof(schema_A28q_Y,axiom,equals(eval(q_Y), q_Y)).
fof(schema_A28q_VAR_2,axiom,equals(eval(q_VAR_2), q_VAR_2)).
fof(schema_A28q_x0,axiom,equals(eval(q_x0), q_x0)).
fof(schema_A28q_VAR_1,axiom,equals(eval(q_VAR_1), q_VAR_1)).
fof(schema_A28q_X,axiom,equals(eval(q_X), q_X)).
fof(schema_A29_q_VAR_0,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_0, q_VAR_0, T), T)))).
fof(schema_A29_q_Y,axiom,(! [T]: (reach(T) => equals(sub(q_Y, q_Y, T), T)))).
fof(schema_A29_q_VAR_2,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_2, q_VAR_2, T), T)))).
fof(schema_A29_q_x0,axiom,(! [T]: (reach(T) => equals(sub(q_x0, q_x0, T), T)))).
fof(schema_A29_q_VAR_1,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_1, q_VAR_1, T), T)))).
fof(schema_A29_q_X,axiom,(! [T]: (reach(T) => equals(sub(q_X, q_X, T), T)))).
fof(schema_A30_q_VAR_0_q_Y,axiom,(! [T]: (reach(T) => equals(sub(q_Y, q_VAR_0, T), q_Y)))).
fof(schema_A30_q_VAR_0_q_VAR_2,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_2, q_VAR_0, T), q_VAR_2)))).
fof(schema_A30_q_VAR_0_q_x0,axiom,(! [T]: (reach(T) => equals(sub(q_x0, q_VAR_0, T), q_x0)))).
fof(schema_A30_q_VAR_0_q_VAR_1,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_1, q_VAR_0, T), q_VAR_1)))).
fof(schema_A30_q_VAR_0_q_X,axiom,(! [T]: (reach(T) => equals(sub(q_X, q_VAR_0, T), q_X)))).
fof(schema_A30_q_Y_q_VAR_0,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_0, q_Y, T), q_VAR_0)))).
fof(schema_A30_q_Y_q_VAR_2,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_2, q_Y, T), q_VAR_2)))).
fof(schema_A30_q_Y_q_x0,axiom,(! [T]: (reach(T) => equals(sub(q_x0, q_Y, T), q_x0)))).
fof(schema_A30_q_Y_q_VAR_1,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_1, q_Y, T), q_VAR_1)))).
fof(schema_A30_q_Y_q_X,axiom,(! [T]: (reach(T) => equals(sub(q_X, q_Y, T), q_X)))).
fof(schema_A30_q_VAR_2_q_VAR_0,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_0, q_VAR_2, T), q_VAR_0)))).
fof(schema_A30_q_VAR_2_q_Y,axiom,(! [T]: (reach(T) => equals(sub(q_Y, q_VAR_2, T), q_Y)))).
fof(schema_A30_q_VAR_2_q_x0,axiom,(! [T]: (reach(T) => equals(sub(q_x0, q_VAR_2, T), q_x0)))).
fof(schema_A30_q_VAR_2_q_VAR_1,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_1, q_VAR_2, T), q_VAR_1)))).
fof(schema_A30_q_VAR_2_q_X,axiom,(! [T]: (reach(T) => equals(sub(q_X, q_VAR_2, T), q_X)))).
fof(schema_A30_q_x0_q_VAR_0,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_0, q_x0, T), q_VAR_0)))).
fof(schema_A30_q_x0_q_Y,axiom,(! [T]: (reach(T) => equals(sub(q_Y, q_x0, T), q_Y)))).
fof(schema_A30_q_x0_q_VAR_2,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_2, q_x0, T), q_VAR_2)))).
fof(schema_A30_q_x0_q_VAR_1,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_1, q_x0, T), q_VAR_1)))).
fof(schema_A30_q_x0_q_X,axiom,(! [T]: (reach(T) => equals(sub(q_X, q_x0, T), q_X)))).
fof(schema_A30_q_VAR_1_q_VAR_0,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_0, q_VAR_1, T), q_VAR_0)))).
fof(schema_A30_q_VAR_1_q_Y,axiom,(! [T]: (reach(T) => equals(sub(q_Y, q_VAR_1, T), q_Y)))).
fof(schema_A30_q_VAR_1_q_VAR_2,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_2, q_VAR_1, T), q_VAR_2)))).
fof(schema_A30_q_VAR_1_q_x0,axiom,(! [T]: (reach(T) => equals(sub(q_x0, q_VAR_1, T), q_x0)))).
fof(schema_A30_q_VAR_1_q_X,axiom,(! [T]: (reach(T) => equals(sub(q_X, q_VAR_1, T), q_X)))).
fof(schema_A30_q_X_q_VAR_0,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_0, q_X, T), q_VAR_0)))).
fof(schema_A30_q_X_q_Y,axiom,(! [T]: (reach(T) => equals(sub(q_Y, q_X, T), q_Y)))).
fof(schema_A30_q_X_q_VAR_2,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_2, q_X, T), q_VAR_2)))).
fof(schema_A30_q_X_q_x0,axiom,(! [T]: (reach(T) => equals(sub(q_x0, q_X, T), q_x0)))).
fof(schema_A30_q_X_q_VAR_1,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_1, q_X, T), q_VAR_1)))).
fof(schema_A31_q_VAR_0_q_say,axiom,(! [T, T_1]: ((reach(T_1)) => equals(sub(q_say(T_1), q_VAR_0, T), q_say(sub(T_1, q_VAR_0, T)))))).
fof(schema_A31_q_VAR_0_q_bel,axiom,(! [T, T_1]: ((reach(T_1)) => equals(sub(q_bel(T_1), q_VAR_0, T), q_bel(sub(T_1, q_VAR_0, T)))))).
fof(schema_A31_q_Y_q_say,axiom,(! [T, T_1]: ((reach(T_1)) => equals(sub(q_say(T_1), q_Y, T), q_say(sub(T_1, q_Y, T)))))).
fof(schema_A31_q_Y_q_bel,axiom,(! [T, T_1]: ((reach(T_1)) => equals(sub(q_bel(T_1), q_Y, T), q_bel(sub(T_1, q_Y, T)))))).
fof(schema_A31_q_VAR_2_q_say,axiom,(! [T, T_1]: ((reach(T_1)) => equals(sub(q_say(T_1), q_VAR_2, T), q_say(sub(T_1, q_VAR_2, T)))))).
fof(schema_A31_q_VAR_2_q_bel,axiom,(! [T, T_1]: ((reach(T_1)) => equals(sub(q_bel(T_1), q_VAR_2, T), q_bel(sub(T_1, q_VAR_2, T)))))).
fof(schema_A31_q_x0_q_say,axiom,(! [T, T_1]: ((reach(T_1)) => equals(sub(q_say(T_1), q_x0, T), q_say(sub(T_1, q_x0, T)))))).
fof(schema_A31_q_x0_q_bel,axiom,(! [T, T_1]: ((reach(T_1)) => equals(sub(q_bel(T_1), q_x0, T), q_bel(sub(T_1, q_x0, T)))))).
fof(schema_A31_q_VAR_1_q_say,axiom,(! [T, T_1]: ((reach(T_1)) => equals(sub(q_say(T_1), q_VAR_1, T), q_say(sub(T_1, q_VAR_1, T)))))).
fof(schema_A31_q_VAR_1_q_bel,axiom,(! [T, T_1]: ((reach(T_1)) => equals(sub(q_bel(T_1), q_VAR_1, T), q_bel(sub(T_1, q_VAR_1, T)))))).
fof(schema_A31_q_X_q_say,axiom,(! [T, T_1]: ((reach(T_1)) => equals(sub(q_say(T_1), q_X, T), q_say(sub(T_1, q_X, T)))))).
fof(schema_A31_q_X_q_bel,axiom,(! [T, T_1]: ((reach(T_1)) => equals(sub(q_bel(T_1), q_X, T), q_bel(sub(T_1, q_X, T)))))).
fof(schema_43_q_VAR_0_friar,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_0, T, q_friar), q_friar)))).
fof(schema_43_q_VAR_0_romeo,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_0, T, q_romeo), q_romeo)))).
fof(schema_43_q_VAR_0_juliet,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_0, T, q_juliet), q_juliet)))).
fof(schema_43_q_Y_friar,axiom,(! [T]: (reach(T) => equals(sub(q_Y, T, q_friar), q_friar)))).
fof(schema_43_q_Y_romeo,axiom,(! [T]: (reach(T) => equals(sub(q_Y, T, q_romeo), q_romeo)))).
fof(schema_43_q_Y_juliet,axiom,(! [T]: (reach(T) => equals(sub(q_Y, T, q_juliet), q_juliet)))).
fof(schema_43_q_VAR_2_friar,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_2, T, q_friar), q_friar)))).
fof(schema_43_q_VAR_2_romeo,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_2, T, q_romeo), q_romeo)))).
fof(schema_43_q_VAR_2_juliet,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_2, T, q_juliet), q_juliet)))).
fof(schema_43_q_x0_friar,axiom,(! [T]: (reach(T) => equals(sub(q_x0, T, q_friar), q_friar)))).
fof(schema_43_q_x0_romeo,axiom,(! [T]: (reach(T) => equals(sub(q_x0, T, q_romeo), q_romeo)))).
fof(schema_43_q_x0_juliet,axiom,(! [T]: (reach(T) => equals(sub(q_x0, T, q_juliet), q_juliet)))).
fof(schema_43_q_VAR_1_friar,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_1, T, q_friar), q_friar)))).
fof(schema_43_q_VAR_1_romeo,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_1, T, q_romeo), q_romeo)))).
fof(schema_43_q_VAR_1_juliet,axiom,(! [T]: (reach(T) => equals(sub(q_VAR_1, T, q_juliet), q_juliet)))).
fof(schema_43_q_X_friar,axiom,(! [T]: (reach(T) => equals(sub(q_X, T, q_friar), q_friar)))).
fof(schema_43_q_X_romeo,axiom,(! [T]: (reach(T) => equals(sub(q_X, T, q_romeo), q_romeo)))).
fof(schema_43_q_X_juliet,axiom,(! [T]: (reach(T) => equals(sub(q_X, T, q_juliet), q_juliet)))).
fof(schema_A32_q_VAR_0,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_X, T1, q_Forall(q_X, T2)), q_Forall(q_X, T2))))).
fof(schema_A32_q_Y,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_X, T1, q_Forall(q_X, T2)), q_Forall(q_X, T2))))).
fof(schema_A32_q_VAR_2,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_X, T1, q_Forall(q_X, T2)), q_Forall(q_X, T2))))).
fof(schema_A32_q_x0,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_X, T1, q_Forall(q_X, T2)), q_Forall(q_X, T2))))).
fof(schema_A32_q_VAR_1,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_X, T1, q_Forall(q_X, T2)), q_Forall(q_X, T2))))).
fof(schema_A32_q_X,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_X, T1, q_Forall(q_X, T2)), q_Forall(q_X, T2))))).
fof(schema_A33_q_VAR_0_q_Y,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_VAR_0, T1, q_Forall(q_Y, T2)), q_Forall(q_Y, sub(q_VAR_0, T1, T2)))))).
fof(schema_A33_q_VAR_0_q_VAR_2,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_VAR_0, T1, q_Forall(q_VAR_2, T2)), q_Forall(q_VAR_2, sub(q_VAR_0, T1, T2)))))).
fof(schema_A33_q_VAR_0_q_x0,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_VAR_0, T1, q_Forall(q_x0, T2)), q_Forall(q_x0, sub(q_VAR_0, T1, T2)))))).
fof(schema_A33_q_VAR_0_q_VAR_1,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_VAR_0, T1, q_Forall(q_VAR_1, T2)), q_Forall(q_VAR_1, sub(q_VAR_0, T1, T2)))))).
fof(schema_A33_q_VAR_0_q_X,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_VAR_0, T1, q_Forall(q_X, T2)), q_Forall(q_X, sub(q_VAR_0, T1, T2)))))).
fof(schema_A33_q_Y_q_VAR_0,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_Y, T1, q_Forall(q_VAR_0, T2)), q_Forall(q_VAR_0, sub(q_Y, T1, T2)))))).
fof(schema_A33_q_Y_q_VAR_2,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_Y, T1, q_Forall(q_VAR_2, T2)), q_Forall(q_VAR_2, sub(q_Y, T1, T2)))))).
fof(schema_A33_q_Y_q_x0,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_Y, T1, q_Forall(q_x0, T2)), q_Forall(q_x0, sub(q_Y, T1, T2)))))).
fof(schema_A33_q_Y_q_VAR_1,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_Y, T1, q_Forall(q_VAR_1, T2)), q_Forall(q_VAR_1, sub(q_Y, T1, T2)))))).
fof(schema_A33_q_Y_q_X,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_Y, T1, q_Forall(q_X, T2)), q_Forall(q_X, sub(q_Y, T1, T2)))))).
fof(schema_A33_q_VAR_2_q_VAR_0,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_VAR_2, T1, q_Forall(q_VAR_0, T2)), q_Forall(q_VAR_0, sub(q_VAR_2, T1, T2)))))).
fof(schema_A33_q_VAR_2_q_Y,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_VAR_2, T1, q_Forall(q_Y, T2)), q_Forall(q_Y, sub(q_VAR_2, T1, T2)))))).
fof(schema_A33_q_VAR_2_q_x0,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_VAR_2, T1, q_Forall(q_x0, T2)), q_Forall(q_x0, sub(q_VAR_2, T1, T2)))))).
fof(schema_A33_q_VAR_2_q_VAR_1,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_VAR_2, T1, q_Forall(q_VAR_1, T2)), q_Forall(q_VAR_1, sub(q_VAR_2, T1, T2)))))).
fof(schema_A33_q_VAR_2_q_X,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_VAR_2, T1, q_Forall(q_X, T2)), q_Forall(q_X, sub(q_VAR_2, T1, T2)))))).
fof(schema_A33_q_x0_q_VAR_0,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_x0, T1, q_Forall(q_VAR_0, T2)), q_Forall(q_VAR_0, sub(q_x0, T1, T2)))))).
fof(schema_A33_q_x0_q_Y,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_x0, T1, q_Forall(q_Y, T2)), q_Forall(q_Y, sub(q_x0, T1, T2)))))).
fof(schema_A33_q_x0_q_VAR_2,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_x0, T1, q_Forall(q_VAR_2, T2)), q_Forall(q_VAR_2, sub(q_x0, T1, T2)))))).
fof(schema_A33_q_x0_q_VAR_1,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_x0, T1, q_Forall(q_VAR_1, T2)), q_Forall(q_VAR_1, sub(q_x0, T1, T2)))))).
fof(schema_A33_q_x0_q_X,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_x0, T1, q_Forall(q_X, T2)), q_Forall(q_X, sub(q_x0, T1, T2)))))).
fof(schema_A33_q_VAR_1_q_VAR_0,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_VAR_1, T1, q_Forall(q_VAR_0, T2)), q_Forall(q_VAR_0, sub(q_VAR_1, T1, T2)))))).
fof(schema_A33_q_VAR_1_q_Y,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_VAR_1, T1, q_Forall(q_Y, T2)), q_Forall(q_Y, sub(q_VAR_1, T1, T2)))))).
fof(schema_A33_q_VAR_1_q_VAR_2,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_VAR_1, T1, q_Forall(q_VAR_2, T2)), q_Forall(q_VAR_2, sub(q_VAR_1, T1, T2)))))).
fof(schema_A33_q_VAR_1_q_x0,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_VAR_1, T1, q_Forall(q_x0, T2)), q_Forall(q_x0, sub(q_VAR_1, T1, T2)))))).
fof(schema_A33_q_VAR_1_q_X,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_VAR_1, T1, q_Forall(q_X, T2)), q_Forall(q_X, sub(q_VAR_1, T1, T2)))))).
fof(schema_A33_q_X_q_VAR_0,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_X, T1, q_Forall(q_VAR_0, T2)), q_Forall(q_VAR_0, sub(q_X, T1, T2)))))).
fof(schema_A33_q_X_q_Y,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_X, T1, q_Forall(q_Y, T2)), q_Forall(q_Y, sub(q_X, T1, T2)))))).
fof(schema_A33_q_X_q_VAR_2,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_X, T1, q_Forall(q_VAR_2, T2)), q_Forall(q_VAR_2, sub(q_X, T1, T2)))))).
fof(schema_A33_q_X_q_x0,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_X, T1, q_Forall(q_x0, T2)), q_Forall(q_x0, sub(q_X, T1, T2)))))).
fof(schema_A33_q_X_q_VAR_1,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_X, T1, q_Forall(q_VAR_1, T2)), q_Forall(q_VAR_1, sub(q_X, T1, T2)))))).
fof(schema_A34_q_VAR_0,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_VAR_0, T1, quote(T2)), quote(T2))))).
fof(schema_A34_q_Y,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_Y, T1, quote(T2)), quote(T2))))).
fof(schema_A34_q_VAR_2,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_VAR_2, T1, quote(T2)), quote(T2))))).
fof(schema_A34_q_x0,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_x0, T1, quote(T2)), quote(T2))))).
fof(schema_A34_q_VAR_1,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_VAR_1, T1, quote(T2)), quote(T2))))).
fof(schema_A34_q_X,axiom,(! [T1, T2]: ((reach(T1) & reach(T2)) => equals(sub(q_X, T1, quote(T2)), quote(T2))))).