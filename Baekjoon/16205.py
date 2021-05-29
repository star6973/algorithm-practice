n, sign = list(map(str, input().split()))
big_alpha = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
small_alpha = list('abcdefghijklmnopqrstuvwxyz')

# 카멜 표기법
if n == '1':
    camel = sign
    snake = ''
    pascal = ''
    for i in range(len(sign)):
        if i == 0 and sign[i] not in big_alpha:
            pos = small_alpha.index(sign[i])
            pascal += big_alpha[pos]
            snake += sign[i]
        else:
            if sign[i] in big_alpha:
                pos = big_alpha.index(sign[i])
                snake += '_' + small_alpha[pos]
                pascal += sign[i]
            else:
                snake += sign[i]
                pascal += sign[i]

    print(camel, snake, pascal)

# 스네이크 표기법
if n == '2':
    camel = ''
    snake = sign
    pascal = ''
    j = -99
    for i in range(len(sign)):
        if i == 0 and sign[i] not in big_alpha:
            pos = small_alpha.index(sign[i])
            pascal += big_alpha[pos]
            camel += sign[i]
        else:
            if sign[i] == '_':
                j = i
                camel += ''
                pascal += ''
                continue
            if i == j + 1:
                if sign[i] not in big_alpha:
                    pos = small_alpha.index(sign[i])
                    camel += big_alpha[pos]
                    pascal += big_alpha[pos]
            else:
                camel += sign[i]
                pascal += sign[i]

    print(camel, snake, pascal)


# # 파스칼 표기법
if n == '3':
    camel = ''
    snake = ''
    pascal = sign
    for i in range(len(sign)):
        if i == 0 and sign[i] in big_alpha:
            pos = big_alpha.index(sign[i])
            camel += small_alpha[pos]
            snake += small_alpha[pos]
        else:
            if sign[i] in big_alpha:
                pos = big_alpha.index(sign[i])
                snake += '_' + small_alpha[pos]
            else:
                snake += sign[i]

            camel += sign[i]

    print(camel, snake, pascal)