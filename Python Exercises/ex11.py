from os import stat


def copy_content():
    file1 = open('file1.txt', 'r+')
    file2 = open('file2.txt', 'r+')

    if stat('file1.txt').st_size == 0 and stat('file2.txt').st_size > 0:
        for line in file2.readlines():
            file1.write(line)
        print('File2 Copied to File1\n')

    if stat('file1.txt').st_size > 0 and stat('file2.txt').st_size == 0:
        for line in file1.readlines():
            file2.write(line)
        print('File1 Copied to File2\n')

    file1.close()
    file2.close()


def main():
    copy_content()


if __name__ == '__main__':
    main()
