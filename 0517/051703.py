a = [1, 2, 3]
print(a)
print(enumerate(a))
print(list(enumerate(a)))
print(list(enumerate(a, 200)))

mList = ['홍길동', '장길산', '임거정']
index = 0
for item in mList : #String으로 저장
    print("{}번 {}".format(index, item))
    index += 1

for item in enumerate(mList): #tuple로 저장
    print("{}번 {}".format(item[0], item[1]))

for item in enumerate(mList):
    print("{}번 {}".format(*item)) #별 표시는 unpack

a, b, c = 10, 20, 30 #자동으로 =의 오른쪽에서는 pack(할당), 왼쪽에서는 unpack이 생긴다. 

print('='*20)
import pprint

singer = ['bts', '볼빨간사춘기', 'bts', '블랙핑크', '태연']
print(singer)
pprint.pprint(singer)