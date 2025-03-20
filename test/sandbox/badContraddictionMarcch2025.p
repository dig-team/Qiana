fof(a1,axiom,(p(f(c))) => (p(f(c)))).
fof(a2,axiom,![X1] : p(f(c)) | ~p(f(c))).

fof(axiom5,axiom,![XC, X1, X2] :(ist(XC, q_And(X1, X2)) => (ist(XC, X1) & ist(XC, X2)))).
fof(axiom6,axiom,![XC, X1, X2] :(ist(XC, q_And(X1, X2)) <=> ist(XC, q_And(X2, X1)))).
fof(axiom7,axiom,![XC, X1] :(ist(XC, q_Neg(q_Neg(X1))) <=> ist(XC, X1))).
fof(axiom8,axiom,![XC, X1, X2, X3] :(ist(XC, q_And(q_And(X1, X2), X3)) <=> ist(XC, q_And(X1, q_And(X2, X3))))).
fof(axiom9,axiom,![XC, X1, X2, X3] :(ist(XC, q_OR(q_And(X1, X2), X3)) <=> ist(XC, q_And(q_OR(X1, X3), q_OR(X2, X3))))).
fof(axiom10,axiom,![XC, X1, X2] :((ist(XC, q_OR(X1, X2)) & ist(XC, q_Neg(X1))) => ist(XC, X2))).
fof(axiom12,axiom,![X1] :(X1 = X1)).
fof(axiom13,axiom,![X1, X2] :(X1 = X2 => X2 = X1)).
fof(axiom14,axiom,![X1, X2, X3] :((X1 = X2 & X2 = X3) => X1 = X3)).
fof(axiom15sub,axiom,![X1,X2,X3,Y1,Y2,Y3] :((X1 = Y1&X2 = Y2&X3 = Y3) => sub(X1,X2,X3) = sub(Y1,Y2,Y3))).
fof(axiom15eval,axiom,![X1,Y1] :((X1 = Y1) => eval(X1) = eval(Y1))).
fof(axiom16ist,axiom,![X1,X2,Y1,Y2] :((X1 = Y1&X2 = Y2) => ist(X1,X2) <=> ist(Y1,Y2))).
fof(axiom16wft,axiom,![X1,Y1] :((X1 = Y1) => wft(X1) <=> wft(Y1))).
fof(axiom16term,axiom,![X1,Y1] :((X1 = Y1) => term(X1) <=> term(Y1))).
fof(axiom17,axiom,![X1] :(term(q_Quote(X1)))).
fof(axiom18sub,axiom,![X1,X2,X3] :((term(X1)&term(X2)&term(X3)) => term(sub(X1,X2,X3)))).
fof(axiom18eval,axiom,![X1] :((term(X1)) => term(eval(X1)))).
fof(axiom19,axiom,![X1] :(wft(q_Quote(X1)))).
fof(axiom20,axiom,![X1] :(wft(X1))).
fof(axiom21sub,axiom,![X1,X2,X3] :((wft(X1)&wft(X2)&wft(X3)) => wft(sub(X1,X2,X3)))).
fof(axiom21eval,axiom,![X1] :((wft(X1)) => wft(eval(X1)))).
fof(axiom22,axiom,![X1] :(term(X1) => eval(q_Quote(X1)) = X1)).
fof(axiom23sub,axiom,![X1,X2,X3] :((term(X1)&term(X2)&term(X3)) => eval(sub(X1,X2,X3)) = sub(eval(X1),eval(X2),eval(X3)))).
fof(axiom23eval,axiom,![X1] :((term(X1)) => eval(eval(X1)) = eval(eval(X1)))).
fof(axiom24ist_q_ist,axiom,![X1,X2] :((term(X1)&term(X2)) => eval(q_ist(X1,X2)) = q_ist(X1,X2))).
fof(axiom24wft_q_wft,axiom,![X1] :((term(X1)) => eval(q_wft(X1)) = q_wft(X1))).
fof(axiom24term_q_term,axiom,![X1] :((term(X1)) => eval(q_term(X1)) = q_term(X1))).
fof(axiom25,axiom,![X1, X2] :(eval(q_And(X1, X2)) = q_And(X1, X2))).
fof(axiom26,axiom,![X1, X2] :(eval(q_Forall(X1, X2)) = q_Forall(X1, X2))).
fof(axiom27,axiom,![X1] :(eval(q_Neg(X1)) = q_Neg(X1))).
fof(axiom28,axiom,![X1] :(eval(X1) = X1)).
fof(axiom29,axiom,![X1, X2, X3] :(term(X1) => sub(X1, X1, X3) = X3)).
fof(axiom30,axiom,![X1, X2, X3] :(term(X1) => sub(X1, X2, X3) = X1)).
fof(axiom31sub,axiom,![X1,X2,X3, Y1, Y2] :((term(X1)&term(X2)&term(X3)) => sub(sub(X1,X2,X3), Y1, Y2) = sub(sub(X1, Y1, Y2),sub(X2, Y1, Y2),sub(X3, Y1, Y2)))).
fof(axiom31eval,axiom,![X1, Y1, Y2] :((term(X1)) => sub(eval(X1), Y1, Y2) = eval(sub(X1, Y1, Y2)))).
fof(axiom32,axiom,![X1, X2, X3] :((term(X1) & term(X2)) => sub(q_Forall(X1, X2), X1, X3) = q_Forall(X1, X2))).
fof(axiom33,axiom,![X1, X2, X3, X4] :((term(X1) & term(X2)) => sub(q_Forall(X3, X1), X2, X4) = q_Forall(X3, sub(X1, X2, X4)))).
fof(axiom34,axiom,![X1, X2, X3] :((term(X1) & term(X2)) => sub(q_Quote(X1), X2, X3) = q_Quote(X1))).
fof(axiom1finist_q_ist,axiom,![X1,X2] :((wft(X1)&wft(X2)) => q_Truth(q_ist(X1,X2)) <=> ist(eval(X1),eval(X2)))).
fof(axiom1finwft_q_wft,axiom,![X1] :((wft(X1)) => q_Truth(q_wft(X1)) <=> wft(eval(X1)))).
fof(axiom1finterm_q_term,axiom,![X1] :((wft(X1)) => q_Truth(q_term(X1)) <=> term(eval(X1)))).
fof(axiom2fin,axiom,![X1, X2] :((term(X1) & term(X2)) => q_Truth(q_And(X1, X2)) <=> (q_Truth(X1) & q_Truth(X2)))).
fof(axiom3fin,axiom,![X1] :(term(X1) => (q_Truth(q_Neg(X1)) <=> ~(q_Truth(X1))))).
fof(axiom4fin,axiom,![X1] :(term(X1) => q_Truth(q_Forall(X1)) <=> (![X2] :q_Truth(sub(X1, X2, q_Quote(X2)))))).
fof(axiom11fin,axiom,![XC, X1] :((term(X1) => (ist(XC, q_Forall(X1)) => ![X2] :ist(XC, sub(X1, X2, q_Quote(X2))))))).