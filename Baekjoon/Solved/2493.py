N = int(input())
tower = list(map(int, input().split()))

'''
    스택을 이용
    확인하고자 하는 현재 값과 스택에 쌓인 값만 비교한다
'''

answer = [0 for i in range(len(tower))]
stack = []
for i, t in enumerate(tower):
    while stack:
        if stack[-1][1] >= t:
            answer[i] = str(stack[-1][0] + 1)
            break
        else:
            # stack의 마지막 값이 비교하려는 값보다 크지 않다면, 앞으로도 볼 이유가 없기에 삭제해준다
            stack.pop()

    if stack == []:
        answer[i] = "0"
    stack.append((i, t))

print(" ".join(answer))