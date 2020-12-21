'''
    1018. 문자열 거리 최소화 하기

    N의 두 문자열 X, Y 가 주어졌을 때 두 문자열의 거리는, 같은 위치의 서로 다른 문자의 수로 정의한다.
    즉, Distance(X, Y) = Sum(f(i)) (i = 0..N-1)

            f(i) = 1,  if X[i] != Y[i]

            f(i) = 0,  if X[i] == Y[i]

    예를 들어, "ant" 와 "art" 의 거리는 1 이다.
    두 문자열 A, B가 주어진다고 하자. 이 때, A의 길이는 B보다 짧거나 같다.
    당신은 A의 길이가 B와 같아질 때까지 다음 동작을 수행할 수 있다.

        - 임의의 문자 C를 선택하여 A의 앞에 붙인다.
        - 임의의 문자 C를 선택하여 A의 뒤에 붙인다.

    위의 연산을 적용하여 A의 길이를 B와 같게 만들고자 하는데 이 때,두 문자열의 거리를 최소화 하고자 한다.

    # 입력
        첫 줄에는 테스트 케이스의 수 T ( <= 1,000) 가 주어집니다.
        두 번째 줄부터 T + 1 번 째 줄까지는 최소거리를 구하는 문자열 A, B가 공백으로 구분되어 입력 됩니다.

    # 출력
        각 테스트 케이스당 한줄에 하나씩 최소 거리를 출력 해 주세요.
'''

# 접근법: 예를 들어, A = 'koder', B = 'topcoder'라 한다면,
# 문자열 A를 문자열 B의 한 글자씩 앞에서부터 비교를 한다.
# B1 = 'topco', B2 = 'opcod', B3 = 'pcode', B4 = 'coder'와 같이
# A와 B1~B4까지 비교해가며 가장 많이 같은 경우를 생각해 주면 된다.

# 문자열 A와 B의 서로 다른 문자의 개수 반환 함수(문자열의 최소 거리)
# 주어진 문제의 조건 중 A <= B
def same_len(A, B):
    cnt = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            cnt +=1
    return cnt

T = int(input())
for t in range(T):
    A, B = input().split()
    ans = []

    sub = len(B) - len(A) + 1
    # A와 B의 길이가 같다면 sub = 1이므로, for문은 한 번만 돌게 된다.
    for i in range(sub):
        ans.append(same_len(A, B[i:i+len(A)]))

    print(min(ans))