'''
    1026. 인접한 문자 제거하기

    다음과 같이 인접한 문자를 모두 제거하는 기능을 구현하세요.

    문자열 S 가 주어질 때,
    S[i] == S[i+1] 인 가장 작은 i 를 찾습니다.
    S[i] 와 S[i+1] 를 제거합니다.
    S[i] == S[i+1] 인 i 가 존재하지 않을 때까지 반복합니다.

    예를 들어, 입력 문자열 S 가 SIEEILLL 이라면 위의 과정을 통해 아래 순서대로 변하게 됩니다.

                        SIEEILL -> SIILL -> SLL -> S

    위의 과정이 완료된 후 남은 문자열을 답으로 출력합니다.

    # 입력
        첫 줄에는 테스트 케이스 T (1 <= T <= 10,000) 이 주어집니다.
        다음줄부터 각 줄엔 하나의 테스트 케이스에 대한 문자열 S가 주어집니다.
        문자열 S 의 길이는 1 이상 50 이하이며 모두 영문 대문자로 구성되어 있습니다.

    # 출력
        한 줄에 하나씩 인접한 문자들을 제거하고 남은 결과를 출력합니다.
'''

# 15분
def remove(S):
    for idx in range(len(S)-1):
        if S[idx] == S[idx+1]:
            # print('before:', S)
            S.pop(idx)
            S.pop(idx)
            # print('after:', S)
            remove(S)
            break

    return S

T = int(input())

for t in range(T):
    S = list(input())

    result = remove(S)

    for r in result:
        print(r, end='')
    print()