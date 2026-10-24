# Practical 11: AVL Tree Implementation (All Parts)

# 11(A): AVL Insert with LL Rotation
class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None
        self.height = 1

def height(n):
    return n.height if n else 0

def rotate_right(y):
    x = y.left
    y.left = x.right
    x.right = y
    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))
    return x

def insert(root, key):
    if not root:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    root.height = 1 + max(height(root.left), height(root.right))
    balance = height(root.left) - height(root.right)
    if balance > 1 and key < root.left.key:
        return rotate_right(root)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

print("--- 11(A) Insert & Balance ---")
root = None
for x in [30, 20, 10]:
    root = insert(root, x)
inorder(root)
print()

# 11(B): Right Rotation (LL Case)
print("\n--- 11(B) LL Case (Right Rotation) ---")
root_ll = Node(30)
root_ll.left = Node(20)
root_ll.left.left = Node(10)
root_ll = rotate_right(root_ll)
print("New Root:", root_ll.key)

# 11(C): Left Rotation (RR Case)
print("\n--- 11(C) RR Case (Left Rotation) ---")
def rotate_left(x):
    y = x.right
    x.right = y.left
    y.left = x
    return y

root_rr = Node(10)
root_rr.right = Node(20)
root_rr.right.right = Node(30)
root_rr = rotate_left(root_rr)
print("New Root:", root_rr.key)
