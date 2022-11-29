# Задача 1. В каждой группе учится от 20 до 30 студентов.
#  По итогам экзамена все оценки заносятся в таблицу. Каждой группе отведена своя строка.
# Определите группу с наилучшим средним баллом.

import numpy as np
from random import randint


def Student():

    from random import randint

    stroka = 2
    stolbec = 20
    numbers = [0] * stroka
    gruppa = [0] * stroka

    for i in range(len(numbers)):
        numbers[i] = list(randint(2, 5) for _ in range(stolbec))
        gruppa[i] = sum(numbers[i])/stolbec

    for j in numbers:
        print(j)

    if gruppa[0] > gruppa[1]:
        print(f"Группа 1 - {gruppa[0]}, группа 2 - {gruppa[1]}")
        print(f"Группа 1 имеет наилучший средний балл!")
    else:
        print(f"Группа 1 - {gruppa[0]}, группа 2 - {gruppa[1]}")
        print(f"Группа 2 имеет наилучший средний балл!")


# Задача 2. Дана квадратная матрица, заполненная случайными числами.
# Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.

def El():

    number = np.random.randint(10, size=(5, 5))
    sum = 0
    sum_stroka = 0
    for i in range(5):
        for j in range(5):
            if i == j:
                sum += number[i, j]

    print(number)

    for i in range(5):
        for j in range(5):
            sum_stroka += number[i, j]
        if sum_stroka > sum:
            print(
                f"Cумма элементов {i+1} строки ({sum_stroka}) превосходит {sum}.")
        sum_stroka = 0


# Задача 3. В двумерном массиве хранятся средние дневные температуры
# с мая по сентябрь за прошлый год. Каждому месяцу соответствует своя строка.
# Определите самый жаркий и самый холодный 7-дневный промежуток этого периода.
# Выведите его даты.

def Pogoda():

    number = [
        [16, 16, 18, 17, 18, 19, 18, 16, 17, 18, 19, 19, 20, 21, 18, 19, 15, 16, 17, 18, 19, 19, 20, 21, 21, 20, 20, 21, 22, 20, 21],
        [20, 19, 20, 19, 20, 19, 21, 22, 23, 24, 25, 22, 20, 21, 21, 22, 23, 24, 22, 21, 22, 20, 22, 22, 22, 22, 21, 22, 21, 22],
        [23, 24, 25, 26, 27, 26, 22, 22, 21, 23, 24, 22, 25, 22, 21, 20, 22, 23, 24, 25, 26, 27, 22, 25, 26, 22, 23, 22, 21, 22, 22],
        [27, 26, 27, 27, 28, 29, 25, 26, 25, 25, 24, 22, 25, 22, 21, 20, 22, 23, 24, 25, 26, 27, 22, 25, 26, 22, 23, 22, 21, 22, 22],
        [20, 20, 20, 20, 20, 20, 19, 18, 19, 20, 20, 20, 20, 19, 18, 17, 18, 18, 17, 17, 17, 16, 15, 14, 14, 15, 16, 13, 12, 11]
    ]

    a = number[0]+number[1]+number[2]+number[3]+number[4]
    kount = 1
    x = []

    for i in range(len(a)):
        summ = sum(a[i:i+7])/7
        if (len(a[i:i+7])) == 7:
            x.append(summ)
            kount += 1
            print(a[i:i+7], summ)

    minn = min(x)
    maxx = max(x)

    mesyac_min=0
    date_min=0
    mesyac_max=0
    date_max=0
    j = 0

    for i in range(len((a))):
        if sum(a[i:i+7])/7 == minn:
            j = i
            mesyac_min=j//len(number[0])
            mesyac_min1= mesyac_min+5
            date_min=j%len(number[0])+1

    print(f"Cамый холодный 7-дневный промежуток в период с мая по сентябрь 2021 года: c {date_min+1} по {date_min+7} число {mesyac_min1} месяца (средняя температура {int(minn)} градусов по Цельсию).")

    for i in range(len((a))):
        if sum(a[i:i+7])/7 == maxx:
            m = i
            mesyac_max=m//len(number[0])+1
            mesyac_max1= mesyac_max+5
            date_max=m%len(number[0])
            date_max=date_max-date_max

    print(f"Cамый жаркий 7-дневный промежуток в период с мая по сентябрь 2021 года: c {date_max+1} по {date_max+7} число {mesyac_max1} месяца (средняя температура {int(maxx)} градусов по Цельсию).")
