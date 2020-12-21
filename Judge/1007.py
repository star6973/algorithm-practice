'''
    1007. 유일한 수

    텔동 한쪽에 있는 마을 "짝" 에는 모든 숫자들이 두개씩 쌍을 이루어 존재하고 있습니다.
    하지만 어디에도 솔로는 존재하듯, 이곳에도 짝을 이루지 못한 숫자 하나가 있지요.
    그나마 다행인건 단 하나의 숫자만 짝이 없을 뿐, 나머지는 짝이 있어요.
    짝을 만들어주기 위하여 단 하나만 있는 숫자를 찾아 주세요.
'''

T = int(input())

result = []
for i in range(T):
    N = int(input())
    K = list(map(int, input().split()))

    dic = {}
    for k in K:
        dic[k] = K.count(k)

    result = []
    for idx, d in enumerate(dic):
        if dic[d] == 1:
            result.append(d)
        idx += 1

for r in result:
    print(r)