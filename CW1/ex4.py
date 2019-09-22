from itertools import permutations


def biggerIsGreater(word):
    perm_words = permutations(word)
    perm_list = []
    for perm in perm_words:
        perm_list.append(''.join(perm))
    print(*perm_list)
    if len(perm_list) > 2:
        count = 0
        for index, permu in enumerate(perm_list):
            if permu > word and count ==0:
                count += 1
                print(perm_list[index], index)
                return
    else:
        print('No answer')


def main():
    word = input('Enter a word: ')
    biggerIsGreater(word)


if __name__ == '__main__':
    main()

"""
def next_permutation(s):
    i =len(s)-1
    while i >0 and s[i-1]>s[i]:
        i-=1
        if i <= 0:
            return False
    j = len(s)-1
    while s[j]<= s[j-1]:
        j-=1
        temp =s[i-1]
        s[i-1]=s[j]
        s[i]= temp
    s[i:] = s[len(s) - 1: i - 1: -1]
    return True

        if next_permutation(word):
        print("".join(word))
    else:
        print("no answer")

"""
