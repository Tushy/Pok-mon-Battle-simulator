import os
from time import sleep

c = 0
while c != 3600:
    ping = os.popen('ping pokeapi.co -n 1')
    result = ping.readlines()
    msLine = result[-1].strip()
    print(msLine.split(' = ')[-1])
    c += 60
    sleep(60)
