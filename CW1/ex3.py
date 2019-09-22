def upper_implement(s):
    result = ''
    for let in s:
        if let.islower():
            upper_value = ord(let) - 32
            upper_let = chr(upper_value)
        result = result + upper_let
        if let == ' ':
            result = result+let
    return result


def split_implement(s, sep):
    result = []
    count = 0
    for i, char in enumerate(s):
        if char == sep:
            result.append(s[count:i])
            count = i + 1
    if count == 0:
        return [s]
    result.append(s[count:i + 1])

    return result


def main():
    s = input('Enter a string: ')
    sep = input('Enter a separator')
    print(upper_implement(s))
    print(split_implement(s, sep))


if __name__ == '__main__':
    main()
