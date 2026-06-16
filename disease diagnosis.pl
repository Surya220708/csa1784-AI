% Exp. 28: Medical Diagnosis (Prolog)
% Aim: Diagnose disease from symptoms

symptom(fever).
symptom(cough).
symptom(runny_nose).
symptom(body_ache).

disease(flu, [fever, cough, body_ache]).
disease(cold, [runny_nose, cough]).
disease(covid, [fever, cough, runny_nose]).

diagnose(Disease, Symptoms) :-
    disease(Disease, Required),
    subset(Required, Symptoms).

% Definition of subset/2
subset([], _).
subset([H|T], List) :-
    member(H, List),
    subset(T, List).

% Queries:
% ?- diagnose(D, [fever, cough, body_ache]).
%
% Output:
% D = flu.
%
% ?- diagnose(cold, [runny_nose, cough]).
%
% Output:
% true.