while True:
    string = input()
    if string == '.':
        break

    stack = []
    ans = True
    for s in string:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ']':
            if stack != [] and stack[-1] == '[':
                stack.pop(-1)
            else:
                ans = False
                break
        elif s == ')':
            if stack != [] and stack[-1] == '(':
                stack.pop(-1)
            else:
                ans = False
                break
        
    if ans != False and stack == []:
        print('yes')
    else:
        print('no')
