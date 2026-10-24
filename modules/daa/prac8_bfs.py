# Practical 8(D): Breadth First Search (BFS)

graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 4],
    3: [1, 4],
    4: [2, 3]
}

visited = {0}
queue = [0]

print("BFS Traversal:")
while queue:
    v = queue.pop(0)
    print(v, end=" ")
    for n in graph[v]:
        if n not in visited:
            visited.add(n)
            queue.append(n)
print()
