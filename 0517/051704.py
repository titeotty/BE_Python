# 사용자 함수

# 1. 아무것도 없을 때, 받고 전달하기
# def fun1(받는 자리)
# return문을 통해 전달함
def fun1() :
    pass    #이 자리에서 아무것도 안한다.

def fun2(a, b) :
    print("함수 입장에서 받아온 데이터는 {}, {}이다.".format(a, b))

def fun3():
    a = 10
    b = 20
    return a + b

def fun4():
    a = 10
    b = 20
    return a + b, a*b, a-b

def fun5(a, b, c):
    sum = a + b + c
    avg = (a + b + c) / 3
    remainder = (a+b+c)%3
    remainder2 = sum //3
    return sum, avg, remainder, remainder2

#5-1 받는값, 주는값 둘 다 보유한 함수
def fun6(a, b, c=1000):     #c는 초기값으로 1000을 가짐. 데이터 개수가 부족하면 1000출력
                            #a, b는 positional argument, c는 named argument라고 함
                            #named argument(keyword argument)자리에 값이 오지 않으면 
    sum = a + b + c
    avg = (a + b + c) / 3
    remainder = (a+b+c)%3
    remainder2 = sum //3
    return sum, avg, remainder, remainder2

def usercode():
    a, b, c = fun4() #fun4가 리턴하는 값이 3개이기 때문에 저장하는 변수도 3개
    print(a,b,c)

#함수를 사용하는 방법
# 1. fun1() 사용
fun1()  #함수 호출
        #fun1 호출 시 전달할 인수는 없다.
        #받아오는 것 없다. 함수 입장에서 return이 없다

# 2. fun2 사용
fun2(10, 20)    #10-> a, 20 -> b... 순서대로 전달
#fun2(10)        #10 -> a, ? -> b
#에러 메세지:fun2() missing 1 required positonal argument : 'b'

#fun2(10, 20, 30)    #10 -> a, 20 -> b, 30 -> ?
#에러 메세지:fun2 takes 2 positional arguments but 3 were given
l = [100, 300]
#fun2(l)

mList= [100, 300]
#fun2(mList)
fun2(*mList)    #unpack 되면서, mList[0] -> a, mList[1] -> b

a = fun3()  #함수가 return이 있을 때는 return 결과를 변수 저장하거나 print 함수로 출력
print(a)

a, b, c = fun4() #fun4가 리턴하는 값이 3개이기 때문에 저장하는 변수도 3개

print(a, b, c)
# a, b = fun4() #too many values to unpack
# a, b, c, d = fun4() #not enough values to unpack

fun5(100, 200, 300)

r1, r2, r3, r4 = fun5(100, 200, 300)
print("call fun5")
print(r1, r2, r3, r4)
r1, r2, r3, r4 = fun6(1000, 2000, 4000)
r1, r2, r3, r4 = fun6(1000, 2000, c =5000)

print("="*20)
print(fun1)
print(fun2)
print(fun3)
if __name__ == '__main__':  #entry point for python code
    usercode()