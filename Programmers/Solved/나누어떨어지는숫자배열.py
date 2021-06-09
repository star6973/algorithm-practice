def solution(arr, divisor):
    answer = []

    for a in arr:
        if a % divisor == 0:
            answer.append(a)
    
    answer.sort()
    if answer != []:
        return answer
    else:
        return [-1]

arr = [3,2,6]
divisor = 10
s = solution(arr, divisor)
print(s)