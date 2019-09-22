import random


def main():
    num = random.randint(1, 9)
    attempts = 0
    guess = int(input("Enter a number from 1 to 9: "))
    while num != guess:
        attempts += 1
        if guess < num:
            print("guess is low, try again")
            guess = int(input("Enter a bigger number from 1 to 9: "))
        elif guess > num:
            print("guess is high, try again")
            guess = int(input("Enter a smaller number from 1 to 9: "))
        else:
            print("you guessed it, good job!")
            break
    print('you needed {} attempt to guess it!'.format(attempts + 1))


if __name__ == '__main__':
    main()
