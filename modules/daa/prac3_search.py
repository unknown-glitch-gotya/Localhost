# Practical 3(D): Search an Element

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
key = 20
temp = head

while temp:
    if temp.data == key:
        print("Element Found")
        break
    temp = temp.next
else:
    print("Element Not Found")
