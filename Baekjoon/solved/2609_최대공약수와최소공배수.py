n, m = map(int, input().split())

num_n = []
for i in range(1, n+1):
    if n % i == 0:
        num_n.append(i)

num_m = []
for j in range(1, m+1):
    if m % j == 0:
        num_m.append(j)

# 공약수
inter_num = set(num_n).intersection(set(num_m))

# 최대공약수(공통 약수 중 최대값)
print(max(inter_num))

# 최소공배수(n * m = gcd * lcm을 이용)
print((n * m) // max(inter_num))