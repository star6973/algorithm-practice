'''

    한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.
    각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

    [제한 조건]
    1. numbers는 길이 1 이상 7 이하인 문자열입니다.
    2. numbers는 0~9까지 숫자만으로 이루어져 있습니다.
    3. "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

'''

# from itertools import combinations, permutations, combinations_with_replacement
#
# # 순열과 조합 예제
# pool = [1, 2, 3]
# print(list(permutations(pool)))
# print(list(permutations(pool, 2)))
# print(list(permutations(pool, 1)))
# print()
# print(list(combinations(pool, 2)))
# print(list(combinations(pool, 1)))
# print()
# print(list(itertools.combinations_with_replacement(pool, 2)))
# print(list(itertools.combinations_with_replacement(pool, 1)))
# print()
# print(list(itertools.cycle(pool)))

from itertools import permutations

def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False

    return True

def solution(numbers):
    numbers = list(numbers)

    result = []
    for i in range(1, len(numbers) + 1):
        iter_numbers = list(permutations(numbers, i))
        iter_numbers = [''.join(num) for num in iter_numbers]

        for num in iter_numbers:
            if int(num) == 0 or int(num) == 1:
                pass
            else:
                if isPrime(int(num)):
                    result.append(int(num))

    return len(list(set(result)))