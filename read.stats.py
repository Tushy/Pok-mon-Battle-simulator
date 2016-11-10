import csv


def read_stats(pokemon, stat):
    with open('./pokemon/%s/stats.csv' % pokemon, 'r') as file:
        r = csv.DictReader(file, delimiter=';')
        for stats in r:
            Speed = int(stats['speed'])
            SpAtt = int(stats['special_attack'])
            Att = int(stats['attack'])
            SpDef = int(stats['special_defense'])
            Def = int(stats['defense'])
            Hp = int(stats['hp'])

            if stat == 'speed':
                return Speed
            elif stat == 'special_attack':
                return SpAtt
            elif stat == 'attack':
                return Att
            elif stat == 'special_defense':
                return SpDef
            elif stat == 'defense':
                return Def
            elif stat == 'hp':
                return Hp

print(read_stats('bulbasaur','speed'))
