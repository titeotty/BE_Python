'''
가변 인자와 키워드 인자에 유의해
코드의 결과를 쓰시오
'''
print("*"* 30, "\na)")
def hap(*nums) :
    s = 0
    for num in nums :
        s+= num
    return s

print(hap(1, 2, 3))
print(hap(*[1, 2, 3, 4]))   #리스트인 1, 2, 3, 4를 *연산자를 사용해 가변인자로 풀어서 분해하여 할당함

print("*"* 30, "\nb)")
def kwtest(**kwargs) :
    a = 0
    for key in kwargs :
        if key in ['java', 'python'] :
            a += kwargs[key]
    return a

print(kwtest(java=10, python=12, kotlin=36, c=8))
print(kwtest(**{'java':10, 'C++':7, 'python':5}))   #딕셔너리인 값을 **연산자를 사용해 키워드 인자로 분해하여 할당