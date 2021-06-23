# 근의 공식: (-b +- 루트(b^2 - 4ac)) //

import math

def solution(brown, red):

    t = (brown-4) // 2
    x1 = int((t+math.sqrt(t*t - 4*red)) // 2)  # 가로
    x2 = int((t-math.sqrt(t*t - 4*red)) // 2)  # 세로

    # print([x1+2, x2+2])
    return [x1+2, x2+2]

s = solution(24, 24)
print(s)