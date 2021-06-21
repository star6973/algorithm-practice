def solution(n):
    answer = 0
    copy_n = n
    while True:
        # 조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
        next_n = copy_n + 1

        # 조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
        n_bin_count = bin(n).count('1')
        next_n_bin_count = bin(next_n).count('1')
        if n_bin_count != next_n_bin_count:
            copy_n += 1
            continue
        
        # 조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.
        answer = next_n
        break

    return answer

n = 78
s = solution(n)
print(s)