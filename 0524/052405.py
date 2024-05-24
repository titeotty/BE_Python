#이거시험이래여

def sum(a: int, b: bool):
    #받아온 인수의 타입 확정? 잘보세여 정수가 아닌 실수값을 계산x
    #인수의 타입이 다르기 때문에 확인하는 작업이 필요함
    print('인수 a의 타입은, ', type(a), "인수 b의 타입은, ", type(b))
    #정수면 두 수를 더하고, 실수면 두 수를 더하고 -1을 하고, 문자열이면 두 문자열 중간에 '+'를 추가하는 걸 만들수잇다.
    return a + b

# def sum2(name="DMU", a, *arg, **kwarg): #keyword 인수의 위치에 문제가 있다.
def sum2(a, *arg, name="DMU", **kwarg):
    print(a)
    print(name)
    print(arg)
    for key in karg.keys():
        print(key, '=>', karg[key], end='/ ')
    print()

def sum3(*arg1, **arg2):
    pass

#이걸잘봐야해요
if __name__ == "__main__":
    print(sum(1,2))
    print(sum(1.5, 2.7))
    print(sum('abc', 'xyz'))

    print("*"*10, "sum2","*"*10)
    print(sum2(10, 20, 30, 40, 50, n1=100, n2=200, n3=300, name='sw'))
    #앞에 정수(30-50)들은 묶여서 arg(튜플)로 들어가고, n1, n2등은 묶여서 karg(딕셔너리)로 들어감
    print("*"*20) 
    print(sum2(10, 20, 30, 40, 50, name='sw2', n1=100, n2=200, n3=300)) 
    print("*"*20) 
    print(sum2(10, 20, 30, 40, 50, name='sw2', n1=100, n2=200, n3=300, name2='sw3')) 
    #keyword인수는 중복불가능

