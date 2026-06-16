
parent(tom, bob).
parent(tom, liz).
parent(bob, ann).
parent(bob, pat).
parent(pat, jim).

ancestor(X, Y) :-
    parent(X, Y).

ancestor(X, Y) :-
    parent(X, Z),
    ancestor(Z, Y).

% Queries:
% ?- ancestor(tom, jim).
%
% Output:
% true.
%
% ?- ancestor(tom, X).
%
% Output:
% X = bob ;
% X = liz ;
% X = ann ;
% X = pat ;
% X = jim.