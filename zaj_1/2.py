def conv_to_dec(plik):
    with open(plik) as f:
        wszystkie_linie = f.readlines()

        for liczba in wszystkie_linie:
            liczba = liczba.strip()

            lista = []
            for i in str(liczba):
                lista.append(i)

                result = 0
                for i in reversed(lista):
                    dec = int(i) * (2 ** int(lista.index(i)))
                    result += dec

                print(result)



conv_to_dec('liczby.txt')