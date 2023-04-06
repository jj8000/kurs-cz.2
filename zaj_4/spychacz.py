# spychacz
# Wyświetlamy spychacz oraz 5 punktów
# G - ruch o jedno pole, L - obrót w lewo o 90 stopni, R - obrót w prawo
# Wyświetl animację poruszania się spychacza wraz z pozostawionym śladem
# Wypisz komunikat Wygrał/Przegrał

import matplotlib
import matplotlib.pyplot as plt
import random
import numpy as np


class Target:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __repr__(self):
        return f'({self.x}, {self.y})'

class Spychacz:
    def __init__(self):
        self.x = 5
        self.y = 5
        self.orientation = 1


xy = [(x, y) for x in range(1, 10) for y in range(1,10)]
xy_sample = random.sample(xy, 5)
target_list = [Target(x, y) for x, y in xy_sample]

print(target_list)


Spychacz = Spychacz()

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
        plt.scatter(Spychacz.x, Spychacz.y, s = 100, marker='^', color='r')
    if Spychacz.orientation == 2:
        plt.scatter(Spychacz.x, Spychacz.y, s = 100, marker='>', color='r')
    if Spychacz.orientation == 3:
        plt.scatter(Spychacz.x, Spychacz.y, s = 100, marker='v', color='r')
    if Spychacz.orientation == 4:
        plt.scatter(Spychacz.x, Spychacz.y, s = 100, marker='<', color='r')

display()
# plt.show()

# plt.figure(figsize=(8, 8))
# plt.xticks(np.arange(0, 11, 1))
# plt.yticks(np.arange(0, 11, 1))
# plt.plot(boundary2, boundary1, linewidth=3, color='k')
# plt.plot(boundary1, boundary4, linewidth=3, color='k')
# plt.plot(boundary3, boundary4, linewidth=3, color='k')
# plt.plot(boundary2, boundary3, linewidth=3, color='k')
# for t in target_list:
#     plt.scatter(t.x, t.y, color='y')
# plt.grid(linewidth=1, linestyle=':')


plt.pause(1)
path = input("Podaj ścieżkę(G - ruch, L - obrót w lewo, R - obrót w prawo): ")

raw_path = list(path)

def przemiesc_spychacz():
    if i == 'G':
        if Spychacz.orientation == 1: #północ
            Spychacz.y += 1
        if Spychacz.orientation == 2: #wschód
            Spychacz.x += 1
        if Spychacz.orientation == 3: #południe
            Spychacz.y -= 1
        if Spychacz.orientation == 4: #zachód
            Spychacz.x -= 1
    if i == 'L':
        if Spychacz.orientation == 1:
            Spychacz.orientation = 4
        else:
            Spychacz.orientation -= 1
    if i == 'R':
        if Spychacz.orientation == 4:
            Spychacz.orientation = 1
        else:
            Spychacz.orientation += 1


def sprawdzenie():
    for t in target_list:
        if t.x == Spychacz.x and t.y == Spychacz.y:
            target_list.remove(t)

slady_x = [Spychacz.x]
slady_y = [Spychacz.y]

def slad():
    slady_x.append(Spychacz.x)
    slady_y.append(Spychacz.y)


for i in raw_path:
    przemiesc_spychacz()
    sprawdzenie()
    slad()
    plt.plot(slady_x, slady_y)
    display()
    plt.pause(1)

if len(target_list) == 0:
    print('Wygrałeś!')
else:
    print('Przegrałeś!')
# plt.ion()
plt.show()

# zad 1 - określ najkrótszą możliwą ścieżkę tak by zebrać wszystkie punkty. Wypisz rozwiązanie. (Dijkstra)
# zad 2 - dodaj kontener, zrób algorytm do wepchnięcia ich do kontenera, nie można pchać dwóch kul naraz
