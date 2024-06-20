'''
1에서 100 사이의 섭씨 온도 9개를 난수로 생성
생성한 값들로 정렬 리스트 생성
섭씨 온도를 화씨 온도로 변환하는 람다 함수 사용
map()으로 섭씨 온도에 대응되는 화씨 온도 리스트 생성
반복 for문에서 zip()함수 사용해서 결과 출력

output :
- 섭씨 온도 리스트
- 화씨 온도 리스트
'''
import random
fahFun = lambda cels : cels * 8/5 + 32

l1 = []
def celRan(start, end, count) :
    for i in range(9) :
        l1.append(random.randint(start, end))

celRan(1, 100, 9)
sL1 = sorted(l1)
print("섭씨 온도 : ", sL1)

l2 = list(map(fahFun, sL1))
print("화씨 온도 : ", l2)

for cel, fah in zip(sL1, l2) :
    print(f"섭씨 : {cel} => 화씨 : {fah}")