import matplotlib
import matplotlib.pyplot as plt

# sprawdzenie wersji
print(matplotlib.__version__)

# x = [0, 10, 30, 50, 100]
# y = [-2, 4, 7, 5, 12]
# y1 = [-12, 54, 37, 25, 82]


# załadowanie danych
# plt.plot(x, y)
# plt.plot(x, y1)

# wyświetlenie wykresu
# plt.show()

import numpy as np
# np_x = np.array([0,20,100])
# np_y = np.array([2,5,200])
#
# plt.plot(np_x, np_y, 'x') # dołożenie 'x' lub 'o' wyświetla zbiór obserwacji
# plt.show()

linia_punktów = np.array([4,2,8,2,7,1,0])

# linewidth - grubość linii
# marker - znacznik obserwacji

# plt.plot(linia_punktów, linewidth = '1', marker = '>', linestyle = '-.')
# plt.show()

# 'o', '*', '.', 'x', '+', 'D' /diament/, '^', '>', '<', 'v' /trójkąty skierowane w jakimś kierunku'

#linestyle:
# - - linia
# : - linia kropkowana
# -- kreskowana
# -. kreskowano kropkowana

# color:
# r - red
# g - green
# b - blue
# c - cyan
# m - magenta
# y - yellow
# k - black
# w - white

# plt.plot(linia_punktów, marker = 'o', ms = 20, mec = 'k', mfc = 'y')
# plt.show()

# ms - marker size, mec - marker edge color, mfc - marker foreground color

#
# p_x1 = [0,4,8,16]
#
# p_y1 = [5,2,7,1]
# p_y2 = [9,-1,6,2]
#
# plt.xlabel('Punkty x')
# plt.ylabel('Punkty y')
#
# plt.title('Wykres z danymi')
#
# # font
#
# f = {
#     'family' : 'Times New Roman',
#     'color' : 'blue',
#     'size' : 15
# }
#
#
# plt.title('Wykres z danymi', fontdict=f, loc = 'left')
# plt.plot(p_x1, p_y1, p_x1, p_y2)
#
# plt.grid()
# plt.show()

# zad 1 Wygeneruj 3 listy po 10 elementów z zakresu od -10;10
# zaprezentuj na wykresie: r,g,b, różne style linii itd.

import random

# list1 = []
# list2 = []
# list3 = []
#
# def ran10(arg: list):
#     while len(arg) < 10:
#         arg.append(random.randint(-10, 10))
#
#     print(arg)
#
# ran10(list1)
# ran10(list2)
# ran10(list3)
#
# plt.xlabel('Oś numeru losowania')
# plt.ylabel('Oś losowań')
#
# p_x = [x for x in range(1, 11)]
# print(p_x)
#
# plt.plot(p_x, list1, color = 'red', marker = 'o', linestyle = ':')
# plt.plot(p_x, list2, color = 'green', linestyle = '--', marker = 'D')
# plt.plot(p_x, list3, color = 'blue', marker = '^', mec = 'red', mfc = 'orange')
# plt.show()

# szybciej zrobić listy przy pomocy random.sample

# x1 = [0,5,10,15,20]
# y1 = [2,5,2,91,1]
#
# plt.subplot(1, 2, 1)
# plt.plot(x1, y1)
#
# x2 = [5,7,2,1,9]
# y2 = [2,5,3,2,1]
#
# plt.subplot(1, 2, 2)
# plt.plot(x2, y2)
#
# plt.show()

#
# import pandas as pd
#
# df_iris = pd.read_csv('iris.csv')
#
# setosa_sl = []
# setosa_sw = []
# setosa_pl = []
# setosa_pw = []
#
# virginica_sl = []
# virginica_sw = []
# virginica_pl = []
# virginica_pw = []
#
# versicolor_sl = []
# versicolor_sw = []
# versicolor_pl = []
# versicolor_pw = []
#
# for idx in df_iris.index:
#     if df_iris.loc[idx, 'species'] == 'setosa':
#         setosa_sl.append(df_iris.loc[idx, 'sepal_length'])
#         setosa_sw.append(df_iris.loc[idx, 'sepal_width'])
#         setosa_pl.append(df_iris.loc[idx, 'petal_length'])
#         setosa_pw.append(df_iris.loc[idx, 'petal_width'])
#
# for idx in df_iris.index:
#     if df_iris.loc[idx, 'species'] == 'virginica':
#         virginica_sl.append(df_iris.loc[idx, 'sepal_length'])
#         virginica_sw.append(df_iris.loc[idx, 'sepal_width'])
#         virginica_pl.append(df_iris.loc[idx, 'petal_length'])
#         virginica_pw.append(df_iris.loc[idx, 'petal_width'])
#
# for idx in df_iris.index:
#     if df_iris.loc[idx, 'species'] == 'versicolor':
#         versicolor_sl.append(df_iris.loc[idx, 'sepal_length'])
#         versicolor_sw.append(df_iris.loc[idx, 'sepal_width'])
#         versicolor_pl.append(df_iris.loc[idx, 'petal_length'])
#         versicolor_pw.append(df_iris.loc[idx, 'petal_width'])


# plt.subplot(2, 2, 1)
# plt.scatter(setosa_pw, setosa_sl)
# plt.scatter(virginica_pw, virginica_sl)
# plt.scatter(versicolor_pw, versicolor_sl)
#
# plt.subplot(2, 2, 2)
# plt.scatter(setosa_sl, setosa_sw)
# plt.scatter(virginica_sl, virginica_sw)
# plt.scatter(versicolor_sl, versicolor_sw)
#
# plt.subplot(2, 2, 3)
# plt.scatter(setosa_pw, setosa_pl)
# plt.scatter(virginica_pw, virginica_pl)
# plt.scatter(versicolor_pw, versicolor_pl)
#
# plt.subplot(2, 2, 4)
# plt.scatter(setosa_sw, setosa_pw)
# plt.scatter(virginica_sw, virginica_pw)
# plt.scatter(versicolor_sw, versicolor_pw)




