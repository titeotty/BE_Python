from random import randint
n1 = randint(1, 99)
n2 = randint(1, 99)
n3 = randint(1, 99)
if n1 < n2:
    max3 = n2
else:
    max3 = n1
if max3 < n3:
    max3 = n3
print('%d %d %d 중에서 최대: %d' % (n1, n2, n3, max3))

print("두번째 결과는 ", max(n1, n2, n3))    