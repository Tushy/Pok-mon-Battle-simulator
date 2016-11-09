import csv


def CheckBestand(pokemon):
    try:
        with open(pokemon + '.csv', 'r+') as csvfile:
            bestand = csv.reader(csvfile,  delimiter=';')
            for row in bestand:
                return(row)
    except:
        with open(pokemon + '.csv', 'w'):
            return(['0','0'])

def Write_Uitslag(pokemon, win):
    vorige_uitslag = CheckBestand(pokemon)
    won = vorige_uitslag[0]
    lose = vorige_uitslag[1]
    won = int(won)
    lose = int(lose)
    with open(pokemon + '.csv', 'w') as csvfile:
        bestand = csv.writer(csvfile,  delimiter=';')
        if win == True:
            uitslag_nieuw = [won ,lose]
            uitslag_nieuw[0] = won +1
            bestand.writerow(uitslag_nieuw)
        else:
            uitslag_nieuw = [won ,lose]
            uitslag_nieuw[1] = lose +1
            bestand.writerow(uitslag_nieuw)




win = True
Write_Uitslag('mew', win)
