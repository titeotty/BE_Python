from random import choice

madewin = {'가위' : '보', '바위' : '가위', '보' : '가위'}

game = ['가위 바위 보 게임', '가위', '바위', '보']
msg = ['비겼습니다', '축하합니다! 당신이 이겼습니다.']
msg.append('아쉽지만, 컴퓨터가 이겼습니다')

print((game[0] + '시작 ').center(55, '='))

while True :
    try: 
        s = ' 0(종료), 1(가위), 2(바위), 3(보) 중 하나 선택 >> '
        num = int(input(s))
    except :
        num = 1
    if num == 0:
        break

    if not (0 <= num <= 3) :
        print('입력이 잘못되었습니다')
        continue

    player = game[num]
    com = choice(game[1:])

    if player == com:
        winner = 0
        
    elif madewin[player] == com:
        winner = 1

    else :
        winner = 2

    print('당신: ', player, 'vs', '컴퓨터: ', com)
    print(msg[winner])

print('종료합니다')