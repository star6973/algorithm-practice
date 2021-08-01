def measure(num, n):
    div = -1
    rest = []
    while div != 0:
        div = num // 2
        rest.append(num % 2)
        num =  div
    
    rest = list(reversed(rest))

    if len(rest) != n:
        for _ in range(n - len(rest)):
            rest.insert(0, 0)
    
    return rest

def solution(n, arr1, arr2):
    answer = []

    secret_map1 = []
    secret_map2 = []

    for a1, a2 in zip(arr1, arr2):
        secret_map1.append(measure(a1, n))
        secret_map2.append(measure(a2, n))
    
    for map1, map2 in zip(secret_map1, secret_map2):
        tmp = []
        for m1, m2 in zip(map1, map2):
            tmp.append(m1 | m2)
        answer.append(tmp)
    
    result = []
    for i in range(len(answer)):
        tmp = ''
        for j in range(len(answer)):
            if answer[i][j] == 1:
                tmp += '#'
            else:
                tmp += ' '
        result.append(tmp)

    return result

n = 6
a1 = [46, 33, 33 ,22, 31, 50]
a2 = [27 ,56, 19, 14, 14, 10]
s = solution(n, a1, a2)
print(s)