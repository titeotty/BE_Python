'''
Q3. 문자열 리스트 'HelloPython!' 생성
슬라이스를 위한 3개의 정수를 input으로 받은 후
슬라이스 결과를 출력하는 프로그램을 작성
output :
- 슬라이스를 위해 첨자를 HelloPython의 위 아래로
- 슬라이스 된 문자
'''
pyList = list('HelloPython!')
print('012345678901')
print('HelloPython!')
print('210987654321')

while True:
    ipN = input('슬라이스 [?:?:?] 3개 입력 (종료: 0 0 0) : ')
    sliceNum = list(map(int, ipN.split()))

    if sliceNum == [0, 0, 0]:
        print("*"*10, "종료", "*"*10)
        break

    print(pyList[sliceNum[0] : sliceNum[1] : sliceNum[2]])