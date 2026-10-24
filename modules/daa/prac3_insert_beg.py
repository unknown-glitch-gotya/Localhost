# Practical 3(A): Insert at Beginning

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node(20)
b = Node(30)
a.next = b
new = Node(10)
new.next = a
head = new

while head:
    print(head.data, end=" -> ")
    head = head.next
print("None")
