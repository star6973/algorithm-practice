'''
    1028. 단색이 좋아좋아 HARD

    한 줄에 빨강, 파랑, 초록 색상의 공들이 섞여 있습니다.
    각 공의 색깔은 순서대로 R, B, G 로 표현합니다.

    여러분은 한 턴에 제일 앞의 공 혹은 제일 뒤의 공을 제거할 수 있습니다.
    한 색깔의 공만 남기기 위해서는 최소 몇 번의 턴이 필요할까요?
'''

T = int(input())

for i in range(T):
    RGB = input()
    # 첫 번째 문자를 비교 대상으로 선정
    compare_rgb = RGB[0]

    cnt = 1
    max = 0
    # 두 번째 문자부터 비교 대상 문자와 비교해보면서
    # 같다면 count를 늘려주고 다르면 최종 count된 값을 max값과 비교하여 max값을 결정
    for rgb in RGB[1:]:
        if compare_rgb == rgb:
            cnt +=1
        else:
            if max < cnt:
                max = cnt

            # 다르다면 비교 대상 문자를 다른 문자로 바꿔준다.
            compare_rgb = rgb
            cnt = 1

    # 예외1. 'RRGGG'인 경우 max값이 R만 세주고 2로 끝나고, cnt값은 G를 세주어 3이 된 상태에서, cnt값이 더 크기 때문에 max값을 갱신해줘야 한다.
    # 예외2. 'R'인 경우 위의 반복문이 실행되지 않고 max값이 1이기 때문에 문자열의 길이만큼으로 갱신해줘야 한다.
    if max < cnt:
        max = cnt

    print(len(RGB) - max)