num1, num2 = input('실수 두 개 입력 >> ').split()
num1, num2 = float(num1), float(num2) 
print('{} > {} 결과: {}'.format(num1, num2, num1 > num2))
print('{} >= {} 결과: {}'.format(num1, num2, num1 >= num2))
print('{} < {} 결과: {}'.format(num1, num2, num1 < num2))
print('{} <= {} 결과: {}'.format(num1, num2, num1 <= num2))
print('{} == {} 결과: {}'.format(num1, num2, num1 == num2))
print('{} != {} 결과: {}'.format(num1, num2, num1 != num2))