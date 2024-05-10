import random
# value = random.randint(1, 46)

# valueList = []
# valueList.append(value)

# valueSet = set()
# valueSet.add(value)
#로또번호 생성
valueSet = set()

while True:
    value = random.randint(1, 46)
    valueSet.add(value)
    if len(valueSet) == 6:
        break
print(valueSet)
print('='*20)

valueSet2 = random.sample(range(1, 46), 6)
print(valueSet2)