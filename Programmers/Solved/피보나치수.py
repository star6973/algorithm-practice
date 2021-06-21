def fibo(n):
    fiboList = [1, 1]
    if n == 1 or n == 2:
        return 1

    # print(fiboList)

    for i in range(2, n):
        fiboList.append(fiboList[i-1] + fiboList[i-2])
        # print(fiboList)

    return fiboList.pop()

def solution(n):
    answer = fibo(n) % 1234567
    return answer

n = 5
s = solution(n)
print(s)


'''
    def fibonacci(num):
        a, b = 0, 1
        for i in range(num):
            a, b = b, a+b
        return a
'''