from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for c in course:
        tmp = []
        for order in orders:
            tmp += combinations(sorted(order), c)
        
        counter = Counter(tmp)
        counter = dict(sorted(counter.items(), key=lambda x: -x[1]))

        max_count = 2
        for count in counter:
            if max_count <= counter[count]:
                max_count = counter[count]
                answer.append(''.join(count))

    answer.sort()
    return answer

orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
s = solution(orders, course)
print(s)