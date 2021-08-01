def solution(arr):
    min_num = 999999999
    for a in arr:
        if min_num >= a:
            min_num = a

    answer = []
    for a in arr:
        if a != min_num:
            answer.append(a)

    if answer == []:
        return [-1]
    else:
        return answer

arr = [4,3,2,1]
s = solution(arr)
print(s)