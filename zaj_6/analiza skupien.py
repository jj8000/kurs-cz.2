import random
import matplotlib.pyplot as plt

ilosc_obserwacji = 30
# wymiar_jednostki = 1
# ilosc_klas = 3
random.seed(6)

class Obserwacja:

    ekstensja = []
    def __init__(self, x, y):
        self.x = x
        self.y = y
        Obserwacja.ekstensja.append(self)
        self.klasa = 1


    def __repr__(self):
        return f'({self.x}, {self.y}, {self.klasa})'


for i in range(ilosc_obserwacji):
    x = random.randint(0, 9) + random.randint(1, 9)/10
    y = random.randint(0, 9) + random.randint(1, 9)/10
    o = Obserwacja(x, y)

plt.xticks([i for i in range(11)])
plt.yticks([i for i in range(11)])
plt.grid()

temp = []

while len(Obserwacja.ekstensja) != 0:

    for o in Obserwacja.ekstensja:
        if len(temp) == 0:
            temp.append(o)
            continue
        if o.x // 1 == temp[0].x // 1 and o.y // 1 == temp[0].y // 1:
            temp.append(o)
        else:
            continue

    for o in temp:
        o.klasa = len(temp)
    for o in temp:
        if o.klasa == 1:
            plt.scatter(o.x, o.y, c='r')
        elif o.klasa == 2:
            plt.scatter(o.x, o.y, c='y')
        else:
            plt.scatter(o.x, o.y, c='b')
        Obserwacja.ekstensja.remove(o)
    temp.clear()


plt.show()