edge(david, isa, diabetics).
edge(diabetics, shouldAvoid, sugar).
edge(candy, contains, sugar).
edge(snickers, ako, candy).

value(Node, Slot, Value):- edge(Node, Slot, Value).
value(Node, Slot, Value):-
    edge(Node, isa, Node1),
    value(Node1, Slot, Value).
value(Node, Slot, Value):-
    edge(Node, ako, Node1),
    value(Node1, Slot, Value).
value(Node, shouldAvoid, Node1):-
    edge(Node1, contains, Stuff),
    value(Node, shouldAvoid, Stuff).
