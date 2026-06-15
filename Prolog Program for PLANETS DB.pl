planet(earth, rocky, medium, temperate, third_closest).
planet(mars, rocky, small, cold, fourth_closest).
planet(jupiter, gas_giant,large, cold, fifth_closest).
planet(saturn, gas_giant,large, cold, sixth_closest).
planet_properties(N,T,S,Temp,Pos) :- planet(N,T,S,Temp,Pos).
?- planet_properties(earth, Type, Size, Temp, Pos).
?- planet_properties(Name, gas_giant, _, _, _).
