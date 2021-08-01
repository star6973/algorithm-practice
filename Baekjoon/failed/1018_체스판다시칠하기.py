N, M = map(int, input().split())
chess = []
for i in range(N):
    chess.append(list(input()))

black_chess = ''.join(['BWBWBWBW', 'WBWBWBWB'] * 4)
white_chess = ''.join(['WBWBWBWB', 'BWBWBWBW'] * 4)

answer = []
for i in range(len(chess)):
    split_chess = []
    for j in range(len(chess)):
        if i <= N - 8 and j <= M - 8:
            split_chess = ''.join([''.join([chess[n][m] for m in range(j, j + 8)]) for n in range(i, i + 8)])
            
            cnt = 0
            if split_chess[0][0] == 'B' and split_chess != black_chess:
                for s, b in zip(split_chess, black_chess):
                    if s != b:
                        cnt += 1
            elif split_chess[0][0] == 'W' and split_chess != white_chess:
                for s, b in zip(split_chess, white_chess):
                    if s != b:
                        cnt += 1
            answer.append(cnt)

if min(answer) > 32:
    print(64 - min(answer))
else:
    print(min(answer))