# Класс - это шаблон кода, по которому создаются объекты. Т. е. сам по себе класс ничего не делает, но с его помощью
# можно создать объект и уже его использовать в работе. Данные внутри класса делятся на свойства и методы. Свойства
# класса (они же поля или атрибуты) - это характеристики объекта класса. Методы класса - это функции,
# с помощью которых можно оперировать данными класса.
from hero import *
# создаём объекты
myhero1 = Hero("Vurdalak", 5, "paladin")
myhero2 = Hero("Cherep", 3, "ork")

myhero1.show_hero()
myhero2.move()
myhero1.level_up()
myhero1.show_hero()
myhero2.set_health(40)
myhero2.show_hero()