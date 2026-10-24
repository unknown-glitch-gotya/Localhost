# Practical 2(D): Compare Execution Time of All Three Sorting Algorithms

import random, time

def bubble(a):
    a = a.copy()
    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

def insertion(a):
    a = a.copy()
    for i in range(1, len(a)):
        key, j = a[i], i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key

def merge(a):
    if len(a) > 1:
        m = len(a) // 2
        l, r = a[:m], a[m:]
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

for n in [100, 500, 1000]:
    a = [random.randint(1, 1000) for _ in range(n)]
    print("\nInput Size:", n)
    for name, func in [("Bubble", bubble),
                       ("Insertion", insertion),
                       ("Merge", merge)]:
        start = time.time()
        func(a)
        print(name, "Time:", round(time.time() - start, 5), "sec")
