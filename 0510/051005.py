day = dict({'월':'Monday', '화':'Tuesday', '수':'Wednesday', '목':'Thursday', '금':'Friday'})
print(day)
print(day.keys())
print(day.values())
print(day.items())

for key in day.keys():
    print(f'{key}의 값은 {day[key]}')
    #key를 통해서 value 접근은 가능
    #value를 통해서 key 접근은 불가능
print('='*20)

for item in day.items():
    print(f'{item[0]} 키의 값은 {item[1]}')
print('='*20)

for item in day.items():
    print('{} 키의 값은 {}'.format(*item))
print('='*20)

for item in day:
    print(item)
    print('{}의  값은 {}'.format(item, day[item]))
print('='*20)

city = {'대한민국':'부산', '뉴질랜드':'웰링톤', '캐나다':'몬트리올'}
print(city['캐나다'])
print(city.get('캐나다'))
print(city.get('서울')) #get 메서드 사용시 에러x 대신 'None'값 출력
#print(city['서울']) keyError - 없는 키 사용 할 때 에러남
print(city.get('서울', '그런 키 없네요'))
print('='*20)

city.pop('캐나다')
print(city) #city에서 캐나다 값을 꺼내와서 사라짐