# Practical 2(C): Merge Sort

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
print("Sorted List:", a)
