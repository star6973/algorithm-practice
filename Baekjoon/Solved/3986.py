N = int(input())
cnt = 0

for i in range(N):
    word = list(input())

    stack = []
    j = 0
    while True:
        # word의 마지막이 끝나는 동시에, 스택이 비어있다면 좋은 글자로 판명
        if j == len(word):
            if stack == []:
                cnt += 1
            break
        
        if stack == []:
            stack.append(word[j])
            j += 1

        else:
            # 스택에 마지막에 담긴 글자가 새로 들어올 글자와 같은 경우
            # 스택에 담긴 글자를 없애고 다음 위치로 이동
            if stack[-1] == word[j]:
                stack.pop(-1)
                j += 1
            else:
                stack.append(word[j])
                j += 1
print(cnt)