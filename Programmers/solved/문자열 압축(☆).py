def solution(s):
    result = set()
    for i in range(1, len(s) + 1):
        tmp = []
        for j in range(0, len(s), i):
            tmp.append(s[j:j + i])
        # print(tmp)

        idxList = set()
        for k in range(len(tmp)):
            std = tmp[k]
            for m in range(k + 1, len(tmp)):
                if std != tmp[m]:
                    idxList.add(m)
                    break
        idxList.add(k + 1)
        idxList = sorted(idxList)
        # print(idxList)

        answer = ''
        k = 0
        p = 0
        for idx in idxList:
            # print(tmp[p:idx])
            size = len(tmp[p:idx])
            if size == 1:
                answer += tmp[p:idx][0]
            else:
                answer += (str(size) + tmp[p:idx][0])
            p = idx

        # print(answer)
        result.add(answer)
        # print()

    # print(sorted(result, key=lambda x: len(x)))
    # print(sorted(result, key=lambda x: len(x))[0])
    return len(sorted(result, key=lambda x: len(x))[0])