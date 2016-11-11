import os
from time import sleep

print('PokeAPI\n')

# Pingt de server elke 30 seconden om te zien hoe snel de server de requests kan verwerken.
c = 0
while c != 3600:
    ping = os.popen('ping pokeapi.co -n 1')
    result = ping.readlines()
    msLine = result[-1].strip()
    print('Ping: ' + msLine.split(' = ')[-1])
    c += 60
    sleep(30)
