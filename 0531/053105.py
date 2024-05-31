lst = [5, 23, 1, 17, 3]
print("원본", lst)
print("정렬", sorted(lst))
print("역정렬", sorted(lst, reverse=True))
print('')

slst = ["xy", "def", "abca", "mnoasdf"]
print("원본", slst)
print("정렬", sorted(slst))
print("역정렬", sorted(slst, reverse=True))
print('')

studentlst = [('홍길동', 90, 85, 92), ('장길산', 89, 95, 93), ('임거정', 91, 87, 90)]
print("원본", studentlst)
print("정렬", sorted(studentlst))
print("역정렬", sorted(studentlst, reverse=True))
print('')

#studentlst의 두번째 숫자인 90, 89, 91을 차례대로 정렬
print("두번째 숫자를 키로 정렬", sorted(studentlst, key=lambda student : student[1]))
