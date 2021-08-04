grid = []
for i in range(4):
    grid.append(list(map(int, input().split())))

def DFS(x, y, case):
    # global answer

    if (case == 'down' and x >= 4) or (case == 'right' and y >= 4) or (case == 'diagonal' and x >= 4 or y >= 4):
        return

    num = grid[x][y]
    print("num = ", num)
    print(answer)
    
    if num == 0:
        return
    else:
        if answer[case][num] == []:
            answer[case][num].append((x, y))

        else:
            last_x, last_y = answer[case][num][-1][0], answer[case][num][-1][1]            

            print("last_x, last_y = ", last_x, last_y)
            if case == 'down':
                if x == last_x + 1 and y == last_y:
                    answer[case][num].append((x, y))
                    return DFS(x+1, y, 'down')
                else:
                    return

            elif case == 'right':
                if x == last_x and y == last_y + 1:
                    answer[case][num].append((x, y))
                    return DFS(x, y+1, 'right')
                else:
                    return

            else:
                if x == last_x + 1 and y == last_y + 1:
                    answer[case][num].append((x, y))
                    return DFS(x, y+1, 'diagonal')
                else:
                    return

answer = {'down': {1: [], 2: []}, 'right': {1: [], 2: []}, 'diagonal': {1: [], 2: []}}
for x in range(len(grid)):
    for y in range(len(grid[x])):
        print("(x, y) = ", (x, y), grid[x][y])
        DFS(x+1, y, 'down')       # Down
        DFS(x, y+1, 'right')      # Right
        DFS(x+1, y+1, 'diagonal') # Diagonal


print(sorted(list(set(answer['down'][1]))))
print(sorted(list(set(answer['down'][2]))))
print()
print(sorted(list(set(answer['right'][1]))))
print(sorted(list(set(answer['right'][2]))))
print()
print(sorted(list(set(answer['diagonal'][1]))))
print(sorted(list(set(answer['diagonal'][2]))))

# 0 0 0 0
# 0 1 1 0
# 0 0 1 0
# 0 0 0 2