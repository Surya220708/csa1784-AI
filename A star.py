from queue import PriorityQueue

graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 3, 'E': 6},
    'C': {'F': 2},
    'D': {},
    'E': {'G': 1},
    'F': {'G': 4},
    'G': {}
}

h = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 3,
    'E': 1,
    'F': 2,
    'G': 0
}

start = 'A'
goal = 'G'

pq = PriorityQueue()
pq.put((h[start], 0, start, [start]))

visited = set()

while not pq.empty():
    f, g, node, path = pq.get()

    if node == goal:
        print("Path:", " -> ".join(path))
        print("Cost:", g)
        break

    if node not in visited:
        visited.add(node)

        for nbr, cost in graph[node].items():
            g_new = g + cost
            f_new = g_new + h[nbr]
            pq.put((f_new, g_new, nbr, path + [nbr]))