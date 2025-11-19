%----Hypothesis
fof(h1,axiom,
    ! [X] : 
        (ist(say(friar), X) => q_Truth(X))
).

fof(h5,axiom,
    ist(say(friar), q_Forall(q_X1, q_Not(q_And(q_drinkPotion(q_X1),q_Not(q_appearDead(q_X1))))))
).

fof(h2,axiom,
    ! [X,Y] : (
    (madLove(X,Y) & ist(bel(X),q_dead(q_Quote(Y)))) =>
    dead(X)
)).

fof(h3,axiom,
    madLove(romeo,juliet)
).

fof(h4,axiom,
    madLove(juliet,romeo)
).

fof(h6,axiom,
    drinkPotion(juliet)
).

%fof(h8,axiom, ! [X,Y] :( appearDead(X) => ist(Y,q_appearDead(q_Quote(X))))).
fof(h8_romeo,axiom, ! [X] :( appearDead(X) => ist(bel(romeo),q_dead(q_Quote(X))))).

fof(h9,axiom,
    ! [X,Y] :(
    dead(X) => ist(Y,q_dead(q_Quote(X)))
)).

% The formula bellow provides the truth of the friar's assertion directly as otherwise we hit a timeout
% But a separate tests shows it is redundant with the rest, so this is indeed a timeout and not a cheat
fof(redundant_1,axiom, ![X] : (drinkPotion(X) => appearDead(X))).

fof(h10,axiom,
    ! [X] :(
    ist(bel(romeo), q_Not(q_And(q_appearDead(q_Quote(X)), q_Not(q_dead(q_Quote(X))))))
)).

%----Conclusions

fof(true_goal,conjecture, dead(juliet)).
