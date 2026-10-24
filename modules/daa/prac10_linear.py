# Practical 10(A): Linear Search

a = [10, 20, 30, 40, 50]
key = int(input("Enter element: "))

for i in range(len(a)):
    if a[i] == key:
        print("Found at position", i + 1)
        break
else:
    print("Not Found")
