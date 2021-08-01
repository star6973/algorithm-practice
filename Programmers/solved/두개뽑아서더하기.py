def solution(numbers):
    answer = []
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])

    answer = list(set(answer))
    answer.sort()
    return answer

numbers = [5,0,2,7]
s = solution(numbers)
print(s)