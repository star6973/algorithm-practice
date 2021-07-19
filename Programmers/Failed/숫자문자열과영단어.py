wordDict = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}

def solution(s):
    for k, v in wordDict.items():
        if s.count(v) >= 1:
            s = s.replace(v, str(k))

    return int(s)

s = "one4seveneight"
s = solution(s)
print(s)