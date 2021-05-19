# '''
#
#     5656. 벽돌 깨기
#
# '''
#
# A = [[1, 0, 0], [1, 0, 0], [1, 2, 1]]
#
# def explosion(A, i, j):
#
#     if A[i][j] == 1:
#
#
#     for i in range(len(A)):
#         for j in range(len(A[0])):
#             if A[i][j] > 1:
#
#
# for i in range(len(A)):
#     for j in range(len(A[0])):
#
#         # 선택된 값이 1보다 큰 경우, 상하좌우로 확인
#         if A[i][j] > 1:
#             if A[i-1][j] == 1:
#                 A[i-1][j] = '*'
#             else:
#                 explosion(A[i-1][j])
#
#             if A[i+1][j] == 1:
#                 A[i+1][j] = '*'
#             else:
#                 explosion(A[i+1][j])
#
#             if A[i][j-1] == 1:
#                 A[i][j-1] = '*'
#             else:
#                 explosion(A[i][j-1])
#
#             if A[i][j+1] == 1:
#                 A[i][j+1] = '*'
#             else:
#                 explosion(A[i][j+1])