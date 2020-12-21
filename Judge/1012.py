'''
    1012. 정렬

    정렬은 컴퓨터과학에서 오래된 주제입니다.
    그만큼 다양한 알고리즘이 나와있는데요, 일반적으로 정렬의 최고 시간복잡도는 O(n log n)이지만
    데이터가 특정 형태를 이루면 O(n) 까지의 시간복잡도로 정렬이 가능하기도 합니다.
    이 문제에서는 일반적인 정렬을 구현하여, 입력되는 숫자를 오름차순으로 정렬하려 출력해 주세요.

    # 입력
        첫 줄에는 테스트 케이스의 수 T (1 <= T <= 100) 이 주어집니다.
        두번째 줄에는 정렬할 숫자의 갯수 n ( 1 <= n <= 1,000) 과, 각 숫자 k 가 n개 만큼 주어집니다. k는 32bit signed integer 입니다.

    # 출력
        각 테스트 케이스마다 정렬된 결과를 공백으로 구분하여 출력 해 주세요.
'''

# 5분
T = int(input())

for t in range(T):
    n = int(input())
    k = list(map(int, input().split()))

    for idx, num in enumerate(sorted(k)):
        if idx == n-1:
            print(num)
        else:
            print(num, end=' ')
        idx += 1