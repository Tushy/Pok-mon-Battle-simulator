import os
from time import sleep

# Pingt de server elke 30 seconden om te zien hoe snel de server de requests kan verwerken.

def ping():
    ping = os.popen('ping pokeapi.co -n 1')
    result = ping.readlines()
    msLine = result[-1].strip()
    return('Ping: ' + msLine.split(' = ')[-1])
