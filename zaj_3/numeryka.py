import numpy as np
from numpy import random

# wylosuj tabl. z wartościami od -10 do 10, (10 na 10)
# wskaż wartość najczęściej występującą

tablica = np.random.randint(-1000, 1001, size=(10, 10))
print(tablica)

# lista = tablica.tolist()
# lista2 = []
# for row in lista:
#     for i in row:
#         lista2.append(i)
#
# print(lista2)
#
# liczebnosc = {}
# for i in lista2:
#     n = lista2.count(i)
#     liczebnosc.update({i: n})
#
# wynik = sorted(liczebnosc.items(), key = lambda x: x[1], reverse = True)
#
# print(wynik)
#
# tab1d = tablica.reshape(100)
# print(tab1d)
#
# print(np.bincount(tab1d+11).argmax()-11)
#
#
# print(np.sort(tablica))
# print()
# print(np.sort(tablica, axis=0))

# wskaż, w którym wierszu suma elementów jest największa

print(np.sum(tablica, axis=1))
print(np.sum(tablica, axis=1).argmax())
print(np.sum(tablica, axis=1).max())

# zad 6 wylosuj tablicę 30 elementów z wartościami parzystymi od -50 do 50

# lista = []
# while len(lista) < 31:
#     i = np.random.randint(-50, 51)
#     if i % 2 == 0:
#         lista.append(i)
#
# print(lista)
# tablica = np.array(lista)
# print(tablica)

# zad 6 wskaż medianę z tablicy
# zad 7 nałóż filtr, który przepuści tylko liczby jednocyfrowe

# print(np.median(tablica))
# filtr = np.absolute(tablica) < 10
# print(tablica[filtr])

# zad 8 dla tablicy z zadania 5 wskaż pozycję
# elementu którego suma cyfr jest największa
# zad 9 stwórz tablice (n x n), wypełnioną samymi zerami,
# wstaw do niej na losowe pozycje dokładnie 30% jedynek (zaokr.)

def SumofDigits(arg: int):
    sum = 0
    arg = str(arg)
    arg = arg.lstrip('-')
    for i in arg:
        sum += int(i)
    return sum

print(SumofDigits(-9780652))

print(tablica)
tablica2 = tablica.reshape(100)
for n in tablica2:
    n = SumofDigits(n)


print()
print(tablica)
print(tablica2)








