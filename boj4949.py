while True:
    str = input()
    if (str == "."):
        break
    stack = []
    for c in str:
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
