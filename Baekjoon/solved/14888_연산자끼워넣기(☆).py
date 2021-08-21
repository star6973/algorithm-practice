""" 
    1. 연산자 우선순위는 무시
    2. op list 인덱스 위치는 각각 0: 덧셈, 1: 뺄셈, 2: 곱셈, 3: 나눗셈으로, 개수가 정해짐
"""
N = int(input())
numbers = list(map(int, input().split()))
op = list(map(int, input().split()))
operator = ["+", "-", "*", "/"]
op_list = []
for i, o in enumerate(op):
    for j in range(o):
        op_list.append(operator[i])

from itertools import permutations

per_ops = list(set(permutations(op_list, len(op_list))))

num_ops = []
for ops in per_ops:
    n = numbers[0]
    for i in range(len(numbers) - 1):
        if ops[i] == "+":
            n += numbers[i+1]
        if ops[i] == "-":
            n -= numbers[i+1]
        if ops[i] == "*":
            n *= numbers[i+1]
        if ops[i] == "/":
            if n // numbers[i+1] < 0:
                n = -(-n // numbers[i+1])
            else:
                n = n // numbers[i+1]

    num_ops.append(n)

print(max(num_ops))
print(min(num_ops))