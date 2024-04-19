#import random
from random import randint
#while True:
do:
    #num1 = random.randint(1, 99);
    #num2 = random.randint(1, 99);
    #num1 = randint(1, 99);
    #num2 = randint(1, 99);
    num1, num2 = randint(1, 99), randint(1, 99)
    result = num1 * num2
    print('%d * %d = %d' % (num1, num2, result))
    print()
    more = input('계속 y / n ? ')
'''
    if more in 'nN':
    #if more == "n" or more == "N":
        break
'''
while more not in 'nN'
