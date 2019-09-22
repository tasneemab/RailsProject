def dividedBy7(x):
    if x % 7 == 0:
        return True
    else:
        while x > 0:
            if x % 10 == 7:
                return True
            x = x / 10
        return x > 0


numbers = list(range(0, 100))
result = (list(filter(dividedBy7, numbers)))
for num in result:
    print(num, end=" ")
