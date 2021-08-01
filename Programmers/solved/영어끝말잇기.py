def solution(n, words):
    answer = []
    cnt = [0 for _ in range(n+1)]

    prev = words[0]
    answer.append(prev)
    cnt[1] += 1
    
    for i in range(1, len(words)):
        if words[i] not in answer and prev[-1] == words[i][0]:
            answer.append(words[i])
            cnt[i%n + 1] += 1
            prev = words[i]
        else:
            return [i%n + 1, cnt[i%n + 1] + 1]

    return [0, 0]

n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
s = solution(n, words)
print(s)