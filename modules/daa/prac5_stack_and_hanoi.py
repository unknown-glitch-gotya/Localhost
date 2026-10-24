# Practical 5: Stack Using Array, Linked List & Tower of Hanoi (All Parts)

# 5(A): Stack Using Array
print("--- 5(A) Stack Using Array ---")
stack = []
stack.append(10); stack.append(20); stack.append(30)
print("Stack:", stack)
print("Popped:", stack.pop())
print("Top:", stack[-1])
print("Stack:", stack)

# 5(B): Stack Using Linked List
print("\n--- 5(B) Stack Using Linked List ---")
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
def pop_ll():
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

push(10); push(20); push(30)
display()
print("Popped:", pop_ll())
display()

# 5(C): Tower of Hanoi
print("\n--- 5(C) Tower of Hanoi (3 Disks) ---")
def hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(source, "->", destination)
        return
    hanoi(n - 1, source, destination, auxiliary)
    print(source, "->", destination)
    hanoi(n - 1, auxiliary, source, destination)

hanoi(3, 'A', 'B', 'C')

# 5(D): Stack Operations with Underflow Check
print("\n--- 5(D) Stack Operations with Underflow Check ---")
stk = []
def push_check(x):
    stk.append(x)
def pop_check():
    if not stk:
        print("Stack Underflow")
    else:
        print("Deleted:", stk.pop())

push_check(10); push_check(20); push_check(30)
print("Stack:", stk)
pop_check(); pop_check(); pop_check(); pop_check()
print("Final Stack:", stk)
