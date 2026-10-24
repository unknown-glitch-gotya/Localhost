# Practical 1: Algorithm Analysis – Time Complexity Calculation (Step Counting Method)
# Recursive Algorithm (Factorial)

steps = 0

def factorial(n):
    global steps
    steps += 1
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = 5
result = factorial(num)
print("Factorial =", result)
print("Total Steps =", steps)
