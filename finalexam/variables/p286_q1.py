'''
1~100까지의 정수 중 난수 10개를 생성
생성된 난수 10개의 합, 평균, 최댓값, 최솟값을 출력
'''
import random
l1 = []

def sumFun(start, end, count) :
    global l1
    for i in range(10) :
        l1.append(random.randint(1, 100))

sumFun(1, 100, 10)
print("랜덤 난수 10개 출력 : ", l1)
print("합 : ", sum(l1))
midL1 = sum(l1) / len(l1)
print("평균 : ", midL1)
print("최댓값 ", max(l1))
print("최솟값 ", min(l1))
