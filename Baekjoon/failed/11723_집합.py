M = int(input())
S = set()
for i in range(M):
    input_string = input().split(" ")
    calc = input_string[0]
    if len(input_string) == 2:
        x = int(input_string[1])

    if calc == "add":
        if x not in S:
            S.add(x)
    if calc == "remove":
        if x in S:
            S.remove(x)
    if calc == "check":
        if x in S:
            print(1)
        else:
            print(0)
    if calc == "toggle":
        if x in S:
            S.remove(x)
        else:
            S.add(x)
    if calc == "all":
        S = set([i for i in range(1, 21)])
    if calc == "empty":
        S = set()