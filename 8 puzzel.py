from queue import PriorityQueue

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Manhattan Distance Heuristic
def heuristic(state):
    h = 0
    for i in range(9):
        if state[i] != 0:
            goal_pos = state[i] - 1
            h += abs(i // 3 - goal_pos // 3) + abs(i % 3 - goal_pos % 3)
    return h


# Generate Successor States
def successors(state):
    moves = []
    blank = state.index(0)

    possible = []

    # Up
    if blank > 2:
        possible.append(blank - 3)

    # Down
    if blank < 6:
        possible.append(blank + 3)

    # Left
    if blank % 3 != 0:
        possible.append(blank - 1)

    # Right
    if blank % 3 != 2:
        possible.append(blank + 1)

    for pos in possible:
        s = list(state)
        s[blank], s[pos] = s[pos], s[blank]
        moves.append(tuple(s))

    return moves


# A* Search
def solve(start):
    pq = PriorityQueue()
    pq.put((heuristic(start), 0, start))

    parent = {start: None}
    cost = {start: 0}

    while not pq.empty():
        _, g, current = pq.get()

        if current == GOAL:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            return path[::-1]

        for nxt in successors(current):
            new_cost = g + 1

            if nxt not in cost or new_cost < cost[nxt]:
                cost[nxt] = new_cost
                priority = new_cost + heuristic(nxt)

                pq.put((priority, new_cost, nxt))
                parent[nxt] = current

    return None


# Display Board
def print_board(state):
    for i in range(0, 9, 3):
        row = state[i:i+3]
        print(" ".join("_" if x == 0 else str(x) for x in row))
    print()


# Main Program
print("Enter 9 numbers (0 for blank) separated by spaces:")
numbers = list(map(int, input().split()))

if len(numbers) != 9:
    print("Error: Enter exactly 9 numbers!")
else:
    start = tuple(numbers)

    print("\nInitial State:")
    print_board(start)

    solution = solve(start)

    if solution:
        print("Solution Found!")
        print("Total Moves =", len(solution) - 1)

        for step, state in enumerate(solution):
            print("Step", step)
            print_board(state)
    else:
        print("No solution exists.")