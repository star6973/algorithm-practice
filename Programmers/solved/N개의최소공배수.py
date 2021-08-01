def GCD(n1, n2):
    n1_gcd = set()
    n2_gcd = set()

    for i in range(1, n1+1):
        if n1 % i == 0:
            n1_gcd.add(i)
    
    for j in range(1, n2+1):
        if n2 % j == 0:
            n2_gcd.add(j)
    
    return max(n1_gcd.intersection(n2_gcd))

def LCM(n1, n2):
    gcd = GCD(n1, n2)
    return gcd * (n1 // gcd) * (n2 // gcd)

def solution(arr):
    answer = 0

    # 1. 내림차순으로 정렬
    arr.reverse()
    
    # 2. 앞에서부터 2개씩 최대공약수를 구한뒤, 최소공배수를 구하고 앞에 값으로 삽입(최소공배수의 누적이라고 생각하자)
    for i in range(len(arr)-1):
        num1, num2 = arr[i], arr[i+1]
        arr[i+1] = LCM(num1, num2)
    
    answer = arr[-1]
    return answer   

arr = [2]
s = solution(arr)
print(s)