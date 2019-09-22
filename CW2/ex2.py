def flatten(li):
    return sum(([x] if not isinstance(x, list) else flatten(x)
                for x in li), [])


def main():
    n_list = [1, 2, [3, 4, [5, 6, [7, 8], 9]], 10]
    print(n_list)
    print(flatten(n_list))


if __name__ == '__main__':
    main()
# [1,2,[3,4,[5,6,[7,8],9]],10]
