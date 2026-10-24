# Practical 10: Searching Techniques (All Parts)

import time

# 10(A): Linear Search
a = [10, 20, 30, 40, 50]
key = 30
for i in range(len(a)):
    if a[i] == key:
        print("Linear Search: Found at position", i + 1)
        break
else:
    print("Linear Search: Not Found")

# 10(B): Binary Search
low, high = 0, len(a) - 1
while low <= high:
    mid = (low + high) // 2
    if a[mid] == key:
        print("Binary Search: Found at position", mid + 1)
        break
    elif a[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Binary Search: Not Found")

# 10(C): Interpolation Search
low, high = 0, len(a) - 1
while low <= high and a[low] <= key <= a[high]:
    if a[low] == a[high]:
        break
    pos = low + (key - a[low]) * (high - low) // (a[high] - a[low])
    if a[pos] == key:
        print("Interpolation Search: Found at position", pos + 1)
        break
    elif a[pos] < key:
        low = pos + 1
    else:
        high = pos - 1
else:
    print("Interpolation Search: Not Found")
