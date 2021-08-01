import sys

st = list(sys.stdin.readline().split())
for i, s in enumerate(st):
    s = s[::-1]
    st[i] = int(s)

print(max(st))