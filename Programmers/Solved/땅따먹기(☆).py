def solution(land):
    answer = []
    for i in range(len(land)):
        for j in range(len(land[i])):
            if i != 0:
                land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])

    answer = max(land[-1]) 
    return answer

land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
s = solution(land)
print(s)