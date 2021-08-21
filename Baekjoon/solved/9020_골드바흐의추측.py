N = int(input())

def prime_list(n):
    sieve = [False, False] + [True] * n

    m = int(n ** 0.5)
    for i in range(2, m+1):
        if sieve[i] == True:
            for j in range(i+i, n, i): # i 이후 i의 배수들은 False로 판단
                sieve[j] = False

    return sieve

for n in range(N):
    n = int(input())

    prime = prime_list(n)
    print(prime)

    A = n // 2
    B = A
    for _ in range(n):
        if prime[A] and prime[B]:
            print(A, B)
            break
        A -= 1
        B += 1