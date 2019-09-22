def bracketsVerifier(str):
    correct = []
    brackets = {'{': '}', '[': ']', '(': ')'}

    for parentheses in str:
        if parentheses in brackets:
            correct.append(parentheses)
        elif len(correct) == 0 or brackets[correct.pop()] != parentheses:
            return False
    return len(correct) == 0


def main():
    print(bracketsVerifier("(){}[]"))
    print(bracketsVerifier("()[{)}"))
    print(bracketsVerifier("()"))
    print(bracketsVerifier("([{}])"))


if __name__ == '__main__':
    main()
