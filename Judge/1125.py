'''
    1125. 좌우로 밀착 I

    겁 없이 해병대에 자원한 02학번 광성이. 오늘은 입대하는 날이다.
    포항에 집결하자 광성이와 같은 훈련병들이 가슴에 번호표를 달고 어수선하게 흝어지어 있었다.
    질서정연한 것을 좋아하는 해병대 훈련 교관(DI)은 어수선하게 서 있는 훈련병들에게 소리쳤다.

    "자, 번호와 상관없이 C열 종대로 줄 맞추어 섭니다!! 실시!!!"

    쭈뼛쭈뼛 순서와 상관없이 C열로 줄 맞추어 선 광성이와 훈련병들. 해병대는 가입소 기간동안 자진하여 퇴소를 할 수 있다.

    "자자, 본격적인 훈련을 시작하기 전에 집에 갈 사람들은 좌측으로 빠집니다. 실시!!"

    중간 중간 좌측으로 빠지는 훈련병들을 보며 집에 갈까 말까 갈팡질팡하던 광성이. 고민 끝에 좌측으로 빠지려던 찰나,

    "동작 그만! 좌로 밀착한 후 다시 앞으로 밀착하여 빈자리를 채웁니다!!! 실시!!"

    아뿔싸!! 늦었다!! 어서 좌로 밀착한 후 다시 앞으로 밀착하자!!!!

    # 입력
        첫 줄에는 테스트 케이스 개수 T (1 <= T <= 100)가 주어진다.
        각 테스트 케이스마다 행의 수 R, 열의 수 C (1 <= R, C <= 100) 가 주어지고 이후 R 줄에 걸쳐 C개의 번호가 주어진다.
        번호는 0부터 R*C 범위 내이고, 0은 빈자리를 의미한다. 0을 제외한 번호의 중복은 없다.

    # 출력
        빠진 사람 자리를 먼저 좌측으로 밀착하여 채운 후 다시 앞으로 밀착하여 채운 결과를 출력한다.
    주의) 각 줄의 마지막에 공백이 있으면 안됨을 유의해주세요.
'''

class Queue:
    def __init__(self):
        self.items = []

    def isEmpy(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

T = int(input())
for t in range(T):
    R, C = map(int, input().split())

    arr = [[int(c) for c in input().split()] for r in range(R)]

    queue = Queue()
    for r in range(R):
        zero_cnt = 0
        for c in range(C):
            if arr[r][c] == 0:
                zero_cnt += 1
            else:
                queue.enqueue(arr[r][c])

        for c in range(C):
            if c < C - zero_cnt:
                arr[r][c] = queue.dequeue()
            else:
                arr[r][c] = 0

    for c in range(C):
        zero_cnt = 0
        for r in range(R):
            if arr[r][c] == 0:
                zero_cnt += 1
            else:
                queue.enqueue(arr[r][c])

        for r in range(R):
            if r < R - zero_cnt:
                arr[r][c] = queue.dequeue()
            else:
                arr[r][c] = 0

    for r in range(R):
        for c in range(C):
            print(arr[r][c], end = ' ')
        print()