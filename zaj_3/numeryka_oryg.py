import numpy as np

# tablica = np.array([1,2,3,4,5,6,7,8,9])
#
# print(tablica)
# print(type(tablica))
# tablica = list(tablica)
# print(tablica)
# print(type(tablica))
#
# tablica0D = np.array(2)
# print(tablica0D.ndim)           # sprawdzenie wymiaru
#
# tablica1D = np.array([1,2,3,4])
# print(tablica1D.ndim)
#
tablica2D = np.array([[1,2,3],[5,4,2]])
#
# print(tablica2D)
# print(tablica2D.ndim)
#
# tablica3D = np.array([[[1,2,3,4], [4,3,2,1]],[[5,4,3,2], [1,2,3,0]]])
# print(tablica3D)
# print(tablica3D.ndim)
#
# tablica = np.ones(8)            # tablica z samymi zerami
# print(tablica)
# tablica = np.zeros(8)           # tablica z samymi 1
# print(tablica)
#
# tablica = np.arange(5)          # zakres od do (od sie zawiera)
# print(tablica)
# tablica = np.arange(5, 10)      # zakres od do
# print(tablica)
# tablica = np.arange(5, 10, 2)   # zakres od do, co ile
# print(tablica)
#
# tablica = np.linspace(0,100, num=5)
# print(tablica)
#
# tablica = np.array([5,43,23,8,9,123,23,42,23,-5,0])
#
# print(tablica[0])
#
# print(tablica2D[0, 2])
# print(tablica3D[0, 1, 1])
#
# print(tablica[1:4]) # ciecie
#
# print(tablica[1:8:2]) # od do co ile
# tablica = np.array([1,2,3,4,5])
# print(tablica[::2]) # co drugi element
#
# print(tablica2D[1, :2]) # z wiersza o numerze 1 wybierz 2 pierwsze elementy
# print(tablica2D[0:2, 2]) # z obu wymiarow wez element o indexie 2
#
# print(tablica2D[0:2, 0:2]) # wytnij lewy gorny rog 2 x 2
#
# # i - int, b - bool, f - float, M - datetime, O - object,
# # S - string, U - unicode String
#
# tablica = np.array(['bmw', 'audi', 'mercedes'])
# print(tablica.dtype)
#
# # for i in range(255):
# #     print(i , chr(i))
#
# tablica = np.array([1,2,3,1], dtype='U')
#
# print(tablica)
# print(tablica.dtype)
# arr = np.array([5.13, 4.92, 9.7])
# arr = arr.astype('i')
# arr = arr.astype('bool')
# print(arr)
#
# tablica = np.array([1,4,5,3])
# # kopia = tablica.view()        # domyslnie kopia referencji do oryginalu
# kopia = tablica.copy()          # kopia zawartosci do nowej pamieci
# tablica[1] = -100
#
# print(tablica)
# print(kopia)
#
# dane = np.array([1,2,3,4,5,6,7,8])
#
# print(tablica3D.shape)
# print(dane.reshape(2,2,2))
#
# for e in dane:
#     print(e)
#
# for e in dane.reshape(2,4):
#     print(e)
#
# for e in np.nditer(tablica3D):
#     print(e)
#
# for nr, e in np.ndenumerate(tablica3D):
#     print(nr, e)


t1 = np.array([1,2,9])
t2 = np.array([8,8,2,2,2,2,12,2])

tablica = np.concatenate((t1,t2))

print(tablica)

t1 = np.array([[0,1], [2,3]])
t2 = np.array([[4,5], [6,7]])

# oś pozioma to 0, oś pionowa to 1

# print(np.concatenate((t1,t2), axis= 0))
print(np.concatenate((t1,t2), axis= 1))

t1 = np.array([1,2,9])
t2 = np.array([8,7,6])

# print(np.stack((t1,t2), axis=0))
# print(np.stack((t1,t2), axis=1))

print(np.hstack((t1,t2))) # dolozenie do rzedu
print(np.vstack((t1,t2))) # dolozenie do kolumn

print(np.dstack((t1,t2))) # dlozenie do wysokosci elementow i zagniezdzenie +1 o wartosc wysokosci
val = np.array_split(tablica, 3)
print(type(val[0]))
print(np.array_split(tablica, 3))

print(tablica)
print(np.where(tablica == 2))
print(np.where(tablica2D == 2))
val = np.where(tablica2D == 2)
print(type(val))

print(tablica2D)
print(np.sort(tablica2D))

print(len(tablica))
print(tablica)
filt = [True, False, True, False, False, False, False,True, False, False, False]
print(tablica[filt])

filtr = tablica % 2 != 0

print(tablica[filtr])

tablica2D[tablica2D % 2 == 0] = 1
print(tablica2D)

# zad 1 Wylosuj tablica 10 x 10 z wartosciami od -10 do 10
# zad 2 Wskaz wartosc najczesciej wystepujaca z zad 1

tablica = np.random.randint(-10, 11, (10,10))
# print(tablica)
# tablica = tablica.reshape(100)
# print(np.bincount(tablica+10).argmax()-10)

#zad 3 Posortuj tablice zad 1 w wierszach a potem w kolumnach

# tablica = np.sort(tablica)
# tablica = np.sort(tablica, axis=0)
print(tablica)

# zad 4 Wskaz w którym wierszu suma elementow jest nawieksza

print(np.sum(tablica, axis=1).argmax())

# zad 5 Wylosuj tablice 30 elementow wartosciami parzystymi od -50 do 50

tablica = np.random.randint(-25, 25, 30) * 2

# zad 6 Wskaz mediane z tablicay z zad 5
# zad 7 Naloz filtr ktory przepusci tylko liczby jednocyfrowe

print(np.median(tablica))
print(tablica[(tablica < 10) & (tablica > -10)])

# zad 8 dla tablicy z zad 5 wskaz pozycje elementu ktorego suma cyfr jest najwieksza
#* dowolne liczby calkowite
# zad 9 stworz tablice (N x N), wypelniona samymi zerami, wstaw do niej na losowe pozycje
# dokladnie 30% jedynek (liczone z zaokragleniem)






