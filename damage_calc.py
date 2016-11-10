import csv


def damage_type_calculator(pokemon, move_power, aanval_type):
    """Deze functie berekend de effectieve schade die een pokémon doet met zijn aanval. Er wordt gekeken naar de damage van de
    aanval en deze wordt in acht genomen bij de berekening. Ook wordt er gekeken naar de types van de tegenstander
    en het typen van de aanval. Het mag natuurlijk niet zo zijn dat een vuur aanval super-effectief is tegen
    een vuur pokémon."""
    pokemon_type_bestand = './pokemon/' + pokemon + '/stats.csv'  # Open het bestand van de pokémon

    with open(pokemon_type_bestand, 'r') as file:  # Lees de relevante data in van het geopende bestand
        reader = csv.DictReader(file, delimiter=';')
        for item in reader:
            pokemon_types_temp = item['type']
            SpAtt = int(item['special_attack'])
            Att = int(item['attack'])

    pokemon_types = []  # Lege lijst voor de type van de pokémon
    for item in pokemon_types_temp.split("'"):
        if item.isalpha():  # Voeg alle data van de type toe aan een lijst zolang de data een karakter is uit het alfabet
            pokemon_types.append(item)

    effect = []  # Bereken het effect dat een aanval heeft op de tegenstander. Dit is niet gelijk voor de verschillende type aanvallen
    for item in pokemon_types:
        effect_bestand = './pokemon/types/' + item + '.csv'
        with open(effect_bestand, 'r') as file:
            reader = csv.DictReader(file, delimiter=';')
            for item in reader:  # Afhankelijk van de verschillende type aanval en het effect van de aanval op de tegenstander worden er verschillende waarden toegevoegd aan de lijst 'effect'
                if aanval_type in item['half_damage_from']:
                    effect.append(0.5)
                elif aanval_type in item['double_damage_from']:
                    effect.append(2)
                elif aanval_type in item['no_damage_from']:
                    effect.append(0)
                else:
                    effect.append(1)

    damage = (SpAtt + Att) * (move_power / 100 + 1) * 10  # De damage berekening, dit is de standaard berekening waar
    #  het volgende stuk code de damage aanpast afhankelijk van de effectiviteit

    if 0 in effect:
        return damage * 0  # Voor niet effectieve aanvallen. normal op ghost bijvoorbeeld
    elif 2 in effect:
        return damage * 2  # Voor super-effectieve aanvallen. Water op vuur bijvoorbeeld.
    elif 0.5 in effect:
        return damage * .5  # Voor niet-erg-effectieve aanvallen. Vuur op vuur bijvoorbeeld
    else:
        return damage  # Voor normale aanvallen, als een aanval niet een andere status krijgt wordt de
        #  standaard damage waarde gebruikt
