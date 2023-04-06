import random

cena = [random.randint(1, 100) for i in range(100)]
waga = [random.randint(1, 12) for i in range(100)]

max_kg = 30 #maksymalny ciężar plecaka

with open('plecak_towary.txt', 'w') as f:
    for i in range(100):
        f.write(f'{cena[i]};{waga[i]}\n')

with open('plecak_towary.txt', 'r') as f:
    towary = f.readlines()

lista_towarow = []

for towar in towary:
    towar = towar.strip().split(';')
    lista_towarow.append(towar)

lista_towarow.sort(key=lambda x: int(x[0])/int(x[1]), reverse=True)
print(lista_towarow)

plecak = []

for towar in lista_towarow:
    if int(towar[1]) <= max_kg:
        plecak.append(towar)
        max_kg -= int(towar[1])
    else:
        continue

print(plecak)
print(max_kg)

