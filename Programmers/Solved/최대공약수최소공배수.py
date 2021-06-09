def solution(n, m):
    answer = []
    measure_n = []
    measure_m = []

    for i in range(1, n+1):
        if n % i == 0:
            measure_n.append(i)
    
    for i in range(1, m+1):
        if m % i == 0:
            measure_m.append(i)

    gcd = max(set(measure_n).intersection(set(measure_m)))
    lcm = gcd * (n // gcd) * (m // gcd)

    answer = [gcd, lcm]

    return answer

n = 30
m = 24
s = solution(n, m)
print(s)