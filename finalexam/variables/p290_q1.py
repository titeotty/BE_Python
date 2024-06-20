'''
출력 결과를 쓰시오
'''
print("*"* 30, "\na)")

def lang(name) :
    print(name, 'programming language')

lang('python')
lang('java')

print("*"* 30, "\nb)")

def comp(x, y):
    return x * y - (x + y)

print(comp(3, 4))
print(comp(2, 3))