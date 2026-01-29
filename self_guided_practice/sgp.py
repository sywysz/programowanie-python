import requests
import time
import numpy as np
import json


path_imgw = 'https://danepubliczne.imgw.pl/api/data/synop/'
is_station_in_database = False
is_hour_valid = False


def download_data(path):
    stacje_get = requests.get(path)
    stacje = json.loads(stacje_get.text)
    return np.array(stacje)

def download_new_data(path):
    stacje_get = requests.get(path)
    return stacje_get.json()

stacje = download_data(f'{path_imgw}station/')


#Wypisanie stacji do konsoli
stacje_lista = []
for st in stacje:
    stacje_lista.append(st["id_stacji"])
    print(f'{st["id_stacji"]}              {st["stacja"]}')


#Wpisanie danych przez użytkownika
while is_station_in_database == False:
    user_stacja = input("Wprowadź kod stacji: ")
    if user_stacja not in stacje_lista:
        print('Zły kod. Spróbuj ponownie.')
    else:
        print(f'Prawidłowo wybrano stację. Wybrany kod to {user_stacja}.')
        is_station_in_database = True


user_path = f'{path_imgw}id/{user_stacja}'
while is_hour_valid == False:
    user_time = input("Wprowadź godzinę zakończenia obserwacji (równe godziny, np. 17:00 = 17): ")
    if  1 > int(user_time) > 24:
        print('Godzina została wprowadzona źle. Podaj godzinę w zakresie 1-24.')
    else:
        print(f'Ustalono godzinę zakończenia na {user_time}:00.')
        is_hour_valid = True


#Przygotowanie danych do pobierania
user_stacja_dane = None
for st in stacje:
    if st['id_stacji'] == user_stacja:
        user_stacja_dane = st

temp_list = [float(user_stacja_dane['temperatura'])]
current_time = stacje[0]['godzina_pomiaru']

#Pobieranie danych z IMGW przez kolejne godziny
while True: 
    new_data = download_new_data(user_path) 
    if current_time == user_time: 
        break 
    else: 
        if current_time == new_data['godzina_pomiaru']: 
            print('Proszę czekać.') 
            time.sleep(10 * 60)
        else: 
            temp_list.append(float(new_data['temperatura']))
            current_time = new_data['godzina_pomiaru'] 
            print(f'Dodano dane z godziny {current_time}. Aktualna temperatura to {temp_list[-1]}')

#Wypisanie wyników do konsoli
sr_temp = sum(temp_list) / len(temp_list)
message = f'Średnia temperatura dla stacji {user_stacja_dane['stacja']} (id: {user_stacja}) wynosi {sr_temp}°C.'
print(message)

#Wpisanie i zformatowanie wyników do pliku results.txt
with open('programowanie-python/self_guided_practice/results.txt', 'a', encoding='utf-8') as file:
    contents = f'Stacja {user_stacja_dane['stacja']}\nGodziny pomiaru: {stacje[0]['godzina_pomiaru']}-{user_time}\nTemperatury pomiaru:\n'
    for item in temp_list:
        contents += f'  {item}\n'
    contents += f'{message}\n##########\n##########\n'
    file.write(contents)
