
'''
모듈 math의 factorial(), 
모듈 statistics의 median(), mean(), variance(), stdev() 함수를 사용
리스트 자료의 중앙 값, 평균, 분산, 표준편차를 출력
'''
from math import factorial
from statistics import median, mean, variance, stdev

if __name__ == '__main__' :
    st = [80, 99, 77, 65, 92, 74, 82]

    print("1! = ", factorial(1))
    print("6! = ", factorial(6))
    print("11! = ", factorial(11))
    print("16 = ", factorial(16))

    medianVal = round(median(st),2)
    meanVal = round(mean(st),2)
    varianceVal = round(variance(st), 2)
    stdevVal = round(stdev(st), 2)

    print(f"중앙값: {medianVal}")
    print(f"평균: {meanVal}")
    print(f"분산: {varianceVal}")
    print(f"표준편차: {stdevVal}")