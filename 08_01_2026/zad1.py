import csv
import numpy as np
import os

path = 'C:/Users/364264/Documents/programowanie/programowanie-python/08_01_2026/dane/'
lista_plikow = os.listdir(path)
lista = []

for plik in lista_plikow:
    nazwa  = f'{path}{plik}'

    with open(nazwa, 'r', encoding='utf-8') as tabela:
        csvreader = csv.reader(tabela)
        next(csvreader)
        
        for wiersz in csvreader:
            lista.append(wiersz)

tablica = np.array(lista)

temperatura = []
opad = []

for i in range(0, len(tablica[:,4])):
    temperatura.append(float(tablica[i,4]))

for i in range(0, len(tablica[:,8])):
    opad.append(float(tablica[i,8]))

temperatura = np.array(temperatura)
opad = np.array(opad)

min_temp = min(temperatura)
max_temp = max(temperatura)
#print(f'MIN: {min_temp}\nMAX: {max_temp}')

index_min_temp = np.where(temperatura == min_temp)
index_max_temp = np.where(temperatura == max_temp)

godzina_min_temp = tablica[index_min_temp,3]
data_min_temp = tablica[index_min_temp,2]
lokalizacja_min_temp = tablica[index_min_temp,1]

godzina_max_temp = tablica[index_max_temp,3]
data_max_temp = tablica[index_max_temp, 2]
lokalizacja_max_temp = tablica[index_max_temp, 1]

print(f'Minimalną temperaturę powietrza zanotowano na stacji {lokalizacja_min_temp[0][0]} w dniu {data_min_temp[0][0]} o godzinie {godzina_min_temp[0][0]} i wyniosła {min_temp}.')
print(f'Maksymalną temperaturę powietrza zanotowano na stacji {lokalizacja_max_temp[0][0]} w dniu {data_max_temp[0][0]} o godzinie {godzina_max_temp[0][0]} i wyniosła {max_temp}.')

niezerowy_opad_index = np.where(opad > 0)

print(niezerowy_opad_index)

niezerowy_opad_lokalizacja = tablica[niezerowy_opad_index,1]
niezerowy_opad_data = tablica[niezerowy_opad_index,2]
niezerowy_opad_godzina = tablica[niezerowy_opad_index,3]

for j in range(0,len(niezerowy_opad_index[0])):
    print(f'Opad wystapił na stacji {niezerowy_opad_index[0]}')