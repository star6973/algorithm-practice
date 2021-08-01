from collections import deque

def solution(numbers, target):
    queue = deque()
    queue.append(0)
    
    for num in numbers:
        sub_queue = []
        for q in queue:
            sub_queue.append(q + num)
            sub_queue.append(q - num)

        queue = sub_queue

    return queue.count(target)

numbers = [1, 1, 1, 1, 1]
target = 3
s = solution(numbers, target)
print(s)