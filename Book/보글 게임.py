dx = [-1, -1, -1, 1, 1, 1, 0, 0]
dy = [-1, 0, 1, -1, 0, 1, -1, 1]

def inRange(y, x):
    rangeX = [x for x in range(len(board))]
    rangeY = [y for y in range(len(board))]

    if x in rangeX and y in rangeY:
        return True
    else:
        return False

def hasWord(y, x, word):
    # 기저 사례 1. 시작 위치가 범위 밖이면 무조건 실패
    if inRange(y, x) == False:
        # print('범위를 벗어남')
        return False

    # 기저 사례 2. 첫 글자가 일치하지 않으면 실패
    if board[y][x] != word[0]:
        # print('첫 글자가 다름')
        return False

    # 기저 사례 3. 단어 길이가 1이면 성공
    if len(word) == 1:
        print('찾고자 하는 단어 존재함!!!')
        return True

    # 인접한 8칸을 검사
    for direction in range(8):
        nextY = y + dy[direction]
        nextX = x + dx[direction]

        # print(nextY, nextX)

        if hasWord(nextY, nextX, word[1:]):
            return True

    return False

board = [['U', 'R', 'L', 'P', 'M'], ['X', 'P', 'R', 'E', 'T'], ['G', 'I', 'A', 'E', 'T'],
         ['X', 'T', 'N', 'Z', 'Y'], ['X', 'O', 'Q', 'R', 'S']]

for i in range(len(board)):
    for j in range(len(board[i])):
        print(board[i][j], end=' ')
    print()
print()
print(hasWord(2, 0, 'GIRL'))