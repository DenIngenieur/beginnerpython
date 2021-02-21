# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 14:26:05 2020

@author: rudy
"""

invoer = '  -2.103805  '

# test alle randgevallen !!!
# invoer = ''
# invoer = '0'
# invoer = '-0'
# invoer = '1'
# invoer = '-1'
# invoer = '.1'
# invoer = '-.1'


numString = invoer.strip() # verwijder spaties voor en achter

if(numString == ''):
    raise SystemExit('Geen invoer!')

print ('numString = ', numString)


##########################
# controle eerste kerakter
##########################

teken = 1 # dit gebruiken we voor positief/negatief
start = 0 # als er geen min (of plus) staat, dan begint het getal op positie 0
if(numString[0].isnumeric()):
    pass # dit doet niets, wil zeggen: ga maar door
elif(numString[0] == '+'): # moest iemand een + ingeven, dat is legaal
    start = 1 # als er een plus staat, dan begint het getal op positie 1
elif(numString[0] == '-'):
    teken = -1
    start = 1 # als er een min staat, dan begint het getal op positie 1
elif(numString[0] == '.'): # we accepteren decimale getallen started met punt
    # we verwachten een nummer als eerste cijfer, dus plakken we een 0 vooraan
    numString = '0' + numString 
else:
    raise SystemExit("Geen geldig teken!") # in de loop wordt dit continue!
    

################
# alternatief 1 
################

# nieuweString = ''
# machtTien = 0
# puntGevonden = False

# for plaats, karakter in enumerate(numString[start::]):
#     if(karakter.isnumeric()):
#         nieuweString += karakter
#     elif(karakter == '.' and puntGevonden == False):
#         puntGevonden = True # max 1 decimaal punt!
#         machtTien = len(numString[start::]) - plaats - 1
#         print ('Decimaal punt gevonden op plaats:', plaats)
#     else:
#         raise SystemExit("Ongeldige invoer!") # in de loop wordt dit continue!
   

################
# alternatief 2
################

nieuweString = numString[start::]    
machtTien = 0 

aantalPunten = nieuweString.count('.') 
print('Aantal decimale punten', aantalPunten)
if(aantalPunten > 1):
    raise SystemExit('Ongeldige invoer, meer dan 1 decimaal punt!') # in de loop wordt dit continue!

if(aantalPunten == 1):
    plaatsDecimaal = nieuweString.find('.')
    machtTien = len(numString[start::]) - plaatsDecimaal - 1
    print ('Decimaal punt gevonden op plaats:', plaatsDecimaal)
    # verwijder decimaal punt
    nieuweString = nieuweString[0 : plaatsDecimaal] + nieuweString[plaatsDecimaal + 1 ::]

if(not(nieuweString.isnumeric())):
    raise SystemExit('Ongeldige invoer!') # in de loop wordt dit continue!
     
    
##########
# uitkomst
##########
    
print('Nieuwe string =', nieuweString)

getal = int(nieuweString)
getal *= teken
getal /= 10**machtTien

print('getal =', getal)
        
    