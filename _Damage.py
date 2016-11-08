import csv

with open('bulbasaurr.csv', 'w') as file:
    fieldnames = ['Pokemon', 'Type', 'Speed', 'SpDef', 'SpAtt', 'Def', 'Att', 'Hp']
    writer = csv.DictWriter(file, fieldnames=fieldnames, lineterminator='\n', delimiter=',')

    writer.writeheader()
    writer.writerow({'Pokemon': 'balbasaur', 'Type': 'poison, grass', 'Speed': '45', 'SpDef': '65', 'SpAtt': '65','Def': '49', 'Att': '49', 'Hp': '45'})

with open('bulbasaurr.csv', 'r') as file:
    r = csv.DictReader(file)
    for stats in r:
        Speed = int(stats['Speed'])
        SpAtt = int(stats['SpAtt'])
        Att = int(stats['Att'])
        SpDef = int(stats['SpDef'])
        Def = int(stats['Def'])
        Hp = int(stats['Hp'])

def damage():
    effective_Hp = (SpDef + Def) * Hp
    total_damage = (Speed + SpAtt + Att) * 1.4 * 10

    return (effective_Hp - total_damage)

print(damage())


'''
Defence(HP) = (Sp DEF + DEF) * HP
ATTACK = (Speed + Sp att + att * 1.6)  *  10
'''
