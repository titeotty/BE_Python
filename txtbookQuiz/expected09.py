month = int(input('월 입력 ? '))
if 11 <= month <= 12 or 1 <= month <= 3:
    print('%d월 겨울' % month)
elif 4 <= month <= 5:
    print('%d월 봄' % month)
elif 6 <= month <= 8:
    print('%d월 여름' % month)
elif 9 <= month <= 10:
    print('%d월 가을' % month)
else:
    print('%d: 잘못 입력' % month)