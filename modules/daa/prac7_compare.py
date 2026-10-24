# Practical 7(D): Compare Queue Operations (List vs Deque)

import time
from collections import deque

n = 10000

q = []
start = time.time()
for i in range(n):
    q.append(i)
for i in range(n):
    q.pop(0)
print("List Time:", round(time.time() - start, 4))

q = deque()
start = time.time()
for i in range(n):
    q.append(i)
for i in range(n):
    q.popleft()
print("Deque Time:", round(time.time() - start, 4))
