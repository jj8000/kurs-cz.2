# utwórz słownik, klucz - liczba długości słow, wartości - lista z tymi słowami

def lendict(plik):
    with open(plik, 'r') as f:
        dane = f.readlines()
        dict = {}
        keys = set()
        for word in dane:
            word = word.strip()
            keys.add(len(word))

    print(keys)


    # for x, y in dict.items():
    #     if y == max(dict.values()):
    #         print(x)

lendict('tj.txt')


# pastebin.com/14fz3d86