data = open("anagram.txt", "r")

new = data.read()

lists = new.split("\n")
print(lists)

for i in lists:
    lin = i.split(' ')
    print(lin)


    for i in lin:
        len(lin)

print()
def wypisz_anagramy(plik):
    with open(plik) as f:
        wszystkie_linie = f.readlines()

        for linia in wszystkie_linie:
            zbior_rozmiarow = set()
            linia = linia.strip()
            for slowo in linia.split(' '):
                zbior_rozmiarow.add(str(sorted(slowo)))

            if len(zbior_rozmiarow) == 1:
               print(linia)

wypisz_anagramy('anagram.txt')

