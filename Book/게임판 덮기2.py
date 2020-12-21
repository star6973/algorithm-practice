da = [[0, 1], [1, 1], [0, 1], [1, 0]]
db = [[1, 0], [0, 1], [-1, 1], [1, 1]]

# 현재 위치에서 가능한 경우를 확인
def isCover(board, idx, jdx):
    # 인덱스 값의 범위가 넘어갈 때
    if idx < 0 or jdx < 0 or idx >= len(board) or jdx >= len(board[0]):
        return False
    # 이미 블록이 쌓여있을 때
    if board[idx][jdx] == "#":
        return False
    # 빈 블록일 때
    if board[idx][jdx] == ".":
        return True


def setBoard(board):

    cnt = 0

    # 빈 칸을 n^2으로 다 찾는게 아니라 빈 칸 딱 하나만 찾아서 그걸로 4번 돌려야 함
    x = -1
    y = 0
    for idx in range(len(board)):
        for jdx in range(len(board[idx])):
            if board[idx][jdx] == ".":
                x = jdx
                y = idx
                break
        if x != -1: #빈 칸 찾았으면 break로 빠져나옴
            break
    if x == -1:
        return 1

    for i in range(4):
        ax = x + da[i][0]
        ay = y + da[i][1]
        bx = x + db[i][0]
        by = y + db[i][1]

        if isCover(board, ay, ax) and isCover(board, by, bx):

            board[y][x] = "#"
            board[ay][ax] = "#"
            board[by][bx] = "#"

            cnt += setBoard(board)

            # 실패한 경우 다시 원위치로
            board[y][x] = "."
            board[ay][ax] = "."
            board[by][bx] = "."

    return cnt

T = int(input())
for t in range(T):

    H, W = map(int, input().split())
    game_board = []
    for h in range(H):
        game_board.append(list(input()))

    cnt = setBoard(game_board)

    print(cnt)