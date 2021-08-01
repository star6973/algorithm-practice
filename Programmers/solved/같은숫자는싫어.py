def solution(arr):
    answer = []
    
    now_idx = 0
    now_num = arr[now_idx]

    while True:
        # print("idx, num = ", now_idx, now_num)
        if now_idx >= len(arr):
            break
        if now_num == arr[now_idx]:
            now_num = arr[now_idx]
        else:
            answer.append(now_num)
            now_num = arr[now_idx]

        # print(answer)
        now_idx += 1

    answer.append(now_num)
    return answer

arr = [4,4,4,3,3]	
s = solution(arr)
print(s)