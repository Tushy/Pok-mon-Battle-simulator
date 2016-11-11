# Pok-mon-Battle-simulator
Pokémon battle sim
READ ME PBS
POKÉMON BATTLE SIMULATOR
__________________________________________________________________________________________________
1. Beschrijving en gebruikershandleiding Pokémon Battle Simulator
2. Handige tool
3. Systeemvereisten
4. Nawoord van de makers

__________________________________________________________________________________________________

Welkom bij Pokémon Battle Simulator (PBS)

Om het programma te starten open je "PBS.py".

Dit is een programma om twee Pokémon met elkaar te vergelijken, en een gevecht te simuleren. 
Het programma is te gebruiken met één speler en met twee spelers. 

Er zijn twee opties om een Pokémon te selecteren. Wanneer er een Pokémon geselecteerd wordt haalt het programma alle data van de
geselecteerde Pokémon op die gebruikt wordt voor het gevecht. Dit kan helaas even duren als het druk is!
Het is mogelijk om je Pokémon te veranderen tot er op 'Fight!' wordt geklikt.
Wanneer je tevreden bent met de keuze van je Pokémon klikt je op 'Fight!' in het midden van het scherm, en het gevecht begint!

Vanaf het moment dat je het gevecht start worden de aanvallen van je Pokémon geladen. Dit zorgt er voor dat het programma even iets
langzamer is omdat het met internet moet verbinden. 

Zodra de aanvallen van de Pokémon geladen zijn kan je beginnen met het gevecht! 
Klik op de aanval die je wil uitvoeren bij de Pokémon die aan de beurt is. In het tekstveld onderaan het scherm staat hoeveel HP de
vijand nog heeft, en hoeveel schade je dus nog moet aanrichten tot je hebt gewonnen.
Hierna is de andere Pokémon aan de beurt. Ook hier kan je de aanval van de Pokémon selecteren en zie je de resterende HP van de vijand
weer staan. 

Het gevecht is afgelopen als één van de twee Pokémon geen HP meer heeft en knock-out is gegaan.
Gefeliciteerd aan de winnaar!

__________________________________________________________________________________________________

De stats, moves, sprites en namen van alle Pokémons worden gehaald van de PokeApi. 
In de tools map staat een programma dat gebruikt kan worden om te testen of de PokeAPI beschikbaar is voor communicatie.

__________________________________________________________________________________________________

Om het spel te kunnen spelen via Python 3.4 moet je eerst een aantal modules downloaden. 
Download de volgende modules via PIP:
-	Pip install json
-	Pip install requests

Vereisten:
-	Om Pokémon Battle Simulator te spelen heb je een internet connectie nodig. 
-	OS vereisten:

o	Windows 7/8/10

__________________________________________________________________________________________________


Wij hebben er voor gekozen om veel functies op te nemen in één bestand zodat alle data centraal opgehaald worden. Dit is gedaan om de
hoeveelheid requests naar de server van de API te verminderen en de applicatie sneller te laten laden. Wij hebben hierdoor ook 
geprobeert om alle relevante data op te slaan in variabele zodat de functie ook zo min mogelijk wordt gebruikt.
Er zijn een aantal modules gebruikt tijdens de ontwikkeling maar zijn er daar achter gekomen dat dit niet werkt op mac, waardoor we
daar omheen hebben moeten werken.
Wij hebben gebruik gemaakt van threading om de data van de Pokémon tegelijk op te halen zodat het minder lang duurt om de data van
de Pokémon te laden.
