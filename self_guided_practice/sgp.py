import requests
import time
import pandas as pd
import numpy as np
path_imgw = 'https://danepubliczne.imgw.pl/api/data/synop/station/'
station_in_database = False

stacje_get = list(requests.get('https://danepubliczne.imgw.pl/api/data/synop/station'))

stacje = pd.read_json(stacje_get[0]) #NIE DZIALA
#Wpisanie danych od użytkownika
#print(stacje.to_string())
while station_in_database == False:
    user_stacja = input("Wprowadź kod stacji: ")
    if station_in_database == False:
        print('Spróbuj ponownie')
    else:
        print('Prawidłowo wybrano stację')
user_path = path_imgw + user_stacja
print(user_path)
user_time = input("Wprowadź godzinę zakończenia obserwacji: ")
#Pobieranie danych z IMGW
    #Sprawdzenie godziny
#time_now = time.time()
    #Jeśli upłynęło 5 minut odśwież w poszukiwaniu nowych danych
        #Dodaj nowy plik csv do folderu z danymi
#Przetwarzanie danych
    #