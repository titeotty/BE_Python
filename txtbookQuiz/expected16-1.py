import random
before = random.randint(1, 100)
print('첫 값은 {} 입니다.'.format(before))

while True:
    print()
    op = input('산술 연산의 종류를 입력하세요. >> ')
    if op not in '+-*/%':
        break
    else:
        oprd = int(input('두 번째 피연산자를 입력하세요. >> '))
        match(op):
            case '+': after = before + oprd
            case '-': after = before - oprd
            case '*': after = before * oprd
            case "/": after = before / oprd
            case "%": after = before % oprd

        print('{} {} {} = {}'.format(before, op, oprd, after))
        print()