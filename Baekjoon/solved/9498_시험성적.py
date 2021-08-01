'''
    90 ~ 100점은 A
    80 ~ 89점은 B
    70 ~ 79점은 C
    60 ~ 69점은 D
    나머지 점수는 F
'''

N = int(input())

if N >= 90 and N <= 100:
    print("A")
elif N >= 80 and N < 90:
    print("B")
elif N >= 70 and N < 80:
    print("C")
elif N >= 60 and N < 70:
    print("D")
else:
    print("F")