a = ['FTP', 'telnet', 'SMTP', 'DNS']
b = (20, 23, 25, 53)
print("="*20)
x = 10
y = 20
z = zip(a, b) #zip 함수 첫번째 인자가 key, 두번째 인자가 value
l = [1, 2, 3, 4]
print(l)
print(z)
print(list(z))
print(dict(z)) 
#zip 함수의 결과를 z에 저장, z를 이용해서 dict 함수를 실행
print(dict(zip(a, b))) 
#zip 함수의 결과를 바로 이용해서 dict 함수 실행
print("="*20)
print(tuple(z))
print(tuple(zip(a, b)))
