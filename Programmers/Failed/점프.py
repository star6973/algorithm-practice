def solution(n, i, prev, check):
    print("안녕", n, prev[i], prev, check)
    if check[i] == False:
        n -= prev[i]
        check[i] = True
    else:
        return
    
    if n == 1 or prev == [0, 0, 0]:
        print("잘가", n, prev[i], prev, check)
        return n

    elif n <= 0:
        print("돌아가", n, check)
        n += prev[i]
        i += 1
        if i >= len(prev):
            i = 0
            return
        else:
            return solution(n, i, prev, check)
    
    else:
        print("가자", n, prev[i], check)
        prev = [prev[i]*2, prev[i], prev[i]//2]
        return solution(n, i, prev, check)

N = 13
s = solution(N-1, 0, [2, 1, 1/2], [False, False, False])