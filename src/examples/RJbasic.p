%----Hypothesis
fof(h1,axiom,
    ! [X] : 
        (ist(say(friar), X) => truthPredicate(X))
).

fof(h2,axiom,
    ! [X,Y] : (
    (madLove(X,Y) & ist(bel(X),q_dead(quote(Y)))) =>
    dead(X)
)).

fof(h3,axiom,
    madLove(romeo,juliet)
).

fof(h4,axiom,
    madLove(juliet,romeo)
).

fof(h5,axiom,
    ist(say(friar), q_Forall(q_x0, q_Not(q_And(q_drinkPotion(q_x0),q_Not(q_appearDead(q_x0))))))
).

fof(h6,axiom,
    drinkPotion(juliet)
).

fof(h8,axiom,
    ! [X,Y] :(
    appearDead(X) => ist(Y,q_appearDead(quote(X)))
)).

fof(h9,axiom,
    ! [X,Y] :(
    dead(X) => ist(Y,q_dead(quote(X)))
)).

fof(h10,axiom,
    ! [X] :(
    ist(bel(romeo), q_Not(q_And(q_appearDead(quote(X)), q_Not(q_dead(quote(X))))))
)).

%----Conclusions

fof(true_goal,conjecture,
    dead(juliet)
).
