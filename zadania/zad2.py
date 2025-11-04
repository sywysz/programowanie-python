tekst_roznica = ''
tekst_w_pliku = ''

wiek1 = int(input('Podaj wiek studenta: '))

with open('C:/Users/364264/Documents/programowanie/programowanie-python/zadania/wiek_drugiego_studenta.txt') as czyt_plik:
    zawartosc = []
    for liczba in czyt_plik:
        zawartosc.append(int(liczba))
    wiek2 = zawartosc[0]

if wiek1 < wiek2:
    tekst_roznica = f'Pierwszy student jest młodszy od studenta pierwszego o {wiek2 - wiek1} lat(a).'
    print(tekst_roznica)

with open('C:/Users/364264/Documents/programowanie/programowanie-python/zadania/wiek2.txt', 'a') as plik:
    plik.write(f'{tekst_roznica}\n')