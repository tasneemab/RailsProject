class Text(object):

    def __init__(self, font=None, text=' '):
        self.__font = font
        self.__text = text

    def set_font(self, fo):
        self.__font == fo

    def get_font(self):
        return self.__font

    def get_text(self):
        return self.__text

    def write(self, txt):
        self.__text = self.__text + txt

    def show(self):
        return '[{}]'.format(self.__font) + self.__text + '[{}]'.format(self.__font)

    def restore(self, num):
        return SaveText.get_version(num)


class SaveText(Text):
    copies = {}
    editNum = 0

    def save_text(self, text):
        SaveText.copies[SaveText.editNum] = [text.get_text(), text.get_font()]
        SaveText.editNum += 1

    def get_version(self, num):
        return SaveText.copies[num][0]


def main():
    text = Text()
    saver = SaveText()

    text.write("At the very beginning ")
    saver.save_text(text)
    text.set_font("Arial")
    saver.save_text(text)
    text.write("there was nothing.")
    saver.save_text(text)
    print(text.show())
    print(saver.get_version(0))
    print(saver.get_version(2))


if __name__ == '__main__':
    main()
