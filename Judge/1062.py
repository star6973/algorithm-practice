'''
    1062. 일의 위치 출력하기

    32-bit signed integer는 32개의 비트로 표현되는 정수형 입니다.
    비트로 표현했을 때, 1의 위치는 어떻게 되는지 출력하는 프로그램을 만들어 주세요.

    예를 들어 5가 비트로 표현되는것은 00000000 00000000 00000000 00000101와 같고, 1의 위치는 0과 2가 됩니다. (가장 오른쪽이 0번째 입니다)

    # 입력
        첫 줄에는 테스트 케이스의 수 T (1 <= T <= 1000)가 주어지며,
        두 번째 줄 부터는 32-bit signed integer 인 N (N >= 0)이 주어집니다.

    #출력
        각 테스트 케이스당 1의 위치를 LSB(오른쪽, 0부터 시작)부터 공백으로 구분하여 출력해주세요.
        만약 1이 한개도 없으면 -1을 출력해 주세요.

        각 줄의 마지막에 공백이 있으면 안됨을 유의해주세요.
        즉, 공백을 _ 로 표현하면, 아래와 같이 출력되어야만 정답이고
        0_1_3

        아래와 같이 출력되면 출력형식 오류가 됩니다.
        0_1_3_
'''

# 17분
T = int(input())

for t in range(T):
    num = int(input())

    cnt = 0
    div = num
    count = []
    # 1이 한 개도 없는 경우는 모두 0인 경우
    if num == 0:
        print(-1)
    else:
        while div != 1:
            r = num % 2
            div = num // 2
            num = div


            if r == 1:
                count.append(cnt)
            cnt += 1
        count.append(cnt)

    for idx, c in enumerate(count):
        if idx == len(count):
            print(c)
        else:
            print(c, end=' ')