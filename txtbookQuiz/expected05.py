time = input('시각 정보(16:30:15) 입력 >> ')
print('입력 시각 정보:', time)
hours, mins, secs = time.split(':')
print('{}시 {}분 {}초'.format(hours, mins, secs))
print(f'{hours}시 {mins}분 {secs}초')