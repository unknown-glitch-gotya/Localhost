# Practical 9(D): Display Shortest Distances from User Input

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'B': 3, 'C': 1}
}

source = input("Enter source (A/B/C/D): ")
dist = {v: float('inf') for v in graph}
dist[source] = 0
visited = set()

while len(visited) < len(graph):
    u = min((v for v in graph if v not in visited),
            key=lambda v: dist[v])
    visited.add(u)
    for v, w in graph[u].items():
        dist[v] = min(dist[v], dist[u] + w)

print("Shortest Distances:", dist)
