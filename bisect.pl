half(X, Y):- Y is X / 2.

bisect:-
    write('Number please: '),
    read(X),
    half(X, Y),
    write('Half of '),
    write(X),
    write(' is '),
    write(Y),
    nl.
