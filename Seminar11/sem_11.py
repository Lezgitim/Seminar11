# Задача 1. Постройте график функции𝑓(𝑥)=5𝑥^2+10𝑥−30
# По графику определите, при каких значения x значение функции отрицательно.

from tkinter import *
import numpy as np
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from random import randint


def graph():

    fig, ax = plt.subplots()
    fig, ax1 = plt.subplots()
    

    x = np.linspace(-5, 5, 1000)
    y = 5*x**2+10*10*x-30

    b = y
    b = str(b)
    b = b.split()

    c = x
    c = str(c)
    c = c.split()

    znacheniyax = []
    for i in range(len(y)):
        if f"-" in b[i]:
            znacheniyax.append(c[i])
    print(f"Значение функции отрицательно при х равной {znacheniyax}")

    ax.plot(x, y)
    ax1.plot(x, y)


    ax1.set_ylim([-1, -500])
    plt.show()


# Задача 2. Имеются данные о площади и стоимости 15 домов.
# Риелтору требуется узнать в каких домах стоимость квадратного метра меньше 50000 рублей.
# Предоставьте ему графические данные о стоимости квадратного метра каждого дома
# и список подходящих ему домов, отсортированных по площади.
# Данные о домах сформируйте случайным образом. Площади от 100 до 300 кв. метров,
# цены от 3 до 20 млн.

def rieltor():

    dom = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    ceni_vseh_za_metr = []
    ploshad_vseh = []

    for i in range(len(dom)):
        ploshad = randint(100, 300)
        cena = randint(3000000, 20000000)
        a = cena//ploshad
        ploshad_vseh.append(ploshad)
        ceni_vseh_za_metr.append(a)
    print(ploshad_vseh)
    print(ceni_vseh_za_metr)

    ploshad_vseh2 = sorted(ploshad_vseh)
    b = []
    kount = 0
    for i in range(len(dom)):
        kount = 0
        for j in range(len(dom)):
            if ceni_vseh_za_metr[j] < 50000 and ploshad_vseh2[i] == ploshad_vseh[j] and kount == 0:
                b.append(
                    f'Дом № {j+1}: {ceni_vseh_za_metr[j]} рублей за квадратный метр (площадью {ploshad_vseh[j]} кв.м)')
                kount += 1

    b = str(b)
    b = b.split(',')
    for i in range(len(b)):
        b[i] = b[i]+'\n'+'\n'

    doma = ('1', '2', '3', '4', '5', '6', '7', '8',
            '9', '10', '11', '12', '13', '14', '15')
    y_pos = np.arange(len(doma))
    plt.bar(y_pos, ceni_vseh_za_metr, align='center', alpha=0.5)
    plt.xticks(y_pos, doma)
    plt.ylabel('Цена за один квадратный метр')
    plt.xlabel('Номер дома')
    plt.title('Стоимость домов за один квадратный метр')

    top = Tk()
    top.title("Дома стоимостью за один квадратный метр меньше 50000 рублей")
    text = Text(top, wrap='word')
    text.insert(INSERT, b)

    text.pack()

    plt.show()
