data = open('anagram.txt', 'r')

def alfabetycznie(arg: str):

    list = []
    for i in arg:
        list.append(i)
    return ''.join(sorted(list))

def list_anagrams(plik):

    with open(plik) as f:
        for line in f.readlines():
            line = line.strip()
            zbior = set()
            for i in line.split(' '):
                zbior.add(alfabetycznie(i))
            if len(zbior) == 1:
                print(line)

list_anagrams('anagram.txt')




