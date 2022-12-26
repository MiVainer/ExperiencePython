Numbers = {"Миша": "8-923-733-32-87", "Семён": "8-919-232-31-22", "Катя": "8-922-132-31-11", "Маша": "8-999-111-22-33"}
print(Numbers)
print(Numbers["Катя"])
print(Numbers.keys())  # вывод всех ключей
print(Numbers.values())  # вывод всех значений
del (Numbers["Миша"])  # удаление элемента словаря
print(Numbers)
Numbers.clear()  # удаление всех элементов словаря
print(Numbers)
