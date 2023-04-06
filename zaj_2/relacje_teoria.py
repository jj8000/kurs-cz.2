
class KlasaB:
    def __init__(self):
        self.tytul = 'moja klasa B'
        self.ilosc = 50
        self.klasaA = None

    def dodaj_klasaA(self, ka):
        if self.klasaA == None:
            self.klasaA = ka
            ka.dodaj_klasaB(self)

    def __str__(self):
        return f'{self.tytul}'


class KlasaA:

    def __init__(self):
        self.info = 'podstawowe'
        self.klasaB = None

    def dodaj_klasaB(self, kb):
        if self.klasaB == None:
            self.klasaB = kb
            kb.dodaj_klasaA(self)

    def __str__(self):
        return f'{self.info} {self.klasaB}'


ka1 = KlasaA()
kb1 = KlasaB()

kb1.dodaj_klasaA(ka1)

print(ka1)


