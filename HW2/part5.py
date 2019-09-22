class Warrior(object):
    def __init__(self, health=50, attack=5, defence=0, vampirism=0):
        self.health = health
        self.max_health = self.health
        self.attack = attack
        self.defence = defence
        self.vampirism = vampirism

    @property
    def is_alive(self):
        return bool(self.health > 0)

    def equip_weapon(self, weapon):
        self.health += weapon.health
        self.attack += weapon.attack
        if self.attack < 0: self.attack = 0
        if type(self).__name__ == 'Defender':
            self.defence += weapon.defence
            if self.defence < 0: self.defence = 0
        if type(self).__name__ == 'Vampire':
            self.vampirism += weapon.vampirism
            if self.vampirism < 0: self.vampirism = 0
        if type(self).__name__ == 'Healer':
            self.heal_pwr += weapon.heal_pwr
            if self.heal_pwr < 0: self.heal_pwr = 0


class Knight(Warrior):
    def __init__(self):
        Warrior.__init__(self, attack=7)


class Defender(Warrior):
    def __init__(self):
        Warrior.__init__(self, health=60, attack=3)
        self.defence = 2


class Rookie(Warrior):
    def __init__(self):
        Warrior.__init__(self, health=50, attack=1)


class Vampire(Warrior):
    def __init__(self):
        Warrior.__init__(self, health=40, attack=4)
        self.vampirism = 50


class Lancer(Warrior):
    def __init__(self):
        Warrior.__init__(self, attack=6)
        self.lancerism = 50


class Healer(Warrior):
    def __init__(self):
        Warrior.__init__(self, health=60, attack=0)
        self.heal_pwr = 2

    def heal(self, unit):
        unit.health = min(unit.max_health, unit.health + self.heal_pwr)


class Weapons:
    def __init__(self, health=0, attack=0, defence=0, vampirism=0, heal_pow=0):
        self.health = health
        self.attack = attack
        self.defence = defence
        self.vampirism = vampirism
        self.heal_pwr = heal_pow


class Sword(Weapons):
    def __init__(self):
        Weapons.__init__(self, health=5, attack=2)


class Shield(Weapons):
    def __init__(self):
        Weapons.__init__(self, health=20, attack=-1, defence=2)


class GreatAxe(Weapons):
    def __init__(self):
        Weapons.__init__(self, health=-15, attack=5, defence=-2, vampirism=10)


class Katana(Weapons):
    def __init__(self):
        Weapons.__init__(self, health=-20, attack=6, defence=5, vampirism=50)


class MagicWand(Weapons):
    def __init__(self):
        Weapons.__init__(self, health=30, attack=3, heal_pow=3)


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

    @staticmethod
    def straight_fight(army1, army2):
        while army1.units and army2.units:
            for i in range(min(len(army1.units), len(army2.units))):
                if fight(army1.units[i], army2.units[i]):
                    army2.units[i] = 0
                else:
                    army1.units[i] = 0
            while 0 in army1.units:
                army1.units.remove(0)
            while 0 in army2.units:
                army2.units.remove(0)
        return bool(army1.units)


def fight(unit1, unit2, unit3=0, unit4=0):
    if not unit2.is_alive:
        return True
    while unit1.health > 0:
        if unit1.attack > unit2.defence:
            unit2.health += unit2.defence - unit1.attack
            unit1.health += ((unit1.attack - unit2.defence) *
                             unit1.vampirism)
            # Attacking second_army's second unit (Lancer's ability).
            if unit4 and type(unit1).__name__ == 'Lancer':
                unit4.health -= ((unit1.attack - unit2.defence) * unit1.lancerism)
            # Healing first_army's first unit (Healer's ability).
            if type(unit3).__name__ == 'Healer':
                unit3.heal(unit1)
        if not unit2.is_alive:
            return True
        if unit2.attack > unit1.defence:
            unit1.health += unit1.defence - unit2.attack
            unit2.health += ((unit2.attack - unit1.defence) * unit2.vampirism)
            # Attacking first_army's second unit(Lancer's ability).
            if unit3 and type(unit2).__name__ == 'Lancer':
                unit3.health -= ((unit2.attack - unit1.defence) * unit2.lancerism)
            # Healing second_army's first unit (Healer's ability).
            if type(unit4).__name__ == 'Healer':
                unit4.heal(unit2)
    return False


def main():
    ogre = Warrior()
    lancelot = Knight()
    richard = Defender()
    eric = Vampire()
    freelancer = Lancer()
    priest = Healer()

    sword = Sword()
    shield = Shield()
    axe = GreatAxe()
    katana = Katana()
    wand = MagicWand()
    super_weapon = Weapons(50, 10, 5, 150, 8)

    ogre.equip_weapon(sword)
    ogre.equip_weapon(shield)
    ogre.equip_weapon(super_weapon)
    lancelot.equip_weapon(super_weapon)
    richard.equip_weapon(shield)
    eric.equip_weapon(super_weapon)
    freelancer.equip_weapon(axe)
    freelancer.equip_weapon(katana)
    priest.equip_weapon(wand)
    priest.equip_weapon(shield)

    print(ogre.health)
    print(lancelot.attack)
    print(richard.defence)
    print(eric.vampirism)
    print(freelancer.health)
    print(priest.heal_pwr)

    assert not fight(ogre, eric)
    assert not fight(priest, richard)
    assert fight(lancelot, freelancer)

    my_army = Army()
    my_army.add_units(Knight, 1)
    my_army.add_units(Lancer, 1)

    print(fight(ogre, eric))
    print(fight(priest, richard))
    print(fight(lancelot, freelancer))

    print('-------------------------')

    print(freelancer.is_alive)
    print(freelancer.health)
    priest.heal(freelancer)
    print(freelancer.health)

    enemy_army = Army()
    enemy_army.add_units(Vampire, 1)
    enemy_army.add_units(Healer, 1)

    my_army.units[0].equip_weapon(axe)
    my_army.units[1].equip_weapon(super_weapon)

    enemy_army.units[0].equip_weapon(katana)
    enemy_army.units[1].equip_weapon(wand)

    battle = Battle()

    battle.fight(my_army, enemy_army)


if __name__ == '__main__':
    main()
