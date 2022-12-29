# Функции к вкладке Классы

class Hero(): # родительский класс для класса SuperHero
    """Класс создания героев для игры"""
    def __init__(self, name, level, race): # В классе def является ни функцией, а методом.
        """initiate our Hero"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100
    def show_hero(self):
        """Показать параметры героя"""
        discription = ('\n' + self.name + " Level is: " + str(self.level) + "\nRace is: " + self.race + "\nHealth is: " + str(self.health) + '\n').title()
        print(discription)

    def level_up(self):
        "Повышение уровня героя"
        self.level = self.level + 1 # Можно заменить записью self.level += 1

    def move(self):
        """Start moving hero"""
        print("Hero " + self.name + " start moving")

    def set_health(self, new_health):
        """New health"""
        self.health = new_health

class SuperHero(Hero): # дочерний класс класса Hero
    """Class to create SuperHero"""
    def __init__(self, name, level, race, magiclevel):
        """initiate superhero"""
        super().__init__(name, level, race)
        self.magiclevel = magiclevel
        self.magic = 100

    def makemagic(self):
        """Use magic"""
        self.magic -= 10

    def show_hero(self):
        """Показать параметры героя"""
        discription = ('\n' + self.name + " Level is: " + str(self.level) + "\nMagic level is: " + str(self.magiclevel) +
                       "\nRace is: " + self.race + "\nHealth is: " + str(self.health) + '\n' + "Magic is: " + str(self.magic)).title()
        print(discription)