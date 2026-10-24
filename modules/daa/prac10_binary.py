# Practical 10(B): Binary Search

a = [10, 20, 30, 40, 50]
key = int(input("Enter element: "))

low, high = 0, len(a) - 1
while low <= high:
    mid = (low + high) // 2
    if a[mid] == key:
        print("Found at position", mid + 1)
        break
    elif a[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Not Found")
