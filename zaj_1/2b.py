def bintodec(bin):

    suma = 0
    potega = 1
    for e in bin[::-1]:
        if e == '1':
            suma += potega
        potega *= 2

    return suma

#
# print(bintodec('10011'))
# #
def conv_to_dec(plik):
    with open(plik, 'r') as f:
        dane = f.readlines()
        for liczba in dane:
            liczba = liczba.strip()
            print(bintodec(liczba))



# def najw(plik):
#     with open(plik) as f:
#         wszystkie_linie = f.readlines()
#
#
#         lista = []
#         for i in wszystkie_linie:
#             liczba = bin(i)
#             lista.append(liczba)
#
#     print(lista)
#
#
#
conv_to_dec('liczby.txt')
# najw('liczby.txt')

def even(plik):
    with open(plik) as f:
        dane = f.readlines()

        for i in dane:
            i = i.strip()
            if not i.endswith('1'):
                print(i)

# even('liczby.txt')

