# Practical 4(C): Circular Linked List - Delete from Beginning

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node(10)
b = Node(20)
c = Node(30)
a.next, b.next, c.next = b, c, a

head = b
c.next = head

temp = head
for i in range(2):
    print(temp.data, end=" -> ")
    temp = temp.next
print("Head")
