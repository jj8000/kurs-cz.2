# odczytaj plik oceny i przedmioty analogicznie z wykorzystaniem ekstensji
# wypisz wszystkie oceny z matematyki
# wypisz średnią z każdego przedmiotu dla Eweliny Bator
# Kto jest najlepszym uczniem?
# Proporcjonalnie ilość pał/wszytskie oceny - kto wystawił najwięcej pał i z jakiego przedmiotu?


class Uczen:

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


class Przedmiot:

    ekstensja = list()

    def __init__(self, linia):
        dane = linia.strip().split(';')
        self.IDprzedmiotu = dane[0]
        self.nazwaprzedmiotu = dane[1]
        self.nazwisko_naucz = dane[2]
        self.imie_naucz = dane[3]
        Przedmiot.ekstensja.append(self)

    def __repr__(self):
        return f'({self.IDprzedmiotu})'

class Ocena:

    ekstensja = list()

    def __init__(self, linia):
        dane = linia.strip().split(';')
        self.IDucznia = dane[0]
        self.ocena = dane[1]
        self.data = dane[2]
        self.IDprzedmiotu = dane[3]
        Ocena.ekstensja.append(self)

    def __repr__(self):
        return f'({self.ocena}, {self.IDprzedmiotu}, {self.IDucznia}, {self.data})'



def zaladuj_uczniow(plik):

    with open(plik) as f:
        f.readline()

        for linia in f.readlines():
            Uczen(linia)

def zaladuj_przedmioty(plik):

    with open(plik) as f:
        f.readline()

        for linia in f.readlines():
            Przedmiot(linia)

def zaladuj_oceny(plik):

    with open(plik) as f:
        f.readline()

        for linia in f.readlines():
            Ocena(linia)

zaladuj_uczniow('uczniowie.txt')
zaladuj_przedmioty('przedmioty.txt')
zaladuj_oceny('oceny.txt')

# print(Uczen.ekstensja)
# print(Przedmiot.ekstensja)
# print(Ocena.ekstensja)

def oceny_z_przedmiotu():
    lista_ocen = []
    for o in Ocena.ekstensja:
        if o.IDprzedmiotu == '6':
            lista_ocen.append(o.ocena)
    return lista_ocen

# print(oceny_z_przedmiotu())

def id_ucznia(imie: str, nazwisko: str):
    for u in Uczen.ekstensja:
        if u.imie == imie and u.nazwisko == nazwisko:
            return u.IDucznia


# (id_ucznia("Ewelina", "Bator"))

def srednia_ucznia(imie: str, nazwisko: str):
    sum = 0
    count = 0
    for o in Ocena.ekstensja:
        if id_ucznia(imie, nazwisko) == o.IDucznia:
            sum += int(o.ocena)
            count += 1
    return sum/count

print(srednia_ucznia('Ewelina', 'Bator'))

def srednia_ucznia_id(id):
    sum = 0
    count = 0
    for o in Ocena.ekstensja:
        if id == int(o.IDucznia):
            sum += int(o.ocena)
            count += 1
    return sum/count



def srednie_ocen():
    klucze = set()

    for u in Uczen.ekstensja:
        klucze.add(int(u.IDucznia))

    klucze = sorted(klucze)
    # print(klucze)
    wykaz_srednich = {key: srednia_ucznia_id(key) for key in klucze}
    # print(srednie_ocen)



klucze = set()

for u in Uczen.ekstensja:
    klucze.add(int(u.IDucznia))
klucze = sorted(klucze)
# print(klucze)
wykaz_srednich = {key: srednia_ucznia_id(key) for key in klucze}
# print(srednie_ocen)
print(wykaz_srednich)
# najlepsza_srednia()

print(srednia_ucznia_id(33))

najlepszy_uczen = None
start = 0
for x, y in wykaz_srednich.items():

    if y > start:
        start = y
        najlepszy_uczen = x

print(najlepszy_uczen, start)

def id_ucznia(id:int):
    for u in Uczen.ekstensja:
        if int(u.IDucznia) == id:
            return u.nazwisko, u.imie

print(id_ucznia(253))