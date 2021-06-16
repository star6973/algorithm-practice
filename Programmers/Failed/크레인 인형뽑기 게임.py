def solution(board, move):
    result = []
    for m in move:
        for i in range(len(board)):
            if board[i][m-1] != 0:
                result.append(board[i][m-1])
                board[i][m-1] = 0
                break

    i = 0
    cnt = 0
    # print(result)
    while i != len(result)-1:
        if result[i] == result[i+1]:
            del result[i]
            del result[i]
            print(result)
            cnt += 2
            i = 0
        else:
            i += 1

        if len(result) <= 1:
            break

    # print(result)
    # print(cnt)
    return cnt