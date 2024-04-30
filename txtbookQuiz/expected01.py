# str = input('문자열 입력 >> ')
# strLen = len(str)
# print('참조할 첨자: 0 ~ %d' % (strLen-1))
# while True:
#     n = int(input('참조할 첨자 입력 >> '))
#     if 0 <= n <= (strLen - 1):
#         print('문자열: ', str, ', 길이: ', strLen)
#         print('참조 문자: ', str[n])
#         break
#     else:
#         print('인덱스 범위가 잘못되었습니다.')
# else:
#     print("수고했어요...")
    

input_str = input("문자열 입력 >> ")

#문자열의 소속 문자를 참조할 범위를 출력
print("참조 할 첨자 : 0 ~ ", len(input_str) - 1)

#첨자 하나를 입력받음
index = int(input("참조할 첨자 입력 >> "))

#입력된 첨자가 유효한지 확인 후 문자열의 전체, 길이, 참조 문자 출력
if 0 <= index < len(input_str) :
    print("전체 문자열: ", input_str)
    print("문자열 길이: ", len(input_str))
    print("참조된 문자: ", input_str[index])

else :
    print("첨자가 유효하지 않습니다.")