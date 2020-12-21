'''
    1054. [자바실습시험 - 연습문제 2] 가장 짧은 문자열 찾기

    N개의 문자열이 주어졌을 때 가장 짧은 문자열을 출력하시오. 가장 작은 짧은 문자열이 여러 개 있을 경우 처음 등장한 문자열을 출력하시오.

    # 입력
        첫번째 줄에 문자열의 수 N(1<=N<=100)이 주어짐
        두번째 줄부터는 길이가 1이상인 N개의 문자열이 주어짐

    # 출력
        N개의 문자열 중 가장 짧은 문자열을 출력함
'''

N = int(input())

string = []
for n in range(N):
    string.append(input())

short = string[0]
for i in range(len(string)):
    if len(string[i]) < len(short):
        short = string[i]

print(short)