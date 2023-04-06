
class Administrator:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.liczba_pkt = 0

    def get_admin_id(self):
        return self.imie[1] + self.nazwisko[1] + '#' + str(self.liczba_pkt)

    def __str__(self):
        return 'Admin: ' + self.get_admin_id()


class Czlonek:

    def __init__(self, login, haslo):
        self.login = login
        self.haslo = haslo
        self.aktywny = True

    def __str__(self):
        return self.login

    def __repr__(self):
        return self.login


class Grupa:

    def __init__(self, admin, max_ilosc_czlonkow):
        self.Admin = admin
        self.max_ilosc_czlonkow = max_ilosc_czlonkow
        self.lista_czlonkow = list()
        self.lista_czlonkow.append(self.Admin)

    def dodaj_czlonka(self, nowy_czlonek):
        if self.czy_mozna_dodac():
            self.lista_czlonkow.append(nowy_czlonek)

    def czy_mozna_dodac(self):
        return len(self.lista_czlonkow) < self.max_ilosc_czlonkow

    def pokaz_czlonkow(self):
        for czlonek in self.lista_czlonkow:
            print(czlonek)

    def walidacja_niku_czlonka(self):
        # czlonek musi miec nick z duzej litery
        poprawne = list()
        for czlonek in self.lista_czlonkow:
            if isinstance(czlonek, Administrator):
                poprawne.append(czlonek)
            elif czlonek.login[0].isupper():
                poprawne.append(czlonek)
        self.lista_czlonkow = poprawne

    def filtr_haslo_7(self):
        lista_czlonkow = list()

        for czlonek in self.lista_czlonkow:
            if isinstance(czlonek, Czlonek) and czlonek.haslo[0] == '7':
                lista_czlonkow.append(czlonek)

        return lista_czlonkow


admin1 = Administrator('Wojtek', 'Czajkowski')

grupa_aa = Grupa(admin1, 5)

grupa_aa.dodaj_czlonka(Czlonek('jasio01', '723456789'))
grupa_aa.dodaj_czlonka(Czlonek('Jasio02', '765432'))
grupa_aa.dodaj_czlonka(Czlonek('jasio03', '987654321'))
grupa_aa.dodaj_czlonka(Czlonek('Jasio04', '76543222'))
grupa_aa.dodaj_czlonka(Czlonek('Jasio05', '12345123412'))
grupa_aa.dodaj_czlonka(Czlonek('Jasio06', '111111111'))

grupa_aa.pokaz_czlonkow()
# grupa_aa.walidacja_niku_czlonka()

print("Po walidacji:")
grupa_aa.pokaz_czlonkow()

print(grupa_aa.filtr_haslo_7())

