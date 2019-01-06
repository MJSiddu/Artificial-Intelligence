append([ ], List, List).
append([Head | Tail], List, [Head | NewTail]):-
  append(Tail, List, NewTail).

