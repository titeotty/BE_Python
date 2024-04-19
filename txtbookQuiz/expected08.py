num = int(input('정수 입력 >> '))
exp = int(input('2의 지수승 입력 >> '))
#num = 24
#exp = 3
print()
print('정수 {} >> {}, 결과: {}'.format(num, exp, num << exp))
print('정수 {} * 2**{}, 결과: {}'.format(num, exp, num * 2**exp))
print('이진수(32비트): {0:032b} 정수: {0}'.format(num))
print('이진수(32비트): {:032b} 정수: {} << {}'.format(num << exp, num, exp))
print('이진수(32비트): {:032b} 정수: {} * 2**{}'.format(num * 2**exp, num, exp))


num2 = -1
print('정수 {0:32b} >> {1}'.format(num2 & 0xffffffff, exp))
print('결과 {0:32b}'.format((num2 << 2) & 0xffffffff))