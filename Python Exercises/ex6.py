def findDigits(num):
    digits = []
    while num > 0:
        dig = num % 10
        digits.append(dig)
        num = num // 10
    return digits[::-1]


def findDigitsSum(num):
    sum = 0
    while num > 0:
        dig = num % 10
        sum = sum + dig
        num = num // 10
    return sum


def main():
    num = int(input("Please enter a 5 digits number \n"))
    print("You entered the number:", num)
    print("The digits of this number are :", ','.join(str(a) for a in findDigits(num)))
    print("The sum of the digits is :", findDigitsSum(num))


if __name__ == '__main__':
    main()
