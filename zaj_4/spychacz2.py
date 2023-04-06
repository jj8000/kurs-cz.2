# zad 1 - określ najkrótszą możliwą ścieżkę tak by zebrać wszystkie punkty. Wypisz rozwiązanie. (Dijkstra)

import matplotlib
import matplotlib.pyplot as plt
import random
import numpy as np
import pandas as pd

# d(i)	 -	koszt dojścia od wierzchołka vo do wierzchołka i-tego wzdłuż najkrótszej ścieżki. Koszt dojścia jest sumą wag krawędzi, przez które przechodzimy posuwając się wzdłuż wyznaczonej najkrótszej ścieżki.
# p(i)	 -	dla i-tego wierzchołka grafu p(i) zawiera numer wierzchołka poprzedzającego na najkrótszej ścieżce

# random.seed(3)

target_amount = 5  # liczba celów do zebrania
target_numbers = [i for i in range(1, target_amount + 1)]


class Spychacz:
    def __init__(self):
        self.x = 5
        self.y = 5
        self.orientation = 1


Spychacz = Spychacz()


class Target:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.l = (abs(self.x - Spychacz.x) + abs(self.y - Spychacz.y))
        random.shuffle(target_numbers)
        self.number = target_numbers.pop()

    def __repr__(self):
        return f'(Numer {self.number}, x={self.x}, y={self.y})'

    def dist(self, other):
        if self != other:
            return abs(self.x - other.x) + abs(self.y - other.y)


xy = [(x, y) for x in range(1, 10) for y in range(1, 10)]
xy_sample = random.sample(xy, target_amount)
target_list = [Target(x, y) for x, y in xy_sample]
print(target_list)

target_dict = {}

for t in target_list:
    target_dict.update({t.number: [t.x, t.y, t.l]})

# print(target_dict)

idx = ['x', 'y', 'L']

df = pd.DataFrame(target_dict, index=idx)
df = df.transpose()
print(df)
numer_celu = ([df['L'].idxmin()][0])


# print(df)

def ustal_wektor():
    return (df.loc[df['L'].idxmin(), 'x'] - Spychacz.x, df.loc[df['L'].idxmin(), 'y'] - Spychacz.y)


wektor = (ustal_wektor()[0], ustal_wektor()[1])


# print(ustal_wektor())
# print(wektor)


def obrot_do_x():
    if wektor[0] < 0:
        Spychacz.orientation = 4
    if wektor[0] == 0:
        pass
    if wektor[0] > 0:
        Spychacz.orientation = 2
    display()
    plt.pause(1)


def jedz_x():
    if wektor[0] < 0:
        Spychacz.x -= 1
    if wektor[0] == 0:
        pass
    if wektor[0] > 0:
        Spychacz.x += 1
    slad()
    plt.plot(slady_x, slady_y)
    display()
    plt.pause(1)


def obrot_do_y():
    if wektor[1] < 0:
        Spychacz.orientation = 3
    if wektor[1] == 0:
        pass
    if wektor[1] > 0:
        Spychacz.orientation = 1
    display()
    plt.pause(1)


def jedz_y():
    if wektor[1] < 0:
        Spychacz.y -= 1
    if wektor[1] == 0:
        pass
    if wektor[1] > 0:
        Spychacz.y += 1
    slad()
    plt.plot(slady_x, slady_y)
    display()
    plt.pause(1)


boundary1 = [0, 0]
boundary2 = [0, 10]
boundary3 = [10, 10]
boundary4 = [10, 0]

plt.figure(figsize=(10, 10))
plt.xticks(np.arange(0, 11, 1))
plt.yticks(np.arange(0, 11, 1))
plt.plot(boundary2, boundary1, linewidth=3, color='k')
plt.plot(boundary1, boundary4, linewidth=3, color='k')
plt.plot(boundary3, boundary4, linewidth=3, color='k')
plt.plot(boundary2, boundary3, linewidth=3, color='k')
for t in target_list:
    plt.scatter(t.x, t.y, color='y')
plt.grid(linewidth=1, linestyle=':')


def display():
    if Spychacz.orientation == 1:
        plt.scatter(Spychacz.x, Spychacz.y, s=100, marker='^', color='r')
    if Spychacz.orientation == 2:
        plt.scatter(Spychacz.x, Spychacz.y, s=100, marker='>', color='r')
    if Spychacz.orientation == 3:
        plt.scatter(Spychacz.x, Spychacz.y, s=100, marker='v', color='r')
    if Spychacz.orientation == 4:
        plt.scatter(Spychacz.x, Spychacz.y, s=100, marker='<', color='r')


display()
plt.pause(1)


# path = input("Wciśnij ENTER aby uruchomić spychacz")

#
# def przemiesc_spychacz():
#     if i == 'G':
#         if Spychacz.orientation == 1: #północ
#             Spychacz.y += 1
#         if Spychacz.orientation == 2: #wschód
#             Spychacz.x += 1
#         if Spychacz.orientation == 3: #południe
#             Spychacz.y -= 1
#         if Spychacz.orientation == 4: #zachód
#             Spychacz.x -= 1
#     if i == 'L':
#         if Spychacz.orientation == 1:
#             Spychacz.orientation = 4
#         else:
#             Spychacz.orientation -= 1
#     if i == 'R':
#         if Spychacz.orientation == 4:
#             Spychacz.orientation = 1
#         else:
#             Spychacz.orientation += 1
#
#


def sprawdzenie():
    for t in target_list:
        if t.x == Spychacz.x and t.y == Spychacz.y:
            target_list.remove(t)
    df.drop(index=numer_celu, inplace=True)


slady_x = [Spychacz.x]
slady_y = [Spychacz.y]


def slad():
    slady_x.append(Spychacz.x)
    slady_y.append(Spychacz.y)


while len(target_list) != 0:
    ustal_wektor()
    wektor = [ustal_wektor()[0], ustal_wektor()[1]]
    print(wektor)
    obrot_do_x()
    for i in range(abs(wektor[0])):
        jedz_x()
    obrot_do_y()
    for i in range(abs(wektor[1])): 
        jedz_y()
    sprawdzenie()
    if len(target_list) == 0:
        print('Koniec trasy')
        break
    numer_celu = ([df['L'].idxmin()][0])
    print(df)
    plt.pause(1.5)



plt.show()


# zad 2 - dodaj kontener, zrób algorytm do wepchnięcia ich do kontenera, nie można pchać dwóch kul naraz
