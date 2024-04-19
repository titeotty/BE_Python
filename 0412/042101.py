# 등 8개, on/off 상태 관리

#초기 상태
cStat = 0b01010101

#비트 연산 : 특정 비트를 확인하려면 특정 비트 값 1. 나머지는 0
mask1 = 0b10000000 #시프트 연산을 사용하면 여러 개의 mask 정의 불필요

d = int(input("확인하려는 등 번호는 ")) #등번호는 0 ~ 7
r = cStat & mask1 >> d #정수 출력 - 정수 값의 의미를 확인하기 어렵다.

print(r)


print(bin(r))

# r2 = r >> ( 7 - d )
if((cStat & mask1 >> d ) >> (7-d)==1):
    print(d, "등의 상태는 on")
    # print(str(d) + "등의 상태는 on")
else:
    print(d, "등의 상태는 off")
print()