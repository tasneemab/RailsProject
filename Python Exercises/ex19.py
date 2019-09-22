def find_divided_by3(num):
    dividedby3 = []
    smaller = [int(x) for x in range(1, num)]
    for x in smaller:
        if x % 3 == 0:
            dividedby3.append(x)
    return dividedby3


def main():
    num = input("Enter a number:")
    print(find_divided_by3(int(num)))


if __name__ == '__main__':
    main()
