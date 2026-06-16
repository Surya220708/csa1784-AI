% Aim: Query fruit-color relationships

fruit(apple).
fruit(banana).
fruit(orange).
fruit(grape).

color(apple, red).
color(banana, yellow).
color(orange, orange).
color(grape, purple).

fruit_color(F, C) :-
    fruit(F),
    color(F, C).

% Query:
% ?- fruit_color(X, Y).

% Output:
% X = apple,  Y = red ;
% X = banana, Y = yellow ;
% X = orange, Y = orange ;
% X = grape,  Y = purple.