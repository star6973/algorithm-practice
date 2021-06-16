def solution(participant, completion):
    participant.sort()
    completion.sort()

    for idx, p in enumerate(completion):
        if participant[idx] != completion[idx]:
            return participant[idx]

    return participant[len(participant) - 1]