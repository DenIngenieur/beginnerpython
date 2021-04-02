# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 12:17:40 2021

@author: rudy
"""

"""
Magic numbers zijn nummers die in een formule staan. Doorgaans staan ze daar
voor een reden, maar de reden is soms onduidelijk. Daarom worden ze magic 
genoemd. Het lijkt of ze uits het niets verschenen zijn, zonder reden. 
Dit is geen goed idee. Een formule bestaat best uit variabelen en eventueel 
constanten, geen nummers. De uitzondering is als het vanzelfsprekend is, 
bijvoorbeeld de 2 in een kwadraat. 
"""
from math import ceil, modf


"""
Voorbeeld van een oefening (oorspronkelijk voor Java):
Een behanger wenst te weten hoeveel rollen papier hij nodig heeft voor
het behangen van een volledige muur zonder deuren of vensters. 1 rol
behangpapier is 10 m lang en 50 cm breed. De lengte en de breedte van de
muur (=gehele getallen) worden ingevoerd in cm en het programma moet het
aantal rollen meedelen dat de behanger nodig heeft.
"""
#%% initialisatie
lengte = 5*100 # lengte in meter in cm
hoogte = int(2.5*100) # hoogte inm meter naar cm
# hoogte = 4*100 # hoogte inm meter naar cm

oppervlakteRol = 10*100 * 50 # 10m omzetten naar cm
oppervlakteMuur = lengte * hoogte

print(f"Oppervlakte rol in cm²: {oppervlakteRol}, en in m²: {oppervlakteRol/10000}")
print(f"Oppervlakte muur in cm²: {oppervlakteMuur}, en in m²: {oppervlakteMuur/10000}")

#%% eerste poging (// is de gehele deling):
aantalRollen = oppervlakteMuur//oppervlakteRol
print(f"1 - Aantal rollen: {aantalRollen}")

#%% tweede poging (plus 1 rol):
aantalRollen = (oppervlakteMuur + oppervlakteRol)//oppervlakteRol
print(f"2 - Aantal rollen: {aantalRollen}")

#%% derde poging (met het magisch nummer):
aantalRollen = (oppervlakteMuur + oppervlakteRol - 1)//oppervlakteRol
print(f"3 - Aantal rollen: {aantalRollen}")

# Als je deze formule uitwerkt, dan krijg je:
#     oppervlakteMuur/oppervlakteRol + 1 - 1/oppervlakteRol
#     Je ziet direct dat die laatste term onzinnig is, wiskundig gezien.
#     Wat is de eenheid van die -1? 
# De formule werkt natuurlijk, en het resultaat is goed, maar je moet beginnen 
# denken waar die -1 vandaan komt, plus, wiskundig is het niet zinnig. 
# Dit is dus geen goede manier om dit op te lossen.

#%% vierde poging (met floats en afronding naar boven):
aantalRollen = ceil(oppervlakteMuur/oppervlakteRol)
print(f"4 - Aantal rollen: {aantalRollen}")

#%% vijfde poging (rekening houden met verlies - muren zijn nooit recht):
aantalRollen = ceil(oppervlakteMuur/oppervlakteRol)
if(oppervlakteMuur % oppervlakteRol == 0):
    aantalRollen += 1
print(f"5 - Aantal rollen: {aantalRollen}")

#%% zesde poging (rekening houden met verlies - muren zijn nooit recht):
# python heeft geen constanten, maar de conventie is hoofletters voor de naam
OVERSCHOT = 0.2

rest, aantalRollen = modf((oppervlakteMuur + oppervlakteRol)/oppervlakteRol)
print("mathf")
print("rest =", rest)
print("aantal rollen =", aantalRollen)
if (rest < OVERSCHOT and rest != 0):
    aantalRollen += 1
print(f"6 - Aantal rollen: {aantalRollen}")    