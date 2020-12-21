'''

    4371. 항구에 들어오는 배

    민석이는 항구가 있는 작은 마을에 산다. 이 항구에는 배가 아주 드물게 지나다닌다.
    민석이는 어느날 모든 배들이 항구에 들어온 것을 보았다. 민석이는 이 날을 1일차로 지정하였다.

    민석이는 배가 한 척이라도 항구에 들렀던 날을 “즐거운 날"로 이름짓고, 1일차부터 즐거운 날들을 모두 기록하였다.
    그러던 중, 한 가지 규칙을 발견했는데, 그 규칙은 각 배들은 항구에 주기적으로 들른다는 것이었다.

    예를 들어, 주기가 3인 배는 항구에 1일차, 4일차, 7일차, 10일차 등에 방문하게 된다.
    민석이가 1일차부터 기록한 “즐거운 날"들의 목록이 주어질 때, 항구에 들렀던 배의 최소 수를 알아내자.
    이 때, 항상 답이 존재하는 입력만 주어진다.

'''

for t in range(int(input())):
    funny = []
    for n in range(int(input())):
        funny.append(int(input()))
    #
    # answer = []
    # cache = [0 for _ in range(len(funny))]
    # cache[0] = 1
    # for i in range(2, len(funny)):
    #     period = funny[i] - funny[i-1]
    #
    #     if cache[i] != 0:
    #     if funny[i] == funny[1] + period:
    #         cache[i] = 1
    #
    # print(cache)










    # for i in range(1, len(funny)):
    #     print(i)
    #     ans = []
    #     temp = funny[i]
    #     period = temp - funny[0]
    #     ans.append(funny[0])
    #     for f in funny:
    #         if temp in funny:
    #             print('같은 경우', temp)
    #             ans.append(temp)
    #         next_funny = temp + period
    #         temp = next_funny
    #
    #     answer.append(ans)
    #
    # print(answer)
    # # print('#{0} {1}'.format(t+1, len(answer)))