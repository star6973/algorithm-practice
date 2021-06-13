def solution(s):
    answer = 0
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop(-1)
        else:
            stack.append(i)

    if stack == []:
        return 1
    
    return answer

s = "abab"
s = solution(s)
print(s)