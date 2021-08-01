def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    # print("answer = ", answer)

    j = 0
    n = 0
    while n != len(arr2[0]):
        for i in range(len(arr1)):
            tot = 0
            for m in range(len(arr2)):
                tmp = arr1[i][j] * arr2[m][n]
                j += 1
                tot += tmp
            # print(i, j, m, n, tot)
            answer[i][n] = tot
            j = 0

        i = 0
        j = 0
        m = 0
        n += 1

    return answer

arr1 = [[2, 3, 2], [4, 2, 4]]
arr2 = [[5, 4], [2, 4], [1, 2]]
s = solution(arr1, arr2)
print(s)