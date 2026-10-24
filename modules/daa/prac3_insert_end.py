# Practical 3(B): Insert at End

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
new = Node(30)
temp = head
while temp.next:
    temp = temp.next
temp.next = new

while head:
    print(head.data, end=" -> ")
    head = head.next
print("None")
