
# daty

#sluzy do nich jedna biblioteka

import datetime as dt

teraz = dt.datetime.now()

print(teraz)
print(type(teraz))

print(teraz.year, teraz.month, teraz.day, teraz.hour, teraz.minute, teraz.second)

urodziny = dt.datetime(2012, 1, 1)          # strefa czasowa None
print(urodziny)

# %a, %A - nazwa dnia tygodnia, mala - skrocona
# %y, %Y - rok (mala - dwie ostatnie cyfry)
# %b %B - miesiac (skrocony, pelen)
# %d - dzien miesiaca
# %n - numer miesiaca
# %H - godziny (24)
# %I - godziny (12)
# %M - minuty
# %S - sekundy
# %x - lokalny zapis daty
# %X - lokalny zapis czasu

# https://docs.,python.org/3/library/time.html

print(teraz.strftime("%y -- %d -/- %M:%S"))

data_str = "2000,11!30"

#jakas_data = dt.datetime.strptime(data_str, "%Y, %n!%d")
#print(jakas_data)

start = dt.datetime.now()

ile = 5000
str = 'ala'

while ile:
    str += "ma"
    ile -= 1

stop = dt.datetime.now()
delta = stop - start
print(delta)

print(teraz)
ile = dt.timedelta(days=3, minutes=40)

print(teraz + ile)