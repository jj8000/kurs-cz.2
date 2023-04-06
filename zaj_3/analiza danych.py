import pandas as pd

print(pd.__version__)           # sprawdzenie wersji

zbior = [5,4,2,7,-9]

dane = pd.Series(zbior)         # konwersja listy na Series

print(type(dane))           # Typ Series
print(dane)
print(dane[3])          # wybór elemenu z Series
print(dane[3:])         # slice dziala normalnie

# print(dane[-1])      # brak wstecznego indeksowania

zbior = [['s', 'b', 'c'], '14h', '6h', '0h', '2h']
idx = ['Poniedzialek', 'Wtorek', 'Sroda', 'Czwartek', 'Piatek']
godziny_pracy = pd.Series(zbior, index=idx)         # ustawienie wlasnych indeksow

# wybor elementu po nowym indeksie
# ustawienie indeksow nie resetuje indeksowania liczbowego od 0

print(godziny_pracy['Wtorek'])      # wypis indeksu
print(godziny_pracy[0])             # wypis indeksu

godziny_pracy['Sobota'] = '5h'      # wstawienie nowego elementu

print(godziny_pracy)


dania = {
    "rosol" : 350,
    "schabowy" : 550,
    "barszcz" : 280,
    "jajko sadzone" : 80
}

ser_dania = pd.Series(dania)        # konwersja ze slownikow na Series

print(ser_dania)
print(type(ser_dania))

dict_dania = dict(ser_dania)        # konwersja z Series na dania

print(dict_dania)
print(type(dict_dania))

filtr_dan = ["rosol", "jajko sadzone"]      # wybrane indeksy
print(pd.Series(dict_dania, index=filtr_dan))   # wybor indeksow z slownika

# usuniecie elementu z Series takie smao jak slownik

del ser_dania["rosol"]
print(ser_dania)

# pobranie wartosci zwraca numpy array
dane = ser_dania.values

print(type(dane))
print(dane)

list_val = list(ser_dania.values)
print(list_val)
# print(dane[len(dane)-1])

obiad = {
    'Nazwa obiadu' : ["rosol","schabowy", "barszcz","jajko sadzone"],
    'Kalorycznosc' : [350, 450, 280, 80],
    'Bialko' : [0, 40, 0, 8],
    'Weglowodany' : [50, 35, 40, 20]
}

# stworzenie ramki z slownika z danymi
df = pd.DataFrame(obiad)

print(type(df))
print(df)

# df[2] - koncepcja numeracji wiersza nie dziala

print(df.loc[2]) # Wybor wiersza po lokalizacji

# slice dziala
print(df[:3])

# filtr po loc
idx = [1,2]

print(df.loc[[1,2]])  # print(df.loc[idx])

# df.loc[1,2] # nie dziala

idx_dni = ['dzien1', 'dzien2', 'dzien3', 'dzien4']

df = pd.DataFrame(obiad, index = idx_dni)

print(df)
dana = df.loc['dzien2']
print(dana)
print(type(dana))

# wypisz dane o dataframe
print(df.info())

# odniesienie od kolumny zwraca Series
print(df['Nazwa obiadu'])
spis = df['Nazwa obiadu'].values.tolist()   # pobranie wartosci z kolumny i konwersja na liste

print(spis)
print(type(spis))


# wziecie elementu na krzy kolumna x wiersz
print(df['Kalorycznosc'].iloc[2])

csv_kostiumy = pd.read_csv('https://analityk.edu.pl/wp-content/uploads/2020/12/Halloween.csv', header=2)

print(csv_kostiumy)
print(csv_kostiumy.info())

# wypisz 5 pierwszych wartosci
print(csv_kostiumy.head())

# wypisz 5 ostatnich wartosci
print(csv_kostiumy.tail())

# wybor 10 pozycji, wypisanie ich regionow
print(csv_kostiumy[:10]['region'])

# zamiana indeksu na region
csv_kostiumy = csv_kostiumy.set_index('region')
print(csv_kostiumy)

# wypisanie najpopularniejszego kostiumu w stanie Alabama
print(csv_kostiumy.loc['Alabama'][0])
print(csv_kostiumy.loc['Alabama', '1'])

