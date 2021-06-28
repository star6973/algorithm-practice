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

    idx = 0
    curr_msg = msg[idx]
    print(curr_msg)
    while idx < len(msg):
        print(idx, curr_msg)
        
        # 1. 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다.
        for key in dictionary.keys():
            if curr_msg in key:
                w = key
        
        # 2. w에 해당하는 사전의 색인 번호를 출력하고, 입력에서 w를 제거한다.
        answer.append(dictionary[w])
        w = ""

        # 3. 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록한다.
        if 

    return answer

msg = "KAKAO"
s = solution(msg)
print(s)