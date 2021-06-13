def solution(N, stages):
    answer = dict()

    for i in range(1, N+1):
        challengers = 0
        failers = 0
        for j in range(len(stages)):
            if stages[j] >= i:
                challengers += 1
            if stages[j] == i:
                failers += 1
        # print("현재 스테이지 : {}, 도전자 수 : {}, 실패한 사람 수 : {}".format(i, challengers, failers))
        if failers == 0:
            answer[i] = 0
        else:
            answer[i] = failers / challengers

    answer = list(dict(sorted(answer.items(), key=lambda x: -x[1])).keys())

    return answer

N = 5
stages = [4, 4, 4, 4]	
s = solution(N, stages)
print(s)