def solution(new_id):
    answer = ''
    new_id = list(new_id)

    big_alpha = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    small_alpha = list('abcdefghijklmnopqrstuvwxyz')
    num = list('0123456789')
    sign = list('-_.')

    # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    for i in range(len(new_id)):
        if new_id[i] in big_alpha:
            pos = big_alpha.index(new_id[i])
            new_id[i] = small_alpha[pos]
    
    # print("1단계 문자열 = {}".format(''.join(new_id)))

    # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    i = 0
    while i != len(new_id):
        if new_id[i] not in big_alpha and new_id[i] not in small_alpha and new_id[i] not in num and new_id[i] not in sign:
            new_id.pop(i)
            continue
        i += 1

    # print("2단계 문자열 = {}".format(''.join(new_id)))

    # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    i = 0
    while i != len(new_id)-1:
        if new_id[i] == '.' and new_id[i+1] == '.':
            new_id.pop(i)
            continue
        i += 1
    
    # print("3단계 문자열 = {}".format(''.join(new_id)))

    # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    if len(new_id) >= 1 and new_id[0] == '.':
        new_id.pop(0)
    if len(new_id) >= 1 and new_id[-1] == '.':
        new_id.pop(-1)

    # print("4단계 문자열 = {}".format(''.join(new_id)))

    # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if new_id == []:
        new_id.append("a")

    # print("5단계 문자열 = {}".format(''.join(new_id)))

    # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    #      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id.pop(-1)
    
    # print("6단계 문자열 = {}".format(''.join(new_id)))

    # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id.append(new_id[-1])
    
    # print("7단계 문자열 = {}".format(''.join(new_id)))

    answer = ''.join(new_id)
    return answer

id = "abcdefghijklmn.p"
s = solution(id)
print(s)