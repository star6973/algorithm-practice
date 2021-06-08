dct = ''.join(list(map(str, input().split())))
ascending = ''.join([str(_) for _ in range(1, 9)])
descending = ''.join([str(_) for _ in range(8, 0, -1)])

if dct == ascending:
    print('ascending')
elif dct == descending:
    print('descending')
else:
    print('mixed')