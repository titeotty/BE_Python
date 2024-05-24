def sum(*arg) :
    #인수가 없으면 0반환, 인수가 있으면 모두 합산한 결과를 반환
    print(type(arg))
    print(len(arg))
    r = 0

    for item in arg:
        r+= item

        return r
    
def sum2(value, *arg) :
    pass

def legacySum(argt):
    print(type(argt))
    print(len(argt))

if __name__ == '__main__':
    #프로그램의 시작점 entry point
    r = sum()
    r2 = sum(10, 20)
    r3 = legacySum(tuple()) #empty tuple 전달
    t = tuple([10,20])
    # t = tuple(10, 20) #오류 - 튜플은 값을 하나만 줄 수 있음
    r4 = legacySum(t)

    rr = sum(10, 20, 30, 40, 50)
    print('*' * 50)
    print(sum)
    print(sum2)
    print(legacySum)