# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 17:08:53 2020

@author: rudy
"""

# functies - deel 1

#%% principe
print('Functies - principe')

# code
# meer code
# meer code

x1 = 0.7853981633974483
 
x3 = x1 * x1 * x1
x5 = x3 * x1 * x1
x7 = x5 * x1 * x1
 
f3 = 2 * 3
f5 = f3 * 4 * 5
f7 = f5 * 6 * 7
 
waarde1 = x1 - x3/f3 + x5/f5 - x7/f7
print("waarde1 =", waarde1)

# meer code
# meer code
# meer code

x2 = 1.0471975511965976
 
x3 = x2 * x2 * x2
x5 = x3 * x1 * x2 # OEPS!!!
x7 = x5 * x2 * x2
 
f3 = 2 * 3
f5 = f3 * 4 * 5
f7 = f5 * 6 * 7
 
waarde2 = x2 - x3/f3 + x5/f5 - x7/f7
print("waarde2 =", waarde2)

# meer code
# ...


# Code HERHALEN is ZELDEN een goed idee!!!

# de functie die hetzelfde doet:
# keyword def om de functie te definiëren
def sinus(x):
    x3 = x * x * x
    x5 = x3 * x * x
    x7 = x5 * x * x 
     
    f3 = 2 * 3
    f5 = f3 * 4 * 5
    f7 = f5 * 6 * 7
     
    waarde = x - x3/f3 + x5/f5 - x7/f7
    
    return waarde # keyword return: einde functie, plus kan iets terug geven


print()

a = sinus(x1)
print(f"sinus({x1}) = {a}") # 45° in radialen
print(f"sinus({x2}) = {sinus(x2)}") # 60° in radialen

# de ingebouwde sinus functie uit de math bibliotheek importeren
from math import sin

print()
print(f"sinus({x1}) - sin({x1}) = {sinus(x1) - sin(x1)}")
print(f"sinus({x2}) - sin({x2}) = {sinus(x2) - sin(x2)}")
print(f"waarde2 - sin({x2}) = {waarde2 - sin(x2)}")

"""
Voordelen van functies:
    - geen onnodige herhaling van code
    - herbruikbaar (ook door anderen)
    - verbergen van complexiteit
    - leesbaarder programma
    - opdelen van programma in kleinere delen, beter beheersbaar
    - 1 keer schrijven en testen
    - ...
    
"""


#%% betere sinus functie, met docstring
print()
print ("Functies - betere versie - docstring")

def sinus2(x):
    """
    Dit is de 'docstring'.
    Het commando help(sinus2) zal alles teruggeven wat hier staat. 
    Werkt ook met CTRL + i !!!
    
    Parameters
    ----------
    x : float
        Hoek in radialen.

    Returns
    -------
    waarde : float
        Sinus van de hoek, berekend met reeksontwikkeling.
    """

    faculteit = 1
    teken = 1
    waarde = 0
    for i in range(1, 21, 2):
        waarde += teken * x**i/faculteit
        teken *= -1
        faculteit *= (i+1)*(i+2)
    return waarde


x1 = 0.7853981633974483
x2 = 1.0471975511965976

print()
print("sinus2(x1) =", sinus2(x1))
print("sinus2(x2) =", sinus2(x2))

print(f"sinus2({x1}) - sin({x1}) = {sinus2(x1) - sin(x1)}")
print(f"sinus2({x2}) - sin({x2}) = {sinus2(x2) - sin(x2)}")

print()
print("Help:")
help(sinus2)

#%% demo docstring auto in Spyder

# functie hier
    
    

#%% functie zonder parameters
print()
print('Functies - zonder parameters')

def printLijn():
    print('-'*25)
    print()

print()        
print('Titel')
printLijn()
print('Subtitel')
printLijn()


#%% 1, 2, veel... parameters
print()
print('Functies - 1 of meer parameters')

def dubbel(x):
    return x*2

print()
print(dubbel(2))
print(dubbel('Rudy'))

def telOp(x,y):
    if(type(x) != type(y)):
        print('Parameters moeten hetzelfde type hebben!')
        return
    return x+y

print()
print(telOp(2, 3))
print(telOp('Hello ', 'World!'))
print(telOp(1.2, 3.7))
print(telOp('hello', 3))

print()
def som(*getallen):
    # print(type(getallen), getallen) # best geen print statements in functies!
    s = 0 
    for getal in getallen:
        s += getal
    return s

print()
print(som(1, 2))
print(som(1, 2, 3))
print(som(1, 2, 3, 4))
print(som(1, 2, 3, 4, 5))
print(som())

def gemiddeldResultaat(**punten):
    som = 0
    max = 0
    for key in punten:
        som += punten[key]
        if(max < punten[key]):
            max = punten[key]
            beste = key
    gemiddelde = som/len(punten)
    
    print("punten: ", punten)
    print("gemiddelde =", gemiddelde)
    print("beste vak: ", beste)

gemiddeldResultaat(fysica = 85, biologie = 73, chemie = 55, wiskunde = 91)
gemiddeldResultaat(fysica = 85, biologie = 73)


#%% bij naam en defaults
print()
print('Functies - parameters bij naam - default waardes')

def berekenSnelheid(tijd, afstand):
    snelheid = afstand / tijd
    return f'snelheid = {snelheid} km/u'

print()
print(berekenSnelheid(tijd = 5, afstand = 100))
print(berekenSnelheid(afstand = 150, tijd = 3))
print(berekenSnelheid(3, afstand = 150))


def berekenSoortelijkGewicht(massa = 1000, volume = 1):
    sg = massa/volume
    return f'soortelijk gewicht ρ = {sg} kg/m³'

print()
print('Water:', berekenSoortelijkGewicht()) # geen argumenten, defaults
print('Kwik:', berekenSoortelijkGewicht(189.644, 0.014))
print('Alcohol:', berekenSoortelijkGewicht(massa = 790))
print('Alcohol:', berekenSoortelijkGewicht(790)) # positie van argument
print('Alcohol:', berekenSoortelijkGewicht(volume = 1.2658229))


#%% nesting
print()
print('Functies in functies in functies in...')

def aPlusBMaalC(a,b,c):
    def xMaalY(x,y):
        return x*y
    
    maal = xMaalY(b,c)
    return a + maal

print()
resultaat = aPlusBMaalC(2, 3, 4)
print(resultaat)

def weerAPlusBMaalC(a,b,c):
    def xMaalY():
        return b*c # inner functie ziet de variabelen van de outer functie
    
    maal = xMaalY()
    return a + maal

print()
resultaat = weerAPlusBMaalC(2, 3, 4)
print(resultaat)

