from random import choice


# calculate random math problem using eval
def randomCalculator(x, y):
    functions = ['+', '*', '%', '/']
    operation = choice(functions)
    prob = str(x) + operation + str(y)
    print(prob)
    result = eval(prob)
    return result


# calculate random math problem using choice
def random_calculator(x, y):
    functions = [add(x, y), multiply(x, y), modulo(x, y), division(x, y)]
    result = choice(functions)

    return result


def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


def modulo(x, y):
    return x % y


def division(x, y):
    return x / y


def main():
    print(random_calculator(4, 3))
    print(randomCalculator(2, 3))


if __name__ == '__main__':
    main()
