def myFun1():
    pass

def myFun2(a):
    print(a)

def myFun3():
    return 100

def myFun4(a, b):
    return a + b

def myFun5():
    return [10, 20, 30][0]

myFun1()        #반환값이 없을 때에는 독립적으로 호출
myFun2(100)     #반환값이 없어서 독립적으로 호출, 주는 값만 존재
myFun3()        #반환값이 있을 때에는 독립적으로 호출하지 않는다
r = myFun3()
print(r)

r2 = myFun4(100, 1)
print(r2)

rr1 = myFun5()
print(rr1)