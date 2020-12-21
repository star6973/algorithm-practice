import time
import numpy as np

def movingAverage1(A, M):
    start = time.time()

    ret = []
    N = len(A)
    for i in range(M-1, N):
        partialSum = 0
        for j in range(M):
            partialSum += A[i-j]
        ret.append(partialSum // M)

    end = time.time()
    print('{:.10f}'.format(end - start))
    return ret

def movingAverage2(A, M):
    start = time.time()

    ret = []
    for i in range(len(A)-M+1):
        partialSum = A[i:i+M]
        ret.append(sum(partialSum) // M)

    end = time.time()
    print('{:.10f}'.format(end - start))
    return ret

def movingAverage3(A, M):
    start = time.time()

    ret = []
    N = len(A)
    partialSum = 0
    for i in range(M-1):
        partialSum += A[i]  # M-2일까지의 몸무게들의 합

    for i in range(M-1, N):  # M-1일부터 N-1일까지
        partialSum += A[i]   # 현재 위치의 몸무게 더하기
        ret.append(partialSum // M)
        partialSum -= A[i-M+1]  # 가장 맨 앞의 몸무게 빼기

    end = time.time()
    print('{:.10f}'.format(end - start))
    return ret


A = np.random.randint(100000, size=1000000)
M = 3
movingAverage1(A, M)
movingAverage2(A, M)
movingAverage3(A, M)