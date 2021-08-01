N = int(input())
answer = 0
for i in range(N):
    checker = []
    is_grouping = True

    word = input()    
    checker.append(word[0])

    for j in range(1, len(word)):
        if checker[-1] == word[j]:
            continue
        else:
            if word[j] in checker:
                is_grouping = False                
                break
            else:
                checker.append(word[j])
    
    if is_grouping:
        answer += 1

print(answer)