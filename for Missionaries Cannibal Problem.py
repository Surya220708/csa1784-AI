from collections import deque

start = (3, 3, 1)   # (Missionaries, Cannibals, Boat)
goal = (0, 0, 0)

moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]

def valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if m and m < c:
        return False
    if (3-m) and (3-m) < (3-c):
        return False
    return True

q = deque([(start, [start])])
visited = {start}

while q:
    (m, c, b), path = q.popleft()

    if (m, c, b) == goal:
        print("Shortest Solution:")
        for step in path:
            print(step)
        break

    for dm, dc in moves:
        if b:  # Boat on left
            nm, nc, nb = m-dm, c-dc, 0
        else:  # Boat on right
            nm, nc, nb = m+dm, c+dc, 1

        if valid(nm, nc):
            state = (nm, nc, nb)
            if state not in visited:
                visited.add(state)
                q.append((state, path + [state]))