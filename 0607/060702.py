lst =[1, 3, 5, 6]
try :
    a = 10/'a'
    print(lst[5])
    for i in range(3): #syntax에러는 포함이 안됨
        print(i)

except SyntaxError :
    print("문법이 잫못된 문장이 있다.")

except IndexError :
    print("첨자가 잘못되었네요")

except TypeError:
    print("연산에 잘못된 타입의 데이터가 있다.")

except :
    print("뭔가 모르는 문제가 생겼다.")

finally :
    print("끝났다.")