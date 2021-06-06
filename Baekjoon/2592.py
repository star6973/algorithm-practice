numbers = [int(input()) for _ in range(10)]
unique_numbers = list(set(numbers))
cnt_numbers = dict()

for unum in unique_numbers:
    cnt_numbers[unum] = 0

for num in numbers:
    cnt_numbers[num] += 1

cnt_numbers = dict(sorted(cnt_numbers.items(), key=lambda x: (-x[1], x[0])))

total_nums = sum(numbers)
len_nums = len(numbers)
mean_nums = total_nums // len_nums

print(mean_nums)
print(list(cnt_numbers.keys())[0])