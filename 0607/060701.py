try :
    a = 10 / 0
    print(a)
except TypeError as te :
    print("코드에러")
except ZeroDivisionError as ze :
    print("0으로 나누는 부분이 생겼다.")
except :
    print("경고")
else :
    print("try 블록을 모두 마쳤다. except 없이")
finally :
    print("어쨌든 끝났다.")

for idx in range(1, 11) :
    print(idx)
else :
    print("for 끝났다.")    