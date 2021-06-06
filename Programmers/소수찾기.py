import math

def solution(n):
    answer = 0
    array = [True for _ in range(n+1)] # 맨 처음 배열은 0부터 시작하는 배열로 설정

    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:
            # i를 제외한 i의 배수 제거
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1
    
    
    answer = len([i for i in range(2, n+1) if array[i] == True])

    return answer

n = 10
s = solution(n)
print(s)