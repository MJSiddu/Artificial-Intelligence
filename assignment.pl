edge(albert, isa, man).
edge(louis, isa, man).
edge(frank, isa, turkey).
edge(man, ako, human).
edge(human, ako, creature).
edge(turkey, ako, bird).
edge(bird, ako, creature).
edge(louis, legs, one).
edge(human, legs, two).
edge(turkey, fly, no).
edge(bird, fly, yes).

value(Who, isa, Set):- 
    edge(Who, isa, Set).

value(Who, isa, Set):- 
    edge(Who, isa, Y),
    value(Y, ako, Set).

value(X, ako, Y):- 
    edge(X, ako, Y).

value(X, ako, Y):- 
    edge(Z, ako, Y),
    value(X, ako, Z).

value(X, legs, Val):- 
    edge(X, legs, Val).
value(X, legs, Val):- 
    value(X, isa, Y),
    value(Y, legs, Val), !.
value(X, legs, Val):- 
    value(X, ako, Y), 
    value(Y, legs, Val).

value(X, fly, Val):- 
    edge(X, fly, Val).
value(X, fly, Val):- 
    value(Y, fly, Val), !,
    value(X, isa, Y).
value(X, fly, Val):- 
    value(Y, fly, Val), 
    value(X, ako, Y).






