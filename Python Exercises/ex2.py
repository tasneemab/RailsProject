num1 = 0
num2 = 1
while True:
    prevNum1 = num1
    prevNum2 = num2
    num1 = prevNum2
    num2 = prevNum1 + prevNum2
    if num2 < 10000:
        print(num2)
    elif num2 > 10000:
        break