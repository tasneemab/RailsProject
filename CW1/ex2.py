def mix_str(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    length = len1 if len1 > len2 else len2
    result = ''
    for i in range(length):
        if i < len1:
            result += s1[i]
        if i < len2:
            result += s2[i]

    return result


def main():
    str1 = input('Enter the first string: ')
    str2 = input('Enter the second string: ')
    print(mix_str(str1, str2))


if __name__ == '__main__':
    main()
