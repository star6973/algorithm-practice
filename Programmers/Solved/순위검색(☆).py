from itertools import combinations

def solution(info, query):
    answer = []

    # 지원자 정보 딕셔너리 만들기
    apply = {}
    for i, data in enumerate(info):
        data = data.split(" ")
        conditions = data[:-1]
        score = int(data[-1])

        # 조건 조합
        for j in range(5):
            combi = list(combinations(range(4), j))
            for com in combi:
                template = ["-" for _ in range(4)]
                for c in com:
                    template[c] = conditions[c]
                
                template = "".join(template)
                
                if template in apply:
                    apply[template].append(score)
                else:
                    apply[template] = [score]

    for value in apply.values():
        value.sort()

    for qr in query:
        qr = [q for q in qr.split(" ") if 'and' not in q]
        qry_cnd = qr[:-1]
        qry_cnd = "".join(qry_cnd)
        qry_score = int(qr[-1])

        if qry_cnd in apply:
            data = apply[qry_cnd]
            if len(data) > 0:
                start, end = 0, len(data) # lower bound 알고리즘 통해 인덱스 찾기
                
                while start != end and start != len(data):
                    if data[(start + end) // 2] >= qry_score:
                        end = (start + end) // 2
                    else:
                        start = (start + end) // 2 + 1
                answer.append(len(data) - start)
        else:
            answer.append(0)

    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
s = solution(info, query)
print(s)