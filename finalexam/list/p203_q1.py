'''
Q1. 1~99까지의 난수 10개로 리스트를 만든다
output :
- 만든 리스트
- 정렬된 리스트
- 역순 리스트
'''
import random

l1 = [] 
for i in range(10) :
    n = random.randint(1, 99)
    l1.append(n)

print('리스트', l1)
print('정렬 리스트', sorted(l1))
print('역순 리스트', l1[::-1])