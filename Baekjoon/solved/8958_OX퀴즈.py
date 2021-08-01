import sys

N = int(input())
for i in range(N):
    test_case = sys.stdin.readline().strip()

    ans = 0
    result = 0
    prev = test_case[0]
    for j in range(len(test_case)):
        if prev == test_case[j]:
            if prev == 'X' and test_case[j] == 'X':
                ans = 0
            else:
                ans += 1
        else:
            if prev == 'X' and test_case[j] == 'O':
                ans += 1
            else:
                ans = 0
        
        prev = test_case[j]
        result += ans
    
    print(result)