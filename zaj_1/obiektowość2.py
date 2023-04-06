# utwórz listę wsz. ob. kl. uczeń
# Wypisz uczniów mieszkających na ul. Wyzwolenia
# Wypisz klasy oraz ilość uczniów w danej klasie
# Utwórz słownik, gdzie kluczem będzie numer klasy, a wartościami lista obiektów klasy uczeń (z tej klasy)

class Uczen:
    def __init__(self, IDucznia, nazwisko, imie, ulica, dom, IDklasy):
        self.IDucznia = IDucznia
        self.nazwisko = nazwisko
        self.imie = imie
        self.ulica = ulica
        self.dom = dom
        self.IDklasy = IDklasy

    def __repr__(self):
        return f'({self.IDucznia}, {self.nazwisko})'

lista_uczniow = []
with open('uczniowie.txt', 'r') as f:
    data = f.readlines()

    for i in data:
        i = i.strip()
        lista_uczniow.append(i)

l2=[]
for u in lista_uczniow:
    u2 = u.split(';')
    l2.append(u2)

# print(lista_uczniow)
# print(l2)

object_list = []

for i in l2:
       u = Uczen(i[0], i[1], i[2], i[3], i[4], i[5])
       object_list.append(u)

object_list.pop(0)

print(object_list)

#2

for u in object_list:
    if u.ulica == 'Wyzwolenia':
        print(u)

#3

klasy = set()

for u in object_list:
    klasy.add(u.IDklasy)


liczebnosc_klas = {key: 0 for key in klasy}

for u in object_list:
    if u.IDklasy in liczebnosc_klas.keys():
        liczebnosc_klas[u.IDklasy] += 1

print(liczebnosc_klas)

dzienniki = {key: [] for key in klasy}
print(dzienniki)

for u in object_list:
    if u.IDklasy in dzienniki.keys():
        dzienniki[u.IDklasy].append(u)

print(dzienniki)

#pastebin.com/E9Jy4TWj

'''class Uczen:

    ekstensja = list()

    def __init__(self, linia):
        dane = linia.strip().split(';')
        self.IDucznia = dane[0]
        self.nazwisko = dane[1]
        self.imie = dane[2]
        self.ulica = dane[3]
        self.dom = dane[4]
        self.IDklasy = dane[5]
        Uczen.ekstensja.append(self)

    def __repr__(self):
        return f'({self.imie}, {self.nazwisko})'

def zaladuj_dane(plik):

    with open(plik) as f:
        f.readline()

        for linia in f.readlines():
            Uczen(linia)

zaladuj_dane('uczniowie.txt')

# for u in Uczen.ekstensja:
#     if u.ulica == 'Wyzwolenia':
#         print(u.imie)

def slownik_klasa_licznosc():
    slownik_klasa_licznosc = dict()

    for u in Uczen.ekstensja:
        if u.IDklasy not in slownik_klasa_licznosc.keys():
            slownik_klasa_licznosc[u.IDklasy] = 0
        slownik_klasa_licznosc[u.IDklasy] += 1

    return slownik_klasa_licznosc


def slownik_klasa_uczniowie():
    slownik_klasa_uczniowie = dict()

    for u in Uczen.ekstensja:
        if u.IDklasy not in slownik_klasa_uczniowie.keys():
            slownik_klasa_uczniowie[u.IDklasy] = list()
        slownik_klasa_uczniowie[u.IDklasy].append(u)

    return slownik_klasa_uczniowie

for k, v in slownik_klasa_uczniowie().items():
    print(k, v)

# 1. Utworz liste wsyztskich obiektow klasy uczen
# 2. Wypisz uczniow ktorzy mieszkaja na ulicy wyzwolenia
# 3. Wypisz klasy oraz ilosc uczniow w danej klasie
# 4. Utworz slownik, gdzie kluczem bedzie numer klasy, a wartosciami lista obiektow klasy uczen (z tej klasy)




# slownik['1a'] = slownik['1a'] + 2'''