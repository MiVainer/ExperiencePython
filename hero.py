# Функции к вкладке Классы

class Hero():
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
