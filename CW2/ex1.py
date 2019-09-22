def find_freq(s):
    words = [str(x) for x in s.split()]
    wordz =set(words)
    min_words = list(wordz)
    freq = []
    for i in range(len(min_words)):
        count = 0
        for j in range(len(words)):
            if min_words[i] == words[j]:
                count+=1
        freq.append(count)
    dictt = dict(zip(min_words,freq))
    return dictt


def main():
    s = input('Enter a string: ')
    print(find_freq(s))


if __name__ == '__main__':
    main()
