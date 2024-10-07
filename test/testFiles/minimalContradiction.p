%----Hypothesis
fof(h1,axiom,
    ! [X] : 
        (ist(say(friar), X) => truthPredicate(X))
).

fof(h2,axiom,
    ~(! [X] : 
        (ist(say(friar), X) => truthPredicate(X))
     )
).
