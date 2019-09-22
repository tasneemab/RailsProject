from random import sample


def step2_randoms():
    randoms = sample(range(100), 15)
    print(randoms)
    print(randoms[0::2])


def main():
    step2_randoms()


if __name__ == '__main__':
    main()
