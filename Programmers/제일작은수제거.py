def solution(arr):
    min_num = 999999999
    for a in arr:
        if min_num < a:
            min_num = a

    for a in arr:
        if a == min_num:
            arr.pop(a)

    if arr == []:
        return [-1]
    else:
        return list(reversed(arr))

arr = [4,3,2,1]
s = solution(arr)
print(s)