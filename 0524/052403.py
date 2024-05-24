from modules.m052401 import add

def add2(a, b, c = 20):
    return a + b + c


if __name__ == "__main__":
    r = add(10, 20)
    print(r)
    r = add(10) #타입에러 b의 인수를 안줌
    r2 = add2(10, 20) #초기값을 갖는 인수가 있을 때, 위치 인수를 생략하면 해당 초기값 사용
                      #인수를 전달할 때 위치에 따라서 전달

    print(r2)
    r3 = add2(c=100, b=200, a=50)
    print(r3)
    r4 = add2(b=200, a=50)
    print(r4)
    #r5 = add2(b=50, 100) #위치인수는 키워드 인수 앞에 와야한다.
    r5 = add2(100, b =50)