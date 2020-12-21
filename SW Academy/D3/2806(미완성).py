'''

    2806. N-Queen

    8*8 체스보드에 8개의 퀸을 서로 공격하지 못하게 놓는 문제는 잘 알려져 있는 문제이다.
    퀸은 같은 행, 열, 또는 대각선 위에 있는 말을 공격할 수 있다. 이 문제의 한가지 정답은 아래 그림과 같다.

    이 문제의 조금 더 일반화된 문제는 Franz Nauck이 1850년에 제기했다.
    N*N 보드에 N개의 퀸을 서로 다른 두 퀸이 공격하지 못하게 놓는 경우의 수는 몇가지가 있을까?
    N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

'''

N = int(input())
board = [[0 for i in range(N)] for j in range(N)]
print(board)

for i in range(len(board)):
    for j in range(len(board)):
        if board[i][j] != 1:
            for s in range(len(board)):
                board[s][j] = 2
            for t in range(len(board)):
                board[i][t] = 2


            board[i][j] = 1