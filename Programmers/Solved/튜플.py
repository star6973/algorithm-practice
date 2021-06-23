import re

def solution(s):

    s = re.split('[{{}}]', s)
    s = list(filter(lambda x: x != '' and x != ',', s))
    s = [set(map(int, _.split(','))) for _ in s]
    s = sorted(s, key=lambda x: len(x))
    # print(s)

    result = []
    dic = dict()
    for i in range(len(s)):
        # print(s[i])
        for j in s[i]:
            if j not in dic.keys():
                result.append(j)
                dic[j] = 1
                break

    return result