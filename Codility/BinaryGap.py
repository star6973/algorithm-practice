def integerToBinary(N):
    result = []
    while N:
        result.append(str(N % 2))
        N //= 2

    return ''.join(result)

def solution(N):
    # write your code in Python 3.6

    # make binary
    binary = integerToBinary(N)
    binary = binary.split("1")
    # print(binary)

    answer = []
    for idx, b in enumerate(binary):
        if idx != 0 and b != "":
            answer.append(len(b))
    # print(answer)

    if answer == []:
        return 0
    else:
        return max(answer)

N = 66561
s = solution(N)
print(s)