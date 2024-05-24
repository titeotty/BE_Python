import modules.m052401 as mmm #모듈 추가하기
'''
def add(a, b):
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
'''

def naemaeumdaero():
    print(mmm.add(10, 20))
    print(mmm.subtract(10, 20))
    print(mmm.multiply(10, 20))
    print(mmm.divide(10, 0))
    print(mmm.divide(0, 10))
    print(mmm.divide(10, 20))
    r = mmm.divide(10, 20)
    r1, r2, r3 = mmm.divide(10, 20) #반환받은 tuple 타입 데이터는 1개
    print("divide 함수 호출 결과: ", r)
    print("반환된 결과의 길이는 ", len(mmm.divide(10, 20)))
    print("반환된 결과의 타입은 ", type(mmm.divide(10, 20)))

if __name__ == "__main__":
    naemaeumdaero()