# Practical 2: Implementing and Analyzing Sorting Algorithms

# 2(A): Bubble Sort
a = [5, 3, 8, 2, 1]
for i in range(len(a)):
    for j in range(len(a) - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print("Bubble Sorted:", a)

# 2(B): Insertion Sort
a = [5, 3, 8, 2, 1]
for i in range(1, len(a)):
    key, j = a[i], i - 1
    while j >= 0 and a[j] > key:
        a[j + 1] = a[j]
        j -= 1
    a[j + 1] = key
print("Insertion Sorted:", a)

# 2(C): Merge Sort
def merge(a):
    if len(a) > 1:
        mid = len(a) // 2
        l, r = a[:mid], a[mid:]
        merge(l)
        merge(r)
        i = j = k = 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                a[k] = l[i]
                i += 1
            else:
                a[k] = r[j]
                j += 1
            k += 1
        while i < len(l):
            a[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            a[k] = r[j]
            j += 1
            k += 1

a = [5, 3, 8, 2, 1]
merge(a)
print("Merge Sorted:", a)
