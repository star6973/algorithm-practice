'''

    5658. 보물상자 비밀번호

    각 변에 다음과 같이 16진수 숫자(0~F)가 적혀 있는 보물상자가 있다.
    보물 상자의 뚜껑은 시계방향으로 돌릴 수 있고, 한 번 돌릴 때마다 숫자가 시계방향으로 한 칸씩 회전한다.
    각 변에는 동일한 개수의 숫자가 있고, 시계방향 순으로 높은 자리 숫자에 해당하며 하나의 수를 나타낸다.

    예를 들어 [Fig.1]의 수는 1A3, B54, 8F9, D66이고, [Fig.2]의 수는 61A, 3B5, 48F, 9D6이다.
    보물상자에는 자물쇠가 걸려있는데, 이 자물쇠의 비밀번호는 보물 상자에 적힌 숫자로 만들 수 있는 모든 수 중, K번째로 큰 수를 10진 수로 만든 수이다.

    N개의 숫자가 입력으로 주어졌을 때, 보물상자의 비밀 번호를 출력하는 프로그램을 만들어보자.
    (서로 다른 회전 횟수에서 동일한 수가 중복으로 생성될 수 있다. 크기 순서를 셀 때 같은 수를 중복으로 세지 않도록 주의한다.)



    [제약 사항]

    N은 4의 배수이고, 8이상 28이하의 정수이다. (8 ≤ N ≤ 28)
    N개의 숫자는 각각 0이상 F이하로 주어진다. (A~F는 알파벳 대문자로만 주어진다.)
    K는 생성 가능한 수의 개수보다 크게 주어지지 않는다.

'''

# 1. N / 4 칸씩 나누기
# 2. 결국 N / 4 회전 후 원위치로 옴
# 3. 네개의 변이기 때문에 A, B, C, D 리스트에 나누기
# 4. 각 리스트에 입력된 문자열을 한 칸씩 돌리면서 넣기
# 5. A, B, C, D의 값을 정렬
# 6. 10진수로 출력하기

T = int(input())

for t in range(1, T + 1):

    N, K = map(int, input().split())
    num = input()

    split_num = N // 4
    A, B, C, D = [], [], [], []

    for i in range(split_num):
        A.append(num[: split_num])
        B.append(num[split_num: 2 * split_num])
        C.append(num[2 * split_num: 3 * split_num])
        D.append(num[3 * split_num: 4 * split_num])

        num = num[len(num) - 1] + num[:len(num) - 1]
        # print(num)

    not_sort_num = list(set(A + B + C + D))
    # print(not_sort_num)

    sort_num = sorted(not_sort_num)
    # print(sort_num)

    max_num = len(sort_num) - K
    # print(max_num)

    print('#{} {}'.format(t, int(sort_num[max_num], 16)))