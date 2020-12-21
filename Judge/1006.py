'''
    1006. 거스름돈

    최근 개인 사업을 시작한 광성이는 매일 아침마다 은행에 가서 동전과 지폐들을 교환해 오는것이 일이다.
    현금으로 물건 값을 지불할 경우 조금 더 싸게 한 덕분에 현금으로 구입하는 사람이 많은데, 대부분의 손님들이 물건값보다는
    더 많은 돈을 내서 꼭 거스름돈이 필요해지는 일이 발생하기 때문이다. 그래서 최대한 적은 지폐랑 동전을 사용하여 거스름돈을 주고 싶은데,
    광성이를 위해서 물건값(C)와 받은 금액(R) 이 주어졌을때, 거스름돈으로 지불할 지폐 혹은 동전의 최소 갯수를 출력하는 프로그램을 작성하라.

    예를들여 물건값이 1천원이고, 받은 돈이 1만원이면 거스름돈은 5천원 한장과 1천원 4장으로 총 5장의 현금이 필요하며,
    물건값이 520원이고 받은돈이 1천원일 경우 1백원 짜리 동전 4개와 50원짜리 동전 1개, 그리고 10원짜리 3개로 총 8개의 동전이 필요합니다.
'''

def chargeMoney(money):
    mList = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    mCount = [0, 0, 0, 0, 0, 0, 0, 0]
    result = []

    for m in mList:
        div = money // int(m)
        if div != 0:
            mCount[mList.index(m)] += div
            money = money % int(m)

    return mCount

T = int(input())
r = []
for i in range(T):
    C, R = map(int, input().split())
    rest = R - C
    r.append(rest)

for i in range(T):
    cm = chargeMoney(r[i])
    for c in cm:
        print(c, end=' ')
    print()
