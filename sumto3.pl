%==============================================================================
%
% sumto(X, Y) if Y is the sum of the integers from 0 to X
%
%==============================================================================
sum(X, _):- X >= 0, write('This only works for nonnegative integers.'), nl, !.
sumto(0, 0):- !.
sumto(X, Y):- X1 is X - 1, sumto(X1,Y1), Y is Y1 + X.
