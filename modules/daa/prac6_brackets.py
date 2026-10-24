# Practical 6(C): Check Three Types of Brackets

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
