# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 13:43:34 2020

@author: rudy
"""

# de winkel:
#     Uw vriendin heeft een zeer gespecialiseerde chocoladewinkel.
#     Ze verkoopt repen chocolade, maar er zijn maar 3 soorten repen 
#     beschikbaar: witte-, zwarte- en melkchocoladerepen. 
#     Witte kost 1.2 euro/reep, zwarte 1.3 en melk 1.5. 
#     Uw vriendin vraagt u om een kassasysteem te maken.
#     De vereisten zijn:
#         de kassa begint met een bepaalde voorraad, eventueel ook met een 
#          kleine hoeveelheid geld
#         men geeft telkens in hoeveel repen wit, zwart en melk een klant koopt
#         dan toont het systeem hoeveel de klant moet betalen, en hoeveel er nog 
#          in voorraad is van elke soort
#         belangrijk: een klant kan niet meer kopen dan dat er in voorraad is, 
#          het systeem moet een waarschuwing geven als dat gebeurd en de invoer 
#          weigeren
        
#     Uitbreiding:
#         de leverancier komt langs
#         geef negatieve waarden in voor het aantal geleverde repen
#         de voorraad moet aangevuld worden met deze waarden
#         de winst op wit is 10 cent, op zwart 12 cent en op melk 15 cent, dus de 
#          inkoopprijs is goedkoper dan de verkoopprijs
#         uw vriendin kan alleen betalen met het geld dat in de kassa zit, en 
#          kan niet meer kopen dan waar ze geld voor heeft, het systeem moet de 
#          invoer weigeren als er niet genoeg geld beschikbaar is.  

witInkoopPrijs = 1.1
zwartInkoopPrijs = 1.18
melkInkoopPrijs = 1.35

winstWit = 0.10
winstZwart = 0.12
winstMelk = 0.15

startAantalWit = 10
startAantalZwart = 10
startAantalMelk = 10

kassa = 10 # startkapitaal 

wit = {'type' : 'witte chocolade',
       'voorraad' : startAantalWit,
       'inkoop' : witInkoopPrijs,
       'verkoop': witInkoopPrijs + winstWit
       }

zwart = {'type' : 'zwarte chocolade',
        'voorraad' : startAantalZwart,
       'inkoop' : zwartInkoopPrijs,
       'verkoop': zwartInkoopPrijs + winstZwart
       }

melk = {'type' : 'melkchocolade',
        'voorraad' : startAantalMelk,
       'inkoop' : melkInkoopPrijs,
       'verkoop': melkInkoopPrijs + winstMelk
       }

stock = {'wit' : wit, 'zwart' : zwart, 'melk' : melk}

while(True):
    aantalWit = input('Geef het aantal witte repen (geheel getal!): ')
    aantalZwart = input('Geef het aantal zwarte repen (geheel getal!): ')
    aantalMelk = input('Geef het aantal melk repen (geheel getal!): ')
    
    # herbegin als geen integer
    if(not(aantalWit.isnumeric()) or 
       not(aantalZwart.isnumeric()) or
       not(aantalMelk.isnumeric())): 
        print('Gelieve een geheel getal in te geven!')
        continue
    
    # converteer naar integer en steek in dict, met zelfde keys als stock
    aantal = {'wit' : int(aantalWit), 
             'zwart' : int(aantalZwart), 
             'melk' : int(aantalMelk)
             }
     
    # herbegin als geen voldoende voorraad is
    teWeinigVoorraad = False
    for key in aantal:
        if(aantal[key] > stock[key]['voorraad']):
            print()
            print(f"Maar {stock[key]['voorraad']} {stock[key]['type']} repen meer in voorraad!")
            teWeinigVoorraad = True
    if(teWeinigVoorraad):
        continue
   
    # update voorraad en bereken prijs
    teBetalen = 0
    for key in aantal:
        stock[key]['voorraad'] -= aantal[key]
        teBetalen += stock[key]['verkoop'] * aantal[key]
    teBetalen = round(teBetalen, 2) # opgelet met afrondingen - gebruik round
    
    # opgelet met afrondingen - gebruik round
    kassa = round(kassa + teBetalen, 2) # stop geld in de kassa
    
    print()
    print(f'Te betalen: € {teBetalen}.')

    # print voorraad uit, plus kassa
    print()
    for key in stock:
        print(f"Voorraad {key}: {stock[key]['voorraad']} stuks.")
        
    print(f'Totaal in kassa: € {kassa}.')
    
    # winkel sluiten, kassa afsluiten
    afsluiten = input('Druk op enter voor verder doen, of s + Enter om te stoppen. ')
    if(afsluiten.lower() == 's'):
        print()
        print(f'Totaal in kassa: € {kassa}.')
        break
    
print("Goed gewerkt! Prettige dag nog.")
