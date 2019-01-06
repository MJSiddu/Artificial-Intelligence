likes(bill,[beth]).
likes(john, [mary, jane]).
likes(fred, [mary, alice, judy, nancy]).
likes(tom, []).

about(P):-
    likes(P, X),
    write(P),
    write(' likes '),
    writelist(X).

writelist([H]):-
    write(H),
    write('.'),
    nl, !.
writelist([A,B]):-
    write(A),
    write(' and '),
    write(B),
    write('.'),
    nl, !.
writelist([H | T]):-
    write(H),
    write(', '),
    writelist(T).
writelist([]):-
    write('nobody.').
