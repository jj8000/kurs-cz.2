# 1. Klasa Neuron (nastawienie, liczenie NET, rodzaj neuronu)
# 2. Klasa dana (zawiera info o wyniku)
# 3. Dane odczytujemy z pliku
# 4. Mechanizm załadowania danych, klasyfikacji, uczenia
#
# -> Przechodzimy po każdej danej treningowej, dokonujemy klasyfikacji, weryfikujemy czy poprawna klasa
# jeśli tak, przechodzimy dalej, jeśli nie, uczymy do skutku. Całość procesu uczenia wykonujemy tak długo, aż wszystkie
# dane zostaną dobrze sklasyfikowane bez żadnego kroku uczenia.
# Uwagi: - wagi są wspólne dla wszystkich danych; wagi są 3: x, y, stała
# wagi początkowe losowe

import random

class Neuron:
    def __init__(self, nastawienie, rodzaj):
        self.nastawienie = nastawienie
        self.rodzaj = rodzaj
        if nastawienie not in ['opt', 'pes']:
            raise TypeError
        if rodzaj not in ['u', 'b']:
            raise TypeError

    def net(self, w1, w2, w3, x, y):
        return w1*x + w2*y + w3*1

    def wynik(self, net: float or int):
        if self.rodzaj == 'u':
            if net > 0:
                return 1
            elif net < 0:
                return 0
            else:
                if self.nastawienie == 'opt':
                    return 1
                return 0
        if self.rodzaj == 'b':
            if net > 0:
                return 1
            elif net < 0:
                return -1
            else:
                if self.nastawienie == 'opt':
                    return 1
                return -1

lista_danych = []

class Dana:
    def __init__(self, x, y, decyzja):
        self.x = x
        self.y = y
        self.decyzja = decyzja
        self.otrzymana = None
        lista_danych.append(self)

    def __repr__(self):
        return f'({self.x}, {self.y}, {self.otrzymana}, {self.decyzja})'

Neuron = Neuron('pes', 'u')

with open('zad2.txt', 'r') as f:
    data = f.readlines()[1:]

for i in data:
    i = i.strip().split(';')
    d = Dana(int(i[0]), int(i[1]), int(i[2]))
    # print(d.x, d.y, d.decyzja)

# print(lista_danych)

w1 = random.randint(-2, 2)
w2 = random.randint(-2, 2)
w3 = random.randint(-2, 2)

check = None
while check != True:
    for i in lista_danych:
        net = Neuron.net(w1, w2, w3, int(i.x), int(i.y))
        if Neuron.wynik(net) == i.decyzja:
            check = True
            i.otrzymana = Neuron.wynik(net)
            continue
        elif Neuron.wynik(net) != i.decyzja:
            w1 = w1 + (-Neuron.wynik(net) + i.decyzja) * i.x
            w2 = w2 + (-Neuron.wynik(net) + i.decyzja) * i.y
            w3 = w3 + (-Neuron.wynik(net) + i.decyzja) * 1
            check = False
            break

if check == True:
    print(w1, w2, w3)
    for i in lista_danych:
        print(i)
