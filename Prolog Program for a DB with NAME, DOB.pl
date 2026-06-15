% Facts: person(Name, DateOfBirth)

person('John', '12-05-2000').
person('Alice', '23-08-2001').
person('David', '15-01-1999').
person('Mary', '10-12-2002').

% Rule to find DOB of a person
dob(Name, DOB) :-
    person(Name, DOB).
