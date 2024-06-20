'''
Q2. 튜플 Korean과 English를 만들어 한글을 입력받아 영어를 출력하는 프로그램을 작성
output :
- Korean 튜플
- 한글과 매칭되는 영어단어
- 단어가 사전에 없을 시 알림문구 출력
'''

tK = ('감자', '복숭아', '딸기')
tE = ('potato', 'peach', 'strawberry')
print(tK)
ipK = input('찾을 단어 입력 : ')
flag = 0

for i in range(3) :
    if ipK == tK[i] :
        print(tE[i])
        flag = 1
        break

if flag == 0 :
    print("찾는 단어가 사전에 존재하지 않습니다.")
