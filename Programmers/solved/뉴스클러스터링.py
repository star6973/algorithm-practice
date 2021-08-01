import math

def solution(str1, str2):
    answer = 0

    # 1. 입력된 문자열 모두 소문자 변환
    str1 = str1.lower()
    str2 = str2.lower()

    # 2. 2-gram으로 나누기
    split_str1 = []
    for i in range(len(str1)-1):
        split_str1.append(str1[i]+str1[i+1])

    split_str2 = []
    for i in range(len(str2)-1):
        split_str2.append(str2[i]+str2[i+1])

    # 3. 특수문자, 숫자, 공백이 들어간 문자 제거
    split_alpha_str1 = []
    for i, s1 in enumerate(split_str1):
        if (s1[0].isalpha() == False) or (s1[1].isalpha() == False):
            pass
        else:
            split_alpha_str1.append(s1)

    split_alpha_str2 = []
    for i, s2 in enumerate(split_str2):
        if (s2[0].isalpha() == False) or (s2[1].isalpha() == False):
            pass
        else:
            split_alpha_str2.append(s2)
    

    # 4. 교집합, 합집합 구하기
    intersection_str = set(split_alpha_str1).intersection(set(split_alpha_str2))
    union_str = set(split_alpha_str1).union(set(split_alpha_str2))

    # 5. 자카드 유사도 구하기
    if intersection_str == set() and union_str == set():
        return 1 * 65536
    else:
        intersection_sum = sum([min(split_alpha_str1.count(s), split_alpha_str2.count(s)) for s in intersection_str])
        union_sum = sum([max(split_alpha_str1.count(u), split_alpha_str2.count(u)) for u in union_str])

        answer = math.floor((intersection_sum / union_sum) * 65536)

    '''
        import re

        str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
        str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]
        
        gyo = set(str1) & set(str2)
        hap = set(str1) | set(str2)

        if len(hap) == 0 :
            return 65536

        gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
        hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

        return math.floor((gyo_sum/hap_sum)*65536)
    '''

    return answer

str1 = "aa1+aa2"
str2 = "AAAA12"
s = solution(str1, str2)
print(s)