l = [ 3, 5, 2, 7, 1 ] #list
t = ( 3, 5, 2, 7, 1 ) #tuple

print("리스트의 첫번째 항목은", l[0])
print("튜플의 첫번째 항목은", t[0])

#슬라이싱
print("=========슬라이싱========")
print("#1")
str = "동양미래대학교"
print("문자열의 첫번째 글자는:", str[0])
print(str[0:len(str):1])
print(str[1:len(str):1])
print(str[-1:-len(str):-1])

print("#2")
print("리스트에 슬라이싱 적용")
print(l[2:len(l):1])
print(l[-1:-len(l)-1:-1])

#리스트는 데이터집단, 데이터 추가, 삭제가 가능하다.
l2 = [] #empty list

#튜플은 데이터집단, 데이터 수정이 불가능하다.
t2 = () #empty tuple

#리스트의 부분참조 슬라이싱
alp = list('abcdefghij')
print(alp[1:-1])
print(alp[-1:1:-1])
print(alp[-2:2:-2])

sports = ['풋살', '족구', '비치사커', '야구', '농구', '배구']
sports[0:3] = ['축구']
print(sports)