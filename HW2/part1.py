class Warrior:
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack
        self.is_alive = True

    def hit(self, enemy):
        enemy.health -= self.attack

    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    def __init__(self):
        Warrior.__init__(self, attack=7)


def fight(w1, w2):
    while True:
        w1.hit(w2)
        if w1.health <= 0:
            w1.is_alive = False
            return False

        w2.hit(w1)
        if w2.health <= 0:
            w2.is_alive = False
            return True


def main():
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()

    print(fight(chuck, bruce))
    print(fight(dave, carl))
    print(chuck.is_alive)
    print(bruce.is_alive)
    print(carl.is_alive)
    print(dave.is_alive)

    print(chuck.health, chuck.attack, chuck.is_alive)


if __name__ == '__main__':
    main()
