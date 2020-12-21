'''

    2817. 부분 수열의 합

    A1, A2, ... , AN의 N개의 자연수가 주어졌을 때,
    최소 1개 이상의 수를 선택하여 그 합이 K가 되는 경우의 수를 구하는 프로그램을 작성하시오.

'''

'''

    # 투 포인터를 활용한 알고리즘 코드
    n, m = 5, 5
    data = [1, 2, 3, 2, 5]

    result = 0
    summary = 0
    end = 0

    # start를 차례대로 증가시키며 반복
    for start in range(n):
        # end를 가능한 만큼 이동시키기
        while summary < m and end < n:
            summary += data[end]
            end += 1

        # 부분 합이 m일 때, 카운트 증가
        if summary == m:
            result += 1
        # 현재 start 위치에 있는 값만큼 다시 빼주면서 start를 증가
        summary -= data[start]

    print(result)


    # 구간 합 빠르게 계산하기 -> 접두사 합
    # 1) Prefix Sum을 계산하여 배열 P에 저장(앞에서부터 누적 합을 구함)
    # 2) 매 M개의 쿼리 정보를 확인할 때, 구간 합은 P[R] - P[L-1] 이다.
    n = 5
    data = [10, 20, 30, 40, 50]

    summary = 0
    prefix_sum = [0]
    for i in data:
        summary += i
        prefix_sum.append(summary)

    # 구간 합 계산
    left = 3
    right = 4
    print(prefix_sum[right] - prefix_sum[left-1])

'''

def dfs(idx, summary):

    global cnt

    if idx >= N:
        return

    temp = summary + sequence[idx]
    if temp == K:
        cnt += 1

    dfs(idx+1, summary)  # 다음 인덱스로 넘어가서, 인덱스에 해당하는 값과 summary의 합이 입력받은 K와 같은지 비교
    dfs(idx+1, temp)     # 다음 인덱스로 넘어가서, 인덱스에 해당하는 값과 이전의 인덱스에 있던 값들의 합이 입력받은 K와 같은지 비교


for t in range(int(input())):
    N, K = map(int, input().split())
    sequence = list(map(int, input().split()))
    cnt = 0

    dfs(0, 0)
    print('#{0} {1}'.format(t+1, cnt))