# n개의 요소가 들어있는 배열 중 서로 다른 m개를 뽑는 경우의 수
def pick(arr, picked, m):

    # 더이상 뽑을 기회가 없으면, 지금까지 뽑은 경우의 수 반환
    if m == 0:
        print(picked)
        return picked

    # 아직 아무것도 안뽑았을 경우
    if picked == []:
        smallest = 0
    # 뽑은 경우, 가장 마지막 요소에서 하나 더 큰 값
    else:
        smallest = picked[len(picked)-1] + 1

    for next in range(smallest, len(arr)):
        picked.append(next)
        pick(arr, picked, m-1)
        picked.pop()

pick([0, 1, 2, 3, 4, 5], [], 2)