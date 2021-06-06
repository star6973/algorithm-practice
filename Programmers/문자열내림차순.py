def solution(s):
    answer = ''
    # alpha = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    # alpha_cnt = [0 for _ in range(len(alpha))]
    
    # for i in range(len(s)):
    #     alpha_cnt[alpha.index(s[i])] += 1
    # # print(alpha_cnt)

    # unique_alpha = list(set(s))
    # unique_alpha_dict = dict()
    # for a in unique_alpha:
    #     unique_alpha_dict[a] = alpha.index(a)
    
    # unique_alpha_dict_sort = dict(sorted(unique_alpha_dict.items(), key=lambda x: -x[1]))

    # for k, v in unique_alpha_dict_sort.items():
    #     cnt = alpha_cnt[alpha.index(k)]
    #     while cnt != 0:
    #         answer += k
    #         cnt -= 1

    answer = ''.join(sorted(s, reverse=True))

    return answer

s = "ZbcdefgaaaaaAA"
s = solution(s)
print(s)