from collections import deque

def water_jug():
    visited = set()
    q = deque([((0, 0), [])])

    while q:
        (a, b), path = q.popleft()

        if a == 2:
            path.append((a, b))
            print("Solution Steps:")
            for step in path:
                print(step)
            return

        if (a, b) in visited:
            continue

        visited.add((a, b))

        moves = [
            (4, b),                    # Fill 4L jug
            (a, 3),                    # Fill 3L jug
            (0, b),                    # Empty 4L jug
            (a, 0),                    # Empty 3L jug
            (max(0, a-(3-b)), min(3, b+a)),  # 4 -> 3
            (min(4, a+b), max(0, b-(4-a)))   # 3 -> 4
        ]

        for move in moves:
            q.append((move, path + [(a, b)]))

water_jug()