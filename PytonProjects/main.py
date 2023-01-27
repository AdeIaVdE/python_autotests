import requests
import json
#Создание покемона
token = '9b30fb81c0503f93fa12dbeb291148e3'

response = requests.post('https://pokemonbattle.me:5000/pokemons', json = {
    "name": "Бульбазавр",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
}, headers = {'Content-type': 'application/json','trainer_token': token})

print(response.json())

#Смена имени покемона

response_change = requests.put ('https://pokemonbattle.me:5000/pokemons', json = {
     "pokemon_id": 3473,
    "name": "Ihar",
    "photo": ""
}, headers = {'Content-type': 'application/json','trainer_token': token})

print(response.json())


#Поймать покемона в покебол

response_change = requests.put ('https://pokemonbattle.me:5000/trainers/add_pokeball', json = {
     "pokemon_id": "3473"
}, headers = {'Content-type': 'application/json','trainer_token': token})

print(response.json())

