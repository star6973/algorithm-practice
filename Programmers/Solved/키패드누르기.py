def distance(a, b, m, h):
    dis_a = abs(a[0] - m[0]) + abs(a[1] - m[1])
    dis_b = abs(b[0] - m[0]) + abs(b[1] - m[1])

    # print("비교하기, dis_a = {0}, dis_b = {1}".format(dis_a, dis_b))

    if dis_a < dis_b:
        return "L"
    elif dis_a > dis_b:
        return "R"
    else:
        if h == "right":
            return "R"
        else:
            return "L"

def solution(numbers, hand):
    answer = ''
    
    phone_num = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    left_num = [1, 4, 7]
    right_num = [3, 6, 9]
    middle_num = [2, 5, 8, 0]
    left_pos = [3, 0]
    right_pos = [3, 2]

    # print("현재 left_pos = {0}, right_pos = {1}".format(left_pos, right_pos))

    for num in numbers:
        num_pos = [0, 0]
        # 현재 num의 좌표 구하기
        for i in range(len(phone_num)):
            for j in range(len(phone_num)-1):
                if num == phone_num[i][j]:
                    num_pos = [i, j]
                    print(num_pos)
        # print("선택된 숫자 = {0}, 위치 = {1}".format(num, num_pos))

        if num in left_num:
            left_pos = num_pos
            answer += "L"
        if num in right_num:
            right_pos = num_pos
            answer += "R"
        if num in middle_num:
            dis = distance(left_pos, right_pos, num_pos, hand)
            answer += dis
            if dis == "L":
                left_pos = num_pos
            else:
                right_pos = num_pos

        # print("현재 left_pos = {0}, right_pos = {1}".format(left_pos, right_pos))

    return answer

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
h = "left"
s = solution(n, h)
print(s)