# plt.show()

# zad 2 stwórz wykres liniowy kursu, zaznacz czerwona obwódką najniższy kurs,
# zaznacz zieloną obwódką najwyższy kurs, markery jako kółka
# uwzględnij sytuację jeśli najniższy lub najwyższy kurs wystąpi kilka razy
#
# df_kurs = pd.read_csv('kursy-EUR2.csv', sep=';', decimal=',')
# # print(df_kurs)
#
# kupno = []
# sprzedaz = []
# for idx in df_kurs.index:
#     kupno.append(float(df_kurs.loc[idx, 'Kupno']))
#     sprzedaz.append(float(df_kurs.loc[idx, 'Sprzedaż']))
#
#
#
# kupno_max = {}
# kupno_min = {}
# sprzedaz_max = {}
# sprzedaz_min = {}
#
# for idx in df_kurs.index:
#     if df_kurs.loc[idx, 'Kupno'] == df_kurs['Kupno'].max():
#         kupno_max.update({idx : df_kurs.loc[idx, 'Kupno']})
#     if df_kurs.loc[idx, 'Kupno'] == df_kurs['Kupno'].min():
#         kupno_min.update({idx : df_kurs.loc[idx, 'Kupno']})
#     if df_kurs.loc[idx, 'Sprzedaż'] == df_kurs['Sprzedaż'].max():
#         sprzedaz_max.update({idx : df_kurs.loc[idx, 'Sprzedaż']})
#     if df_kurs.loc[idx, 'Sprzedaż'] == df_kurs['Sprzedaż'].min():
#         sprzedaz_min.update({idx : df_kurs.loc[idx, 'Sprzedaż']})
#
#
# plt.scatter(kupno_max.keys(), kupno_max.values(), marker='o', c='green')
# plt.scatter(sprzedaz_max.keys(), sprzedaz_max.values(), marker='o', c='green')
# plt.scatter(kupno_min.keys(), kupno_min.values(), marker='o', c='red')
# plt.scatter(sprzedaz_min.keys(), sprzedaz_min.values(), marker='o', c='red')
#
# plt.plot(kupno)
# plt.plot(sprzedaz)
# plt.show()

#
# size = [1,50,20,10,20]
# color = ['pink', 'red', 'brown', 'black', 'magenta']

# plt.scatter(x1, y1, s=size, c=color)
# plt.show()

# x = ['Audi', 'BMW', "Mercedes", 'Fiat', 'Ford']
# y = [5, 2, 7, 8, 13]
#
# plt.bar(x, y, color='r', width=0.5) # domyślnie width=0.8
#
# plt.show()
#
# data = [20, 20, 20, 18, 19, 17, 18, 17, 16, 18, 10, 19, 21, 22, 22, 14, 15, 14, 17, 17]
#
# plt.hist(data)
# plt.show()

# owoce = ['jabłko', 'banan', 'gruszka', 'arbuz', 'kiwi', 'pomidor']
# color = ['g', 'y', 'g', 'pink', 'g', 'r']
# procenty = [10, 20, 50, 5, 7, 8]
#
# exp = [0.1, 0, 0, 0, 0, 0]
#
# plt.pie(procenty, labels=owoce, colors=color, explode = exp, shadow = True)
# plt.legend()
# # plt.savefig('moje')
# plt.show()
#
# rng = np.random.RandomState(0)
# x = rng.randn(100)
# y = rng.randn(100)
# colors = rng.rand(100)
# sizes = 1000 * rng.rand(100)
# print(sizes)
#
# plt.scatter(x, y, c=colors, s=sizes, alpha = 0.5)
# plt.colorbar()
# plt.show()
#
# x = [0,4,3,2,10]
# y = [6,0,2,10,4]
#
# x = []
# y = []
#
# # plt.scatter(x,y)
# # plt.pause(1)
# # plt.scatter(y,x)
# #
# # plt.show()
#
# #zad 1 co sekundę losuj nowy x i y i wyrysuj 10 takich punktów
#
# counter = 0
# while counter < 10:
#     x.append(random.randint(0, 10))
#     y.append(random.randint(0, 10))
#     plt.scatter(x, y)
#     plt.pause(1)
#     # plt.scatter(y, x)
#     counter +=1
#
# plt.show()

# spychacz
# Wyświetlamy spychacz oraz 5 punktów
# G - ruch o jedno pole, L - obrót w lewo o 90 stopni, R - obrót w prawo
# Wyświetl animację poruszania się spychacza wraz z pozostawionym śladem
# Wypisz komunikat Wygrał/Przegrał

target_list = []
class Target:
    def __init__(self):
        self.x = random.randint(1, 9)
        self.y = random.randint(1, 9)
        target_list.append(self)

class Spychacz:
    def __init__(self):
        self.x = 5
        self.y = 5
        self.orientation = 1

T1 = Target()
T2 = Target()
T3 = Target()
T4 = Target()
T5 = Target()

Spychacz = Spychacz()


# counter = 1
# while counter < 5:
#     T1 = Target()
#     counter += 1


boundary1 = [0, 0]
boundary2 = [0, 10]
boundary3 = [10, 10]
boundary4 = [10, 0]

plt.ion()

plt.figure(figsize=(8, 8))
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

plt.show()

# zad 1 - określ najkrótszą możliwą ścieżkę tak by zebrać wszystkie punkty. Wypisz rozwiązanie. (Dijkstra)
# zad 2 - dodaj kontener, zrób algorytm do wepchnięcia ich do kontenera, nie można pchać dwóch kul naraz




