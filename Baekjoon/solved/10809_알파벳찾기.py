alpha = input()
position = [-1 for _ in range(26)]
alpha_pos = 'abcdefghijklmnopqrstuvwxyz'

for i, a in enumerate(alpha):
    ap = alpha_pos.index(a)
    if position[ap] == -1:
        position[ap] = i

for p in position:
    print(p, end=' ')