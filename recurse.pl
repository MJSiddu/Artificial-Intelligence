h(X):- f(X).
h(X):- s(X).
%h(X):- h(Y), p(Y, X).
h(X):- p(Y,X), h(Y).

f(d).
f(m).

s(w).
s(m).

p(d,k).
p(d,r).
