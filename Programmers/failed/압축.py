import string
alpha = string.ascii_uppercase

def solution(msg):
    answer = []
    dictionary = dict()
    
    for a in alpha:
        dictionary[a] = len(dictionary) + 1
    
    '''
        1. 현재 위치에 있는 알파벳으로 시작하는 가장 긴 문자열이 딕셔너리에 있는지 확인하기
        2.
            2-1) 있다면,
                 answer에 인덱스 위치 넣기,
                 다음 문자로 이동해서 1번으로 돌아가기
            2-2) 없다면,
                 dictionary에 현재 문자 추가하기,
                 마지막 글자부터 시작해서 1번으로 돌아가기
    '''

    i = 0
    cur_msg = msg[i]
    while True:

        

        if cur_msg in dictionary:
            print(cur_msg)
            i += 1
            
            if i >= len(msg):
                break
            cur_msg += msg[i]
            continue
        else:
            print(cur_msg)
            
            dictionary[cur_msg] = len(dictionary) + 1
            cur_msg = msg[i]

        


    return answer

msg = "KAKAO"
s = solution(msg)
print(s)