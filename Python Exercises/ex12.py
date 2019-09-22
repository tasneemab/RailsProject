def return_content():
    file = open('file.txt', 'r+')
    lines = file.readlines()
    for line in lines:
        print(line)


def main():
    return_content()


if __name__ == '__main__':
    main()

