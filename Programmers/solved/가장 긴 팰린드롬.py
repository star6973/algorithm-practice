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