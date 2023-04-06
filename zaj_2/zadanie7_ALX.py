

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
        self.NazwaPrzedmiotu = dane[1]
        self.Nazwisko_naucz = dane[2]
        self.Imie_naucz = dane[3]
        Przedmiot.ekstensja.append(self)

    def __repr__(self):
        return f'({self.NazwaPrzedmiotu})'


class Ocena:
    ekstensja = list()

    def __init__(self, linia):
        dane = linia.strip().split(';')
        self.IDucznia = dane[0]
        self.Ocena = dane[1]
        self.Data = dane[2]
        self.IDprzedmiotu = dane[3]
        Ocena.ekstensja.append(self)

    def __repr__(self):
        return f'({self.Ocena})'


def zaladuj_dane_uczniowie(plik):
    with open(plik) as f:
        f.readline()

        for linia in f.readlines():
            Uczen(linia)


def zaladuj_dane_przedmiot(plik):
    with open(plik) as f:
        f.readline()

        for linia in f.readlines():
            Przedmiot(linia)


def zaladuj_dane_oceny(plik):
    with open(plik) as f:
        f.readline()

        for linia in f.readlines():
            Ocena(linia)


zaladuj_dane_uczniowie('uczniowie.txt')
zaladuj_dane_przedmiot('przedmioty.txt')
zaladuj_dane_oceny('oceny.txt')



# 2. Wypisz wszystkie oceny z matematyki

szukany_przedmiot = 'matematyka'
id_przedmiot = 0

for p in Przedmiot.ekstensja:
    if p.NazwaPrzedmiotu == szukany_przedmiot:
        id_przedmiot = p.IDprzedmiotu

print(id_przedmiot)

for o in Ocena.ekstensja:
    if o.IDprzedmiotu == id_przedmiot:
        print(o.Ocena, o.Data, o.IDprzedmiotu)



# 3. Wypisz srednia z kazdego przedmiotu dla Ewelina Bator

id_szukanego_ucznia = 0

for u in Uczen.ekstensja:
    if u.imie == 'Ewelina' and u.nazwisko == 'Bator':
        id_szukanego_ucznia = u.IDucznia

print(id_szukanego_ucznia)

for p in Przedmiot.ekstensja:
    suma = 0
    ilosc = 0

    for o in Ocena.ekstensja:
        if o.IDprzedmiotu == p.IDprzedmiotu and o.IDucznia == id_szukanego_ucznia:
            ilosc += 1
            suma += int(o.Ocena)
    if ilosc > 0:
        print(p.NazwaPrzedmiotu, (suma/ilosc))
    else:
        print(p.NazwaPrzedmiotu, 'brak ocen')



# 5. Proporcjonalnie ilosc_pał(1)/wszystkie_oceny  - kto wystawił najwiecej pał(1) i z jakiego przedmiotu?


dict_przedmiot_stosunek = dict()

for p in Przedmiot.ekstensja:
    ilosc_jedynek = 0
    ilosc_wszystkich_ocen = 0

    for o in Ocena.ekstensja:
        if o.IDprzedmiotu == p.IDprzedmiotu:
            if int(o.Ocena) == 1:
                ilosc_jedynek += 1
            ilosc_wszystkich_ocen += 1

    dict_przedmiot_stosunek[p.IDprzedmiotu] = ilosc_jedynek / ilosc_wszystkich_ocen

print(dict_przedmiot_stosunek)

# I SPOSOB NA WYCIAGNIECIE MAKSYMALNEGO PROCENTA:
# id_max = 0
# max_val = 0
# for k, v in dict_przedmiot_stosunek.items():
#     if v > max_val:
#         max_val = v
#         id_max = k

# II SPOSOB NA WYCIAGNIECIE MAKSYMALNEGO PROCENTA:

id_max = max(dict_przedmiot_stosunek, key=dict_przedmiot_stosunek.get)
for p in Przedmiot.ekstensja:
    if p.IDprzedmiotu == id_max:
        print(p.NazwaPrzedmiotu)


