# Practical 6(A): Check Balanced Parentheses

s = "(a+b)*(c-d)"
stack = []
for ch in s:
    if ch == '(':
        stack.append(ch)
    elif ch == ')':
        if not stack:
            print("Not Balanced")
            break
        stack.pop()
else:
    print("Balanced" if not stack else "Not Balanced")
