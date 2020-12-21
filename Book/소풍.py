import time
import numpy as np

# T = int(input())
# start = time.time()
# for t in range(T):
#     student, friend = map(int, input().split())
#     case = list(map(int, input().split()))
#     case_ = [(case[i], case[i+1]) for i in range(0, len(case)-1, 2)]
#     print(case_)
#
#     cnt = 0
#     for i in range(len(case_)):
#         for j in range(i+1, len(case_)):
#             for k in range(j+1, len(case_)):
#                 print(case_[i], case_[j], case_[k])
#                 if set(list(case_[i] + case_[j] + case_[k])) == set([s for s in range(student)]):
#                     cnt += 1
#
#     print(cnt)
# end = time.time()
# print(end-start)

# taken[i] = i번째 학생이 짝을 이미 찾았으면 True, 아니면 False
def countPairings(taken):

    # 남은 학생들 중 가장 번호가 빠른 학생을 찾는다
    firstFree = -1
    for i in range(student):
        if taken[i] == False:
            firstFree = i
            break

    # 모든 학생이 짝을 찾았으면 한 가지 방법을 찾았으니 종료한다
    if firstFree == -1:
        return 1

    ret = 0
    for pairWith in range(firstFree, student):
        # print(pairWith)
        # print(taken[pairWith])
        # print(areFriends[firstFree][pairWith])
        if taken[pairWith] == False and areFriends[firstFree][pairWith] == True:
            taken[firstFree], taken[pairWith] = True, True
            ret += countPairings(taken)
            taken[firstFree], taken[pairWith] = False, False
        # print()

    return ret


T = int(input())
start = time.time()
for t in range(T):
    student, friend = map(int, input().split())
    case = list(map(int, input().split()))
    # 가장 빠른 순으로 정렬(1/2로 줄일 수 있음)
    case = sorted([sorted([case[i], case[i+1]]) for i in range(0, len(case)-1, 2)])
    print(case)

    taken = [False for idx in range(student)]
    # 서로 친한 경우(case를 바탕으로)
    areFriends = np.zeros((student, student))
    for c in case:
        areFriends[c[0]][c[1]] = True
        # areFriends[c[1]][c[0]] = True # 앞에서 가장 빠른 순으로 정렬했기 때문에 필요없음

    print(taken)
    print(areFriends)

    print(countPairings(taken))
end = time.time()
print(end-start)