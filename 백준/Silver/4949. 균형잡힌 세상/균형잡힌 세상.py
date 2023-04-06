while True:
    s = input()
    
    if s == '.':
        break
    
    if s.count('(') != s.count(')') or s.count('[') != s.count(']'):
        print("no")
        continue
    
    b = ""
    for i in s:
        if i in '()[]':
            b += i

    while '()' in b or '[]' in b:
        if '()' in b:
            b = b.replace('()','')
        if '[]' in b:
            b = b.replace('[]','')

    if b:
        print("no")
    else:
        print("yes")
