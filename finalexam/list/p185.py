print('='*100)
print('얕은 복사')
#얕은복사 '=' 사용해서 변수에 대입시 c언어 포인터마냥 참조만 함
f1 = ['사과', '귤', '복숭아']
f2 = f1

f2.append('파인애플')
print(f1, f2)    #f2에 파인애플을 추가했는데 f1에도 추가됨

f1.pop()
print(f1, f2)   #f1에서 pop을 실행햇는데 f2에서도 빠짐

print('='*100)
print('깊은 복사')
#깊은복사  ':', copy(), list() 함수 중 사용해야함
f1 = ['사과', '귤', '복숭아']
f2 = f1[:]
f3 = f1.copy()
f4 = list(f1) 

f2.pop()
f3.append('copy함수')
f4.append('list함수')
print(f1, f2, f3, f4)   #각각 pop과 append가 따로 적용