import requests


def ping():
    '''
    Ping naar de server van de API om te controlleren of er een internet verbinding beschikbaar is. Als dit niet zo is
    returned er een string voor in de text box van het interface'
    '''
    try:
        requests.get('http://pokeapi.co/api/v2/')
    except:
        return 'U heeft internet nodig voor dit programma'
