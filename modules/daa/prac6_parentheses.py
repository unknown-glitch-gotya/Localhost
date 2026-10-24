# Practical 6: Balanced Parentheses Checker Using Stack (All Parts)

# 6(A): Single Expression Balanced
print("--- 6(A) Balanced Test ---")
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

# 6(B): Single Expression Unbalanced
print("\n--- 6(B) Unbalanced Test ---")
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
    print("Balanced" if not stack else "Not Balanced")

# 6(C): Three Types of Brackets
print("\n--- 6(C) Three Types of Brackets {[()]} ---")
s = "{[()]}"
stack = []
pairs = {')': '(', ']': '[', '}': '{'}
ok = True
for ch in s:
    if ch in "([{":
        stack.append(ch)
    elif ch in ")]}":
        if not stack or stack.pop() != pairs[ch]:
            ok = False
            break
print("Balanced" if ok and not stack else "Not Balanced")

# 6(D): Multiple Expressions
print("\n--- 6(D) Multiple Expressions ---")
expressions = ["(a+b)", "(a+b", "((a+b))", "a+b)"]
for s in expressions:
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if not stack:
                stack.append("Error")
                break
            stack.pop()
    if not stack:
        print(s, ": Balanced")
    else:
        print(s, ": Not Balanced")
