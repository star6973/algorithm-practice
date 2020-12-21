'''
    1003. 0을 만들자 - Small

    길이 n인 정수 순열이 주어 졌을 때, 그 안에 숫자를 3개 골라서 합이 0(Zero) 이 되는 조합이 몇 개 있는지 출력하는 프로그램을 만들어 주세요.
    만약 입력으로 [-3, -2, 0, 1, 1, 2, 3] 이 주어 졌을 때, 합이 0이 되는 조합은 (-3, 1, 2), (-2, 1, 1), (-2, 0, 2), ﻿(-3, 0, 3) ﻿ 으로 총 4 개가 있습니다.
    만약 입력이 [1, 1, 0, -1, -1] 일 경우 0이 되는 조합은 (1, 0, -1) 밖에 없으므로, 답은 1이 됩니다.
'''

N = int(input())
init_list = list(input().split())

idx_1 = 0
idx_2 = 1
idx_3 = 2
i = 0
j = 1
k = 2
sum = 0
count = 0
sum_list = []
result = []

for idx_1 in range(i, N-2):
    for idx_2 in range(j, N-1):
        for idx_3 in range(k, N):
            sum = int(init_list[idx_1]) + int(init_list[idx_2]) + int(init_list[idx_3])
            if sum == 0:
                sum_list = []
                sum_list.append(init_list[idx_1])
                sum_list.append(init_list[idx_2])
                sum_list.append(init_list[idx_3])
                result.append(tuple(sum_list))
                count += 1
            idx_3 += 1
        j += 1
        k = j + 1
        idx_2 += 1
    i += 1
    j = i + 1
    k = j + 1
    idx_1 += 1

print(len(list(set(result))))
# result = list(set(list(tuple(set(r)) for r in result)))
# print(len(result))