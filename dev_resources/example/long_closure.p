
    fof(tauto, axiom, drinkPotion(c) | appearDead(c) | ~appearDead(c)).
    fof(h1, axiom, q_Truth(q_Forall(q_X1, q_Neg(q_And(q_drinkPotion(q_X1),q_Neg(q_appearDead(q_X1))))))).
    fof(goal,conjecture, ![X] : (~q_Truth(q_Sub(q_And(q_drinkPotion(q_X1),q_Neg(q_appearDead(q_X1))),q_X1,q_Quote(X))))).
    
fof(axiom5,axiom,![XC, X1, X2] :(ist(XC, q_And(X1, X2)) => (ist(XC, X1) & ist(XC, X2)))).
fof(axiom6,axiom,![XC, X1, X2] :(ist(XC, q_And(X1, X2)) <=> ist(XC, q_And(X2, X1)))).
fof(axiom7,axiom,![XC, X1] :(ist(XC, q_Neg(q_Neg(X1))) <=> ist(XC, X1))).
fof(axiom8,axiom,![XC, X1, X2, X3] :(ist(XC, q_And(q_And(X1, X2), X3)) <=> ist(XC, q_And(X1, q_And(X2, X3))))).
fof(axiom9,axiom,![XC, X1, X2, X3] :(ist(XC, q_Or(q_And(X1, X2), X3)) <=> ist(XC, q_And(q_Or(X1, X3), q_Or(X2, X3))))).
fof(axiom10,axiom,![XC, X1, X2] :((ist(XC, q_Or(X1, X2)) & ist(XC, q_Neg(X1))) => ist(XC, X2))).
fof(axiom12,axiom,![X1] :(X1 = X1)).
fof(axiom13,axiom,![X1, X2] :(X1 = X2 => X2 = X1)).
fof(axiom14,axiom,![X1, X2, X3] :((X1 = X2 & X2 = X3) => X1 = X3)).
fof(axiom15_q_drinkPotion,axiom,![X1,Y1] :((X1 = Y1) => q_drinkPotion(X1) = q_drinkPotion(Y1))).
fof(axiom15_q_appearDead,axiom,![X1,Y1] :((X1 = Y1) => q_appearDead(X1) = q_appearDead(Y1))).
fof(axiom15_q_ist,axiom,![X1,X2,Y1,Y2] :((X1 = Y1&X2 = Y2) => q_ist(X1,X2) = q_ist(Y1,Y2))).
fof(axiom15_q_Quote,axiom,![X1,Y1] :((X1 = Y1) => q_Quote(X1) = q_Quote(Y1))).
fof(axiom15_q_Neg,axiom,![X1,Y1] :((X1 = Y1) => q_Neg(X1) = q_Neg(Y1))).
fof(axiom15_q_And,axiom,![X1,X2,Y1,Y2] :((X1 = Y1&X2 = Y2) => q_And(X1,X2) = q_And(Y1,Y2))).
fof(axiom15_q_Or,axiom,![X1,X2,Y1,Y2] :((X1 = Y1&X2 = Y2) => q_Or(X1,X2) = q_Or(Y1,Y2))).
fof(axiom15_q_Forall,axiom,![X1,X2,Y1,Y2] :((X1 = Y1&X2 = Y2) => q_Forall(X1,X2) = q_Forall(Y1,Y2))).
fof(axiom15_const_c,axiom,c = c).
fof(axiom15_const_q_c,axiom,q_c = q_c).
fof(axiom15_const_q_X1,axiom,q_X1 = q_X1).
fof(axiom15_const_q_X2,axiom,q_X2 = q_X2).
fof(axiom15_const_q_X3,axiom,q_X3 = q_X3).
fof(axiom15_const_q_X4,axiom,q_X4 = q_X4).
fof(axiom15_const_q_X5,axiom,q_X5 = q_X5).
fof(axiom16_drinkPotion,axiom,![X1,Y1] :((X1 = Y1) => (drinkPotion(X1) <=> drinkPotion(Y1)))).
fof(axiom16_appearDead,axiom,![X1,Y1] :((X1 = Y1) => (appearDead(X1) <=> appearDead(Y1)))).
fof(axiom16_ist,axiom,![X1,X2,Y1,Y2] :((X1 = Y1&X2 = Y2) => (ist(X1,X2) <=> ist(Y1,Y2)))).
fof(axiom16_q_Truth,axiom,![X1,Y1] :((X1 = Y1) => (q_Truth(X1) <=> q_Truth(Y1)))).
fof(axiom17,axiom,![X1] :(q_Term(q_Quote(X1)))).
fof(axiom18_q_drinkPotion,axiom,![X1] :((q_Term(X1)) => q_Term(q_drinkPotion(X1)))).
fof(axiom18_q_appearDead,axiom,![X1] :((q_Term(X1)) => q_Term(q_appearDead(X1)))).
fof(axiom18_q_ist,axiom,![X1,X2] :((q_Term(X1)&q_Term(X2)) => q_Term(q_ist(X1,X2)))).
fof(axiom18_q_Quote,axiom,![X1] :((q_Term(X1)) => q_Term(q_Quote(X1)))).
fof(axiom18_q_Neg,axiom,![X1] :((q_Term(X1)) => q_Term(q_Neg(X1)))).
fof(axiom18_q_And,axiom,![X1,X2] :((q_Term(X1)&q_Term(X2)) => q_Term(q_And(X1,X2)))).
fof(axiom18_q_Or,axiom,![X1,X2] :((q_Term(X1)&q_Term(X2)) => q_Term(q_Or(X1,X2)))).
fof(axiom18_q_Forall,axiom,![X1,X2] :((q_Term(X1)&q_Term(X2)) => q_Term(q_Forall(X1,X2)))).
fof(axiom18_const_c,axiom,q_Term(c)).
fof(axiom18_const_q_c,axiom,q_Term(q_c)).
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
fof(axiom21_const_c_q_c,axiom,q_Wft(q_c)).
fof(axiom22,axiom,![X1] :(q_Eval(q_Quote(X1)) = X1)).
fof(axiom23_const_c_q_c,axiom,q_Eval(q_c) = c).
fof(axiom24_drinkPotion_q_drinkPotion,axiom,![X1] :((q_Term(X1)) => q_Eval(q_drinkPotion(X1)) = q_drinkPotion(X1))).
fof(axiom24_appearDead_q_appearDead,axiom,![X1] :((q_Term(X1)) => q_Eval(q_appearDead(X1)) = q_appearDead(X1))).
fof(axiom24_ist_q_ist,axiom,![X1,X2] :((q_Term(X1)&q_Term(X2)) => q_Eval(q_ist(X1,X2)) = q_ist(X1,X2))).
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
fof(axiom31_q_drinkPotion_q_X1,axiom,![X1, Y1] :((q_Term(X1)) => q_Sub(q_drinkPotion(X1), q_X1, Y1) = q_drinkPotion(q_Sub(X1, q_X1, Y1)))).
fof(axiom31_q_drinkPotion_q_X2,axiom,![X1, Y1] :((q_Term(X1)) => q_Sub(q_drinkPotion(X1), q_X2, Y1) = q_drinkPotion(q_Sub(X1, q_X2, Y1)))).
fof(axiom31_q_drinkPotion_q_X3,axiom,![X1, Y1] :((q_Term(X1)) => q_Sub(q_drinkPotion(X1), q_X3, Y1) = q_drinkPotion(q_Sub(X1, q_X3, Y1)))).
fof(axiom31_q_drinkPotion_q_X4,axiom,![X1, Y1] :((q_Term(X1)) => q_Sub(q_drinkPotion(X1), q_X4, Y1) = q_drinkPotion(q_Sub(X1, q_X4, Y1)))).
fof(axiom31_q_drinkPotion_q_X5,axiom,![X1, Y1] :((q_Term(X1)) => q_Sub(q_drinkPotion(X1), q_X5, Y1) = q_drinkPotion(q_Sub(X1, q_X5, Y1)))).
fof(axiom31_q_appearDead_q_X1,axiom,![X1, Y1] :((q_Term(X1)) => q_Sub(q_appearDead(X1), q_X1, Y1) = q_appearDead(q_Sub(X1, q_X1, Y1)))).
fof(axiom31_q_appearDead_q_X2,axiom,![X1, Y1] :((q_Term(X1)) => q_Sub(q_appearDead(X1), q_X2, Y1) = q_appearDead(q_Sub(X1, q_X2, Y1)))).
fof(axiom31_q_appearDead_q_X3,axiom,![X1, Y1] :((q_Term(X1)) => q_Sub(q_appearDead(X1), q_X3, Y1) = q_appearDead(q_Sub(X1, q_X3, Y1)))).
fof(axiom31_q_appearDead_q_X4,axiom,![X1, Y1] :((q_Term(X1)) => q_Sub(q_appearDead(X1), q_X4, Y1) = q_appearDead(q_Sub(X1, q_X4, Y1)))).
fof(axiom31_q_appearDead_q_X5,axiom,![X1, Y1] :((q_Term(X1)) => q_Sub(q_appearDead(X1), q_X5, Y1) = q_appearDead(q_Sub(X1, q_X5, Y1)))).
fof(axiom31_q_ist_q_X1,axiom,![X1,X2, Y1] :((q_Term(X1)&q_Term(X2)) => q_Sub(q_ist(X1,X2), q_X1, Y1) = q_ist(q_Sub(X1, q_X1, Y1),q_Sub(X2, q_X1, Y1)))).
fof(axiom31_q_ist_q_X2,axiom,![X1,X2, Y1] :((q_Term(X1)&q_Term(X2)) => q_Sub(q_ist(X1,X2), q_X2, Y1) = q_ist(q_Sub(X1, q_X2, Y1),q_Sub(X2, q_X2, Y1)))).
fof(axiom31_q_ist_q_X3,axiom,![X1,X2, Y1] :((q_Term(X1)&q_Term(X2)) => q_Sub(q_ist(X1,X2), q_X3, Y1) = q_ist(q_Sub(X1, q_X3, Y1),q_Sub(X2, q_X3, Y1)))).
fof(axiom31_q_ist_q_X4,axiom,![X1,X2, Y1] :((q_Term(X1)&q_Term(X2)) => q_Sub(q_ist(X1,X2), q_X4, Y1) = q_ist(q_Sub(X1, q_X4, Y1),q_Sub(X2, q_X4, Y1)))).
fof(axiom31_q_ist_q_X5,axiom,![X1,X2, Y1] :((q_Term(X1)&q_Term(X2)) => q_Sub(q_ist(X1,X2), q_X5, Y1) = q_ist(q_Sub(X1, q_X5, Y1),q_Sub(X2, q_X5, Y1)))).
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
fof(axiom31_const_c_q_c,axiom,![X1,X2] : q_Sub(q_c, X1, X2) = q_c).
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
fof(axiom1fin_drinkPotion_q_drinkPotion,axiom,![X1] :((q_Wft(X1)) => (q_Truth(q_drinkPotion(X1)) <=> drinkPotion(q_Eval(X1))))).
fof(axiom1fin_appearDead_q_appearDead,axiom,![X1] :((q_Wft(X1)) => (q_Truth(q_appearDead(X1)) <=> appearDead(q_Eval(X1))))).
fof(axiom1fin_ist_q_ist,axiom,![X1,X2] :((q_Wft(X1)&q_Wft(X2)) => (q_Truth(q_ist(X1,X2)) <=> ist(q_Eval(X1),q_Eval(X2))))).
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
