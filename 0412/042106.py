# from random import randbytes
import random

print(random.randint(100, 200))
# print(random.randbytes(self, 303))

print(random.randint(1,6))
print("===================")
# 주사위 던지는 프로그램
cw = 0
uw = 0
# 컴퓨터가 던지는 주사위
c = random.randint(1, 6)

# 사용자가 던지는 주사위 : prompt 표시
input("주사위를 던지려면 엔터키를 누르세요!")
u = random.randint(1, 6)

print("컴퓨터는 ", c)
print("유저는 ", u)

if c > u:
    print("컴퓨터 승")
    cw = cw+1

elif c < u:
    print("유저 승")
    uw = uw+1

else:
    print("무승부")

r = input("또 할까요? y / n ")

if r == "y":
    r = 1

else :
    r = 0

while r == 0 :
    print("유저 승 ", uw)
    print("컴퓨터 승 ", cw)

while r == 1 :
    # 컴퓨터가 던지는 주사위
    c = random.randint(1, 6)

# 사용자가 던지는 주사위 : prompt 표시
    input("주사위를 던지려면 엔터키를 누르세요!")

    u = random.randint(1, 6)

    print("컴퓨터는 ", c)
    print("유저는 ", u)

    if c > u:
        print("컴퓨터 승")
        cw = cw+1

    elif c < u:
        print("유저 승")
        uw = uw+1

    else:
        print("무승부")

    r = input("또 할까요? y / n ")

    if r == "y":
        r = 1

    else :
        print("유저 승 ", uw)
        print("컴퓨터 승 ", cw)