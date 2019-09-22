def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        print('illegal')
    else:
        return x / y


def main():
    funcs = [multiply, divide]

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    item = map(lambda f: f(num1, num2), funcs)

    print(*list(item), sep="\n")


if __name__ == '__main__':
    main()
