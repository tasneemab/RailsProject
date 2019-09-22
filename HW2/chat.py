VOWELS = "aeiouAEIOU"


class Chat:
    def __init__(self):
        self.human_dialogue = []
        self.robot_dialogue = []

    def connect_human(self, human):
        human.chat = self

    def connect_robot(self, robot):
        robot.chat = self

    def show_human_dialogue(self):
        return "\n".join(self.human_dialogue)

    def show_robot_dialogue(self):
        return "\n".join(self.robot_dialogue)


class Human:
    def __init__(self, name):
        self.__name = name

    def send(self, message):
        robot_message = "".join(["0" if char in VOWELS else "1" for char in message])
        self.chat.robot_dialogue.append(f'{self.__name} said: {robot_message}')
        self.chat.human_dialogue.append(f'{self.__name} said: {message}')


class Robot:
    def __init__(self, serial_number):
        self.__serial_number = serial_number

    def send(self, message):
        robot_message = ''.join(['0' if char in VOWELS else '1' for char in message])
        self.chat.human_dialogue.append(f'{self.__serial_number} said: {message}')
        self.chat.robot_dialogue.append(f'{self.__serial_number} said: {robot_message}')


def main():
    chat = Chat()
    karl = Human('Karl')
    bot = Robot('R2D2')
    chat.connect_human(karl)
    chat.connect_robot(bot)
    karl.send("Hi! What's new?")
    bot.send("Hello, human. Could we speak later about it?")
    print(chat.show_human_dialogue())
    print(chat.show_robot_dialogue())
    print("hello")


if __name__ == '__main__':
    main()
