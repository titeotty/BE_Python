def primeNumber(n):
    if n <= 1:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

n = int(input('소수(prime number)인지를 판별한 2 이상의 정수 입력 >> '))
# cnt = 2
# cnt = True
# for i in range(2, n // 2 + 1):
#     if n % i == 0:
#         cnt = False
#         break
        
# if cnt:
#     print('정수 %d는 소수입니다.' % n)
# else:
#     print('정수 %d는 소수가 아닙니다.' % n)

if primeNumber(n) :
    print("정수 %d는 소수입니다. " %n)

else :
    print("정수 %d는 소수가 아닙니다." %n)