'''
    1033. 소수(Prime Number)

    소수는 양의 약수가 1과 자신만 있는 1보다 큰 자연수 입니다.
    입력으로 주어진 수가 소수인지 아닌지 판단해 주세요.
'''

# Optimized Method
# We can do following optimizations:
#
# Instead of checking till n, we can check till √n
# because a larger factor of n must be a multiple of smaller factor that has been already checked.
# The algorithm can be improved further by observing that all primes are of the form 6k ± 1, with the exception of 2 and 3.
# This is because all integers can be expressed as (6k + i) for some integer k and for i = ? 0, 1, 2, 3, or 4;
# 2 divides (6k + 0), (6k + 2), (6k + 4); and 3 divides (6k + 3). So a more efficient method is to test if n is divisible by 2 or 3,
# then to check through all the numbers of form 6k ± 1.

def isPrime(n):
    # Corner cases
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0):
        return False

    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6

    return True

n = int(input())
if (isPrime(n)):
    print("prime")
else:
    print("not prime")