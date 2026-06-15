% Disease diagnosis rules
disease(flu) :-
    symptom(fever),
    symptom(cough).

disease(malaria) :-
    symptom(fever),
    symptom(headache).

disease(cold) :-
    symptom(cough),
    symptom(sneezing).