# wybrane regiony na ktorych nam zalezy
print(csv_kostiumy.loc[['Texas','Tennessee', 'Virginia']])

# zmiana ilosci max wyswietlanych wierszy
pd.options.display.max_rows = 30
print(pd.options.display.max_rows)

print(csv_kostiumy)

import random as r

df = pd.DataFrame(columns=['nazwa zestawu', 'kcal', 'bialko'])

pd.options.display.max_rows = 101
for i in range(100):
    df.loc[i] = [('zestaw #' + str(i+1)), r.randint(5,300), r.randint(5, 200)]
print(df)

print(df.head(10)) # domyslnie 5 dla head i tail

# max wartosc z kolumny
print(df['kcal'].max())
print(df['kcal'].min())

print(csv_kostiumy.loc['Alabama', '1'])
# zamiana wartosci
csv_kostiumy.loc['Alabama', '1'] = 'Spiderman'
print(csv_kostiumy.loc['Alabama', '1'])

print(csv_kostiumy)


df = pd.read_csv('auta.csv', delimiter = ',')
print(df)

# zakres indeksow
# print(df.index)

# for idx in df.index:
#     # pomijamy wartosic puste -> wartosc pusta to wartosc ?
#     if df.loc[idx, 'price'] != '?':
#         # filtr na cene powyzej 20000
#         if int(df.loc[idx, 'price']) > 20000:
#             print(df.loc[idx])

  # z zignorowaniem bledu konwersji
for idx in df.index:
    try:
        if int(df.loc[idx, 'price']) > 20000:
            print(df.loc[idx])
    except:
        pass

# df = df[df['highway-mpg'] > 30]
#
# print(df)

for idx in df.index:
    if df.loc[idx, 'price'] == '?':
        df.loc[idx, 'price'] = 0

# for idx in df.index:
#     # pomijamy wartosic puste -> wartosc pusta to wartosc ?
#         # filtr na cene powyzej 20000
#     if int(df.loc[idx, 'price']) > 20000:
#         print(df.loc[idx])

# print(df)

# sortowanie wartosci w kolumnie
# df = df.sort_values('highway-mpg')

# sortowanie jako index

# df = df.set_index('highway-mpg')
# df.sort_index()
#
# print(df)

# zad 1 Wypisz nazwiska uporzadkowane alfabetycznie sześcioletnich
# dziewczynek z przedszkola nr 75


# --- moje (rozwiązanie prowadzącego niżej)---

with open('PRZEDSZKOLA.TXT', 'r') as f:
    data = f.readlines()

    for i in data:
        i = i.split(';')
        if i[1] == 'Przedszkole nr 75':
            print(i[0])
            id_75 = i[0]
        continue
print(id_75)

df = pd.read_csv('DZIECI.TXT', delimiter = ';')

# print(df)
# print(df.info())


# for idx in df.index:
#
#     if int(df.loc[idx, 'Wiek']) == 6:
#         print(df.loc[idx])
#     continue

s1 = set()
for idx in df.index:
    try:
        if int(df.loc[idx, 'Wiek']) == 6 and (df.loc[idx, 'Plec']) == 'dziewczynka':
            s1.add(df.loc[idx, 'Pesel'])
    except:
        pass


df = pd.read_csv('PREFERENCJE.TXT', delimiter = ';')

s2 = set()
for idx in df.index:
    try:
        if df.loc[idx, 'Pesel'] in s1 and int((df.loc[idx, 'Id_przedszkola'])) == int(id_75):
            s2.add(df.loc[idx, 'Pesel'])
    except:
        pass


df = pd.read_csv('DZIECI.TXT', delimiter = ';')

for idx in df.index:
    try:
        if df.loc[idx, 'Pesel'] in s2:
            print(df.loc[idx, 'Nazwisko'])
    except:
        pass

# --- Rozwiązanie prowadzącego ---

df_dzieci = pd.read_csv('DZIECI.TXT', sep=';')
df_preferencje = pd.read_csv('PREFERENCJE.TXT', sep=';')
df_przedszkola = pd.read_csv('PRZEDSZKOLA.TXT', sep=';')

