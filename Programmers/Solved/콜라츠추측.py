def solution(num):
    answer = 0
    '''
        1-1. 입력된 수가 짝수라면 2로 나눕니다. 
        1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
        2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다.
    '''

    cnt = 0
    while num != 1:
        if cnt > 500:
            cnt = -1
            break

        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
        cnt += 1

    answer = cnt
    return answer

n = 626331
s = solution(n)
print(s)