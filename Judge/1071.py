'''
    1071. 암호 해석 - 오고고

    당신은 제 3차 세계대전에서 상대국의 암호를 해석하기 위해 고용된 컴퓨터 과학자입니다.
    상대국의 암호는 당신을 혼란에 빠뜨리기 위해 의미있는 문구 사이에 “ogo”로 시작하며 그 뒤에 “go” 라는 문자열이 0번 이상 반복되는 의미없는 문구들을 담아 놓았습니다.

    예를 들어서 “ogo”, “ogogo”, “ogogogo” 는 당신을 혼란에 빠뜨리기 위한 의미없는 문자열이며,
    “go”, “og”, “ogog”, “ogogog”, “oggo”, 는 당신을 혼란에 빠뜨리기 위한 의미없는 문자열이 아닙니다.

    의미없는 문자열은 항상 가질 수 있는 최대 길이로 간주하여야 합니다.
    예를 들어서 “ogogoo”라는 암호가 주어질 때 “ogo”를 의미없는 문자로,
    “goo”를 의미있는 문자로 취하는 것은 불가능하며 “ogogo” 를 의미없는 문자로 간주하여야 합니다.

    우수한 컴퓨터 과학자인 당신은 주어진 암호문에서 모든 의미없는 문자열을 등장할 때 마다 *** 로 대체하기로 하였습니다.
    주어진 암호문에 대하여 당신의 작업물을 출력 해 주세요.
'''

import re

n = int(input())
input_string = input()

string_list = list(input_string)
base = list('ogo')
go = list('go')

for idx in range(n):
    if string_list[idx-1] == '*' and string_list[idx:idx+2] == go:
        string_list[idx:idx+2] = '##'
    elif string_list[idx-1] == '#' and string_list[idx:idx+2] == go:
        string_list[idx:idx + 2] = '##'
    elif string_list[idx:idx+3] == base:
        string_list[idx:idx+3] = '***'

result = ''
for s in string_list:
    result += s

result = re.sub('#', '', result)
print(result)