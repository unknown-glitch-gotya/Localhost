# Practical 1: Algorithm Analysis – Time Complexity Calculation (Step Counting Method)

# ==========================================
# 1. Non-Recursive Algorithm (Finding Maximum Element)
# ==========================================
def find_max(arr):
    steps = 0
    maximum = arr[0]
    steps += 1
    for i in range(1, len(arr)):
        steps += 1  # loop iteration
        if arr[i] > maximum:
            steps += 1  # comparison true
            maximum = arr[i]
            steps += 1  # assignment
    print("Maximum Element:", maximum)
    print("Total Steps:", steps)

arr = [10, 50, 20, 80, 40]
find_max(arr)

# ==========================================
# 2. Recursive Algorithm (Factorial)
# ==========================================
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
