# 1. Losujemy 200 obserwacji, plansza od -100 na 100 po x, y
# 2. k - liczba grup
# 3. Losujemy centroidy
# 4. Przydzielamy do grup
# 5. Wyznaczamy nowe lokalizacje centroidów
# 6. Do momentu aż punkty zmieniają grupy powielamy pkt. 4-6
# 7. Wyświetl reprezentacje przynależnych punktów do grup

import random
import matplotlib.pyplot as plt
import math

obserwacje = []
centroidy = []


class Obserwacja:
    def __init__(self):
        self.x = random.randint(-100, 100)
        self.y = random.randint(-100, 100)
        self.grupa = None
        obserwacje.append(self)


class Centroida:
    def __init__(self, id):
        self.x = random.randint(-100, 100)
        self.y = random.randint(-100, 100)
        self.id = id
        centroidy.append(self)

    def __repr__(self):
        return f'{self.id}, {self.x}, {self.y}'


k = 2  # liczba grup

id_count = 0
for i in range(k):
    id_count += 1
    c = Centroida(id_count)

# print(centroidy)

for i in range(100):
    o = Obserwacja()

for i in obserwacje:
    plt.scatter(i.x, i.y, color='b')

for i in centroidy:
    plt.scatter(i.x, i.y, color='r')


def odleglosc(obserwacja, centroida):
    return math.sqrt((pow(centroida.x - obserwacja.x, 2)) + (pow(centroida.y - obserwacja.y, 2)))


def przydzial():
    for o in obserwacje:
        odleglosci = {c.id: odleglosc(o, c) for c in centroidy}
        najblizsza_centroida = min(odleglosci, key=odleglosci.get)
        o.grupa = najblizsza_centroida



def nowe_lokalizacje():
    for c in centroidy:
         c.x = (sum([o.x for o in obserwacje if o.grupa == c.id])/len([o.x for o in obserwacje if o.grupa == c.id]))
         c.y = (sum([o.y for o in obserwacje if o.grupa == c.id])/len([o.y for o in obserwacje if o.grupa == c.id]))

przydzial()
for i in range(k):
    for o in obserwacje:
        plt.scatter(o.x, o.y if o.grupa == i)

nowe_lokalizacje()

plt.show()

# dodaj 3 nowe metryki (cesarza, rzeki?)
# neurony pd - zrobić sieć 2-3-3 lub 3-3-2













