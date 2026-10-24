# Practical 8(C): Depth First Search (DFS)

graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 4],
    3: [1, 4],
    4: [2, 3]
}

visited = set()

def dfs(v):
    visited.add(v)
    print(v, end=" ")
    for n in graph[v]:
        if n not in visited:
            dfs(n)

print("DFS Traversal:")
dfs(0)
print()
