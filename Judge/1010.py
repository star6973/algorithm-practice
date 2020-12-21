'''
    1010. 접두 소수

    숫자 "2333"의 경우 접두 숫자인 "2", "23", "233", "2333" 이 모두 소수입니다.
    길이 n이 주어졌을 때 길이 n에 해당하는 모든 접두 소수를 출력해주세요.
'''

import math
def isPrime(num):
    state = True
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            state = False

    return state

num = 6
if isPrime(num):
    print('True')
else:
    print('False')