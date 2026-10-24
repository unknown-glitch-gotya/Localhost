# Practical 4: Circular Linked List Operations (All Parts)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 4(A): Insert at Beginning
print("--- 4(A) Insert at Beginning ---")
a = Node(10); b = Node(20); c = Node(30)
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

# 4(B): Insert at End
print("\n--- 4(B) Insert at End ---")
a = Node(10); b = Node(20); c = Node(30)
a.next, b.next, c.next = b, c, a
new = Node(40)
c.next = new
new.next = a
temp = a
for i in range(4):
    print(temp.data, end=" -> ")
    temp = temp.next
print("Head")

# 4(C): Delete from Beginning
print("\n--- 4(C) Delete from Beginning ---")
a = Node(10); b = Node(20); c = Node(30)
a.next, b.next, c.next = b, c, a
head = b
c.next = head
temp = head
for i in range(2):
    print(temp.data, end=" -> ")
    temp = temp.next
print("Head")

# 4(D): Delete from End
print("\n--- 4(D) Delete from End ---")
a = Node(10); b = Node(20); c = Node(30)
a.next, b.next, c.next = b, c, a
b.next = a
temp = a
for i in range(2):
    print(temp.data, end=" -> ")
    temp = temp.next
print("Head")
