def toFah(cel):
    return cel * 9 / 5 + 32

for celsius in range(20, 42, 3):
    fah1 = celsius * 9/5 + 32 #화씨로 변환
    fah1 = toFah(celsius) 
    fah2 = celsius * 2 + 30 #계산하기 쉬운 화씨로 변환 
    print('섭씨:', celsius, '화씨:', fah1, '화씨(약식):', fah2, end = ' ')
    print('차이: %.2f' % abs(fah1 - fah2))