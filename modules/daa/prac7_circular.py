# Practical 7(B): Circular Queue

q = [None] * 3
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
        q[rear] = x

def dequeue():
    global front, rear
    if front == -1:
        print("Queue Empty")
    else:
        print("Deleted:", q[front])
        if front == rear:
            front = rear = -1
        else:
            front = (front + 1) % size

enqueue(10)
enqueue(20)
enqueue(30)
dequeue()
enqueue(40)
print(q)
