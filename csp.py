graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']
result = {}

def is_safe(node, color):
    for neighbor in graph[node]:
        if neighbor in result and result[neighbor] == color:
            return False
    return True

def solve(nodes):
    if not nodes:
        return True

    node = nodes[0]

    for color in colors:
        if is_safe(node, color):
            result[node] = color

            if solve(nodes[1:]):
                return True

            del result[node]

    return False

solve(list(graph.keys()))

print("Map Coloring Solution:")
for state, color in result.items():
    print(state, "->", color)