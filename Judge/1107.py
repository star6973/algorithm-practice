'''
    1107. C++ 프로그래밍 실습시험 연습문제 - 모음 문자 수

    주어진 문자열의 모음 문자들의 총 몇 개 있는지 출력하시오.
    예를 들어 문자열이 "apple"이면 a, e가 각각 한 번씩 등장하므로 2가 출력되어야 합니다.
    문자열의 길이는 0부터 1,000이하이며, 모두 영문자 소문자로만 구성되어 있다.
'''

vowel = ['a', 'e', 'i', 'o', 'u']

T = int(input())

string_alpha = []
for t in range(T):
    string_alpha = input()

    cnt = 0
    for idx, s in enumerate(string_alpha):
        if s in vowel:
           cnt += 1

    print(cnt)