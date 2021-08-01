bracket = input()
stack = []
answer = 0
i = 0
j = 0
for b in bracket:
    print("b = ", b)
    if b == '(':
        stack.append('(')
        i += 1
    if b == '[':
        stack.append('[')
        j += 1
    if b == ')':
        print("stack[-1] = ", stack[-1])
        if stack[-1] == '(':
            print("() 짝 발견")
            stack.pop(-1)
            
            if i == 1:
                answer += 2
                i = 0
            else:
                answer *= 2
                i = 0
        else:
            answer = 0
            break
    if b == ']':
        print("stack[-1] = ", stack[-1])
        if stack[-1] == '[':
            print("[] 짝 발견")
            stack.pop(-1)

            if j == 1:
                answer += 3
                j = 0
            else:
                answer *= 3
                j = 0
        else:
            answer = ''
            break

    print(stack)
    print(answer)