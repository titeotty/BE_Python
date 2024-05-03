l = [10, 2, 6, 5, 1, 50]
print(l)
print(len(l))
l.reverse() #역순으로 변환해서 자기 자신에 저장 / 반환(return)값은 없다.
print(l)
l2 = [10, 2, 6, 5, 1, 50]
l2.sort() #항목을 정렬해서 자기 자신에 저장 / 반환 값은 없음
print(l2)
l2.reverse()
print(l2)

l3 = [10, 2, 6, 5, 1, 50]
print(sorted(l3)) #sorted 내장함수는 정렬된 결과를 반환값으로 저장
print(l3)

print(sorted(l3, reverse=True))

t10 = True
t11 = False
print("boolean True를 정수로 출력하면 {:d}".format(t10))
print("boolean False를 정수로 출력하면 {:d}".format(t11))

t12 = ( 4, 2, 1, 10, 15, 12)
print(t12)
print(sorted(t12))
print(type(sorted(t12)))
t13 = t12 #t12가 튜플이기 때문에 t13도 튜플이 됨
t13 = list(t12)
print("t13의 타입은", type(t13))
t14 = tuple(t13)
print('t14의 타입은 ', type(t14))
print('='*40)
print('t12는 ', t12)
print('t13은 ', t13)
print('t14는 ', t14)