# n = 0
# while n < 5:
#     str = input('다섯 문자 이상의 문자열 입력 >> ')
#     n = len(str)
# else:
#     print("작업 시작...")    
    
# print('입력 문자열: %s' % str)
# print("입력 문자열 {0}".format(str))
# print("첫 문자: %c" % str[4:5])
# print("마지막 문자: %c" % str[-1:7])
# print("첫 문자를 제외한 부분 문자열: %s" % str[1:])
# print("마지막 문자를 제외한 부분 문a자열: %s" % str[:-1])
# print("맨 앞과 뒤의 두 문자씩를 제외한 부분 문자열: %s" % str[2:-2])
# print("문자 하나씩을 건너 뛴 부분 문자열: %s" % str[::2])
# print("역 문자열: %s" % str[::-1])   # str[-1:-n:-1]
# print("   문자열: %s" % str[::1])    # str[0:n:1]

# my_list = [1, None, 3, 4, None, 6]
# print("ㅁㅁ : %s " % my_list[-2:1111111111])

str = input("다섯 문자 이상의 문자열 입력 >> ")
print("입력 문자열: ", str)
print("첫 문자: ", str[0:1])
print("마지막 문자: ", str[-1])
print("첫 문자를 제외한 부분 문자열: ", str[1:])
print("마지막 문자를 제외한 부분 문자열:", str[0:-1])
print("맨 앞과 뒤의 두 문자씩을 제외한 부분 문자열:", str[2:-2])
print("문자 하나씩을 건너뛴 부분 문자열:", str[::2])
print("역 문자열 :", str[::-1])