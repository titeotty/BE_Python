t = ( [1, 3, 2], [6, 3, 9])
print(t[0])
print(t[1])

# t[0] = [100, 50, 80] 튜플 항목에 데이터 할당 불가능
t[0][0] = 999

print(t[0])
print(t[1])

tt = [(10, 2, 5), (20, 30, 40)]
tt[0] = (100, 200)