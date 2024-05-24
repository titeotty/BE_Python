def add(a, b):  #positional argument 
    return a + b

def subtract(a, b):
    if a > b:
        return a - b
    else:
        return b - a
    
def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0 or b == 0:
        return "숫자에 0이 포함되어 있어서 계산을 못하겠습니다."
    
    else :
        return a / b, a // b, a % b

def naemaeumdaero():
    print(add(10, 20))
    print(subtract(10, 20))
    print(multiply(10, 20))
    print(divide(10, 0))
    print(divide(0, 10))
    print(divide(10, 20))
    r = divide(10, 20)
    print("divide 함수 호출 결과: ", r)
    print("반환된 결과의 길이는 ", len(divide(10, 20)))
    print("반환된 결과의 타입은 ", type(divide(10, 20)))

if __name__ == "__main__":
    naemaeumdaero()