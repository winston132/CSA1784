% Facts
parent(john, mary).
parent(mary, sam).

% Rules
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :-
    parent(X, Z),
    ancestor(Z, Y).
