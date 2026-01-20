import requests
import time
import pandas as pd
import numpy as np
import json
path_imgw = 'https://danepubliczne.imgw.pl/api/data/synop/station/'
station_in_database = False

def download_data(path):
    stacje_get = requests.get(path)
    stacje = json.loads(stacje_get.text)
    np_stacje = np.array(stacje)
    return np_stacje

stacje = download_data(path_imgw)

stacje_lista = []
for st in stacje:
    stacje_lista.append(st["id_stacji"])

for st in stacje:
    print(f'{st["id_stacji"]}              {st["stacja"]}')

print(stacje_lista)

#Wpisanie danych od użytkownika
while station_in_database == False:
    user_stacja = input("Wprowadź kod stacji: ")
    if user_stacja not in stacje_lista:
        print('Spróbuj ponownie')
    else:
        print('Prawidłowo wybrano stację')
        station_in_database = True

user_path = path_imgw + user_stacja
user_time = input("Wprowadź godzinę zakończenia obserwacji (równe godziny, np. 17:00 = 17): ")

#Pobieranie danych z IMGW

#time_now = time.time()
    #Jeśli upłynęło 5 minut odśwież w poszukiwaniu nowych danych
        #Dodaj nowy plik csv do folderu z danymi
#Przetwarzanie danych
    #