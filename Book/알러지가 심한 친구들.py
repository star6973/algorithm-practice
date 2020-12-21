import pandas as pd

food = ['갈비찜', '피자', '잡채', '떡볶이', '탕수육', '닭강정']
friend = ['페이', '지아', '민', '수지']
alergy = [['x', 'o', 'o', 'o', 'x', 'x'],
          ['x', 'x', 'x', 'x', 'o', 'o'],
          ['o', 'x', 'o', 'x', 'o', 'x'],
          ['o', 'o', 'x', 'x', 'x', 'o']]

table = pd.DataFrame(alergy, index=friend, columns=food)
print(table)
print()

# # 이름을 이용(.loc)
# print(table.loc[:, '갈비찜':'피자'])
# print()
# print(table.loc['페이':'지아'])
# print()
# print(table.loc['페이':'지아', '잡채':'닭강정'])
# print()
# print(table.loc[['페이', '수지'], ['피자', '잡채', '탕수육']])  # 행, 열
# print()
# print(table.at['페이', '피자'])
# print()
#
# # 위치를 이용(.iloc)
# print(table.iloc[3]) # 수지의 음식
# print()
# print(table.iloc[1:3, 3:5])
# print()
# print(table.iloc[[0, 1, 3], [2, 4, 5]]) # 리스트로 행과 열의 인덱스 선택
# print()
#
# # 조건을 이용
# print(table[table['탕수육'] == 'o']) # 탕수육을 먹을 수 있는 사람 = 지아, 민
# print()
# print(table[table == 'o']) # 알러지가 있는 음식만 보이게(나머지는 결측치로 표현)
# print()

# 각 친구가 먹을 수 있는 음식이 최소한 하나씩 있으려면 최소 몇 가지의 음식을 먹어야 하나?

INF = 987654321
menu = []
M = len(food) # 요리할 수 있는 음식의 종류 수
def canEverybodyEat(menu):
    return len(menu) == len(friend)

# f번 째 음식을 만들지 여부
def selectMenu(menu, f):

    # 음식을 만들 경우
    if f == M:
        if canEverybodyEat(menu):
            return len(menu)
        return INF

    # f번 째 음식을 만들지 않을 경우
    ret = selectMenu(menu, f+1)
    menu.append(f)
    print(menu)
    ret = min(ret, selectMenu(menu, f+1))
    menu.pop()
    return ret

for f in range(len(food)):
    selectMenu(menu, f)
    print(menu)