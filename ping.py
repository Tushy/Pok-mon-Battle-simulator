import requests


def ping():
    try:
        ping = requests.get('http://pokeapi.co/api/v2/')
    except:
        return 'U heeft internet nodig voor dit programma'
