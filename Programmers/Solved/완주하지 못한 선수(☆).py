def solution(participant, completion):
    answer = ""

    player = dict()
    # participant 탐색
    for p in participant:
        player[p] = player.get(p, 0) + 1 # get(x, default_value), x가 비어있는 경우 default_value를 대신 가져옴

    # completion 탐색
    for c in completion:
        player[c] = player.get(c, 0) - 1

    answer = [k for k, v in player.items() if v == 1]
    return answer[0]

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
s = solution(participant, completion)
print(s)