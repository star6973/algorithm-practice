N = int(input())
tower = list(map(int, input().split()))
reversed_tower = list(reversed(tower))

i = 0
j = 1
checked_tower = reversed_tower[-1]
ans = dict()
while tower[0] not in ans.keys():
    if reversed_tower[i] <= reversed_tower[j]:
        ans[reversed_tower[i]] = reversed_tower[i+1]
        i += 1
        j = i + 1
    else:
        i += 1
    
    print(ans)


# ans = dict()
# for i in range(N):
#     for j in range(i+1, N):
#         if reversed_tower[i] < reversed_tower[j]:
#             ans[reversed_tower[i]] = reversed_tower[j]
#             break
#     if j == N-1 and reversed_tower[i] not in ans:
#         ans[reversed_tower[i]] = 0

# for k, v in ans.items():
#     if v != 0:
#         ans[k] = tower.index(v) + 1

# ans = list(reversed(list(v for k, v in ans.items())))
# print(' '.join(map(str, ans)))