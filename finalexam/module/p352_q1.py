from datetime import date, timedelta

today = date.today()
print('%d년 %d월 %d일' % (today.year, today.month, today.day))

xmasday = date(today.year, 12, 25)
delta = xmasday - today
print(f'크리스마스까지 {delta.days}일 남았습니다.')

date100 = timedelta(days=100)
after100 = today + date100
print(f'오늘부터 100일 후는 {after100}입니다.')

bdayInput = input("생일을 입력해주세요 (YYYY-MM-DD): ")
year, month, day = map(int, bdayInput.split('-'))
bday = date(year, month, day)
delta2 = bday - today
print(f'생일까지 {delta2.days}일 남았습니다.')