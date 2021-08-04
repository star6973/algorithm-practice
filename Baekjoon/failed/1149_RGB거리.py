N = int(input())
rgb_prices = []
for n in range(N):
    rgb_prices.append(list(map(int, input().split())))

print(rgb_prices)

colorDict = {}
for i in range(len(rgb_prices)):
    for j in range(len(rgb_prices[i])):
        if rgb_prices[j][i] not in colorDict:
            colorDict[rgb_prices[j][i]] = {}
        else:
            colorDict[rgb_prices[j][i]] = colorDict.get(rgb_prices[i]) + rgb_prices[j][i]
        
        print(colorDict)