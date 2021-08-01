def solution(numbers):
    numbers = [str(num) for num in numbers]

    # hash를 dict()로 선언할 경우, 같은 key값은 중복되어 사라짐.
    hash = []
    for num in numbers:
        ori_num = num
        idx = 0
        temp = num
        while len(num) <= 4:
            temp += num[idx]
            idx += 1
            num = temp

        hash.append([int(temp), ori_num])

    # print(hash)

    hash = sorted(hash, key=lambda x: x[0], reverse=True)
    # print(hash)

    answer = str(int("".join([item[1] for item in hash])))
    return answer

numbers = [0, 0, 0, 0]
s = solution(numbers)
print(s)