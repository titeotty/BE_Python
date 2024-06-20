'''
Q4. 다음 중첩 리스트(data)에서 각 행과 열의 합을 출력하는 프로그램을 작성
output :
- 중첩 리스트 
- 리스트 rsum
- 리스트 csum
'''

data = [[1, 2, 3], 
        [4, 5, 6],
        [7, 8, 9]]

print("중첩 리스트:")
print(data[0])
print(data[1])
print(data[2])

rsum = []
for i in range(3) :
    rsum.append(sum(data[i]))

print("각 행의 합:", rsum)

csum = []
for i in range(3) :
    colSum = 0
    for j in range(3) :
        colSum += data[j][i]
    csum.append(colSum)

print("각 열의 합:", csum)