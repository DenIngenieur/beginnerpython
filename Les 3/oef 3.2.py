# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 17:00:16 2021

@author: rudy
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 14:26:05 2020

@author: rudy
"""

def stringNaarGetal(invoer):
    """
    Zet een string om naar een getal, als die string effectief een 
    numerieke waarde voorstelt. Dit is inclusief wetenschappelijke 
    notatie. In dit geval is wetenschappelijke notatie uitgebreid, 
    de exponent kan ook een decimaal getal zijn!

    Parameters
    ----------
    invoer : String
        Een string die een getal bevat.

    Returns
    -------
    getal : float
        Het getal van de invoer als float.
    """ 

    invoer = invoer.strip().lower() # verwijder spaties, karakters lowercase
    
    # als het een 'e' of 'E' bevat, dan is het wetenschappelijke notatie
    # in dat geval splitsen we in mantisse en exponent
    plaatsE = invoer.find('e') # -1 als niet gevonden!
    if(plaatsE == -1):
        getal = float(invoer)       
    else:
        mantisse = float(invoer[0:plaatsE])
        exponent = float(invoer[plaatsE + 1 ::])
        getal = mantisse * 10**exponent
        
    return getal
  
      

naam = input("Geef uw naam: ")

lijst = [] # maak een lege lijst om getallen op te slaan
som = 0 # initialiseer variabele

# creëer een oneindige loop
while(True):
   invoer =  input('Voer een getal in (of een letter om te stoppen): ')
   # een letter zal ons een ValueError geven
   try:
       getal = stringNaarGetal(invoer)
   except ValueError:
       break
   lijst.append(getal)
   som += getal
   
gemiddelde = som/len(lijst)
print()
print(f"Dag {naam}, het gemiddelde van {lijst} is: {gemiddelde}.")
