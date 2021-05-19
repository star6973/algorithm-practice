'''

    1928. Base64 Decoder

    다음과 같이 Encoding 을 한다.
    1. 우선 24비트 버퍼에 위쪽(MSB)부터 한 byte씩 3 byte의 문자를 집어넣는다.
    2. 버퍼의 위쪽부터 6비트씩 잘라 그 값을 읽고, 각각의 값을 아래 [표-1] 의 문자로 Encoding 한다.

    입력으로 Base64 Encoding 된 String 이 주어졌을 때, 해당 String 을 Decoding 하여, 원문을 출력하는 프로그램을 작성하시오.

    [제약사항]
    문자열의 길이는 항상 4의 배수로 주어진다.
    그리고 문자열의 길이는 100000을 넘지 않는다.

'''
#
# T = int(input())
# for t in range(T):
#
#     # 1바이트 = 8비트 -> 24비트 -> 3바이트
#
#     '''
#         _ 1 _ _ 1 1 // _ _ _ 1 1 _ // _ _ _ _  _ _ // _ _ _ _ _ _
#         2^3+2^1+1
#     '''

# Life itself is a quotation.
# b = 'Life itself is a quotation.'
# b = b.


# # 문자열 encoding => 6비트씩 잘라서 값을 읽고, 표에 있는 문자로 encoding
# # 문자열을 decoding => 원문
# a = 'TGlmZSBpdHNlbGYgaXMgYSBxdW90YXRpb24u'
# print(len(a))