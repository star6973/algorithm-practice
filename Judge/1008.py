'''
    1008. 순환 소수

    두 정수 A, B 가 주어졌을 때 A를 B로 나눈 결과(A/B)를 순환 소수 형태로 출력하세요. (B != 0)
    순환되는 부분은 괄호 안에 출력하도록 합니다.
    만약 숫자가 나누어떨어질 경우 괄호 안에 0을 출력하세요.
'''

T = int(input())

result = []
for i in range(T):
    num = list(map(int, input().split()))

    div = float(num[0] / num[1])
    d = list("{0:0}".format(div))
    print(d)
    index = d.index('.')
    d2 = list(set(d[index+1:]))
    print(d2)



#     index = d.index('.')
#     for i in range(index + 1, len(d)):
#         if d[i] == d[i+1] and d[i+1] == d[i+2]:
#             point = i
#             break
#
#     str = ""
#     for i in range(point+1):
#         if i == point:
#             str += '(' + d[i] + ')'
#         else:
#             str += d[i]
#
#     result.append(str)
#
# for r in result:
#     print(r)