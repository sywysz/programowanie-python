# plik = open("./liczby.txt")
# tresc = plik.read()
# print(tresc)

with open("./liczby.txt") as plik:
    zawartosc = plik.readlines()
       
print(zawartosc)

with open("./liczby.txt") as plik1:
    zawartosc1 = plik1.read().splitlines()

print(zawartosc1)
print(f'Wartosc o indeksie 6 wynosi: {zawartosc1[5]}')

with open("./liczby.txt") as plik2:
    zawartosc2 = []
    for liczba in plik2:
        zawartosc2.append(int(liczba))

print(zawartosc2)