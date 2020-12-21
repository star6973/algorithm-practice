'''

    1244. [S/W 문제해결 응용] 2일차 - 최대 상금

    퀴즈 대회에 참가해서 우승을 하게 되면 보너스 상금을 획득할 수 있는 기회를 부여받는다.
    우승자는 주어진 숫자판들 중에 두 개를 선택에서 정해진 횟수만큼 서로의 자리를 위치를 교환할 수 있다.

    예를 들어, 다음 그림과 3, 2, 8, 8, 8 의 5개의 숫자판들이 주어지고 교환 횟수는 2회라고 하자.
    처음에는 첫번째 숫자판의 3과 네 번째 숫자판의 8을 교환해서 8, 2, 8, 3, 8이 되었다.
    다음으로, 두 번째 숫자판 2와 마지막에 있는 8을 교환해서 8, 8, 8, 3, 2이 되었다.
    정해진 횟수만큼 교환이 끝나면 숫자판의 위치에 부여된 가중치에 의해 상금이 계산된다.
    숫자판의 오른쪽 끝에서부터 1원이고 왼쪽으로 한자리씩 갈수록 10의 배수만큼 커진다.

    위의 예에서와 같이 최종적으로 숫자판들이 8,8,8,3,2의 순서가 되면 88832원의 보너스 상금을 획득한다.
    여기서 주의할 것은 반드시 횟수만큼 교환이 이루어져야 하고 동일한 위치의 교환이 중복되어도 된다.
    다음과 같은 경우 1회의 교환 횟수가 주어졌을 때 반드시 1회 교환을 수행하므로 결과값은 49가 된다.

    94의 경우 2회 교환하게 되면 원래의 94가 된다.
    정해진 횟수만큼 숫자판을 교환했을 때 받을 수 있는 가장 큰 금액을 계산해보자.

'''

for t in range(int(input())):
    num, change = map(str, input().split())
    change = int(change)
    numList = [int(i) for i in num]
    print(numList)

    # 가장 큰 수를 만들려면
    # 1. 맨 앞의 수가 가장 큰 수가 아니라면, 가장 큰 수를 찾아서 맨 앞의 숫자와 바꿔준다.
    # 1-1. 만약 가장 큰 수가 여러 개라면, 여러 개의 가장 큰 수의 인덱스를 찾아서 모두 바꿔본 뒤, 가장 큰 수를 결정한다.
    # 2. 맨 앞의 수가 가장 큰 수가 맞다면, 다음 수를 맨 앞의 수로 생각하고 1번으로 다시 돌아가서 확인해본다.
    # 3. 한 번 움직인 수는 다시 바꾸지 않도록 설정해야 한다.

    flag = [0 for _ in range(len(numList))]
    i = 0
    while change != 0:
        print(numList)
        if numList[i] != max(numList):
            maxNumIdx = [i for i in range(len(numList)) if numList[i] == max(numList)]
            print(maxNumIdx)
            for idx in maxNumIdx:
                if flag[idx] != 0:
                    maxNumIdx.remove(idx)

            print(maxNumIdx)

            if len(maxNumIdx) == 1:
                numList[i], numList[maxNumIdx[0]] = numList[maxNumIdx[0]], numList[i]
                flag[i] += 1
                flag[maxNumIdx[0]] += 1
            else:
                maxNumList = []
                for idx in maxNumIdx:
                    numList[i], numList[idx] = numList[idx], numList[i]
                    maxNumList.append(int("".join([str(n) for n in numList])))
                    numList[i], numList[idx] = numList[idx], numList[i]
                print(maxNumList)

                remaxNumIdx = maxNumList.index(max(maxNumList))
                print(maxNumIdx[remaxNumIdx])
                numList[i], numList[maxNumIdx[remaxNumIdx]] = numList[maxNumIdx[remaxNumIdx]], numList[i]
                print(numList)
                flag[i] += 1
                flag[maxNumIdx[remaxNumIdx]] += 1

        change -= 1