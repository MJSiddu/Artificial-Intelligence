edge(human, ako, creature).
edge(bird, ako, creature).
edge(man, ako, human).
edge(turkey, ako, bird).
edge(albert, isa, man).
edge(louis, isa, man).
edge(frank, isa, turkey).

property(louis, legs, one).
property(human, legs, two).
property(turkey, fly, false).
property(bird, fly, true).

property(X, legs, Z):- edge(X, isa, N), property(N, legs, Z), !.
property(X, legs, Z):- edge(X, ako, N), property(N, legs, Z), !.

property(X, Y, true):- edge(X, isa, Z), property(Z, Y, true), not(property(X, Y, false)).
property(X, Y, false):- edge(X, isa, Z), property(Z, Y, false), not(property(X, Y, true)).
property(X, Y, true):- edge(X, ako, Z), property(Z, Y, true), not(property(X, Y, false)).
property(X, Y, false):- edge(X, ako, Z), property(Z, Y, false), not(property(X, Y, true)).

rel(S, R, D):- edge(S, R, D).
rel(S, R, D):- edge(S1, ako, D), rel(S, R, S1).
