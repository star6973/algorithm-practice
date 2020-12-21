'''
    1009. Endian

    엔디언(Endian or Endianness)은 컴퓨터의 메모리와 같은 1차원의 공간에 여러 개의 연속된 대상을 배열하는 방법을 뜻하며,
    바이트를 배열하는 방법을 특히 바이트 순서(Byte order)라 한다.
    엔디언은 보통 큰 단위가 앞에 나오는 빅 엔디언(Big-endian)과 작은 단위가 앞에 나오는 리틀 엔디언(Little-endian)으로 나눌 수 있다.

    예를 들어 20141127 을 big endian 과 little endian 으로 표현하면 아래와 같다.

        00000001 00110011 01010100 01000111 (Big endian)
        01000111 01010100 00110011 00000001 (Little endian)

    32bit signed ingeger 정수가 주어졌을때 서로 다른 엔디언으로 바꿔 10진수 형태로 출력하라.
'''

# Step_1. 입력된 정수를 엔디언으로 바꾼다(빅엔디언이든 리틀엔디언이든 상관없음).
# Step_2. 만약, 빅엔디언으로 변환했다면 리틀엔디언 형태로 변환한다(순서를 거꾸로 해주면 된다).
# Step_3. 다시 정수로 변환홰준다.

import re
T = int(input())

for i in range(T):
    before_int = int(input())

    # Step_1
    if before_int > 0:
        after_big = re.sub('0x', '', str(hex(before_int)))

        if len(after_big) != 8:
            div = 8 - len(after_big)
            for j in range(div):
                after_big = '0' + after_big

        first = after_big[:2]
        second = after_big[2:4]
        third = after_big[4:6]
        fourth = after_big[6:]

        # Step_2
        first, fourth = fourth, first
        second, third = third, second

        after_small = '0x' + first + second + third + fourth

    # 음수인 경우
    else:
        after_big = re.sub('-0x', '', str(hex(before_int)))

        if len(after_big) != 8:
            div = 8 - len(after_big)
            for j in range(div):
                after_big = '0' + after_big

        first = after_big[:2]
        second = after_big[2:4]
        third = after_big[4:6]
        fourth = after_big[6:]

        temp = first

        if int(fourth) >= 11:
            first = int(fourth) - 1
            first = str(first)
        else:
            first = int(fourth) - 1
            first = '0' + str(first)

        if int(temp) >= 9:
            fourth = int(temp) + 1
            fourth = str(fourth)
        else:
            fourth = int(temp) + 1
            fourth = '0' + str(fourth)

        # Step_2
        second, third = third, second
        after_small = '-0x' + first + second + third + fourth

    # Step_3
    after_int = int(after_small, 16)

    print(after_int)