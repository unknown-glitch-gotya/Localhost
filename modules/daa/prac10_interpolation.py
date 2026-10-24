# Practical 10(C): Interpolation Search

a = [10, 20, 30, 40, 50]
key = int(input("Enter element: "))

low, high = 0, len(a) - 1
while low <= high and a[low] <= key <= a[high]:
    if a[low] == a[high]:
        break
    pos = low + (key - a[low]) * (high - low) // (a[high] - a[low])
    if a[pos] == key:
        print("Found at position", pos + 1)
        break
    elif a[pos] < key:
        low = pos + 1
    else:
        high = pos - 1
else:
    print("Not Found")
