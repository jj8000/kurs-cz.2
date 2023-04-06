#piotrolot1@gmail.com
#[ALX-28]

# wypisz l. pierwsze
# czy więcej parzystych czy nie
# wypisz liczbę o największej ilości cyfr

def primechk(n: int):
    for i in range(2, n):
        if n % i == 0:
            return
    print(n)

def list_primes(plik):
    with open(plik, 'r') as f:
        dane = f.readlines()
        for liczba in dane:
            liczba = int(liczba.strip())

            primechk(liczba)


# primechk(17)
# list_primes('dane.txt')

def evenchk(n: int):
    if n % 2 == 0:
        return True
    return False

def even_or_odd(plik):
    with open(plik, 'r') as f:
        dane = f.readlines()
        evenlist = []
        oddlist = []
        for liczba in dane:
            liczba = int(liczba.strip())

            if evenchk(liczba):
                evenlist.append(liczba)
            else:
                oddlist.append(liczba)

    print(f' {len(evenlist)} - ilość parzystych')
    print(f' {len(oddlist)} - ilość nieparzystych')

def maxlen(plik):
    with open(plik, 'r') as f:
        dane = f.readlines()
        dict = {}
        for liczba in dane:
            liczba = liczba.strip()
            dict[liczba] = len(liczba)

        print(dict)

        print(max(dict.values()))

    for x, y in dict.items():
        if y == max(dict.values()):
            print(x)

def palindrome(plik):
    with open(plik, 'r') as f:
        dane = f.readlines()
        for liczba in dane:
            liczba = liczba.strip()
            if liczba[0::1] == liczba[-1::-1]:
                print(liczba)





def suma_cyfr(liczba):

    lista = []
    for i in liczba:
        lista.append(int(i))
    return sum(lista)



def maxsumofdigits(plik):
    with open(plik, 'r') as f:
        dane = f.readlines()
        counter = 0
        result = None
        for linia in dane:
            liczba = int(linia.strip())
            if suma_cyfr(linia.strip()) > counter:
                counter = suma_cyfr(linia.strip())
                result = liczba
    print(result)






# list_primes('dane.txt')
print('-----')
# even_or_odd('dane.txt')
print('-----')
# maxlen('dane.txt')
print('-----')
# palindrome('dane.txt')
maxsumofdigits('dane.txt')