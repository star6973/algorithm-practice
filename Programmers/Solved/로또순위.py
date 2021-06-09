def solution(lottos, win_nums):
    answer = []
    winning = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    max_win = 0
    min_win = 0
    cnt = 0
    zero = 0
    for l in lottos:
        if l in win_nums:
            cnt += 1
        if l == 0:
            zero += 1
    
    min_win = winning[cnt]
    max_win = winning[cnt + zero]

    answer.append(max_win)
    answer.append(min_win)
    
    return answer

l = [45, 4, 35, 20, 3, 9]
w = [20, 9, 3, 45, 4, 35]
s = solution(l, w)
print(s)