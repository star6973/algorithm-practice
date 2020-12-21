'''
    1004. 뒤집어 더하기

    평소 숫자를 가지고 놀기 좋아하는 종섭이는 숫자를 쓰고 더하고 뒤집고 놀다가 재미있는 성질을 발견했다.
    숫자 120 을 뒤집어서 배열하면 021 이 되는데, 원래 숫자와 뒤집은 숫자를 더하면 141 (120 + 021) 이 된다.
    합한 결과인 141은 앞으로 읽으나 뒤로 읽으나 같은 숫자가 된다는 것.
    이렇게 앞으로 읽으나 뒤로 읽으나 같은 것을 회문(Palindrome) 이라고 하는데, 정수가 주어졌을 때,
    정수를 뒤집어 더했을 경우 더해진 숫자가 회문이 되는지 판단하는 프로그램을 만들자.
'''

def isPalindrome(num):
    # 짝수이면
    if len(num) % 2 == 0:
        return list(num[:len(num)//2]) == list(reversed(num[len(num)//2:]))
    else:
        return list(num[:len(num)//2]) == list(reversed(num[len(num)//2+1:]))

T = int(input())
string = []
for i in range(T):
    num = input()
    reversed_num = num[::-1]
    string.append(int(num) + int(reversed_num))

for i in range(T):
    if isPalindrome(str(string[i])):
        print('yes')
    else:
        print('no')
    i += 1