import csv


def damage_type_calculator(pokemon, move_power, aanval_type):
    pokemon_type_bestand = './pokemon/' + pokemon + '/stats.csv'

    with open(pokemon_type_bestand, 'r') as f:
        r = csv.DictReader(f, delimiter=';')
        for i in r:
            pokemon_types_temp = i['type']
            SpAtt = int(i['special_attack'])
            Att = int(i['attack'])

    pokemon_types = []
    for i in pokemon_types_temp.split("'"):
        if i.isalpha():
            pokemon_types.append(i)

    effect = []
    for i in pokemon_types:
        effect_bestand = './pokemon/types/' + i + '.csv'
        with open(effect_bestand, 'r') as f:
            r = csv.DictReader(f, delimiter=';')
            for i in r:
                if aanval_type in i['half_damage_from']:
                    effect.append(0.5)
                elif aanval_type in i['double_damage_from']:
                    effect.append(2)
                elif aanval_type in i['no_damage_from']:
                    effect.append(0)
                else:
                    effect.append(1)

    # stats

    damage = (SpAtt + Att) * (move_power / 100 + 1) * 10

    if 0 in effect:
        return damage * 0
    elif 2 in effect:
        return damage * 2
    elif 0.5 in effect:
        return damage * .5
    else:
        return damage


print(damage_type_calculator('charizard', 60, 'fire'))
