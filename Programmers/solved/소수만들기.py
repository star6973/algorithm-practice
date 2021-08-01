def isPrime(num):
    cnt = 0
    for i in range(1, num+1):
        if num % i == 0:
            cnt += 1

    if cnt == 2:
        return True
    else:
        return False

def solution(nums):
    answer = 0
    # 서로 다른 3개의 숫자 골라서 합 구하기
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                # 소수인 경우 찾기
                if isPrime(nums[i] + nums[j] + nums[k]):
                    answer += 1
    return answer

nums = [1,2,7,6,4]
s = solution(nums)
print(s)