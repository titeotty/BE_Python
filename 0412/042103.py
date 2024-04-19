# print(range(0, 5))

# list1 = range(0,5)
# print(list1)

# list2 = list(range(5))
# print(list2)


# print ( list(range(1, 10, 3))) # [start = 0], end, [step=1]

# for i in range(0, 10):
#     print(i)

# #range 함수는 값의 집단을 형성해줌
# print("======================================")


#구구단
d = int(input("몇 단을 출력할까요? "))
for i in range(1, 10):
    print(d, "*", i, "=", "{0:2d}".format(d * i))