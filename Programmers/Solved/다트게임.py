def solution(dartResult):
    answer = 0

    import re

    '''
        '*' : 앞에 있는 문자가 여러번 반복 가능
        '+' : 앞에 있는 문자를 최소 1번 이상 반복 가능
        '?' : 앞에 있는 문자가 있어도 되고 없어도 되는 것 
    '''
    split_method = re.compile('[0-9]*[SDT]+[#*]?')
    int_method = re.compile('[0-9]+')
    str_method = re.compile('[SDT]+')
    pri_method = re.compile('[#*]+')

    split_dart = split_method.findall(dartResult)
    # print(split_dart)

    stack = []
    for dart in split_dart:
        # print("dart = ", dart)
        if '#' in dart or '*' in dart:
            numbers = int_method.findall(dart)[0]
            scores = str_method.findall(dart)[0]
            prizes = pri_method.findall(dart)[0]
            
            if scores == 'S':
                numbers = int(numbers)**1
            elif scores == 'D':
                numbers = int(numbers)**2
            elif scores == 'T':
                numbers = int(numbers)**3

            if prizes == '*':
                # 첫 번째에 스타상을 받은 경우
                if stack == []:
                    numbers *= 2
                # 두 번째부터 스타상을 받은 경우
                else:
                    last = stack.pop(-1) * 2
                    numbers *= 2
                    stack.append(last)

            elif prizes == '#':
                numbers *= -1

            stack.append(numbers)

        else:
            numbers = int_method.findall(dart)[0]
            scores = str_method.findall(dart)[0]

            if scores == 'S':
                numbers = int(numbers)**1
            elif scores == 'D':
                numbers = int(numbers)**2
            elif scores == 'T':
                numbers = int(numbers)**3

            stack.append(numbers)
    
    answer = sum(stack)
    return answer

dart = "1S*2D*3T*"
s = solution(dart)
print(s)