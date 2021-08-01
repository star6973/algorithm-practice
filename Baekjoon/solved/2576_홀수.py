numbers = [int(input()) for i in range(7)]
odd_nums = []
for num in numbers:
    if num % 2 != 0:
        odd_nums.append(num)

if odd_nums != []:
    print(sum(odd_nums))
    print(min(odd_nums))
else:
    print(-1)