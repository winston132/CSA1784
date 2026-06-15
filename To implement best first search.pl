% Graph edges
edge(a,b).
edge(a,c).
edge(b,d).
edge(c,e).
edge(d,g).
edge(e,g).

% Heuristic values
h(a,5).
h(b,3).
h(c,4).
h(d,1).
h(e,2).
h(g,0).

% Best First Search
bestfs(Node, Goal) :-
    Node = Goal,
    write('Goal Found: '), write(Goal).

bestfs(Node, Goal) :-
    edge(Node, Next),
    h(Next, _),
    bestfs(Next, Goal).
