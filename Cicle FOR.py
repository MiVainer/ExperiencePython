for i in range(1, 10, 1):
    # цикл будет работать от 1 до 5 с шагом 2. Для обратного отсчёта поставим значение шага со знаком "-"
    if i == 1:
        print('one) квадрат числа i =', i**2)
    elif i == 2:
        print('two) квадрат числа i =', i**2)
    elif i == 3:
        print('three) квадрат числа i =', i**2)
    elif i == 4:
        continue
        # закончить текущую итерацию и перейти к следующей (i == 5)
    elif i == 5:
        print('five) квадрат числа i =', i ** 2)
