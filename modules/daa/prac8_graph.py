# Practical 8: Graph Representation and Traversals (All Parts)

graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 4],
    3: [1, 4],
    4: [2, 3]
}

# 8(A): Adjacency List & Matrix
print("--- 8(A) Adjacency List ---")
for v in graph:
    print(v, ":", graph[v])

print("\n--- 8(A) Adjacency Matrix ---")
n = 5
edges = [(0, 1), (0, 2), (1, 3), (2, 4), (3, 4)]
matrix = [[0] * n for i in range(n)]
for u, v in edges:
    matrix[u][v] = matrix[v][u] = 1
for row in matrix:
    print(row)

# 8(C): DFS
print("\n--- 8(C) Depth First Search (DFS) ---")
visited = set()
def dfs(v):
    visited.add(v)
    print(v, end=" ")
    for n in graph[v]:
        if n not in visited:
            dfs(n)
dfs(0)
print()

# 8(D): BFS
print("\n--- 8(D) Breadth First Search (BFS) ---")
visited_bfs = {0}
queue = [0]
while queue:
    v = queue.pop(0)
    print(v, end=" ")
    for n in graph[v]:
        if n not in visited_bfs:
            visited_bfs.add(n)
            queue.append(n)
print()
