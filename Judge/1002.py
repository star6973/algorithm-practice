'''
    1002. 너의 학번을 알려주마

    한기대의 학번은 총 10자리로, {학번}{학부/과 구분}{일련번호} 로 이루어져 있습니다.
    예를 들여 2014136900 이면 14학번, 컴퓨터공학부, 가나다 순으로 900번째 학생임을 뜻 합니다.
    학번이 입력으로 주어졌을 때, 몇 학번 인지를 출력하는 프로그램을 만들어 주세요.
'''

n = int(input())

studentList = []
for i in range(n):
    studentID = input()
    studentList.append(studentID)
    i += 1

for i in range(n):
    print(studentList[i][2:4])
    i += 1