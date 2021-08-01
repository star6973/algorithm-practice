def solution(clothes):
    clothes_hash = dict()
    for c in clothes:
        k, v = c[0], c[1]
        if v not in clothes_hash:
            clothes_hash[v] = 1
        else:
            clothes_hash[v] = clothes_hash.get(v) + 1

    answer = 1
    for i in clothes_hash.values():
        answer *= (i+1) # 안입는 경우의 수를 더함

    return answer - 1 # 모두 안입는 경우를 뺌

clothes = [["a", "head"], ["b", "eyewear"], ["c", "eyewear"], ["d", "eyewear"], ["e", "head"]]
s = solution(clothes)
print(s)