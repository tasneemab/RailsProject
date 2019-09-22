import math as m

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

    def assault(self, unit):
        if unit.defense < self.attack:
            unit.health -= self.attack - unit.defense
            if type(self).__name__ == 'Vampire':
                self.health += m.floor((self.attack - unit.defense) * self.vampirism)
                if self.health > self.max_health:
                    self.health = self.max_health


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


class Warlord(Warrior):
    def __init__(self):
        Warrior.__init__(self, health=100, attack=4, defence=2)


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


class Army():
    def __init__(self):
        self.units = []

    def add_units(self, unit_type, amount):
        if unit_type.__name__ != 'Warlord':
            for i in range(amount):
                self.units += [unit_type()]
        else:
            for unit in self.units:
                if type(unit).__name__ == 'Warlord':
                    break
            else:
                self.units += [Warlord()]

    def move_units(self):
        if type(self.units[-1]).__name__ != 'Warlord':
            for i in self.units:
                if type(i).__name__ == 'Warlord':
                    self.units.remove(i)
                    self.units += [i]
                    break
        for n in range(int((len(self.units) - 1) * len(self.units) / 2)):
            for a in range(len(self.units) - 2):
                if ((type(self.units[a]).__name__ != 'Lancer' and
                     type(self.units[a + 1]).__name__ == 'Lancer')):
                    extra = self.units[a]
                    self.units[a] = self.units[a + 1]
                    self.units[a + 1] = extra
        if len(self.units) > 1:
            if not self.units[1].is_alive:
                self.units.pop(1)
        for n in range(int((len(self.units) - 1) * len(self.units) / 2)):
            for i in range(1, len(self.units) - 2):
                if ((type(self.units[i]).__name__ != 'Healer' and
                     type(self.units[i + 1]).__name__ == 'Healer')):
                    extra = self.units[i]
                    self.units[i] = self.units[i + 1]
                    self.units[i + 1] = extra
        if not self.units[0].is_alive:
            self.units.pop(0)
            for unit in self.units[:-1]:
                if type(unit).__name__ == 'Lancer':
                    self.units.remove(unit)
                    self.units = [unit] + self.units
                    break
            else:
                for unit in self.units[:-1]:
                    if type(unit).__name__ not in ['Healer', 'Warlord']:
                        self.units.remove(unit)
                        self.units = [unit] + self.units
                        break

    def fight_with(self, enemy):
        front_1 = self.units[0]
        front_2 = enemy.units[0]
        if len(self.units) > 1:
            back_1 = self.units[1]
        if len(enemy.units) > 1:
            back_2 = enemy.units[1]
        front_1.assault(front_2)
        if type(front_1).__name__ == 'Lancer' and len(enemy.units) > 1:
            front_1.lance_assault(front_2, back_2)
        if len(self.units) > 1:
            if type(back_1).__name__ == 'Healer':
                back_1.heal(front_1)
        if len(enemy.units) > 1:
            if not (front_2.is_alive and back_2.is_alive):
                if type(enemy.units[-1]).__name__ == 'Warlord':
                    enemy.move_units()
                else:
                    if not front_2.is_alive:
                        enemy.units.remove(front_2)
                        return True
                    if not back_2.is_alive:
                        enemy.units.remove(back_2)
        elif not front_2.is_alive:
            enemy.units.remove(front_2)
            return True
        else:
            return False


class Battle:

    @staticmethod
    def fight(first_army, second_army):
        for unit in first_army.units:
            if type(unit).__name__ == 'Warlord':
                first_army.move_units()
                break
        for unit in second_army.units:
            if type(unit).__name__ == 'Warlord':
                second_army.move_units()
                break
        while first_army.units and second_army.units:
            if first_army.fight_with(second_army):
                continue
            if not second_army.units:
                return True
            second_army.fight_with(first_army)
        return bool(first_army.units)

    @staticmethod
    def straight_fight(army_1, army_2):
        for unit in army_1.units:
            if type(unit).__name__ == 'Warlord':
                army_1.move_units()
                break
        for unit in army_2.units:
            if type(unit).__name__ == 'Warlord':
                army_2.move_units()
                break
        while army_1.units and army_2.units:
            if type(army_1.units[-1]).__name__ == 'Warlord':
                army_1.move_units()
            if type(army_2.units[-1]).__name__ == 'Warlord':
                army_2.move_units()
            for i in range(min(len(army_1.units), len(army_2.units))):
                if fight(army_1.units[i], army_2.units[i]):
                    army_2.units[i] = 0
                else:
                    army_1.units[i] = 0
            while 0 in army_1.units:
                army_1.units.remove(0)
            while 0 in army_2.units:
                army_2.units.remove(0)
        return bool(army_1.units)


def fight(unit1, unit2):
    if not unit2.is_alive:
        return True
    while unit1.is_alive:
        unit1.assault(unit2)
        if not unit2.is_alive:
            return True
        unit2.assault(unit1)
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
