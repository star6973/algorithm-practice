import string

tmp = string.digits + string.ascii_uppercase
# print("tmp = ", tmp)

# N진수 변환 함수
def convert(num, base):
    q, r = divmod(num, base) # num=변환할 숫자, base=진수, q=몫, r=나머지
    
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]

def solution(n, t, m, p):
    answer = ''

    cnt = 0
    idx = 0
    str = ''
    while True:
        if len(str) >= t * m:
            break
        
        str += convert(idx, n)
        cnt += 1
        idx += 1
    
    cnt = 0
    for i in range(len(str)):
        if m*i + (p-1) < len(str) and cnt != t:
            answer += str[m*i + (p-1)]
            cnt += 1

    return answer

n = 16
t = 16
m = 2
p = 1
s = solution(n, t, m, p)
print(s)