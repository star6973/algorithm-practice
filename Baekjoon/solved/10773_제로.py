N = int(input())
num = []
for i in range(N):
    n = int(input())
    if n != 0:
        num.append(n)
    else:
        num.pop(-1)

if num == []:
    print(0)
else:
    print(sum(num))