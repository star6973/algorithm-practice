def numMeasure(num):
    cnt = 0
    for i in range(1, num+1):
        if num % i == 0:
            cnt += 1
    return cnt

def solution(left, right):
    answer = 0

    for num in range(left, right+1):
        tmp = numMeasure(num)
        if tmp % 2 == 0:
            answer += num
        else:
            answer -= num

    return answer

left = 13
right = 17
s = solution(left, right)
print(s)