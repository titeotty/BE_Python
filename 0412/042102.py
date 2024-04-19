amt = int(input("구매 금액은 "))

if (amt >= 10000 and amt < 20000):
    rate = 0.01
elif (amt >= 20000 and amt < 40000):
    rate = 0.02
elif (amt >= 40000):
    rate = 0.04
else:
    rate = 0.0
pay = amt - (amt * rate)

print("지불 금액은, ", pay)
print("지불 할 금액은 {0:08b}원 입니다.", format(pay))
print("지불 할 금액은 {pay:13d}웝 입니다.") #f-string
