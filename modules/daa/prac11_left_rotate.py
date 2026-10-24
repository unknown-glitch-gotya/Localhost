# Practical 11(C): Perform Left Rotation (RR Case)

class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

def left_rotate(x):
    y = x.right
    x.right = y.left
    y.left = x
    return y

root = Node(10)
root.right = Node(20)
root.right.right = Node(30)
root = left_rotate(root)
print("New Root:", root.key)
