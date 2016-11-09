import csv


def read_moves(pokemon, soort):
    with open('./pokemon/%s/moves.csv' % pokemon, 'r') as file:
        r = csv.DictReader(file, delimiter=';')
        lijst_moves = []
        for moves in r:
            attack_name = moves['attack_name']
            attack_type = moves['attack_type']
            attack_accuracy = moves['attack_accuracy']
            attack_power = moves['attack_power']
            if soort == 'n':
                lijst_moves.append(attack_name)
            elif soort == 'p':
                lijst_moves.append(attack_power)
            elif soort == 'a':
                lijst_moves.append(attack_accuracy)
            elif soort == 't':
                lijst_moves.append(attack_type)

        return (lijst_moves)


print(read_moves('charmander','p')[1] )
