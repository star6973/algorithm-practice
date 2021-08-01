def solution(s, n):
    answer = ''
    small_alpha = list('abcdefghijklmnopqrstuvwxyz')
    big_alpha = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    small_alpha_length = len(small_alpha)
    big_alpha_length = len(big_alpha)

    for i in range(len(s)):
        if s[i] in small_alpha:
            idx = small_alpha.index(s[i])
            new_s = small_alpha[(idx+n) % small_alpha_length]
            answer += new_s
        elif s[i] in big_alpha:
            idx = big_alpha.index(s[i])
            new_s = big_alpha[(idx+n) % big_alpha_length]
            answer += new_s
        else:
            answer += ' '

    return answer

s = "a B z"
n = 4
s = solution(s, n)
print(s)