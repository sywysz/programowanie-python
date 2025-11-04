wiek1 = int(input("Podaj wiek pierwszego studenta: "))
wiek2 = int(input("Podaj wiek drugiego studenta: "))

if wiek1 > wiek2:
    roznica = f'Pierwszy student jest starszy i ma {wiek1} lat(a).'
    print(roznica)

with open('C:/Users/364264/Documents/programowanie/programowanie-python/zadania/wiek1.txt', 'a') as plik:
    plik.write(f'{roznica}\n')