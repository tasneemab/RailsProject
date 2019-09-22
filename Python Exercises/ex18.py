import random
import string


def weakpassword_generator(length):
    chars = string.digits
    return ''.join(random.choice(chars) for i in range(length))


def meduimpassword_generator(length):
    chars = string.digits + string.ascii_letters
    return ''.join(random.choice(chars) for i in range(length))


def strongpassword_generator(length):
    chars = string.digits + string.ascii_letters + string.punctuation
    return ''.join(random.choice(chars) for i in range(length))


def main():
    answer = input('Enter a password string: Weak, medium or Strong ?\n ').lower()
    
    if answer == 'weak':
        print(weakpassword_generator(length=8))
    elif answer == 'medium':
        print(meduimpassword_generator(length=8))
    
    elif answer == 'strong':
        length = input('Enter the length you want for your password, it must be at least 16:\n')
        length = int(length)
        if length >= 16:
            print(strongpassword_generator(length))
        else:
            print(strongpassword_generator(length=16))


if __name__ == '__main__':
    main()
