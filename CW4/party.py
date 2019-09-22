class Friend:
    def __init__(self, name):
        self.__name = name
        self.__message = 'No party...'

    def invite(self, message):
        self.__message = message

    def show_invites(self):
        return self.__message


class Party:
    def __init__(self, place):
        self.__place = place
        self.__friends = []

    def add_friend(self, friend):
        self.__friends.append(friend)

    def del_friend(self, friend):
        self.__friends.remove(friend)

    def send_invites(self, time):
        for friend in self.__friends:
            friend.invite(f'{self.__place}:{time}')

    def friendz(self):
        return self.__friends


def main():
    party = Party("Midnight Pub")
    nick = Friend("Nick")
    john = Friend("John")
    lucy = Friend("Lucy")
    chuck = Friend("Chuck")
    print('Hello, lets have party')
    party.add_friend(chuck)
    party.add_friend(nick)
    party.add_friend(john)
    party.add_friend(lucy)
    party.del_friend(chuck)
    print('Hello, lets have party')
    party.send_invites("Friday, 9:00 PM")
    party.send_invites("Sunday, 10:00 Pm")
    print('Hello, lets have party')



if __name__ == '__main__':
    main()