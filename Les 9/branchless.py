# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 13:52:02 2021

@author: rudy
"""
deler = 0
teller = 0
getal = -2


while (deler < 1):
    try:
        deler = int(input("Geef een strikt positieve gehele deler in: "))
    except ValueError:
        print ("Deler moet een geheel getal zijn!")
        
while (getal != -1):
    if (getal % deler == 0 and getal >= 0):
        teller += 1
        
    # branchles versie van de if hierboven
    # teller += (getal % deler == 0 and getal >= 0)
        
    try:
        getal = int(input("Geef een postief geheel getal in (of stop met -1): "))
    except ValueError:
        print ("Voer een geheel getal in!")

if (teller == 1):
    print(f"Er is {teller} getal deelbaar door {deler}.")
else:
    print(f"Er zijn {teller} getallen deelbaar door {deler}.")
