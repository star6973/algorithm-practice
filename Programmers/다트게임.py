def solution(dartResult):
    answer = 0

    # 스택으로 풀기(괄호 찾는 거 처럼)    
    new_dart = []
    tmp = []
    for i in range(len(dartResult)):
        if dartResult[i] == 'S':
            a = int(''.join(tmp))
            n = a**1
            new_dart.append(n)
            tmp = []

        elif dartResult[i] == 'D':
            a = int(''.join(tmp))
            n = a**2
            new_dart.append(n)
            tmp = []

        elif dartResult[i] == 'T':
            a = int(''.join(tmp))
            n = a**3
            new_dart.append(n)
            tmp = []

        elif dartResult[i] == '*':
            print("* 등장")
            if len(new_dart) == 1:
                print("길이 1")
                answer += 2 * new_dart[-1]
            elif len(new_dart) >= 2:
                print("길이 2 이상", new_dart)
                answer += 2 * (new_dart[-1] + new_dart[-2])
                for j in range(len(new_dart)-2):
                    answer += new_dart[j]
            
        elif dartResult[i] == '#':
            print("# 등장")
            if len(new_dart) == 1:
                print("길이 1")
                answer += (-1) * new_dart[-1]
            elif len(new_dart) >= 2:
                print("길이 2 이상", new_dart)
                answer += (-1) * new_dart[-1]
                for j in range(len(new_dart)-1):
                    answer += new_dart[j]

        # 무조건 숫자
        else:
            tmp.append(dartResult[i])
            print("tmp = ", tmp)
        

        print(dartResult[i], new_dart, answer)

    answer += new_dart[-1]

    print(new_dart)
    
    return answer

dart = "1D2S0T"
s = solution(dart)
print(s)