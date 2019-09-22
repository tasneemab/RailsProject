def word_length(s):
    dictt = {x: len(x) for x in s.split(' ')}
    return dictt


def main():
    print('--------------------------------------l1--------------------------------------')
    l1 = [x for x in range(1, 1000) if x % 7 == 0]
    print(l1,'\n')

    print('--------------------------------------l2--------------------------------------')
    l2 = [x for x in range(1, 1000) for y in str(x) if '3' in y]
    print(l2,'\n')

    print('--------------------------------------l3--------------------------------------')
    l3 = [x for x in 'you are the reason' if x not in ['a', 'o', 'e', 'u', 'i']]
    print(''.join(l3),'\n')

    print('--------------------------------------l4--------------------------------------')
    l4 = [x for x in 'lets get lost somewhere out there'.split(' ') if len(x) < 4]
    print(' '.join(l4),'\n')

    print('--------------------------------------l5--------------------------------------')
    l5 = [x for x in range(1, 1000) for y in range(2, 10) if x % y == 0]
    print(list(set(l5)),'\n')
    print(word_length('hello, its me'))


if __name__ == '__main__':
    main()
