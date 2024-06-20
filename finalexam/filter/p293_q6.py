'''
1에서 30까지의 난수 6개 생성해서 정렬 리스트 만들기
filter()함수 사용하여 3의 배수만 포함한 리스트를 구성
모듈 random의 smaple() 함수를 사용해 리스트 변수 lst에 저장
'''
from random import sample

lst = sorted(sample(range(1, 31), 6))

print("원 리스트: ", lst)

def fThree(num) :
    return num % 3 == 0
    
fLst = list(filter(fThree, lst))
print("필터 리스트: ", fLst)