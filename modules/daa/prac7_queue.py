# Practical 7: Queue Using Array and Linked List (All Parts)

from collections import deque
import time

# 7(A): Queue Using List
print("--- 7(A) Queue Using List ---")
q = []
q.append(10); q.append(20); q.append(30)
print("Queue:", q)
print("Deleted:", q.pop(0))
print("Queue:", q)

# 7(B): Circular Queue
print("\n--- 7(B) Circular Queue ---")
cq = [None] * 3
front = rear = -1
size = 3

def enqueue(x):
    global front, rear
    if (rear + 1) % size == front:
        print("Queue Full")
    else:
        if front == -1:
            front = 0
        rear = (rear + 1) % size
        cq[rear] = x

def dequeue():
    global front, rear
    if front == -1:
        print("Queue Empty")
    else:
        print("Deleted:", cq[front])
        if front == rear:
            front = rear = -1
        else:
            front = (front + 1) % size

enqueue(10); enqueue(20); enqueue(30)
dequeue()
enqueue(40)
print("Circular Queue array:", cq)

# 7(C): Queue Using Deque
print("\n--- 7(C) Queue Using Deque ---")
dq = deque()
dq.append(10); dq.append(20); dq.append(30)
print("Queue:", list(dq))
print("Deleted:", dq.popleft())
print("Queue:", list(dq))
