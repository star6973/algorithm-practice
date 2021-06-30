def check_board(board):
    

def solution(board):
    answer = 1234

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                check_board()

    return answer

board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
s = solution(board)
print(s)