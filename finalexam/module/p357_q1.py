'''
원의 반지름을 난수로 받아
원의 면적을 출력하는 프로그램을 작성
output :
- 원의 반지름
- 원주율 값
- 원의 면적
'''
from math import pi
import random

rd = round(random.random() * 10, 2)
def getarea(int) :
    return 2 * pi * rd

print('원의 반지름 : ', rd)
print('원주율 pi : ', round(pi, 4))
ar = getarea(rd)
print(f'반지름 {rd}인 원의 면적은 {round(ar, 2)}')