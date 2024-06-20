'''
다음 코드의 결과를 기술하시오. 람다(익명)함수 사용
'''
print(list(map(lambda x : x*2, [10, 13, 16, 19])))
print(list(map(lambda x, y : pow(x, y), [3, 2, 1], [1, 2, 3])))