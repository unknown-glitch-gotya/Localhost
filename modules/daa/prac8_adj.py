# Practical 8(A): Adjacency List and Adjacency Matrix

graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 4],
    3: [1, 4],
    4: [2, 3]
}
for v in graph:
    print(v, ":", graph[v])

n = 5
edges = [(0, 1), (0, 2), (1, 3), (2, 4), (3, 4)]
matrix = [[0] * n for i in range(n)]
for u, v in edges:
    matrix[u][v] = matrix[v][u] = 1

for row in matrix:
    print(row)
