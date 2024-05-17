def getprime():
    return 2, 3, 5, 7

r1, r2, r3, r4 = getprime()
print(r1, r2, r3, r4)

prime = getprime()
print(prime)
print(*prime)
