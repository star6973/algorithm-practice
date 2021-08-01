dial = {
    2: 'ABC',
    3: 'DEF',
    4: 'GHI',
    5: 'JKL',
    6: 'MNO',
    7: 'PQRS',
    8: 'TUV',
    9: 'WXYZ'
}

def find_num(s):
    for k, v in dial.items():
        if s in v:
            return k

ip = input()
result = 0
for i in ip:
    num = find_num(i)
    result += (num + 1)

print(result)