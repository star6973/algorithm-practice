import re

def solution(s):
    minus = re.compile("-?[0-9]+")
    answer = minus.findall(s)

    new_ans = []
    for ans in answer:
        new_ans.append(int(ans))

    return str(min(new_ans)) + ' ' + str(max(new_ans))

s = "-1 -2 -3 -4"
s = solution(s)
print(s)