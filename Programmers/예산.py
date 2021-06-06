def solution(d, budget):
    answer = 0
    d.sort()

    sum_d = 0
    for i in range(len(d)):
        if sum_d + d[i] <= budget:
            sum_d += d[i]
            answer += 1
        else:
            break
    
    return answer

d = [2,2,3,3]
b = 10
s = solution(d, b)
print(s)