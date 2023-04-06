class Dziecko:
    spis_dzieci = list()

    def __init__(self, linia_z_danymi):  # Pesel;Nazwisko;Imie;Plec;Wiek
        dane = linia_z_danymi.strip().split(';')
        self.pesel = dane[0]
        self.nazwisko = dane[1]
        self.imie = dane[2]
        self.plec = dane[3]
        self.wiek = int(dane[4])
        self.czy_przyjety = False

        Dziecko.spis_dzieci.append(self)

    @classmethod
    def import_z_pliku(cls, nazwa_pliku):     # zaladuj dane i utworz obiekt
        with open(nazwa_pliku, 'r') as file:
            file.readline()
            for linia in file.readlines():
                Dziecko(linia)

    def __str__(self):
        return f'Dziecko: {self.pesel}, {self.imie}, {self.nazwisko}'

    def __repr__(self):
        return f'{self.pesel}'

    @classmethod
    def znajdz_dziecko_po_peselu(cls, pesel):
        for dziecko_tmp in Dziecko.spis_dzieci:
            if dziecko_tmp.pesel == pesel:
                return dziecko_tmp

    @classmethod
    def zwroc_dzieci_odrzucone(cls):
        lista_odrzuconych = list()
        for dziecko_tmp in Dziecko.spis_dzieci:
            if not dziecko_tmp.czy_przyjety:
                lista_odrzuconych.append(dziecko_tmp)

        return lista_odrzuconych


class Przedszkole:
    spis_przedszkoli = list()

    def __init__(self, linia_z_danymi):
        dane = linia_z_danymi.strip().split(';')
        self.id_przedszkola = dane[0]
        self.nazwa = dane[1]
        self.liczba_miejsc = int(dane[2])
        self.przyjeci = list()

        Przedszkole.spis_przedszkoli.append(self)

    @classmethod
    def import_z_pliku(cls, nazwa_pliku):
        with open(nazwa_pliku, 'r') as file:
            file.readline()
            for linia in file.readlines():
                Przedszkole(linia)

    def __str__(self):
        return f'Przedszkole: {self.nazwa}'

    def __repr__(self):
        return f'{self.nazwa}'

    def przyjmij_dziecko(self, dziecko):
        self.przyjeci.append(dziecko)
        dziecko.czy_przyjety = True

    @classmethod
    def znajdz_przedszkole_po_id(cls, id_przedszkola):
        for przedszkole_tmp in Przedszkole.spis_przedszkoli:
            if przedszkole_tmp.id_przedszkola == id_przedszkola:
                return przedszkole_tmp

    def czy_wolne_miejsce(self):
        return len(self.przyjeci) < self.liczba_miejsc

    @classmethod
    def wypisz_przedszkola_z_wolnymi_miejscami(cls):
        for przedszkole_tmp in Przedszkole.spis_przedszkoli:
            if przedszkole_tmp.czy_wolne_miejsce():
                print(
                    f'{przedszkole_tmp}, miejsc: {przedszkole_tmp.liczba_miejsc}, przyjetych: {len(przedszkole_tmp.przyjeci)}')

    @classmethod
    def znajdz_przedszkole_po_nazwie(cls, nazwa):
        for przedszkole_tmp in Przedszkole.spis_przedszkoli:
            if przedszkole_tmp.nazwa == nazwa:
                return przedszkole_tmp

    @classmethod
    def wypisz_przyjetych(cls, przedszkole):
        for dziecko_tmp in przedszkole.przyjeci:
            print(dziecko_tmp)


class Preferencja:
    spis_preferencji = list()

    def __init__(self, linia_z_danymi):
        dane = linia_z_danymi.strip().split(';')
        self.dziecko = Dziecko.znajdz_dziecko_po_peselu(dane[0])
        self.numer_preferencji = dane[1]
        self.przedszkole = Przedszkole.znajdz_przedszkole_po_id(dane[2])

        Preferencja.spis_preferencji.append(self)

    @classmethod
    def import_z_pliku(cls, nazwa_pliku):
        with open(nazwa_pliku, 'r') as file:
            file.readline()
            for linia in file.readlines():
                Preferencja(linia)

    def __str__(self):
        return f'{self.numer_preferencji} dla {self.dziecko.pesel} do {self.przedszkole.nazwa}'

    @classmethod
    def przydziel_dziecku_przedszkole(cls):
        for preferencja_tmp in Preferencja.spis_preferencji:
            if preferencja_tmp.przedszkole.czy_wolne_miejsce() and not preferencja_tmp.dziecko.czy_przyjety:
                preferencja_tmp.przedszkole.przyjmij_dziecko(preferencja_tmp.dziecko)


Dziecko.import_z_pliku('DZIECI.TXT')
Przedszkole.import_z_pliku('PRZEDSZKOLA.TXT')
Preferencja.import_z_pliku('PREFERENCJE.TXT')

Preferencja.przydziel_dziecku_przedszkole()

print(len(Dziecko.zwroc_dzieci_odrzucone()))

# Przedszkole.wypisz_przedszkola_z_wolnymi_miejscami()
Przedszkole.wypisz_przyjetych(Przedszkole.znajdz_przedszkole_po_nazwie('Przedszkole nr 51'))

