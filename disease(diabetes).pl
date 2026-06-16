disease(diabetes).
disease(hypertension).
disease(obesity).

diet(diabetes, low_sugar).
diet(diabetes, high_fiber).
diet(hypertension, low_salt).
diet(obesity, low_calorie).

recommend_diet(Person, Diet) :-
    disease(D),
    diet(D, Diet).

suitable_food(diabetes, green_vegetables).
suitable_food(hypertension, low_salt_food).

% Query:
% ?- recommend_diet(patient, X).

% Output:
% X = low_sugar ;
% X = high_fiber ;
% X = low_salt ;
% X = low_calorie.