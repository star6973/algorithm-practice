def solution(dirs):

    '''
        단순 좌표값만을 비교하는 것이 아닌, 경로를 확인해야 할 것!
        따라서 튜플을 활용하여 방향도 생각해주자.
        "URU"의 경우 1이 나와야 하는데, 서로 다른 방향임에도 같은 경로를 사용하기 때문.
    '''

    stack = set()
    pos = {"U": [0, 1], "D": [0, -1], "R": [1, 0], "L": [-1, 0]}
    x, y = 0, 0
    for dir in dirs:
        dx, dy = pos[dir]
        nx, ny = x+dx, y+dy

        if nx >= -5 and nx <= 5 and ny >= -5 and ny <= 5:
            go = (x, y, nx, ny)
            back = (nx, ny, x, y)
            x, y = nx, ny
        
            if go not in stack:
                stack.add(go)
                stack.add(back)

    return len(stack) // 2

dirs = "ULURRDLLU"
s = solution(dirs)
print(s)