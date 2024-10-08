%fof(schema_36_bel,axiom,(! [T_1]: ((reach(T_1)) => equals(eval(q_bel(T_1)), bel(eval(T_1)))))).
%fof(schema_37_madLove,axiom,(! [T_1, T_2]: ((reach(T_1) & reach(T_2)) => equals(eval(q_madLove(T_1), q_madLove(T_2)), q_madLove(T_1))))).
%fof(schema_37_madLove,axiom,(! [T_1, T_2]: ((reach(T_1) & reach(T_2)) => equals(eval(q_madLove(T_1), q_madLove(T_2)), q_madLove(T_1), q_madLove(T_2))))).

fof(schema_1,axiom,(! [T_1]: equals(T_1,T_1))).
fof(schema_2,axiom,(! [T_1]: equals(T_1))).