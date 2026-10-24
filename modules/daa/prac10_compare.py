# Practical 10(D): Compare Execution Time of Searching Algorithms

import time

a = list(range(10, 10010, 10))
key = 5000

def linear(a, key):
    for i, x in enumerate(a):
        if x == key:
            return i
    return -1

def binary(a, key):
    low, high = 0, len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == key:
            return mid
        elif a[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def interpolation(a, key):
    low, high = 0, len(a) - 1
    while low <= high and a[low] <= key <= a[high]:
        if a[low] == a[high]:
            return low if a[low] == key else -1
        pos = low + (key - a[low]) * (high - low) // (a[high] - a[low])
        if a[pos] == key:
            return pos
        elif a[pos] < key:
            low = pos + 1
        else:
            high = pos - 1
    return -1

for name, func in [("Linear", linear), ("Binary", binary),
                   ("Interpolation", interpolation)]:
    start = time.perf_counter()
    result = func(a, key)
    elapsed = time.perf_counter() - start
    print(name, "Position:", result + 1,
          "Time:", round(elapsed, 6), "sec")
