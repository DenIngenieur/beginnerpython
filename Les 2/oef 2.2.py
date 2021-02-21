# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 11:27:57 2020

@author: rudy
"""
# oefening 2
# programma dat:
#     een woord vraagt
#     kijkt of dat woor een palindroom is (dat is een woord dat omgekeerd 
#     gelezen hetzelfde is, mam is een palindroom, mama niet).
#     als het woord een palindroom is:
#         toon de tekst: Het woord "<woord>" is een palindroom!
#     anders:
#         toon de tekst: Het woord "<woord>" is geen palindroom!

#    Uitbreiding:
#         blijf woorden vragen tot men het woord 'stop' intikt

woord = input('Voer een woord in: ')

omgekeerd = woord[::-1]

print()
# converteer beide woorden naar hoofdletters om te kunnen vergelijken,
# want een 'p' is niet hetzelfde als een 'P'
if(woord.upper() == omgekeerd.upper()):
    print(f'Het woord "{woord.lower()}" is een palindroom!')
else:
    print(f'Het woord "{woord.lower()}" is geen palindroom!')
    

# Van https://www.leukespreuk.nl/special_palindromen.htm

#     Daad (4 letters)
#     Dood (4 letters)
#     Raar (4 letter)
#     Kajak (5 letters)
#     Lepel (5 letters)
#     Radar (5 letters)
#     Redder (6 letters)
#     Remmer (6 letters)
#     Racecar (7 letters)
#     Rotator (7 letters)
#     Legovogel (9 letters)
#     Maandnaam (9 letters)
#     Tarwewrat (9 letters)
#     Libellebil (10 letters)
#     Meetsysteem (11 letters)
#     Parterretrap (12 letters)
#     Regelnevenleger (15 letters)
#     Sierterppretreis (16 letters)
#     Edelstaalplaatslede (19 letters)
#     Legermeetsysteemregel (21 letters)
#     Koortsmeetsysteemstrook (23 letters)
#     Nepparterreserretrappen (23 letters)

 
# Langste palindroom

#     Parterrestaalplaatserretrap (27 letters)

# Palindroom zinnen 
# Vanwege de spaties zal dit script ze niet herkennen!
# Hoe kun je dit oplossen? 

#     En er is ananas Irene
#     Koortsmeetsysteemstrook
#     Koos u de garage dus ook?
#     Er is daar nog onraad, Sire.
#     Baas, neem een racecar, neem een Saab