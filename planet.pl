% Facts
planet(mercury, rocky, small, hot, closest_to_sun).
planet(venus, rocky, small, hot, second_closest).
planet(earth, rocky, medium, temperate, third_closest).
planet(mars, rocky, small, cold, fourth_closest).
planet(jupiter, gas_giant, large, cold, fifth_closest).
planet(saturn, gas_giant, large, cold, sixth_closest).

% Rule
planet_properties(Name, Type, Size, Temp, Position) :-
    planet(Name, Type, Size, Temp, Position).

% Query 1: Get Earth's properties
?- planet_properties(earth, Type, Size, Temp, Pos).

% Output:
% Type = rocky,
% Size = medium,
% Temp = temperate,
% Pos = third_closest.

% Query 2: Find all gas giant planets
?- planet_properties(Name, gas_giant, _, _, _).

% Output:
% Name = jupiter ;
% Name = saturn.