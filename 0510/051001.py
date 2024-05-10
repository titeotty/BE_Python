mList = [1,5,2,7,3,6]

print(mList)
mList.append(4)
print(mList)
mList.insert(0, 11)
print(mList)
print(mList[0])

print(sorted(mList))
print(sorted(mList, reverse=True))

print("sort 이전 ", mList)
mList.sort()

print("sort 이후", mList)