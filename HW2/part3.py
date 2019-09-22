class Warrior(object):
    def __init__(self, health=50, attack=5, defence=0, vampirism=0, lancerism=0):
        self.health = health
        self.max_health = self.health
        self.attack = attack
        self.defence = defence
        self.vampirism = vampirism
        self.lancerism = lancerism

    @property
    def is_alive(self):
        return bool(self.health > 0)


class Knight(Warrior):
    def __init__(self):
        Warrior.__init__(self, attack=7)


class Defender(Warrior):
    def __init__(self):
        Warrior.__init__(self, health=60, attack=3, defence=2)


class Rookie(Warrior):
    def __init__(self):
        Warrior.__init__(self, health=50, attack=1)


class Vampire(Warrior):
    def __init__(self):
        Warrior.__init__(self, health=40, attack=4, vampirism=0.5)


class Lancer(Warrior):
    def __init__(self):
        Warrior.__init__(self, attack=6, lancerism=0.5)


class Healer(Warrior):
    def __init__(self):
        Warrior.__init__(self, health=60, attack=0)
        self.heal_pwr = 2

    def heal(self, unit):
        unit.health = min(unit.max_health, unit.health + self.heal_pwr)


class Army:
    def __init__(self):
        self.units = []

    def add_units(self, unit_class, amount):
        for _ in range(amount):
            self.units.append(unit_class())

    def is_alive(self):
        return bool(self.find_alive_unit is not None)

    def __len__(self):
        return len(self.units)


class Battle:

    @staticmethod
    def fight(army1, army2):
        army1.units += [0]
        army2.units += [0]
        while army1.units != [0] and army2.units != [0]:
            if fight(army1.units[0], army2.units[0],
                     army1.units[1], army2.units[1]):
                army2.units = army2.units[1:]
            else:
                army1.units = army1.units[1:]
        return army1.units != [0]


def fight(unit1, unit2, unit3=0, unit4=0):
    if not unit2.is_alive:
        return True
    while unit1.is_alive:
        if unit1.attack > unit2.defence:
            unit2.health += unit2.defence - unit1.attack
            unit1.health += ((unit1.attack - unit2.defence) *
                             unit1.vampirism)
            # Attacking second_army's second unit (Lancer's ability).
            if unit4 and type(unit1).__name__ == 'Lancer':
                unit4.health -= ((unit1.attack - unit2.defence) *
                                 unit1.lancerism)
            # Healing first_army's first unit (Healer's ability).
            if type(unit3).__name__ == 'Healer':
                unit3.heal(unit1)
        if unit2.health <= 0:
            return True
        if unit2.attack > unit1.defence:
            unit1.health += unit1.defence - unit2.attack
            unit2.health += ((unit2.attack - unit1.defence) *
                             unit2.vampirism)
            # Attacking first_army's second unit(Lancer's ability).
            if unit3 and type(unit2).__name__ == 'Lancer':
                unit3.health -= ((unit2.attack - unit1.defence) *
                                 unit2.lancerism)
            # Healing second_army's first unit (Healer's ability).
            if type(unit4).__name__ == 'Healer':
                unit4.heal(unit2)
    return False


def main():
    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()
    freelancer = Lancer()
    vampire = Vampire()
    priest = Healer()

    print(fight(chuck, bruce))
    print(fight(dave, carl))
    print(chuck.is_alive)
    print(bruce.is_alive)
    print(carl.is_alive)
    print(dave.is_alive)
    print(fight(carl, mark))
    print(carl.is_alive)
    print(fight(bob, mike))
    print(fight(eric, richard))
    print(fight(ogre, adam))
    print(fight(freelancer, vampire))
    print(freelancer.is_alive)
    print(freelancer.health)
    print(priest.heal(freelancer))
    print(freelancer.health)

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Healer, 1)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 2)
    my_army.add_units(Healer, 1)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 4)
    enemy_army.add_units(Healer, 1)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)
    enemy_army.add_units(Healer, 1)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Healer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Healer, 1)
    army_4.add_units(Lancer, 2)

    battle = Battle()

    print(battle.fight(my_army, enemy_army))
    print(battle.fight(army_3, army_4))


if __name__ == '__main__':
    main()
