str = input('문자열 입력 >> ')
strLen = len(str)
print('참조할 첨자: 0 ~ %d' % (strLen-1))
while True:
    n = int(input('참조할 첨자 입력 >> '))
    if 0 <= n <= (strLen - 1):
        print('문자열: ', str, ', 길이: ', strLen)
        print('참조 문자: ', str[n])
        break
    else:
        print('인덱스 범위가 잘못되었습니다.')
else:
    print("수고했어요...")
