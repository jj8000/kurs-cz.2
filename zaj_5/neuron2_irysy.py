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

import matplotlib.pyplot as plt

class Neuron:
    def __init__(self, nastawienie, rodzaj, w1, w2, w3):
        self.nastawienie = nastawienie
        self.rodzaj = rodzaj
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3
        if nastawienie not in ['opt', 'pes']:
            raise TypeError
        if rodzaj not in ['u', 'b']:
            raise TypeError

    def klasyfikacja(self, species):
        if species == 'setosa':
            return self.w1
        elif species == 'virginica':
            return self.w2
        elif species == 'versicolor':
            return self.w3
        else:
            raise NotImplemented

    def net(self, x, y):
        return self.w1*x + self.w2*y + self.w3*1

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
    def __init__(self, x, y, decyzja1, decyzja2):
        self.x = float(x)
        self.y = float(y)
        self.decyzja1 = decyzja1
        self.decyzja2 = decyzja2
        self.otrzymana1 = None
        self.otrzymana2 = None
        lista_danych.append(self)


    def __repr__(self):
        return f'({self.x}, {self.y}, N1_otrzymana: {self.otrzymana1}, N1_oczekiwana: {self.decyzja1}' \
               f', N2_otrzymana: {self.otrzymana2}, N2_oczekiwana: {self.decyzja2})'


Neuron1 = Neuron('opt', 'u', 1, 0, -1) # setosa, virginica, versicolor
Neuron2 = Neuron('pes', 'b', 1, -1, 1)

with open('iris.csv', 'r') as f:
    data = f.readlines()[1:]

for i in data:
    i = i.strip().split(',')
    d = Dana(i[2], i[3], Neuron1.klasyfikacja(i[4]), Neuron2.klasyfikacja(i[4]))

# print(lista_danych)

count = 0
internal_count = 0
licznik_bledow = 0
check = None
while check != True:
    for i in lista_danych:
        count += 1
        net1 = Neuron.net(Neuron1, i.x, i.y)
        net2 = Neuron.net(Neuron2, i.x, i.y)
        i.otrzymana1 = Neuron.wynik(Neuron1, net1)
        i.otrzymana2 = Neuron.wynik(Neuron2, net2)
        if i.otrzymana1 == i.decyzja1 and i.otrzymana2 == i.decyzja2:
            check = True
            continue
        else:
            while bool(i.otrzymana1 == i.decyzja1 and i.otrzymana2 == i.decyzja2) == 0:
                internal_count +=1
                Neuron1.w1 = Neuron1.w1 + (-i.otrzymana1 + i.decyzja1) * i.x
                Neuron1.w2 = Neuron1.w2 + (-i.otrzymana1 + i.decyzja1) * i.y
                Neuron1.w3 = Neuron1.w3 + (-i.otrzymana1 + i.decyzja1) * 1
                Neuron2.w1 = Neuron2.w1 + (-i.otrzymana2 + i.decyzja2) * i.x
                Neuron2.w2 = Neuron2.w2 + (-i.otrzymana2 + i.decyzja2) * i.y
                Neuron2.w3 = Neuron2.w3 + (-i.otrzymana2 + i.decyzja2) * 1
                check = False
                if internal_count > 30:
                    check = True

                    internal_count = 0
                    continue
                break

if check == True:
    print(Neuron1.w1, Neuron1.w2, Neuron1.w3, Neuron2.w1, Neuron2.w2, Neuron2.w3)
    for i in lista_danych:
        print(i)

print(f'ilość iteracji: {count}')

# dane_x = []
# dane_y = []
# for i in lista_danych:
#     dane_x.append(i.x)
#     dane_y.append(i.y)
#
# plt.scatter(dane_x, dane_y)
# plt.grid()
#
#
# x1= -8
# y1 = (- Neuron1.w1*x1 - Neuron1.w3*1)/Neuron1.w2
#
# x2 = 5
# y2 = (- Neuron1.w1*x2 - Neuron1.w3*1)/Neuron1.w2
#
# plt.plot([x1, x2], [y1, y2])
# x3= -8
# y3 = (- Neuron2.w1*x1 - Neuron2.w3*1)/Neuron2.w2
#
# x4 = 5
# y4 = (- Neuron2.w1*x2 - Neuron2.w3*1)/Neuron2.w2
# plt.plot([x3, x4], [y3, y4])
#
# plt.show()