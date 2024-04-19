n = int(input('소수(prime number)인지를 판별한 2 이상의 정수 입력 >> '))
cnt = 2
for i in range(2, n // 2 + 1):
    if n % i == 0:
        cnt += 1
        break
        
if cnt == 2:
    print('정수 %d는 소수입니다.' % n)
else:
    print('정수 %d는 소수가 아닙니다.' % n)