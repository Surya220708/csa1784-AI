teaches(smith, math).
teaches(jones, science).

studies(alice, math).
studies(bob, science).
studies(charlie, math).

tutor(Student, Teacher) :-
    studies(Student, Subject),
    teaches(Teacher, Subject).

% Queries and Outputs

% ?- tutor(alice, X).
% X = smith.

% ?- tutor(X, jones).
% X = bob.

% ?- tutor(X, Y).
% X = alice,
% Y = smith ;
% X = bob,
% Y = jones ;
% X = charlie,
% Y = smith.