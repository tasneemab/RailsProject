def main():
    homework = open('homework.txt', 'r')
    solution = open('solution.txt', 'w+')
    lines = homework.readlines()
    for line in lines:
        sol = eval(line)
        solution.write(line.rstrip('\r\n') + ' = ' + f'{sol}' + "\n")
        print(line.rstrip('\n') + (' = ' + f'{sol}') + "\n")

    homework.close()
    solution.close()


if __name__ == '__main__':
    main()
