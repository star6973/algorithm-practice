def solution(absolutes, signs):
    answer = 0

    for ab, si in zip(absolutes, signs):
        if si == True:
            answer += ab
        else:
            answer -= ab

    return answer

ab = [1,2,3]
si = [False,False,True]
s = solution(ab, si)
print(s)