import csv

inputerino = input('naam: ')
def damage():
    with open('./pokemon/%s/stats.csv' % inputerino, 'r') as file:
        r = csv.DictReader(file, delimiter=';')
        for stats in r:
            SpAtt = int(stats['special_attack'])
            Att = int(stats['attack'])
            SpDef = int(stats['special_defense'])
            Def = int(stats['defense'])
            Hp = int(stats['hp'])

    effective_Hp = (SpDef + Def) * Hp
    total_damage = (SpAtt + Att) * 1.6 * 10

    return effective_Hp - total_damage


print(damage())

'''
Defence(HP) = (Sp DEF + DEF) * HP
ATTACK = (Sp att + att * 1.6)  *  10
'''
