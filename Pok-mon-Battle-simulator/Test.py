import csv

inputerino = input('naam: ')
def damage():
    with open('./pokemon/%s/stats.csv' % inputerino, 'r') as file:
        stats = csv.DictReader(file, delimiter=';')
        for stat in stats:
            spatt = int(stat['special_attack'])
            att = int(stat['attack'])
            spdef = int(stat['special_defense'])
            defense = int(stat['defense'])
            hp = int(stat['hp'])

        effective_Hp = (spdef + defense) * hp
        total_damage = (spatt + att) * 1.6 * 10

    return effective_Hp - total_damage


print(damage())

'''
Defence(HP) = (Sp DEF + DEF) * HP
ATTACK = (Speed + Sp att + att * 1.6)  *  10
'''
