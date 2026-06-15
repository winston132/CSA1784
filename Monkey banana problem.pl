% Initial facts
monkey(at_door).
box(at_window).
banana(at_center).

% Rule to get the banana
get_banana :-
    write('Monkey goes to the box'), nl,
    write('Monkey pushes the box to the center'), nl,
    write('Monkey climbs on the box'), nl,
    write('Monkey grabs the banana'), nl.
