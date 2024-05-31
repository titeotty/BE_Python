def multi(p):
    return p * 10

lst = [10, 20, 30, 40 , 50]

#map(함수, 데이터) 데이터의 각 항목에 함수를 적용한다. 데이터는 iterable 형식이다. 
print(type(map(multi, lst))) #map 함수의 결과 타입 확인
print(list(map(multi, lst))) #map 함수의 결과를 list 함수를 사용해서 변환해서 출력

#map 함수 풀어쓰기
result = list() #empty리스트 생성
for item in lst :
    result.append(multi(item))
    print(result)

