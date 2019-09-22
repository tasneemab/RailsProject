from random import sample


def diff_avg(list1, list2):
    return abs(sum([x1 - x2 for (x1, x2) in zip(list1, list2)])) / len(list1)


def main():
    list1 = [int(x) for x in sample(range(0, 100), 10)]
    list2 = [int(y) for y in sample(range(0, 100), 10)]
    print(diff_avg(list1, list2))


if __name__ == '__main__':
    main()
