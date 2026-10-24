# Practical 11(D): AVL Tree with Automatic Balancing (LL and RR Rotations)

class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None
        self.h = 1

def ht(n):
    return n.h if n else 0

def insert(r, k):
    if not r:
        return Node(k)
    if k < r.key:
        r.left = insert(r.left, k)
    else:
        r.right = insert(r.right, k)
    r.h = 1 + max(ht(r.left), ht(r.right))
    b = ht(r.left) - ht(r.right)
    if b > 1 and k < r.left.key:
        x = r.left
        r.left = x.right
        x.right = r
        return x
    if b < -1 and k > r.right.key:
        x = r.right
        r.right = x.left
        x.left = r
        return x
    return r

def show(r):
    if r:
        print(r.key, end=" ")
        show(r.left)
        show(r.right)

root = None
for x in [30, 20, 10]:
    root = insert(root, x)
show(root)
print()
