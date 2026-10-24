# Practical 6(D): Check Multiple Expressions

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
