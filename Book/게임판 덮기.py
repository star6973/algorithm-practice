# 현재 위치에서 가능한 경우를 확인
def isCover(board, idx, jdx):
    # 인덱스 값의 범위가 넘어갈 때
    if idx < 0 or jdx < 0 or idx >= len(board) or jdx >= len(board[0]):
        return False
    # 빈 블록일 때
    if board[idx][jdx] == ".":
        return True


def setBoard(board):

    # 만약 채워지는 것이 실패하면 cnt는 0이 유지됨
    cnt = 0

    # 빈 칸을 n^2으로 다 찾는게 아니라 빈 칸 딱 하나만 찾아서 그걸로 4번 돌려야 함
    x = -1
    y = 0
    for idx in range(len(board)):
        for jdx in range(len(board[idx])):

            # 빈 칸이 있으면 그 위치를 고정
            if board[idx][jdx] == ".":
                x = idx
                y = jdx
                break

        # 빈 칸 찾았으면 break로 빠져나옴
        if x != -1:
            break

    # x가 -1로 유지 되었다는 것은 빈 칸이 모두 채워졌다는 것이므로 성공(1을 반환)
    if x == -1:
        return 1

    idx = x
    jdx = y

    # ㄱ 모양
    if isCover(board, idx, jdx + 1) and isCover(board, idx + 1, jdx):

        board[idx][jdx] = "#"
        board[idx][jdx + 1] = "#"
        board[idx + 1][jdx] = "#"

        cnt += setBoard(board)

        # 다시 원위치로(성공하건, 실패하건 다시 원위치로 돌려야지 다른 경우의 수를 확인할 수 있음)
        board[idx][jdx] = "."
        board[idx][jdx + 1] = "."
        board[idx + 1][jdx] = "."

    # 거꾸로 된 ㄱ 모양
    if isCover(board, idx + 1, jdx + 1) and isCover(board, idx, jdx + 1):
        board[idx][jdx] = "#"
        board[idx + 1][jdx + 1] = "#"
        board[idx][jdx + 1] = "#"

        cnt += setBoard(board)

        board[idx][jdx] = "."
        board[idx + 1][jdx + 1] = "."
        board[idx][jdx + 1] = "."

    # 거꾸로된 ㄴ 모양
    if isCover(board, idx + 1, jdx) and isCover(board, idx + 1, jdx - 1):
        board[idx][jdx] = "#"
        board[idx + 1][jdx] = "#"
        board[idx + 1][jdx - 1] = "#"

        cnt += setBoard(board)

        board[idx][jdx] = "."
        board[idx + 1][jdx] = "."
        board[idx + 1][jdx - 1] = "."


    # ㄱ 모양
    if isCover(board, idx + 1, jdx) and isCover(board, idx + 1, jdx + 1):
        board[idx][jdx] = "#"
        board[idx + 1][jdx] = "#"
        board[idx + 1][jdx + 1] = "#"

        cnt += setBoard(board)

        board[idx][jdx] = "."
        board[idx + 1][jdx] = "."
        board[idx + 1][jdx + 1] = "."

    return cnt


T = int(input())
for t in range(T):

    H, W = map(int, input().split())
    game_board = []
    for h in range(H):
        game_board.append(list(input()))

    cnt = setBoard(game_board)

    print(cnt)