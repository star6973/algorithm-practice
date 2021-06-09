def solution(answers):
    one = list(map(int, '12345'))
    two = list(map(int, '21232425'))
    three = list(map(int, '3311224455'))
    clear = [0, 0, 0]

    for i in range(len(answers)):
        if answers[i] == one[i%len(one)]:
            clear[0] += 1
        if answers[i] == two[i%len(two)]:
            clear[1] += 1
        if answers[i] == three[i%len(three)]:
            clear[2] += 1
    
    max_clear = max(clear)
    
    result = []
    for i in range(len(clear)):
        if clear[i] == max_clear:
            result.append(i+1)
    
    return result

a = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2]
s = solution(a)
print(s)