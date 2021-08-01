def solution(files):
    answer = []
    for f in files:
        head = number = tail = ""
        number_check = False
        cnt = 0
        for i in range(len(f)):
            # number 구하기(한 글자에서 최대 다섯 글자 사이의 연속된 숫자로 이루어져 있으며, 앞쪽에 0이 올 수 있음)
            if f[i].isdigit() and cnt < 5:
                number += f[i]
                number_check = True
            
            # head 구하기(숫자가 아닌 문자로 이루어져 있으며, 최소한 한 글자 이상)
            elif number_check == False:
                head += f[i]

            # tail 구하기(나머지 부분으로, 여기에는 숫자가 다시 나타날 수도 있으며, 아무 글자도 없을 수 있음)
            else:
                tail = f[i:]
                break
    
        answer.append((head, number, tail))
    
    # 정렬
    # 1. HEAD 부분을 기준으로 사전 순으로 정렬(문자열 비교 시 대소문자 구분을 하지 않음)
    # 2. NUMBER의 숫자 순으로 정렬(9 < 10 < 0011 < 012 < 13 < 014 순으로 정렬)
    # 3. HEAD 부분과, NUMBER의 숫자도 같을 경우, 원래 입력에 주어진 순서를 유지
    answer.sort(key=lambda x: (x[0].lower(), int(x[1])))
    return [''.join(a) for a in answer]

files = ["abmg1.png", "foo011aaa111bar020.zip", "G-15", "am-g1.png", "MU-ZI01.zip", "mu zi1.png", "foo010bar20.zip"]
s = solution(files)
print(s)