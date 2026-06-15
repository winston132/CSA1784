% Facts
fact(a).
fact(b).

% Rules
fact(c) :- fact(a), fact(b).
fact(d) :- fact(c).
fact(e) :- fact(d).