# print(df_dzieci)
# print(df_preferencje)
# print(df_przedszkola)

# for idx in df_przedszkola.index:
#     if df_przedszkola.loc[idx, 'Nazwa_przedszkola'] == 'Przedszkole nr 75':
#         przedszkole = df_przedszkola.loc[idx]
#
# # print(przedszkole)
#
# pesele = list()
#
# for idx in df_preferencje.index:
#     if df_preferencje.loc[idx, 'Id_przedszkola'] == przedszkole['Id_przedszkola']:
#         pesele.append(df_preferencje.loc[idx, 'Pesel'])
#
# print(pesele)
#
# df_2 = df_dzieci.loc[df_dzieci['Pesel'].isin(pesele)]
#
# wynik = df_2[(df_2['Plec'] == 'dziewczynka') & (df_2['Wiek'] == 6)].sort_values('Nazwisko')
# print(wynik)

# --- Rozwiązanie przez łaczenie ---

# zlaczenie 2 dataframe wymaga ustawienia indexu na takiej samej kolumnie
df_all = df_preferencje.set_index('Pesel').join(df_dzieci.set_index('Pesel'))
df_all = df_all.set_index('Id_przedszkola').join(df_przedszkola.set_index('Id_przedszkola'))

print(df_all)

print(df_all [(df_all['Nazwa_przedszkola'] == 'Przedszkole nr 75') &
              (df_all['Plec'] == 'dziewczynka') &
              (df_all['Wiek'] == 6)]
      .sort_values('Nazwisko')['Nazwisko']
      )

# zad 2 Wypisz wszystkie osoby które na liscie preferencji maja dokladnie 3 przedszkola

df_dzieci = pd.read_csv('DZIECI.TXT', sep=';')
df_preferencje = pd.read_csv('PREFERENCJE.TXT', sep=';')
df_przedszkola = pd.read_csv('PRZEDSZKOLA.TXT', sep=';')

list = []
for idx in df_preferencje.index:
    list.append(df_preferencje.loc[idx, 'Pesel'])

pesele=set()
for i in list:
    if list.count(i) == 3:
        pesele.add(i)
    continue


for idx in df_dzieci.index:
     if df_dzieci.loc[idx, 'Pesel'] in pesele:
        print(df.loc[idx])


# wynik jako dataframe:

wynik = df_dzieci.loc[df_dzieci['Pesel'].isin(pesele)]

print(wynik)

# zad 3 Podaj nazwę przedszkola, które jest wybrane jako pierwszy wybór, nikt nie wybrał go jako kolejny
# zad 4 podaj liczbę tych osób

przedszkola1 = set()
for idx in df_preferencje.index:
    if df_preferencje.loc[idx, 'Numer_preferencji'] == 1:
        przedszkola1.add(df_preferencje.loc[idx, 'Id_przedszkola'])

przedszkola2 = set()
for idx in df_preferencje.index:
    if df_preferencje.loc[idx, 'Numer_preferencji'] != 1:
        przedszkola2.add(df_preferencje.loc[idx, 'Id_przedszkola'])

wynik_zbior = przedszkola1 - przedszkola2
print(wynik)
wynik = df_przedszkola.loc[df_przedszkola['Id_przedszkola'].isin(wynik_zbior)]

print(wynik)

osoby1 = set()
for idx in df_preferencje.index:
    if df_preferencje.loc[idx, 'Id_przedszkola'] in wynik_zbior:
        osoby1.add(df_preferencje.loc[idx, 'Pesel'])

print(osoby1)
print(len(osoby1))

# zad 5 wypisz 3 najbardziej oblegane przedszkola

list = []
for idx in df_preferencje.index:
    list.append(df_preferencje.loc[idx, 'Id_przedszkola'])

popularnosc = {}
for i in list:
    n = list.count(i)
    popularnosc.update({i: n})

posortowane = sorted(popularnosc.items(), key=lambda x:x[1], reverse=True)
print(posortowane)

top3 = []

for i in posortowane:
    if len(top3) <= 2:
        top3.append(i[0])
    else:
        break

print(top3)

wynik = df_przedszkola.loc[df_przedszkola['Id_przedszkola'].isin(top3)]

print(wynik)






