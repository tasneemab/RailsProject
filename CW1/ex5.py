import random


def change(word):
    guessed = []
    for letter in word:
        guessed.append('-')
    return guessed


def hang_man(word):
    lives = len(word)
    char = None
    guessed_chars = []
    guessed_word = change(word)

    while lives > 0 and '-' in guessed_word:
        char = input("Enter a character: ").lower()
        if char in guessed_chars:
            print('You have already guessed this letter!')
        else:
            guessed_chars.append(char)
            for ch in range(len(word)):
                if char in word[ch]:
                    guessed_word[ch] = char
            print(guessed_word)
            if char not in word:
                lives -= 1
                print('Wrong guess')
        if '-' not in guessed_word:
            print('Congratulation you have guessed the word, the word is {}'.format(word.upper()))
        elif '-' in guessed_word and lives == 0:
            print('Game Over!, the word was {}'.format(word.upper()))


def main():
    print(
        'Welcome to hangman game..\nThe computer choose a random word which related to computer field, and you have '
        'to try to guess it letter by letter.\n'
        'Be careful ypu only have the words length attempts !\n ')
    words = ['python', 'html', 'css', 'cobol', 'java', 'javascript', 'ruby', 'matlab']
    random_word = random.choice(words)
    print('The word has {} letters'.format(len(random_word)))
    hang_man(random_word)


if __name__ == '__main__':
    main()
