class Obserwacja:

    ekstencja = list()

    def __init__(self, data):
        dane = data.strip().split(';')
        self.x = int(dane[0])
        self.y = int(dane[1])
        self.oczekiwana = int(dane[2])
        Obserwacja.ekstencja.append(self)

    def __str__(self):
        return f'X: {self.x}, Y: {self.y}, Dec: {self.oczekiwana}'

    @classmethod
    def import_from_file(cls, nazwa_pliku):
        f = open(nazwa_pliku, 'r')
        f.readline()
        dane = f.readlines()
        for dana in dane:
            Obserwacja(dana)

Obserwacja.import_from_file('zad2.txt')

# for obs in Obserwacja.ekstencja:
#     print(obs)

import random as r

class Neuron:

    def __init__(self):
        self.w1 = r.randint(-2,2)
        self.w2 = r.randint(-2, 2)
        self.w3 = r.randint(-2,2)
        self.rodzaj_neuronu = 'u'
        self.nastawienie_pozytywne = False
        self.tempo_uczenia = 1

    def zaladuj_dana(self, obserwacja):
        self.bierzaca_dana = obserwacja

    def oblicz_NET(self):
        self.net = self.w1 * self.bierzaca_dana.x + self.w2 * self.bierzaca_dana.y + self.w3 * 1

    def oblicz_decyzja(self):
        if self.rodzaj_neuronu == 'bi':
            if self.nastawienie_pozytywne:
                if self.net >= 0:
                    self.decyzja = 1
                else:
                    self.decyzja = -1
            else:
                if self.net > 0:
                    self.decyzja = 1
                else:
                    self.decyzja = -1
        else:
            if self.nastawienie_pozytywne:
                if self.net >= 0:
                    self.decyzja = 1
                else:
                    self.decyzja = 0
            else:
                if self.net > 0:
                    self.decyzja = 1
                else:
                    self.decyzja = 0

    def korekta_wag(self):
        self.w1 += self.tempo_uczenia * (self.bierzaca_dana.oczekiwana - self.decyzja) * self.bierzaca_dana.x
        self.w2 += self.tempo_uczenia * (self.bierzaca_dana.oczekiwana - self.decyzja) * self.bierzaca_dana.y
        self.w3 += self.tempo_uczenia * (self.bierzaca_dana.oczekiwana - self.decyzja) * 1

    def __str__(self):
        return f'W1: {self.w1}, W2: {self.w2}, W3: {self.w3}'

neuron = Neuron()
klasyfikacja = 1

while klasyfikacja:
    klasyfikacja = 0
    for obs in Obserwacja.ekstencja:
        neuron.zaladuj_dana(obs)
        neuron.oblicz_NET()
        neuron.oblicz_decyzja()
        while neuron.decyzja != obs.oczekiwana:
            klasyfikacja += 1
            neuron.korekta_wag()
            neuron.oblicz_NET()
            neuron.oblicz_decyzja()

for obs in Obserwacja.ekstencja:
    neuron.zaladuj_dana(obs)
    neuron.oblicz_NET()
    neuron.oblicz_decyzja()
    print(obs, neuron.decyzja)

print(neuron)