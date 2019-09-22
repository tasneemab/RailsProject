def calculator(str):
    return eval(str)


def main():
    answer = input('Do you want to calculate a math expression ? y/n \n')
    if answer == 'n':
        exit(0)
    while answer == 'y':
        print(calculator(input('Enter a math expression\n')))
        answer = input('Do you want to calculate another math expression ? y/n \n')


if __name__ == '__main__':
    main()
