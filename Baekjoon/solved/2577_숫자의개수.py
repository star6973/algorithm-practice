import sys

numbers = [int(sys.stdin.readline().rstrip()) for _ in range(3)]
mult_numbers = 1
for n in numbers:
    mult_numbers *= n

mult_numbers = str(mult_numbers)

answer = [0 for _ in range(10)]
for mn in mult_numbers:
    answer[int(mn)] += 1

for a in answer:
    print(a)