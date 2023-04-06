import matplotlib.pyplot as plt
import numpy as np

class Spychacz():
    a = 0 # kąt

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.droga = list()
        self.droga.append((self.x, self.y))
        self.droga.append((self.x, self.y))

    def gdzieSpychacz(self):
        return self.x, self.y

    def jedz(self, ruch):
        if ruch == 'G':
            if self.a == 0:
                self.y += 10
            elif self.a == 90:
                self.x += 10
            elif self.a == 180:
                self.y -= 10
            elif self.a == 270:
                self.x -= 10
            self.droga.append((self.x, self.y))
            if self.x > 100:
                self.x = 90
            if self.x < 0:
                self.x = 10
            if self.y > 100:
                self.y = 90
            if self.y < 0:
                self.y = 10
        elif ruch == 'R':
            self.a = (self.a + 90) % 360
        elif ruch == 'L':
            self.a = (360 + self.a - 90) % 360
        if self.a == 0:
            m = '^'
        elif self.a == 90:
            m = '>'
        elif self.a == 180:
            m = 'v'
        elif self.a == 270:
            m = '<'
        return self.x, self.y, m


class Cel:
    def __init__(self):
        self.x = np.random.randint(0,10) * 10
        self.y = np.random.randint(0,10) * 10
        self.trafiony = False

plt.axis([-1,101, -1, 101])
plt.grid(10)
plt.plot([0,0], [0,100], color='m')
plt.plot([0,100], [100,100], color='m')
plt.plot([100,100], [100,0], color='m')
plt.plot([100,0], [0,0], color='m')

spychacz = Spychacz(50,50)
sx, sy = spychacz.gdzieSpychacz()
plt.scatter(sx, sy, color = 'b', marker='^')

lista_celow = list()

for i in range(5):
    cel = Cel()
    plt.scatter(cel.x, cel.y, color='y', marker='o')
    lista_celow.append(cel)

plt.pause(1)
trasa = input('Podaj trase:')

licznik_trafien = 0

for ruch in trasa:
    if ruch not in ['G', 'L', 'R']:
        continue
    sx, sy, sm = spychacz.jedz(ruch)
    for cel in lista_celow:
        if sx == cel.x and sy == cel.y and not cel.trafiony:
            cel.trafiony = True
            plt.scatter(cel.x, cel.y, color = 'r', marker='x')
            licznik_trafien+= 1
    plt.scatter(sx, sy, color = 'b', marker=sm)
    plt.plot((spychacz.droga[-1][0], spychacz.droga[-2][0]), (spychacz.droga[-1][1], spychacz.droga[-2][1]))
    print(f'Ilosc trafien: {licznik_trafien}')
    plt.pause(0.5)


if licznik_trafien > 4:
    print('Wygrana')
else:
    print('Przegrana')

plt.show()