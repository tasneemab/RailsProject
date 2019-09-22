class Warrior:
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack

    @property
    def is_alive(self):
        return self.health > 0

    def hit(self, enemy):
        enemy.health -= self.attack


class Knight(Warrior):
    def __init__(self):
        Warrior.__init__(self, attack=7)


class Army:
    def __init__(self):
        self.units = []

    def add_units(self, unit_class, amount):
        for _ in range(amount):
            self.units.append(unit_class())

    @property
    def find_alive_unit(self):
        for unit in self.units:
            if unit.is_alive:
                return unit

    def is_alive(self):
        return self.find_alive_unit is not None

    def __len__(self):
        return len(self.units)


class Battle:

    @staticmethod
    def fight(army1, army2):
        while army1.is_alive and army2.is_alive:
            fight(army1.find_alive_unit, army2.find_alive_unit)
        return army1.is_alive


def fight(unit1, unit2):
    while True:
        unit1.hit(unit2)
        if unit2.health <= 0:
            return True
        unit2.hit(unit1)
        if unit1.health <= 0:
            return False


def main():
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    mike = Knight()
    rog = Warrior()
    ogre = Warrior()

    print(fight(chuck, bruce))
    print(chuck.is_alive)
    print(fight(dave, carl))
    print(dave.is_alive)
    print(carl.is_alive)


if __name__ == '__main__':
    main()
