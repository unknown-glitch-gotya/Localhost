# Practical 3(C): Delete from Beginning

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

head = head.next

while head:
    print(head.data, end=" -> ")
    head = head.next
print("None")
