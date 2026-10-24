# Practical 1: Algorithm Analysis – Time Complexity Calculation (Step Counting Method)
# Non-Recursive Algorithm (Finding Maximum Element)

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
