from pokeapi.pokemon import Pokemon
from tabulate import tabulate

# Hier wordt om input van de gebruiker gevraagd, welke pokémon willen ze tegen elkaar laten vechten?
pokemon1_naam = input('Geef de naam van de eerste pokémon: ')
pokemon1 = Pokemon(pokemon1_naam)
pokemon2_naam = input('Geef de naam van de tweede pokémon: ')
pokemon2 = Pokemon(pokemon2_naam)

# Hier worden de stats en types van de pokémons opgevraagd
stats1 = pokemon1.getStats()
stats2 = pokemon2.getStats()
type1 = pokemon1.getTypes()
type2 = pokemon2.getTypes()

# Hier worden de types per pokémon in een lijst gezet
type_list1 = []
c1 = 0
for t in type1:
    types = type1[c1]
    value = types['name']
    type_list1.append(value)
    c1 += 1

type_list2 = []
c2 = 0
for t in type1:
    types = type1[c2]
    value = types['name']
    type_list2.append(value)
    c2 += 1

# print('Deze pokemon is van het type ' + ', '.join(type_list1))

attack = stats1[4]
stat_value = attack['baseStat']
# print('Attack = ' + str(stat_value))
pokemon1_list = []
pokemon1_list.append('Attack')
pokemon1_list.append(stat_value)
table = []
table.append(pokemon1_list)
print('Pokémon nummer 1: ' + pokemon1_naam)
print('Type ' + ', '.join(type_list1))
print (tabulate(table, headers=["Stat", "Value"]))
