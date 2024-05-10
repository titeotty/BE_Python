a = {1, 3, 5, 7, 9, 4, 6}
b = { 2, 4, 6, 8, 10, 3, 5}
print('='*10,'합집합','='*10)
print('비교 연산자 사용해서 합집합 : ',a | b) 
print('함수 사용해서 합집합 : ',a.union(b))
print('union 이후 ', a)
a.update(b)
print("update 이후 ", a)

a = {1, 3, 5, 7, 9, 4, 6}
b = { 2, 4, 6, 8, 10, 3, 5}
print('='*10,'교집합','='*10)
print ('비교 연산자 사용해서 교집합 : ',a & b) 
print('함수 사용해서 교집합 : ', a.intersection(b))
print('intersection 이후', a) #intersection만 해서는 a 값이 변하지 않음
a.intersection_update(b)
print('intersection_update 이후', a) #intersection update 사용해야 a 값 변환

a = {1, 3, 5, 7, 9, 4, 6}
b = {2, 4, 6, 8, 10, 3, 5}
print('='*10,'차집합','='*10)
print('비교 연산자 사용해서 차집합 : ' ,a - b) 
print('함수 사용해서 차집합 : ', a.difference(b))
print('차집합 이후', a)
a.difference_update(b)
print("difference update 이후", a)

a = {1, 3, 5, 7, 9, 4, 6}
b = {2, 4, 6, 8, 10, 3, 5}
print('='*10,'여집합','='*10)
print('비교 연산자 사용해서 여집합 : ',a ^ b)
print('함수 사용해서 여집합 : ',a.symmetric_difference(b))
print('여집합 이후', a)
a.symmetric_difference_update(b)
print("symmetric_difference update 이후", a)