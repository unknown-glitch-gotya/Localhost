# Practical 9: Shortest Path Using Dijkstra’s Algorithm (All Parts)

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'B': 3, 'C': 1}
}

# 9(A): Graph display & all shortest paths from 'A'
print("--- 9(A) Weighted Graph & Shortest Distances from A ---")
for node in graph:
    print(node, ":", graph[node])

dist = {v: 999 for v in graph}
dist['A'] = 0
visited = set()

while len(visited) < len(graph):
    u = min((v for v in graph if v not in visited), key=lambda v: dist[v])
    visited.add(u)
    for v, w in graph[u].items():
        dist[v] = min(dist[v], dist[u] + w)

print("Shortest Distances from A:", dist)

# 9(C): Shortest distance to D
print("\n--- 9(C) Shortest Distance to Vertex 'D' ---")
print("Shortest Distance to D:", dist['D'])
