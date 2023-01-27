import requests
import pytest

def test_status_code():
    response = requests.get('https://pokemonbattle.me:5000/trainers')
    assert response.status_code == 200

@pytest.mark.parametrize('key,value',[('trainer_name' , 'Op'), ('city', 'Moscow')])
def test_parametr(key,value):
    response = requests.get('https://pokemonbattle.me:5000/trainers', params = {'trainer_id' : '1890'})
    assert response.json()[key] == value
