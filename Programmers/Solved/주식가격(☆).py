def solution(prices):
    answer = [len(prices)-1-i for i in range(len(prices))]

    '''
        1. stack에는 시점을 저장
        2. prices를 돌고 있는 for문을 현재 시점이라고 가정
        3. 현재 시점에 있는 가격이 stack에 저장되어 있는 가격보다 낮아지는 경우(가격이 떨어진 경우),
           stack에 있는 시점을 pop() -> 현재 시점에 있는 가격보다 클 때까지 계속
           answer에 담겨 있는 인덱스의 값을 변경
        4. 비교했을 때 가격이 높은 경우, 더이상 비교할 필요가 없음
    '''

    stack = [0]

    for i in range(1, len(prices)):
        while stack:
            idx = stack[-1]
            prev_price = prices[idx]
            now_price = prices[i]

            # 가격이 떨어지는 경우
            if prev_price > now_price:
                answer[idx] = i - idx
                stack.pop()

            # 가격이 오르거나 유지되는 경우(다음 시점으로 진행)
            else:
                break
        
        stack.append(i)

    return answer

prices = [1, 2, 3, 2, 3]	
s = solution(prices)
print(s)