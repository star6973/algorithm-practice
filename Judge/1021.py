'''
    1021. 연속된 최장 길이

    순열이 주어질 때, 연속으로 증가하는 수의 최장 길이를 구해주세요.

    연속으로 증가한다는 의미는, i+1 번째 수가 i번째 수보다 1이 큰 경우 입니다.
    예를들어 1, 2, 3, 5, 6 의 연속된 최장 길이는 "1, 2, 3" 으로 답이 3이 됩니다.
'''

# 제출 x
T = int(input())

for t in range(T):
    integers = list(map(int, input().split()))
    n = integers.pop(0)

    ans = 0
    if n == 0:
        ans = 0
    elif n == 1:
        ans = 1
    else:
        cnt = 1
        for i in range(len(integers)-1):
            if integers[i]+1 == integers[i+1]:
                cnt += 1
            else:
                cnt = 1

            if ans < cnt:
                ans = cnt

    print(ans)