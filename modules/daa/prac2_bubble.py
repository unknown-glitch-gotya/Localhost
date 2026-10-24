# Practical 2(A): Bubble Sort

a = [5, 3, 8, 2, 1]
for i in range(len(a)):
    for j in range(len(a) - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print("Sorted List:", a)
