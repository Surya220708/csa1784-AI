

rule(
    if([animal(X), has_feather(X)],
       then(bird(X)))
).

rule(
    if([bird(X)],
       then(can_fly(X)))
).

fact(animal(eagle)).
fact(has_feather(eagle)).

forward_chain :-
    fact(X),
    assert(X),
    fail.

forward_chain :-
    rule(if(Conds, then(Conc))),
    call_conds(Conds),
    assert(Conc),
    fail.

forward_chain.

call_conds([]).

call_conds([H|T]) :-
    call(H),
    call_conds(T).

% Queries:
% ?- forward_chain.
%
% To view the derived facts:
% ?- bird(X).
% X = eagle.
%
% ?- can_fly(X).
% X = eagle.