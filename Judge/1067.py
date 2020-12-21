'''
    1067. 팰린드롬(Palindrome) 길게 만들기

    팰린드롬이란 앞으로 읽으나 뒤로 읽으나 똑같은 걸 말합니다.
    문자열이 한 줄 주어질 때, 문자열을 재 배치 해서 팰린드롬을 만들 때 가장 길게 만들 수 있는 길이가 몇 인지 판단하는 프로그램을 만들어 주세요.

    # 입력
        첫 줄에는 테스트 케이스의 수 T (1 <= T <= 1000) 가 주어지며
        두번 째 줄부터 T개의 테스트 케이스로 문자열 (길이는 1자 이상 1000자 이하, 영문 대,소문자 만 주어짐)이 주어집니다.

    # 출력
        각 테스트 케이스마다 입력된 문자열을 재 배열 했을 때 가장 긴 팰린드롬의 길이가 몇 인지를 출력 해 주세요.
        대 소문자는 무시해도 됩니다. (즉 aA를 만들 수 있으면 길이 2인 팰린드롬을 만들 수 있습니다)
'''

# 짝수만 이루어져있으면 모두 합치면 되지만, 중간에 홀수인 경우가 있을 경우
# 짝수개만큼만 남기고, 1을 더해준다(만약 남은 값이 1이 있다면).
import string
T = int(input())

for t in range(T):
    ans = input().lower()
    ans = sorted(ans)

    alpha = list(string.ascii_lowercase)

    even = []
    odd = []
    for a in alpha:
        if ans.count(a) == 0:
            pass
        elif ans.count(a) % 2 == 0:
            even.append(ans.count(a))
        else:
            if ans.count(a) > 1:
                even.append(ans.count(a) - ans.count(a) % 2)
                odd.append(ans.count(a) % 2)
            else:
                odd.append(ans.count(a))

    sum = 0
    for e in even:
        sum += e

    if odd != []:
        sum += 1

    print(sum)