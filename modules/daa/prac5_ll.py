# Practical 5(B): Stack Using Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

top = None

def push(x):
    global top
    n = Node(x)
    n.next = top
    top = n

def pop():
    global top
    if top:
        x = top.data
        top = top.next
        return x
    return "Stack Empty"

def display():
    t = top
    while t:
        print(t.data, end=" -> ")
        t = t.next
    print("None")

push(10)
push(20)
push(30)
display()
print("Popped:", pop())
display()
