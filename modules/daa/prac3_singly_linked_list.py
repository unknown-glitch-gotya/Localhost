# Practical 3: Singly Linked List Operations (All Parts)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 3(A): Insert at Beginning
print("--- 3(A) Insert at Beginning ---")
a = Node(20)
b = Node(30)
a.next = b
new = Node(10)
new.next = a
head = new
cur = head
while cur:
    print(cur.data, end=" -> ")
    cur = cur.next
print("None")

# 3(B): Insert at End
print("\n--- 3(B) Insert at End ---")
head2 = Node(10)
head2.next = Node(20)
end_node = Node(30)
temp = head2
while temp.next:
    temp = temp.next
temp.next = end_node
cur = head2
while cur:
    print(cur.data, end=" -> ")
    cur = cur.next
print("None")

# 3(C): Delete from Beginning
print("\n--- 3(C) Delete from Beginning ---")
head3 = Node(10)
head3.next = Node(20)
head3.next.next = Node(30)
head3 = head3.next
cur = head3
while cur:
    print(cur.data, end=" -> ")
    cur = cur.next
print("None")

# 3(D): Search an Element
print("\n--- 3(D) Search an Element ---")
key = 20
temp = head3
while temp:
    if temp.data == key:
        print("Element Found")
        break
    temp = temp.next
else:
    print("Element Not Found")
