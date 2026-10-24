# Practical 4(A): Circular Linked List - Insert at Beginning

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node(10)
b = Node(20)
c = Node(30)
a.next, b.next, c.next = b, c, a

new = Node(5)
new.next = a
c.next = new
head = new

temp = head
for i in range(4):
    print(temp.data, end=" -> ")
    temp = temp.next
print("Head")
