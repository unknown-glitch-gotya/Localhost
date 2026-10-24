# Practical 6(B): Check Unbalanced Parentheses

s = "(a+b)*(c-d"
stack = []
for ch in s:
    if ch == '(':
        stack.append(ch)
    elif ch == ')':
        if not stack:
            break
        stack.pop()
else:
    if not stack:
        print("Balanced")
    else:
        print("Not Balanced")

if stack and ch == ')':
    print("Not Balanced")
