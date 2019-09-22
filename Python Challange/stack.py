class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    @property
    def size(self):
        return len(self.items)

    def top(self):
        return self.items[len(self.items) - 1]


def main():
    s = Stack()
    print(s.isEmpty())
    s.push(4)
    s.push(8)
    s.push(99)
    s.push('hello')
    print(s.isEmpty())
    print(s.size)
    print(s.top())


if __name__ == '__main__':
    main()
