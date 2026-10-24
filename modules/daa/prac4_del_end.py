# Practical 4(D): Circular Linked List - Delete from End

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node(10)
b = Node(20)
c = Node(30)
a.next, b.next, c.next = b, c, a

b.next = a

temp = a
for i in range(2):
    print(temp.data, end=" -> ")
    temp = temp.next
print("Head")
