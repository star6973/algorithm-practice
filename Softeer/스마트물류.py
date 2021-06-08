N, K = map(int, input().split())
line = list(input())
answer = 0

for i in range(len(line)):
    if line[i] == 'P':     
        for j in range(i-K, i+K+1):
            if j >= 0 and j < len(line) - 1:
                if line[j] == 'H':
                    line[j] = ' '
                    answer += 1
                    break
        print('line = ', line)

print(answer)            
