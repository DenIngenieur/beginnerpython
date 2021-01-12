# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 18:11:19 2021

@author: rudy
"""

def integerNaarRomeins(getal):
    if type(getal) != int:
        raise ValueError
        
    if getal < 1 or getal > 3999:
        raise ValueError
        
    romeinsGetal = ''
    symbolen = { 
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 
        40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 
        500: 'D', 900: 'CM', 1000: 'M'}

    volgorde = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
     
    for x in volgorde:
        if getal != 0:
            quotient = getal//x # gehele deling
     
            # quotient niet nul: tel het aantal symbolen, en voeg ze toe
            if quotient != 0:
                for i in range(quotient):
                    romeinsGetal += symbolen[x]
         
            # zet getal nu gelijk aan de rest van de gehele deling -> modulo
            getal = getal % x
        else:
            break # rest getal = 0, einde bereikt
 
    return romeinsGetal



def romeinsNaarInteger(romeinsGetal):
    getal = 0
    symbolen = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 
        'C': 100, 'D': 500, 'M': 1000}

    romeinsGetal = romeinsGetal.strip().upper()
    # het langste wat we hebben is 3888, 15 tekens lang
    if len(romeinsGetal) > 15:
        raise ValueError
    
    # alleen de toegestane symbolen in de string? 
    toegestaan = set(symbolen.keys()) # converteer naar set
    invoer = set(romeinsGetal)
    # kijk of invoer een deel is van toegestaan
    if not invoer.issubset(toegestaan):
        raise ValueError # geen subset
        
    vorigSymbool = romeinsGetal[0]
    getal = symbolen[vorigSymbool]
    for i in range(1,len(romeinsGetal)):
        huidigSymbool = romeinsGetal[i]
        
        # Als het huidige symbool een grotere waarde heeft dan het 
        # vorige symbool, dan moeten we het huidige bijtellen en 2 keer
        # het vorige aftrekken omdat we het vorige de vorige keer een  
        # keer te veel hebben opgeteld. Met andere woorden, als het 
        # huidige symbool een grotere waarde heeft dan het vorige symbool
        # mochten we het vorige er eigenlijk niet bij optellen.
        # IX = 9, we tellen 1 bij de eerste keer, we tellen dan 10 bij maar 
        # moeten 2*1 aftrekken omdat we de eerste keer 1 niet mochten bijtellen 
        # en de tweede keer nog een 1 moeten aftrekken van 10.
        if symbolen[huidigSymbool] > symbolen[vorigSymbool]:
            getal += symbolen[huidigSymbool] - 2 * symbolen[vorigSymbool]
        else:
            getal += symbolen[huidigSymbool]

        vorigSymbool = huidigSymbool
    
    return getal



# zoek het langste romeinse cijfer (meeste karakters)
max = 0
langste = ''
for i in range(1,4000):
    romeins = integerNaarRomeins(i)
    if max < len(romeins):
        max = len(romeins)
        langste = romeins
    if len(romeins) > 12:
        print('i:', i, 'romeins:', romeins, 'lengte =', len(romeins))

print('lengte', max)
print('langste', langste)
print('waarde:', romeinsNaarInteger(langste))

# zet integer om naar romeins
# while True:
#     try:
#         getal = int(input("Geef een positief geheel getal (< 4000): "))
#     except ValueError:
#         break
#     romeins = integerNaarRomeins(getal)
#     print('romeins:', romeins)
#     print('terug:', romeinsNaarInteger(romeins))

# zet romeins om naar integer
# while True:
#     romeins = input("Geef een geldig romeins getal (Enter = stop): ")
#     if romeins == '':
#         break
#     getal = romeinsNaarInteger(romeins)
#     print('getal:', getal)
#     print('terug:', integerNaarRomeins(getal))
