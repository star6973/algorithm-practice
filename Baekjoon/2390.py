R = int(input())
sangeun = list(input())
N = int(input())
friends = []
for n in range(N):
    friends.append(list(input()))

r_s_p = {
    'RS': 2,
    'SP': 2,
    'PR': 2,
    'RR': 1,
    'SS': 1,
    'PP': 1,
    'RP': 0,
    'SR': 0,
    'PS': 0
}

result = 0
for fri in friends:
    for s, f in zip(sangeun, fri):
        result += r_s_p[s+f]

print(result)
print(2 * R * N)