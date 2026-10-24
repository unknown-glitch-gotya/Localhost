# Practical 11(B): Perform Right Rotation (LL Case)

class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

def right_rotate(y):
    x = y.left
    y.left = x.right
    x.right = y
    return x

root = Node(30)
root.left = Node(20)
root.left.left = Node(10)
root = right_rotate(root)
print("New Root:", root.key)
