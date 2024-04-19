from random import randint
pay = 12000

for i in range(5):
    hour = randint(35, 50) 
    if 40 < hour:
        gross = 40 * pay + (hour - 40) * pay * 1.5 
    else:
        gross = hour * pay
    print('근로 시간 %d 시간, 주급 %d' % (hour, gross))   