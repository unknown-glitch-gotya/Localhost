# Practical 7(C): Queue Using Linked List (collections.deque)

from collections import deque

q = deque()
q.append(10)
q.append(20)
q.append(30)
print("Queue:", list(q))
print("Deleted:", q.popleft())
print("Queue:", list(q))
