def solution(record):
    answer = []

    user_id = dict()
    for rec in record:
        rec = rec.split(" ")
        if rec[0] == "Enter":
            user_id[rec[1]] = rec[2]

        elif rec[0] == "Change":
            user_id[rec[1]] = rec[2]

    chatting = ""
    for rec in record:
        rec = rec.split(" ")
        if rec[0] == "Enter":
            chatting = user_id[rec[1]] + "님이 들어왔습니다."
            answer.append(chatting)
        if rec[0] == "Leave":
            chatting = user_id[rec[1]] + "님이 나갔습니다."
            answer.append(chatting)

    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
s = solution(record)
print(s)