# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 10:52:52 2020

@author: rudy
"""
# oefening 1
# programma dat:
#     naam vraagt
#     een aantal getallen die de gebruiken invoert
#     invoer stopt als men een letter invoert
#     daarna wordt gemiddelde berekend
#     tekst getoond:
#         Dag <naam>, het gemiddelde van de getallen <1, 2, 3> is 2.

naam = input("Geef uw naam: ")

lijst = [] # maak een lege lijst om getallen op te slaan
som = 0 # initialiseer variabele

# creëer een oneindige loop
while(True):
   getal =  input('Voer een getal in (of een letter om te stoppen): ')
   # bemerk de not, that Van True False maakt en omgekeerd
   if(not(getal.isnumeric())):
       break
   lijst.append(getal)
   som += int(getal)
   
gemiddelde = som/len(lijst)
print()
print(f"Dag {naam}, het gemiddelde van {lijst} is: {gemiddelde}.")