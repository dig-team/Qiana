fof(h0,axiom,
    ist(wrote(nadim), q_Forall(q_x0, q_Not(q_And(q_contemporary(q_x0, rhazes),q_Not(q_ist(q_believes(q_x0), q_transmutates(rhazes, copper)))))))
).

fof(h1,axiom,
    ! [X] :
        (ist(wrote(nadim), X) => truthPredicate(X))
).

fof(h2,axiom,
    contemporary(alice,rhazes)
).

%---- Declaration of the predicate transmutates
fof(trivial_arity_2, axiom, ![X1,X2] : transmutates(X1, X2) => transmutates(X1,X2)).

%---- Bogus hypthesis that is proven right
fof(h3,axiom,
    ~ ist(believes(alice), q_believes(alice))
).

fof(axiom5,axiom,![XC, X1, X2] :(ist(XC, q_And(X1, X2)) => (ist(XC, X1) & ist(XC, X2)))).
fof(axiom6,axiom,![XC, X1, X2] :(ist(XC, q_And(X1, X2)) <=> ist(XC, q_And(X2, X1)))).
fof(axiom7,axiom,![XC, X1] :(ist(XC, q_Neg(q_Neg(X1))) <=> ist(XC, X1))).
fof(axiom8,axiom,![XC, X1, X2, X3] :(ist(XC, q_And(q_And(X1, X2), X3)) <=> ist(XC, q_And(X1, q_And(X2, X3))))).
fof(axiom9,axiom,![XC, X1, X2, X3] :(ist(XC, q_Or(q_And(X1, X2), X3)) <=> ist(XC, q_And(q_Or(X1, X3), q_Or(X2, X3))))).
fof(axiom10,axiom,![XC, X1, X2] :((ist(XC, q_Or(X1, X2)) & ist(XC, q_Neg(X1))) => ist(XC, X2))).
fof(axiom12,axiom,![X1] :(X1 = X1)).
fof(axiom13,axiom,![X1, X2] :(X1 = X2 => X2 = X1)).
fof(axiom14,axiom,![X1, X2, X3] :((X1 = X2 & X2 = X3) => X1 = X3)).
fof(axiom15_wrote,axiom,![X1,Y1] :((X1 = Y1) => wrote(X1) = wrote(Y1))).
fof(axiom15_believes,axiom,![X1,Y1] :((X1 = Y1) => believes(X1) = believes(Y1))).
fof(axiom15_q_wrote,axiom,![X1,Y1] :((X1 = Y1) => q_wrote(X1) = q_wrote(Y1))).
fof(axiom15_q_believes,axiom,![X1,Y1] :((X1 = Y1) => q_believes(X1) = q_believes(Y1))).
fof(axiom15_q_ist,axiom,![X1,X2,Y1,Y2] :((X1 = Y1&X2 = Y2) => q_ist(X1,X2) = q_ist(Y1,Y2))).
fof(axiom15_q_truthPredicate,axiom,![X1,Y1] :((X1 = Y1) => q_truthPredicate(X1) = q_truthPredicate(Y1))).
fof(axiom15_q_contemporary,axiom,![X1,X2,Y1,Y2] :((X1 = Y1&X2 = Y2) => q_contemporary(X1,X2) = q_contemporary(Y1,Y2))).
fof(axiom15_q_transmutates,axiom,![X1,X2,Y1,Y2] :((X1 = Y1&X2 = Y2) => q_transmutates(X1,X2) = q_transmutates(Y1,Y2))).
fof(axiom15_q_Quote,axiom,![X1,Y1] :((X1 = Y1) => q_Quote(X1) = q_Quote(Y1))).
fof(axiom15_q_Neg,axiom,![X1,Y1] :((X1 = Y1) => q_Neg(X1) = q_Neg(Y1))).
fof(axiom15_q_And,axiom,![X1,X2,Y1,Y2] :((X1 = Y1&X2 = Y2) => q_And(X1,X2) = q_And(Y1,Y2))).
fof(axiom15_q_Or,axiom,![X1,X2,Y1,Y2] :((X1 = Y1&X2 = Y2) => q_Or(X1,X2) = q_Or(Y1,Y2))).
fof(axiom15_q_Forall,axiom,![X1,X2,Y1,Y2] :((X1 = Y1&X2 = Y2) => q_Forall(X1,X2) = q_Forall(Y1,Y2))).
fof(axiom15_const_nadim,axiom,nadim = nadim).
fof(axiom15_const_rhazes,axiom,rhazes = rhazes).
fof(axiom15_const_copper,axiom,copper = copper).
fof(axiom15_const_alice,axiom,alice = alice).
fof(axiom15_const_q_nadim,axiom,q_nadim = q_nadim).
fof(axiom15_const_q_rhazes,axiom,q_rhazes = q_rhazes).
fof(axiom15_const_q_copper,axiom,q_copper = q_copper).
fof(axiom15_const_q_alice,axiom,q_alice = q_alice).
fof(axiom15_const_q_X1,axiom,q_X1 = q_X1).
fof(axiom15_const_q_X2,axiom,q_X2 = q_X2).
fof(axiom15_const_q_X3,axiom,q_X3 = q_X3).
fof(axiom15_const_q_X4,axiom,q_X4 = q_X4).
fof(axiom15_const_q_X5,axiom,q_X5 = q_X5).
fof(axiom16_ist,axiom,![X1,X2,Y1,Y2] :((X1 = Y1&X2 = Y2) => (ist(X1,X2) <=> ist(Y1,Y2)))).
fof(axiom16_truthPredicate,axiom,![X1,Y1] :((X1 = Y1) => (truthPredicate(X1) <=> truthPredicate(Y1)))).
fof(axiom16_contemporary,axiom,![X1,X2,Y1,Y2] :((X1 = Y1&X2 = Y2) => (contemporary(X1,X2) <=> contemporary(Y1,Y2)))).
fof(axiom16_transmutates,axiom,![X1,X2,Y1,Y2] :((X1 = Y1&X2 = Y2) => (transmutates(X1,X2) <=> transmutates(Y1,Y2)))).
fof(axiom16_q_Truth,axiom,![X1,Y1] :((X1 = Y1) => (q_Truth(X1) <=> q_Truth(Y1)))).
fof(axiom17,axiom,![X1] :(q_Term(q_Quote(X1)))).
fof(axiom18_wrote,axiom,![X1] :((q_Term(X1)) => q_Term(wrote(X1)))).
fof(axiom18_believes,axiom,![X1] :((q_Term(X1)) => q_Term(believes(X1)))).
fof(axiom18_q_wrote,axiom,![X1] :((q_Term(X1)) => q_Term(q_wrote(X1)))).
fof(axiom18_q_believes,axiom,![X1] :((q_Term(X1)) => q_Term(q_believes(X1)))).
fof(axiom18_q_ist,axiom,![X1,X2] :((q_Term(X1)&q_Term(X2)) => q_Term(q_ist(X1,X2)))).
fof(axiom18_q_truthPredicate,axiom,![X1] :((q_Term(X1)) => q_Term(q_truthPredicate(X1)))).
fof(axiom18_q_contemporary,axiom,![X1,X2] :((q_Term(X1)&q_Term(X2)) => q_Term(q_contemporary(X1,X2)))).
fof(axiom18_q_transmutates,axiom,![X1,X2] :((q_Term(X1)&q_Term(X2)) => q_Term(q_transmutates(X1,X2)))).
fof(axiom18_q_Quote,axiom,![X1] :((q_Term(X1)) => q_Term(q_Quote(X1)))).
fof(axiom18_q_Neg,axiom,![X1] :((q_Term(X1)) => q_Term(q_Neg(X1)))).
fof(axiom18_q_And,axiom,![X1,X2] :((q_Term(X1)&q_Term(X2)) => q_Term(q_And(X1,X2)))).
fof(axiom18_q_Or,axiom,![X1,X2] :((q_Term(X1)&q_Term(X2)) => q_Term(q_Or(X1,X2)))).
fof(axiom18_q_Forall,axiom,![X1,X2] :((q_Term(X1)&q_Term(X2)) => q_Term(q_Forall(X1,X2)))).
fof(axiom18_const_nadim,axiom,q_Term(nadim)).
fof(axiom18_const_rhazes,axiom,q_Term(rhazes)).
fof(axiom18_const_copper,axiom,q_Term(copper)).
fof(axiom18_const_alice,axiom,q_Term(alice)).
fof(axiom18_const_q_nadim,axiom,q_Term(q_nadim)).
fof(axiom18_const_q_rhazes,axiom,q_Term(q_rhazes)).
fof(axiom18_const_q_copper,axiom,q_Term(q_copper)).
fof(axiom18_const_q_alice,axiom,q_Term(q_alice)).
fof(axiom18_const_q_X1,axiom,q_Term(q_X1)).
fof(axiom18_const_q_X2,axiom,q_Term(q_X2)).
fof(axiom18_const_q_X3,axiom,q_Term(q_X3)).
fof(axiom18_const_q_X4,axiom,q_Term(q_X4)).
fof(axiom18_const_q_X5,axiom,q_Term(q_X5)).
fof(axiom18_quoted_vars_q_X1,axiom,q_Term(q_X1)).
fof(axiom18_quoted_vars_q_X2,axiom,q_Term(q_X2)).
fof(axiom18_quoted_vars_q_X3,axiom,q_Term(q_X3)).
fof(axiom18_quoted_vars_q_X4,axiom,q_Term(q_X4)).
fof(axiom18_quoted_vars_q_X5,axiom,q_Term(q_X5)).
fof(axiom19,axiom,![X1] :(q_Wft(q_Quote(X1)))).
fof(axiom20_q_X1,axiom,q_Wft(q_X1)).
fof(axiom20_q_X2,axiom,q_Wft(q_X2)).
fof(axiom20_q_X3,axiom,q_Wft(q_X3)).
fof(axiom20_q_X4,axiom,q_Wft(q_X4)).
fof(axiom20_q_X5,axiom,q_Wft(q_X5)).
fof(axiom21_wrote_q_wrote,axiom,![X1] :((q_Wft(X1)) => q_Wft(q_wrote(X1)))).
fof(axiom21_believes_q_believes,axiom,![X1] :((q_Wft(X1)) => q_Wft(q_believes(X1)))).
fof(axiom21_const_nadim_q_nadim,axiom,q_Wft(q_nadim)).
fof(axiom21_const_rhazes_q_rhazes,axiom,q_Wft(q_rhazes)).
fof(axiom21_const_copper_q_copper,axiom,q_Wft(q_copper)).
fof(axiom21_const_alice_q_alice,axiom,q_Wft(q_alice)).
fof(axiom22,axiom,![X1] :(q_Eval(q_Quote(X1)) = X1)).
fof(axiom23_wrote_q_wrote,axiom,![X1] :((q_Term(X1)) => q_Eval(q_wrote(X1)) = wrote(q_Eval(X1)))).
fof(axiom23_believes_q_believes,axiom,![X1] :((q_Term(X1)) => q_Eval(q_believes(X1)) = believes(q_Eval(X1)))).
fof(axiom23_const_nadim_q_nadim,axiom,q_Eval(q_nadim) = nadim).
fof(axiom23_const_rhazes_q_rhazes,axiom,q_Eval(q_rhazes) = rhazes).
fof(axiom23_const_copper_q_copper,axiom,q_Eval(q_copper) = copper).
fof(axiom23_const_alice_q_alice,axiom,q_Eval(q_alice) = alice).
fof(axiom24_ist_q_ist,axiom,![X1,X2] :((q_Term(X1)&q_Term(X2)) => q_Eval(q_ist(X1,X2)) = q_ist(X1,X2))).
fof(axiom24_truthPredicate_q_truthPredicate,axiom,![X1] :((q_Term(X1)) => q_Eval(q_truthPredicate(X1)) = q_truthPredicate(X1))).
fof(axiom24_contemporary_q_contemporary,axiom,![X1,X2] :((q_Term(X1)&q_Term(X2)) => q_Eval(q_contemporary(X1,X2)) = q_contemporary(X1,X2))).
fof(axiom24_transmutates_q_transmutates,axiom,![X1,X2] :((q_Term(X1)&q_Term(X2)) => q_Eval(q_transmutates(X1,X2)) = q_transmutates(X1,X2))).
fof(axiom25,axiom,![X1, X2] :(q_Eval(q_And(X1, X2)) = q_And(X1, X2))).
fof(axiom26,axiom,![X1, X2] :(q_Eval(q_Forall(X1, X2)) = q_Forall(X1, X2))).
fof(axiom27,axiom,![X1] :(q_Eval(q_Neg(X1)) = q_Neg(X1))).
fof(axiom28_q_X1,axiom,(q_Eval(q_X1) = q_X1)).
fof(axiom28_q_X2,axiom,(q_Eval(q_X2) = q_X2)).
fof(axiom28_q_X3,axiom,(q_Eval(q_X3) = q_X3)).
fof(axiom28_q_X4,axiom,(q_Eval(q_X4) = q_X4)).
fof(axiom28_q_X5,axiom,(q_Eval(q_X5) = q_X5)).
fof(axiom29_q_X1,axiom,![X3] :(q_Term(X3) => q_Sub(q_X1, q_X1, X3) = X3)).
fof(axiom29_q_X2,axiom,![X3] :(q_Term(X3) => q_Sub(q_X2, q_X2, X3) = X3)).
fof(axiom29_q_X3,axiom,![X3] :(q_Term(X3) => q_Sub(q_X3, q_X3, X3) = X3)).
fof(axiom29_q_X4,axiom,![X3] :(q_Term(X3) => q_Sub(q_X4, q_X4, X3) = X3)).
fof(axiom29_q_X5,axiom,![X3] :(q_Term(X3) => q_Sub(q_X5, q_X5, X3) = X3)).
fof(axiom30_q_X1_q_X2,axiom,![X3] :(q_Term(X3) => q_Sub(q_X1, q_X2, X3) = q_X1)).
fof(axiom30_q_X1_q_X3,axiom,![X3] :(q_Term(X3) => q_Sub(q_X1, q_X3, X3) = q_X1)).
fof(axiom30_q_X1_q_X4,axiom,![X3] :(q_Term(X3) => q_Sub(q_X1, q_X4, X3) = q_X1)).
fof(axiom30_q_X1_q_X5,axiom,![X3] :(q_Term(X3) => q_Sub(q_X1, q_X5, X3) = q_X1)).
fof(axiom30_q_X2_q_X1,axiom,![X3] :(q_Term(X3) => q_Sub(q_X2, q_X1, X3) = q_X2)).
fof(axiom30_q_X2_q_X3,axiom,![X3] :(q_Term(X3) => q_Sub(q_X2, q_X3, X3) = q_X2)).
fof(axiom30_q_X2_q_X4,axiom,![X3] :(q_Term(X3) => q_Sub(q_X2, q_X4, X3) = q_X2)).
fof(axiom30_q_X2_q_X5,axiom,![X3] :(q_Term(X3) => q_Sub(q_X2, q_X5, X3) = q_X2)).
fof(axiom30_q_X3_q_X1,axiom,![X3] :(q_Term(X3) => q_Sub(q_X3, q_X1, X3) = q_X3)).
fof(axiom30_q_X3_q_X2,axiom,![X3] :(q_Term(X3) => q_Sub(q_X3, q_X2, X3) = q_X3)).
fof(axiom30_q_X3_q_X4,axiom,![X3] :(q_Term(X3) => q_Sub(q_X3, q_X4, X3) = q_X3)).
fof(axiom30_q_X3_q_X5,axiom,![X3] :(q_Term(X3) => q_Sub(q_X3, q_X5, X3) = q_X3)).
fof(axiom30_q_X4_q_X1,axiom,![X3] :(q_Term(X3) => q_Sub(q_X4, q_X1, X3) = q_X4)).
fof(axiom30_q_X4_q_X2,axiom,![X3] :(q_Term(X3) => q_Sub(q_X4, q_X2, X3) = q_X4)).
fof(axiom30_q_X4_q_X3,axiom,![X3] :(q_Term(X3) => q_Sub(q_X4, q_X3, X3) = q_X4)).
fof(axiom30_q_X4_q_X5,axiom,![X3] :(q_Term(X3) => q_Sub(q_X4, q_X5, X3) = q_X4)).
fof(axiom30_q_X5_q_X1,axiom,![X3] :(q_Term(X3) => q_Sub(q_X5, q_X1, X3) = q_X5)).
fof(axiom30_q_X5_q_X2,axiom,![X3] :(q_Term(X3) => q_Sub(q_X5, q_X2, X3) = q_X5)).
fof(axiom30_q_X5_q_X3,axiom,![X3] :(q_Term(X3) => q_Sub(q_X5, q_X3, X3) = q_X5)).
fof(axiom30_q_X5_q_X4,axiom,![X3] :(q_Term(X3) => q_Sub(q_X5, q_X4, X3) = q_X5)).
fof(axiom31_wrote_q_X1,axiom,![X1, Y1] :((q_Term(X1)) => q_Sub(wrote(X1), q_X1, Y1) = wrote(q_Sub(X1, q_X1, Y1)))).
fof(axiom31_wrote_q_X2,axiom,![X1, Y1] :((q_Term(X1)) => q_Sub(wrote(X1), q_X2, Y1) = wrote(q_Sub(X1, q_X2, Y1)))).
fof(axiom31_wrote_q_X3,axiom,![X1, Y1] :((q_Term(X1)) => q_Sub(wrote(X1), q_X3, Y1) = wrote(q_Sub(X1, q_X3, Y1)))).
fof(axiom31_wrote_q_X4,axiom,![X1, Y1] :((q_Term(X1)) => q_Sub(wrote(X1), q_X4, Y1) = wrote(q_Sub(X1, q_X4, Y1)))).
fof(axiom31_wrote_q_X5,axiom,![X1, Y1] :((q_Term(X1)) => q_Sub(wrote(X1), q_X5, Y1) = wrote(q_Sub(X1, q_X5, Y1)))).
fof(axiom31_believes_q_X1,axiom,![X1, Y1] :((q_Term(X1)) => q_Sub(believes(X1), q_X1, Y1) = believes(q_Sub(X1, q_X1, Y1)))).
fof(axiom31_believes_q_X2,axiom,![X1, Y1] :((q_Term(X1)) => q_Sub(believes(X1), q_X2, Y1) = believes(q_Sub(X1, q_X2, Y1)))).
fof(axiom31_believes_q_X3,axiom,![X1, Y1] :((q_Term(X1)) => q_Sub(believes(X1), q_X3, Y1) = believes(q_Sub(X1, q_X3, Y1)))).
fof(axiom31_believes_q_X4,axiom,![X1, Y1] :((q_Term(X1)) => q_Sub(believes(X1), q_X4, Y1) = believes(q_Sub(X1, q_X4, Y1)))).
fof(axiom31_believes_q_X5,axiom,![X1, Y1] :((q_Term(X1)) => q_Sub(believes(X1), q_X5, Y1) = believes(q_Sub(X1, q_X5, Y1)))).
fof(axiom31_q_wrote_q_X1,axiom,![X1, Y1] :((q_Term(X1)) => q_Sub(q_wrote(X1), q_X1, Y1) = q_wrote(q_Sub(X1, q_X1, Y1)))).
fof(axiom31_q_wrote_q_X2,axiom,![X1, Y1] :((q_Term(X1)) => q_Sub(q_wrote(X1), q_X2, Y1) = q_wrote(q_Sub(X1, q_X2, Y1)))).
fof(axiom31_q_wrote_q_X3,axiom,![X1, Y1] :((q_Term(X1)) => q_Sub(q_wrote(X1), q_X3, Y1) = q_wrote(q_Sub(X1, q_X3, Y1)))).
fof(axiom31_q_wrote_q_X4,axiom,![X1, Y1] :((q_Term(X1)) => q_Sub(q_wrote(X1), q_X4, Y1) = q_wrote(q_Sub(X1, q_X4, Y1)))).
fof(axiom31_q_wrote_q_X5,axiom,![X1, Y1] :((q_Term(X1)) => q_Sub(q_wrote(X1), q_X5, Y1) = q_wrote(q_Sub(X1, q_X5, Y1)))).
fof(axiom31_q_believes_q_X1,axiom,![X1, Y1] :((q_Term(X1)) => q_Sub(q_believes(X1), q_X1, Y1) = q_believes(q_Sub(X1, q_X1, Y1)))).
fof(axiom31_q_believes_q_X2,axiom,![X1, Y1] :((q_Term(X1)) => q_Sub(q_believes(X1), q_X2, Y1) = q_believes(q_Sub(X1, q_X2, Y1)))).
fof(axiom31_q_believes_q_X3,axiom,![X1, Y1] :((q_Term(X1)) => q_Sub(q_believes(X1), q_X3, Y1) = q_believes(q_Sub(X1, q_X3, Y1)))).
fof(axiom31_q_believes_q_X4,axiom,![X1, Y1] :((q_Term(X1)) => q_Sub(q_believes(X1), q_X4, Y1) = q_believes(q_Sub(X1, q_X4, Y1)))).
fof(axiom31_q_believes_q_X5,axiom,![X1, Y1] :((q_Term(X1)) => q_Sub(q_believes(X1), q_X5, Y1) = q_believes(q_Sub(X1, q_X5, Y1)))).
fof(axiom31_q_ist_q_X1,axiom,![X1,X2, Y1] :((q_Term(X1)&q_Term(X2)) => q_Sub(q_ist(X1,X2), q_X1, Y1) = q_ist(q_Sub(X1, q_X1, Y1),q_Sub(X2, q_X1, Y1)))).
fof(axiom31_q_ist_q_X2,axiom,![X1,X2, Y1] :((q_Term(X1)&q_Term(X2)) => q_Sub(q_ist(X1,X2), q_X2, Y1) = q_ist(q_Sub(X1, q_X2, Y1),q_Sub(X2, q_X2, Y1)))).
fof(axiom31_q_ist_q_X3,axiom,![X1,X2, Y1] :((q_Term(X1)&q_Term(X2)) => q_Sub(q_ist(X1,X2), q_X3, Y1) = q_ist(q_Sub(X1, q_X3, Y1),q_Sub(X2, q_X3, Y1)))).
fof(axiom31_q_ist_q_X4,axiom,![X1,X2, Y1] :((q_Term(X1)&q_Term(X2)) => q_Sub(q_ist(X1,X2), q_X4, Y1) = q_ist(q_Sub(X1, q_X4, Y1),q_Sub(X2, q_X4, Y1)))).
fof(axiom31_q_ist_q_X5,axiom,![X1,X2, Y1] :((q_Term(X1)&q_Term(X2)) => q_Sub(q_ist(X1,X2), q_X5, Y1) = q_ist(q_Sub(X1, q_X5, Y1),q_Sub(X2, q_X5, Y1)))).
fof(axiom31_q_truthPredicate_q_X1,axiom,![X1, Y1] :((q_Term(X1)) => q_Sub(q_truthPredicate(X1), q_X1, Y1) = q_truthPredicate(q_Sub(X1, q_X1, Y1)))).
fof(axiom31_q_truthPredicate_q_X2,axiom,![X1, Y1] :((q_Term(X1)) => q_Sub(q_truthPredicate(X1), q_X2, Y1) = q_truthPredicate(q_Sub(X1, q_X2, Y1)))).
fof(axiom31_q_truthPredicate_q_X3,axiom,![X1, Y1] :((q_Term(X1)) => q_Sub(q_truthPredicate(X1), q_X3, Y1) = q_truthPredicate(q_Sub(X1, q_X3, Y1)))).
fof(axiom31_q_truthPredicate_q_X4,axiom,![X1, Y1] :((q_Term(X1)) => q_Sub(q_truthPredicate(X1), q_X4, Y1) = q_truthPredicate(q_Sub(X1, q_X4, Y1)))).
fof(axiom31_q_truthPredicate_q_X5,axiom,![X1, Y1] :((q_Term(X1)) => q_Sub(q_truthPredicate(X1), q_X5, Y1) = q_truthPredicate(q_Sub(X1, q_X5, Y1)))).
fof(axiom31_q_contemporary_q_X1,axiom,![X1,X2, Y1] :((q_Term(X1)&q_Term(X2)) => q_Sub(q_contemporary(X1,X2), q_X1, Y1) = q_contemporary(q_Sub(X1, q_X1, Y1),q_Sub(X2, q_X1, Y1)))).
fof(axiom31_q_contemporary_q_X2,axiom,![X1,X2, Y1] :((q_Term(X1)&q_Term(X2)) => q_Sub(q_contemporary(X1,X2), q_X2, Y1) = q_contemporary(q_Sub(X1, q_X2, Y1),q_Sub(X2, q_X2, Y1)))).
fof(axiom31_q_contemporary_q_X3,axiom,![X1,X2, Y1] :((q_Term(X1)&q_Term(X2)) => q_Sub(q_contemporary(X1,X2), q_X3, Y1) = q_contemporary(q_Sub(X1, q_X3, Y1),q_Sub(X2, q_X3, Y1)))).
fof(axiom31_q_contemporary_q_X4,axiom,![X1,X2, Y1] :((q_Term(X1)&q_Term(X2)) => q_Sub(q_contemporary(X1,X2), q_X4, Y1) = q_contemporary(q_Sub(X1, q_X4, Y1),q_Sub(X2, q_X4, Y1)))).
fof(axiom31_q_contemporary_q_X5,axiom,![X1,X2, Y1] :((q_Term(X1)&q_Term(X2)) => q_Sub(q_contemporary(X1,X2), q_X5, Y1) = q_contemporary(q_Sub(X1, q_X5, Y1),q_Sub(X2, q_X5, Y1)))).
fof(axiom31_q_transmutates_q_X1,axiom,![X1,X2, Y1] :((q_Term(X1)&q_Term(X2)) => q_Sub(q_transmutates(X1,X2), q_X1, Y1) = q_transmutates(q_Sub(X1, q_X1, Y1),q_Sub(X2, q_X1, Y1)))).
fof(axiom31_q_transmutates_q_X2,axiom,![X1,X2, Y1] :((q_Term(X1)&q_Term(X2)) => q_Sub(q_transmutates(X1,X2), q_X2, Y1) = q_transmutates(q_Sub(X1, q_X2, Y1),q_Sub(X2, q_X2, Y1)))).
fof(axiom31_q_transmutates_q_X3,axiom,![X1,X2, Y1] :((q_Term(X1)&q_Term(X2)) => q_Sub(q_transmutates(X1,X2), q_X3, Y1) = q_transmutates(q_Sub(X1, q_X3, Y1),q_Sub(X2, q_X3, Y1)))).
fof(axiom31_q_transmutates_q_X4,axiom,![X1,X2, Y1] :((q_Term(X1)&q_Term(X2)) => q_Sub(q_transmutates(X1,X2), q_X4, Y1) = q_transmutates(q_Sub(X1, q_X4, Y1),q_Sub(X2, q_X4, Y1)))).
fof(axiom31_q_transmutates_q_X5,axiom,![X1,X2, Y1] :((q_Term(X1)&q_Term(X2)) => q_Sub(q_transmutates(X1,X2), q_X5, Y1) = q_transmutates(q_Sub(X1, q_X5, Y1),q_Sub(X2, q_X5, Y1)))).
fof(axiom31_q_Neg_q_X1,axiom,![X1, Y1] :((q_Term(X1)) => q_Sub(q_Neg(X1), q_X1, Y1) = q_Neg(q_Sub(X1, q_X1, Y1)))).
fof(axiom31_q_Neg_q_X2,axiom,![X1, Y1] :((q_Term(X1)) => q_Sub(q_Neg(X1), q_X2, Y1) = q_Neg(q_Sub(X1, q_X2, Y1)))).
fof(axiom31_q_Neg_q_X3,axiom,![X1, Y1] :((q_Term(X1)) => q_Sub(q_Neg(X1), q_X3, Y1) = q_Neg(q_Sub(X1, q_X3, Y1)))).
fof(axiom31_q_Neg_q_X4,axiom,![X1, Y1] :((q_Term(X1)) => q_Sub(q_Neg(X1), q_X4, Y1) = q_Neg(q_Sub(X1, q_X4, Y1)))).
fof(axiom31_q_Neg_q_X5,axiom,![X1, Y1] :((q_Term(X1)) => q_Sub(q_Neg(X1), q_X5, Y1) = q_Neg(q_Sub(X1, q_X5, Y1)))).
fof(axiom31_q_And_q_X1,axiom,![X1,X2, Y1] :((q_Term(X1)&q_Term(X2)) => q_Sub(q_And(X1,X2), q_X1, Y1) = q_And(q_Sub(X1, q_X1, Y1),q_Sub(X2, q_X1, Y1)))).
fof(axiom31_q_And_q_X2,axiom,![X1,X2, Y1] :((q_Term(X1)&q_Term(X2)) => q_Sub(q_And(X1,X2), q_X2, Y1) = q_And(q_Sub(X1, q_X2, Y1),q_Sub(X2, q_X2, Y1)))).
fof(axiom31_q_And_q_X3,axiom,![X1,X2, Y1] :((q_Term(X1)&q_Term(X2)) => q_Sub(q_And(X1,X2), q_X3, Y1) = q_And(q_Sub(X1, q_X3, Y1),q_Sub(X2, q_X3, Y1)))).
fof(axiom31_q_And_q_X4,axiom,![X1,X2, Y1] :((q_Term(X1)&q_Term(X2)) => q_Sub(q_And(X1,X2), q_X4, Y1) = q_And(q_Sub(X1, q_X4, Y1),q_Sub(X2, q_X4, Y1)))).
fof(axiom31_q_And_q_X5,axiom,![X1,X2, Y1] :((q_Term(X1)&q_Term(X2)) => q_Sub(q_And(X1,X2), q_X5, Y1) = q_And(q_Sub(X1, q_X5, Y1),q_Sub(X2, q_X5, Y1)))).
fof(axiom31_q_Or_q_X1,axiom,![X1,X2, Y1] :((q_Term(X1)&q_Term(X2)) => q_Sub(q_Or(X1,X2), q_X1, Y1) = q_Or(q_Sub(X1, q_X1, Y1),q_Sub(X2, q_X1, Y1)))).
fof(axiom31_q_Or_q_X2,axiom,![X1,X2, Y1] :((q_Term(X1)&q_Term(X2)) => q_Sub(q_Or(X1,X2), q_X2, Y1) = q_Or(q_Sub(X1, q_X2, Y1),q_Sub(X2, q_X2, Y1)))).
fof(axiom31_q_Or_q_X3,axiom,![X1,X2, Y1] :((q_Term(X1)&q_Term(X2)) => q_Sub(q_Or(X1,X2), q_X3, Y1) = q_Or(q_Sub(X1, q_X3, Y1),q_Sub(X2, q_X3, Y1)))).
fof(axiom31_q_Or_q_X4,axiom,![X1,X2, Y1] :((q_Term(X1)&q_Term(X2)) => q_Sub(q_Or(X1,X2), q_X4, Y1) = q_Or(q_Sub(X1, q_X4, Y1),q_Sub(X2, q_X4, Y1)))).
fof(axiom31_q_Or_q_X5,axiom,![X1,X2, Y1] :((q_Term(X1)&q_Term(X2)) => q_Sub(q_Or(X1,X2), q_X5, Y1) = q_Or(q_Sub(X1, q_X5, Y1),q_Sub(X2, q_X5, Y1)))).
fof(axiom31_const_nadim_q_nadim,axiom,![X1,X2] : q_Sub(q_nadim, X1, X2) = q_nadim).
fof(axiom31_const_rhazes_q_rhazes,axiom,![X1,X2] : q_Sub(q_rhazes, X1, X2) = q_rhazes).
fof(axiom31_const_copper_q_copper,axiom,![X1,X2] : q_Sub(q_copper, X1, X2) = q_copper).
fof(axiom31_const_alice_q_alice,axiom,![X1,X2] : q_Sub(q_alice, X1, X2) = q_alice).
fof(axiom32_q_X1,axiom,![X1, X2] :((q_Term(X1) & q_Term(X2)) => q_Sub(q_Forall(q_X1, X1), q_X1, X2) = q_Forall(q_X1, X1))).
fof(axiom32_q_X2,axiom,![X1, X2] :((q_Term(X1) & q_Term(X2)) => q_Sub(q_Forall(q_X2, X1), q_X2, X2) = q_Forall(q_X2, X1))).
fof(axiom32_q_X3,axiom,![X1, X2] :((q_Term(X1) & q_Term(X2)) => q_Sub(q_Forall(q_X3, X1), q_X3, X2) = q_Forall(q_X3, X1))).
fof(axiom32_q_X4,axiom,![X1, X2] :((q_Term(X1) & q_Term(X2)) => q_Sub(q_Forall(q_X4, X1), q_X4, X2) = q_Forall(q_X4, X1))).
fof(axiom32_q_X5,axiom,![X1, X2] :((q_Term(X1) & q_Term(X2)) => q_Sub(q_Forall(q_X5, X1), q_X5, X2) = q_Forall(q_X5, X1))).
fof(axiom33_q_X1_q_X2,axiom,![X1, X2] :((q_Term(X1) & q_Term(X2)) => q_Sub(q_Forall(q_X2, X1), q_X1, X2) = q_Forall(q_X2, q_Sub(X1, q_X1, X2)))).
fof(axiom33_q_X1_q_X3,axiom,![X1, X2] :((q_Term(X1) & q_Term(X2)) => q_Sub(q_Forall(q_X3, X1), q_X1, X2) = q_Forall(q_X3, q_Sub(X1, q_X1, X2)))).
fof(axiom33_q_X1_q_X4,axiom,![X1, X2] :((q_Term(X1) & q_Term(X2)) => q_Sub(q_Forall(q_X4, X1), q_X1, X2) = q_Forall(q_X4, q_Sub(X1, q_X1, X2)))).
fof(axiom33_q_X1_q_X5,axiom,![X1, X2] :((q_Term(X1) & q_Term(X2)) => q_Sub(q_Forall(q_X5, X1), q_X1, X2) = q_Forall(q_X5, q_Sub(X1, q_X1, X2)))).
fof(axiom33_q_X2_q_X1,axiom,![X1, X2] :((q_Term(X1) & q_Term(X2)) => q_Sub(q_Forall(q_X1, X1), q_X2, X2) = q_Forall(q_X1, q_Sub(X1, q_X2, X2)))).
fof(axiom33_q_X2_q_X3,axiom,![X1, X2] :((q_Term(X1) & q_Term(X2)) => q_Sub(q_Forall(q_X3, X1), q_X2, X2) = q_Forall(q_X3, q_Sub(X1, q_X2, X2)))).
fof(axiom33_q_X2_q_X4,axiom,![X1, X2] :((q_Term(X1) & q_Term(X2)) => q_Sub(q_Forall(q_X4, X1), q_X2, X2) = q_Forall(q_X4, q_Sub(X1, q_X2, X2)))).
fof(axiom33_q_X2_q_X5,axiom,![X1, X2] :((q_Term(X1) & q_Term(X2)) => q_Sub(q_Forall(q_X5, X1), q_X2, X2) = q_Forall(q_X5, q_Sub(X1, q_X2, X2)))).
fof(axiom33_q_X3_q_X1,axiom,![X1, X2] :((q_Term(X1) & q_Term(X2)) => q_Sub(q_Forall(q_X1, X1), q_X3, X2) = q_Forall(q_X1, q_Sub(X1, q_X3, X2)))).
fof(axiom33_q_X3_q_X2,axiom,![X1, X2] :((q_Term(X1) & q_Term(X2)) => q_Sub(q_Forall(q_X2, X1), q_X3, X2) = q_Forall(q_X2, q_Sub(X1, q_X3, X2)))).
fof(axiom33_q_X3_q_X4,axiom,![X1, X2] :((q_Term(X1) & q_Term(X2)) => q_Sub(q_Forall(q_X4, X1), q_X3, X2) = q_Forall(q_X4, q_Sub(X1, q_X3, X2)))).
fof(axiom33_q_X3_q_X5,axiom,![X1, X2] :((q_Term(X1) & q_Term(X2)) => q_Sub(q_Forall(q_X5, X1), q_X3, X2) = q_Forall(q_X5, q_Sub(X1, q_X3, X2)))).
fof(axiom33_q_X4_q_X1,axiom,![X1, X2] :((q_Term(X1) & q_Term(X2)) => q_Sub(q_Forall(q_X1, X1), q_X4, X2) = q_Forall(q_X1, q_Sub(X1, q_X4, X2)))).
fof(axiom33_q_X4_q_X2,axiom,![X1, X2] :((q_Term(X1) & q_Term(X2)) => q_Sub(q_Forall(q_X2, X1), q_X4, X2) = q_Forall(q_X2, q_Sub(X1, q_X4, X2)))).
fof(axiom33_q_X4_q_X3,axiom,![X1, X2] :((q_Term(X1) & q_Term(X2)) => q_Sub(q_Forall(q_X3, X1), q_X4, X2) = q_Forall(q_X3, q_Sub(X1, q_X4, X2)))).
fof(axiom33_q_X4_q_X5,axiom,![X1, X2] :((q_Term(X1) & q_Term(X2)) => q_Sub(q_Forall(q_X5, X1), q_X4, X2) = q_Forall(q_X5, q_Sub(X1, q_X4, X2)))).
fof(axiom33_q_X5_q_X1,axiom,![X1, X2] :((q_Term(X1) & q_Term(X2)) => q_Sub(q_Forall(q_X1, X1), q_X5, X2) = q_Forall(q_X1, q_Sub(X1, q_X5, X2)))).
fof(axiom33_q_X5_q_X2,axiom,![X1, X2] :((q_Term(X1) & q_Term(X2)) => q_Sub(q_Forall(q_X2, X1), q_X5, X2) = q_Forall(q_X2, q_Sub(X1, q_X5, X2)))).
fof(axiom33_q_X5_q_X3,axiom,![X1, X2] :((q_Term(X1) & q_Term(X2)) => q_Sub(q_Forall(q_X3, X1), q_X5, X2) = q_Forall(q_X3, q_Sub(X1, q_X5, X2)))).
fof(axiom33_q_X5_q_X4,axiom,![X1, X2] :((q_Term(X1) & q_Term(X2)) => q_Sub(q_Forall(q_X4, X1), q_X5, X2) = q_Forall(q_X4, q_Sub(X1, q_X5, X2)))).
fof(axiom34_q_X1,axiom,![X1, X2] :((q_Term(X1) & q_Term(X2)) => q_Sub(q_Quote(X1), q_X1, X2) = q_Quote(X1))).
fof(axiom34_q_X2,axiom,![X1, X2] :((q_Term(X1) & q_Term(X2)) => q_Sub(q_Quote(X1), q_X2, X2) = q_Quote(X1))).
fof(axiom34_q_X3,axiom,![X1, X2] :((q_Term(X1) & q_Term(X2)) => q_Sub(q_Quote(X1), q_X3, X2) = q_Quote(X1))).
fof(axiom34_q_X4,axiom,![X1, X2] :((q_Term(X1) & q_Term(X2)) => q_Sub(q_Quote(X1), q_X4, X2) = q_Quote(X1))).
fof(axiom34_q_X5,axiom,![X1, X2] :((q_Term(X1) & q_Term(X2)) => q_Sub(q_Quote(X1), q_X5, X2) = q_Quote(X1))).
fof(axiom1fin_ist_q_ist,axiom,![X1,X2] :((q_Wft(X1)&q_Wft(X2)) => (q_Truth(q_ist(X1,X2)) <=> ist(q_Eval(X1),q_Eval(X2))))).
fof(axiom1fin_truthPredicate_q_truthPredicate,axiom,![X1] :((q_Wft(X1)) => (q_Truth(q_truthPredicate(X1)) <=> truthPredicate(q_Eval(X1))))).
fof(axiom1fin_contemporary_q_contemporary,axiom,![X1,X2] :((q_Wft(X1)&q_Wft(X2)) => (q_Truth(q_contemporary(X1,X2)) <=> contemporary(q_Eval(X1),q_Eval(X2))))).
fof(axiom1fin_transmutates_q_transmutates,axiom,![X1,X2] :((q_Wft(X1)&q_Wft(X2)) => (q_Truth(q_transmutates(X1,X2)) <=> transmutates(q_Eval(X1),q_Eval(X2))))).
fof(axiom2fin,axiom,![X1, X2] :((q_Term(X1) & q_Term(X2)) => (q_Truth(q_And(X1, X2)) <=> (q_Truth(X1) & q_Truth(X2))))).
fof(axiom3fin,axiom,![X1] :(q_Term(X1) => (q_Truth(q_Neg(X1)) <=> ~(q_Truth(X1))))).
fof(axiom4fin_q_X1,axiom,![X2] : ((q_Term(X1) & q_Term(X2)) => (q_Truth(q_Forall(q_X1,X2)) <=> (![X3] : q_Truth(q_Sub(X2, q_X1, q_Quote(X3))))))).
fof(axiom4fin_q_X2,axiom,![X2] : ((q_Term(X1) & q_Term(X2)) => (q_Truth(q_Forall(q_X2,X2)) <=> (![X3] : q_Truth(q_Sub(X2, q_X2, q_Quote(X3))))))).
fof(axiom4fin_q_X3,axiom,![X2] : ((q_Term(X1) & q_Term(X2)) => (q_Truth(q_Forall(q_X3,X2)) <=> (![X3] : q_Truth(q_Sub(X2, q_X3, q_Quote(X3))))))).
fof(axiom4fin_q_X4,axiom,![X2] : ((q_Term(X1) & q_Term(X2)) => (q_Truth(q_Forall(q_X4,X2)) <=> (![X3] : q_Truth(q_Sub(X2, q_X4, q_Quote(X3))))))).
fof(axiom4fin_q_X5,axiom,![X2] : ((q_Term(X1) & q_Term(X2)) => (q_Truth(q_Forall(q_X5,X2)) <=> (![X3] : q_Truth(q_Sub(X2, q_X5, q_Quote(X3))))))).
fof(axiom11fin_q_X1,axiom,![XC, X2] :(q_Term(X2) => (ist(XC, q_Forall(q_X1,X2)) => ![X3] :ist(XC, q_Sub(X2, q_X1, q_Quote(X2)))))).
fof(axiom11fin_q_X2,axiom,![XC, X2] :(q_Term(X2) => (ist(XC, q_Forall(q_X2,X2)) => ![X3] :ist(XC, q_Sub(X2, q_X2, q_Quote(X2)))))).
fof(axiom11fin_q_X3,axiom,![XC, X2] :(q_Term(X2) => (ist(XC, q_Forall(q_X3,X2)) => ![X3] :ist(XC, q_Sub(X2, q_X3, q_Quote(X2)))))).
fof(axiom11fin_q_X4,axiom,![XC, X2] :(q_Term(X2) => (ist(XC, q_Forall(q_X4,X2)) => ![X3] :ist(XC, q_Sub(X2, q_X4, q_Quote(X2)))))).
fof(axiom11fin_q_X5,axiom,![XC, X2] :(q_Term(X2) => (ist(XC, q_Forall(q_X5,X2)) => ![X3] :ist(XC, q_Sub(X2, q_X5, q_Quote(X2)))))).
