'''
    1108. a-b

    숫자 두 개를 입력 받아서 앞의 숫자에서 뒤의 숫자를 뺀 결과를 출력 해 주세요. 단 값이 음수가 될 경우 0을 출력 해 주세요.
'''

a, b = map(int, input().split())
if a > b:
    print(a-b)
else:
    print(0)