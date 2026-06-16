

match_pattern([H|T], H, T).

match_first([X|_], X).

match_last([X], X).
match_last([_|T], X) :-
    match_last(T, X).

match_length([], 0).
match_length([_|T], N) :-
    match_length(T, N1),
    N is N1 + 1.

% Queries:
% ?- match_first([a,b,c], X).
%
% Output:
% X = a.
%
% ?- match_last([a,b,c], X).
%
% Output:
% X = c.
%
% ?- match_length([a,b,c], N).
%
% Output:
% N = 3.