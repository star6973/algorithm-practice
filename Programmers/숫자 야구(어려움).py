'''

    숫자 야구 게임이란 2명이 서로가 생각한 숫자를 맞추는 게임입니다.

    각자 서로 다른 1~9까지 3자리 임의의 숫자를 정한 뒤 서로에게 3자리의 숫자를 불러서 결과를 확인합니다.
    그리고 그 결과를 토대로 상대가 정한 숫자를 예상한 뒤 맞힙니다.

        * 숫자는 맞지만, 위치가 틀렸을 때는 볼
        * 숫자와 위치가 모두 맞을 때는 스트라이크
        * 숫자와 위치가 모두 틀렸을 때는 아웃

    예를 들어, 아래의 경우가 있으면

        A : 123
        B : 1스트라이크 1볼.
        A : 356
        B : 1스트라이크 0볼.
        A : 327
        B : 2스트라이크 0볼.
        A : 489
        B : 0스트라이크 1볼.

    이때 가능한 답은 324와 328 두 가지입니다.

    질문한 세 자리의 수, 스트라이크의 수, 볼의 수를 담은 2차원 배열 baseball이 매개변수로 주어질 때,
    가능한 답의 개수를 return 하도록 solution 함수를 작성해주세요.

    [제한 조건]
    1. 질문의 수는 1 이상 100 이하의 자연수입니다.
    2. baseball의 각 행은 [세 자리의 수, 스트라이크의 수, 볼의 수] 를 담고 있습니다.

'''

from itertools import permutations

def st_B(given, chosen):
    st = 0
    B = 0
    chosen_dif = []
    given_dif = []
    for i in range(3):
        if given[i] == chosen[i]:
            st += 1
        else:
            given_dif.append(given[i])
            chosen_dif.append(chosen[i])

    # print(chosen, given)
    # print(chosen_dif, given_dif)

    for num in chosen_dif:
        if num in given_dif:
            B += 1
    # print(st, B)
    # print()
    return st, B

def solution(baseball):
    first = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))

    second = []
    for each in baseball:
        given = [int(i) for i in str(each[0])]
        stb = (each[1], each[2])

        for chosen in first:
            if st_B(given, chosen) == stb:
                second.append(chosen)
        # print(second)
        first = second
        second = []
    return len(first)

baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]
print(solution(baseball))