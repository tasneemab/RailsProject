def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    num = input('Enter a number:\n')
    print(fibonacci(int(num)))


if __name__ == '__main__':
    main()
