likes(john, [mary, jane]).
likes(fred, [mary, alice, judy, nancy]).
likes(tom, []).

what_about(P):-
    likes(P, X),
    write(P),
    write(' likes '),
    writelist(X).

writelist([]):- nl.
writelist([H | T]):-
    write(H),
    write(', '),
    writelist(T).
