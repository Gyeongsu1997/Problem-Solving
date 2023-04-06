while True:
    s = input()
    if (s == "."):
        break
    stack = []
    for c in s:
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')':
            if not stack or stack.pop() != '(':
                break
        elif c == ']':
            if not stack or stack.pop() != '[':
                break
    else:
        if not stack:
            print("yes")
            continue
    print("no")
