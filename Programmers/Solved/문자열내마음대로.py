from collections import defaultdict

def solution(strings, n):
    answer = []
    seq = defaultdict(list)
    for s in strings:
        seq[s[n]].append(s)

    seq = dict(sorted(seq.items(), key=lambda x: x[0]))
    print(seq)

    for k, v in seq.items():
        if len(v) > 1:
            v.sort()
            seq[k] = v

    for value in list(seq.values()):
        answer += value

    return answer

s = ["sun", "bed", "car"]
n = 1
s = solution(s, n)
print(s)