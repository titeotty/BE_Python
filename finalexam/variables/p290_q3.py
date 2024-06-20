'''
지역 변수와 전역 변수에 유의하여
다음 코드 결과를 기술
'''
def test1() :
    print(a + 1)

a = 1
test1()
print(a)

def test2() :
    b = 11
    print(b+1)
    
b = 1
test2()
print(b)

def test3() :
    global c
    c = 10
    print(c + 1)

c = 1
test3()
print(c)

def test4() :
    d = 10
    e = d + 10
    print(e)

e = 1
test4()
print(e)