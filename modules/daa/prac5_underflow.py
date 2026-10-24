# Practical 5(D): Stack Operations with Underflow Check

stack = []

def push(x):
    stack.append(x)

def pop():
    if not stack:
        print("Stack Underflow")
    else:
        print("Deleted:", stack.pop())

push(10)
push(20)
push(30)
print("Stack:", stack)
pop()
pop()
pop()
pop()
print("Final Stack:", stack)
