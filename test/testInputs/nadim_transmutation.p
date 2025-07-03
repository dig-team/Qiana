%---- Translation of the input text into TPTP

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

