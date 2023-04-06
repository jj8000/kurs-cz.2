from operator import attrgetter


class Osoba:

    def __init__(self, imie, nazwisko, data_urodzenia):
        self.imie = imie
        self.nazwisko = nazwisko
        self.data_urodzenia = data_urodzenia

    def __repr__(self):
        return f'({self.imie}, {self.nazwisko})'

    def __str__(self):
        return f'({self.imie}, {self.nazwisko})'


o1 = Osoba('Weronika', 'Sałata', '1996-01-01')
o2 = Osoba('Daniela', 'Jankowska', '1998-10-12')
o3 = Osoba('Marzena', 'Por', '2001-05-06')
o4 = Osoba('Jan', 'Kowalski', '2007-07-04')
o5 = Osoba('Tomek', 'Kowalczyk', '2005-02-03')
o6 = Osoba('Damian', 'Staszkiewicz', '1992-10-11')

lista_osob = [o1, o2, o3, o4, o5, o6]

# print(o1.imie, o1.nazwisko)

# for osoba_tmp in lista_osob:
#     print(osoba_tmp)

# print(lista_osob)


# utworz klasę zwierzątko z polami imie wlaściciela, waga, rok_urodzenia
# stwórz 10 obiektów klasy zwierzątko
# wypisz najstarsze i najcięższe zwierzą
# posortuj zwierzątka na liście alfabetycznie po imieniu, w drugiej kolejności po imieniu właściciela

class Zwierzątko:



    def __init__(self, imie, imie_wlasciciela, waga, rok_urodzenia):
        self.imie = imie
        self.imie_wlasciciela = imie_wlasciciela
        self.waga = waga
        self.rok_urodzenia = rok_urodzenia

    def __str__(self):
        return f'({self.imie}, {self.imie_wlasciciela}, {self.waga}, {self.rok_urodzenia})'

    def __repr__(self):
        return f'({self.imie}, {self.imie_wlasciciela})'


z1 = Zwierzątko('Melon', 'Marta', 5.6, '2022')
z2 = Zwierzątko('Oreo', 'Alina', 10.3, '2014')
z3 = Zwierzątko('Mruczek', 'Alfred', 5.2, '2016')
z4 = Zwierzątko('Arbuz', 'Jonasz', 10.0, '2019')
z5 = Zwierzątko('Kabel', 'Janina', 9.6, '2010')
z6 = Zwierzątko('Tadeusz', 'Weronika', 11.8, '2009')
z7 = Zwierzątko('Ryszard', 'Jerzy', 9.1, '2008')
z8 = Zwierzątko('Alcest', 'Alina', 8.2, '2011')
z9 = Zwierzątko('Tutka', 'Anna', 7.9, '2022')
z10 = Zwierzątko('Sami', 'Kazimierz', 7.8, '2022')

lista_z = [z1, z2, z3, z4, z5, z6, z7, z8, z9, z10]
print('')
print(max(lista_z, key = lambda n:n.waga))
print(min(lista_z, key = lambda n:n.rok_urodzenia))
print('''

''')
max_weight = max(lista_z, key=attrgetter('waga'))
print(max_weight)
max_age = min(lista_z, key=attrgetter('rok_urodzenia'))
print(max_age)
print('''

''')
print(sorted(lista_z, key = lambda n:n.imie))
print(sorted(sorted(lista_z, key = lambda n:n.imie_wlasciciela), key = lambda n:n.imie))

#pastebin.com/44SbE0Pm

# print('''class Osoba:

    # def __init__(self, imie, nazwisko, data_urodzenia):
    #     self.imie = imie
    #     self.nazwisko = nazwisko
    #     self.data_urodzenia = data_urodzenia

    # def __repr__(self):
    #     return f'({self.imie}, {self.nazwisko})'

    # def __str__(self):
    #     return f'({self.imie}, {self.nazwisko})'

# o1 = Osoba('Weronika', 'Sałata', '1996-01-01')
# o2 = Osoba('Daniela', 'Jankowska', '1998-10-12')
# o3 = Osoba('Marzena', 'Por', '2001-05-06')
# o4 = Osoba('Jan', 'Kowalski', '2007-07-04')
# o5 = Osoba('Tomek', 'Kowalczyk', '2005-02-03')
# o6 = Osoba('Damian', 'Staszkiewicz', '1992-10-11')

# lista_osob = [o1,o2,o3,o4,o5,o6]
# # print(o1.imie, o1.nazwisko)
# for osoba_tmp in lista_osob:
#     print(osoba_tmp)
# print(lista_osob)

# # zad 1 utworz klase zwierzatko, z polami imie, imie_wlasciela, waga, rok_urodzenia
# # zad 2 stworz 10 obiektow klasy zwierzatko
# # zad 3 wypisz najciezsze i najstarsze zwierze
# # zad 4 posortuj zwierzatka na liscie alfabecznie po imieniu, a w drugiej kolejnosci imieniu wlasciela

class zwierzatko:

    def __init__(self, imie, imie_wlasciciela, rok_urodzenia, waga):
        self.imie = imie
        self.imie_wlasciciela = imie_wlasciciela
        self.rok_urodzenia = rok_urodzenia
        self.waga = waga

    def __str__(self):
        return f'{self.imie}'

    def __repr__(self):
        return f'{self.imie}'


z1 = zwierzatko('As', 'Pawel', 2020, 2)
z2 = zwierzatko('Burek', 'Basia', 2000, 4)
z3 = zwierzatko('Julek', 'Kamil', 2021, 2.5)
z4 = zwierzatko('Julian', 'Piotr', 2017, 6)
z5 = zwierzatko('Ruby', 'Piotr', 2015, 7)
z6 = zwierzatko('Czika', 'Weronika', 2013, 12)
z7 = zwierzatko('Wafel', 'Marzena', 2012, 2)
z8 = zwierzatko('Tofik', 'Ola', 2002, 1.5)
z9 = zwierzatko('Blanka', 'Marek', 2000, 5)
z0 = zwierzatko('Azor', 'Darek', 1995, 9)

lista_zwierzat = [z1,z2,z3,z4,z5,z6,z7,z8, z9, z0]

najciezsze = lista_zwierzat[0]
najstarsze = lista_zwierzat[0]

for z_tmp in lista_zwierzat:
    if najstarsze.rok_urodzenia > z_tmp.rok_urodzenia:
        najstarsze = z_tmp
    if najciezsze.waga < z_tmp.waga:
        najciezsze = z_tmp

print(f'Najciezsze: {najciezsze}, Najstarsze: {najstarsze}')

lista_posortowane = list()

while len(lista_zwierzat) > 0:
    min = lista_zwierzat[0]

    for z_tmp in lista_zwierzat:
        if min.imie > z_tmp.imie:
            min = z_tmp
        elif min.imie == z_tmp.imie and min.imie_wlasciciela == z_tmp.imie_wlasciciela:
            min = z_tmp

    lista_posortowane.append(min)
    lista_zwierzat.remove(min)

print(lista_posortowane)




