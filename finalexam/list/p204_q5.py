'''
리스트 sports와 num을 만들고
스포츠 종목과 팀원 수가 번갈아 나오는 리스트를 만든 후 
다음과 같이 출력하는 프로그램을 작성하시오
output :
- sports 리스트
- num 리스트
- sports 리스트 홀수 참조에 빈 문자 ''을 insert() 메서드로 삽입
- 슬라이스 sports[1::2]에 num을 대입
'''

sports = ['축구', '야구', '농구', '배구']
num = [11, 9, 5, 6]

oddNum = [1, 3, 5, 7]
sports1 = list(sports)

for i in range(len(num)) :
    sports1.insert(oddNum[i], num[i])
print(sports1)

sports2 = list(sports)

for i in range(len(num)) :
    sports2.insert(oddNum[i], '')
print(sports2)

sports2[1::2] = num
print(sports2)  