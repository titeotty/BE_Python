import turtle as t
t.shape('turtle')

#삼각형 그리기
for i in range(3):
    t.forward(100)
    t.left(120)


#사각형 그리기
t.pencolor('blue')
for i in range(4) :
    t.left(90)
    t.forward(150)

#삼각형 그리기2
t.pencolor('green')
t.goto(100, -100)
t.goto(-100, -100)
t.home()

#원 그리기
t.circle(60)

#육각형 그리기
for i in range(6) :
    t.left(60)
    t.forward(100)

t.write('좌표 (0,0)')
input()