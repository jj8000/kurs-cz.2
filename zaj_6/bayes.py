import pandas as pd

with open('dane.txt', 'r', encoding='utf8') as f:
    data = f.readlines()

dane = []
for i in data:
    i = i.strip().split(',')
    dane.append(i)

df = pd.DataFrame(dane[1:], columns=dane[0])
# print(df)



warunki = pd.Series(['słonecznie', 'zimno', 'wysokie', 'tak'])

# https://www.alx.pl/ankiety/5415fima











