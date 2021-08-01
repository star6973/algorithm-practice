def solution(nums):
    answer = 0

    choice = len(nums) // 2
    set_nums = set(nums)
    
    if len(set_nums) <= choice:
        answer = len(set_nums)
    else:
        answer = choice

    return answer

nums = [3,3,3,2,2,2]
s = solution(nums)
print(s)