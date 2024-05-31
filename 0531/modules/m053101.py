#가변개수의 인수를 튜플타입으로 넘겨 받는 방법
def sum(*arg) :
    print(type(arg))
    intSum = 0
    floatSum = 0.0
    strConcat = ''

    for item in arg :
        if isinstance(item, int) :
            intSum += item
        elif isinstance(item, float) :
            floatSum += item
        else :
            strConcat += item

    return intSum, floatSum, strConcat