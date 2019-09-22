def getChange(coins, target):
    if target == 0 or target == 1:
        return 1
    if target < 0 or (len(coins) == 0 and target > 0):
        return 0
    else:
        # recursive call for the function, each time it finds a chenge for the number - the last coin
        return getChange(coins[:], target - coins[-1]) + getChange(coins[:-1], target)


def main():
    target = int(input('Enter a number:\n'))
    coins = [x for x in range(1, target)]
    print(getChange(coins, target))


if __name__ == '__main__':
    main()
