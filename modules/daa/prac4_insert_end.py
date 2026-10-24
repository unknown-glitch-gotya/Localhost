# Practical 4(B): Circular Linked List - Insert at End

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node(10)
b = Node(20)
c = Node(30)
a.next, b.next, c.next = b, c, a

new = Node(40)
c.next = new
new.next = a

temp = a
for i in range(4):
    print(temp.data, end=" -> ")
    temp = temp.next
print("Head")
