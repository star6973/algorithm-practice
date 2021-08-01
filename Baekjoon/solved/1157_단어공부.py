from collections import defaultdict

alpha = input()
alpha = alpha.lower()

result = defaultdict(int)
for a in alpha:
    result[a] += 1

max_val = 0
for k, v in result.items():
    if max_val < v:
        max_val = v

max_key = []
for k, v in result.items():
    if max_val == v:
        max_key.append(k)

if len(max_key) >= 2:
    print("?")
else:
    print(max_key.pop().upper())