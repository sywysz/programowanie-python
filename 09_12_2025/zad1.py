import csv
import numpy as np

lista = []

with open(r'C:\Users\364264\Documents\programowanie\programowanie-python\09_12_2025\meteo.csv', 'r') as plik:
    tabela = csv.reader(plik)
    naglowki = next(tabela)

    for wiersz in tabela:
        lista.append(wiersz)

    tablica = np.array(lista)

    print(tablica[3][1])

    # Zad 2

    temperatura = []
    wilgotnosc = []
    cisnienie = []

    def srednia (lista):
        suma = 0
        for w in lista:
            suma += w
        return suma / len(lista)
    
    for wiersz in tablica:
        temperatura.append(float(wiersz[4]))
        wilgotnosc.append(float(wiersz[7]))
        cisnienie.append(float(wiersz[-1]))

    print(f'Średnia temperatura: {srednia(temperatura):.2f}')
    print(f'Średnia wilgotność: {srednia(wilgotnosc):.2f}')
    print(f'Średnia ciśnienie: {srednia(cisnienie):.2f}')

