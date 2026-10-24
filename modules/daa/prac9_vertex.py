# Practical 9(C): Find the Shortest Distance to a Given Vertex

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'B': 3, 'C': 1}
}

dist = {v: float('inf') for v in graph}
dist['A'] = 0
visited = set()

while 'D' not in visited:
    u = min((v for v in graph if v not in visited),
            key=lambda v: dist[v])
    visited.add(u)
    for v, w in graph[u].items():
        dist[v] = min(dist[v], dist[u] + w)

print("Shortest Distance to D:", dist['D'])
