def solution(s):
    answer = True
    stack = []
    
    for i in s:
        if i == '(':
            stack.append(i)
        
        # elif i == ')':
        #     try:
        #         stack.pop()
        #     except Exceptation:
        #         return False 
    
        elif stack == [] and i == ')':
            stack.append(i)
            break
        elif stack != [] and i == ')':
            last = stack.pop()
            if last == '(':
                continue

    if stack != []:
        answer = False

    return answer

s = ")"
s = solution(s)
print(s)