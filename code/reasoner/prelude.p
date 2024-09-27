% Add to vampire database before calling solver

% People have no two opposite beliefs
% fof(prelude1,axiom, ! [X,Y] : (~(ist(X,quoteNeg(Y)) & ist(X,Y)))).

% Modus ponens within agents
% fof(prelude2,axiom, ! [X,Y,Z] : (((ist(X,quoteDisj(quoteNeg(Y),Z))) & ist(X,Y)) => ist(X,Z))).

% Definition of and for agents
% fof(prelude3,axiom, ! [X,Y,Z] : (ist(X,quoteConj(Y,Z))) <=> (ist(X,Y) & ist(X,Z))).


% Test prelude coherence
% fof(preludetest1,axiom,ist(a,b)).
% fof(preludetest2,axiom,ist(a,quoteNeg(b))).