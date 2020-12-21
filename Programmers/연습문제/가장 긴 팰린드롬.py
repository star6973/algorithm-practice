'''

    앞뒤를 뒤집어도 똑같은 문자열을 팰린드롬(palindrome)이라고 합니다.
    문자열 s가 주어질 때, s의 부분문자열(Substring)중 가장 긴 팰린드롬의 길이를 return 하는 solution 함수를 완성해 주세요.
    예를들면, 문자열 s가 'abcdcba'이면 7을 return하고 'abacde'이면 3을 return합니다.

    [제한 조건]
    1. 문자열 s의 길이 : 2,500 이하의 자연수
    2. 문자열 s는 알파벳 소문자로만 구성

'''

def isPalindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False

def solution(s):
    maxLength = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if maxLength > len(s[i:j]):
                break
            if isPalindrome(s[i:j]):
                if maxLength <= len(s[i:j]):
                    maxLength = len(s[i:j])

    return maxLength