# -*- coding: utf-8 -*-
"""
Les 1 van programmeren met Rudy in python.
"""

# dit is commentaar
# dit ook
# commentaar wordt door python genegeerd en is enkel voor mensen!

"""
Dit is een multiline string
maar wordt door python genegeerd
want staat alleen.
Het wordt dan ook aanzien 
als commentaar!
Het staat ook bekend als een docstring - meer later!
"""

#%% sectie 1
a=1

#%% sectie 2
print (a)


#%% Integers - type int - gehele getallen. Zie het variable explorer venster!
print("Integers: gehele getallen")
var1 = 3
var2 = 2

# wijzig variabelen
var1 = var1 + 2
# bemerk de komma in het print statement
print ('var1 is nu:', var1)
# verkorte versie, gaat voor +, -, *, /, // en %
# dit is hetzelfde als var1 = var1 - 2
var1 -= 2
print ('var1 is nu:', var1)
# vermenigvuldiging, deling, gehele deling en rest van een deling
print ("vermenigvuldiging:", var1 * var2)
print ("deling:", var1 / var2)
print ("gehele deling:", var1 // var2)
print ("rest van een deling:", var1 % var2)
# machtsverheffing
print ("machtsverheffing:", var1 ** var2)


#%% Geen maximum voor type int!
print()
var = 100**1000
print ("var =", var)
print("type van var =", type(var)) # type is een python functie
print("var+1 =", var+1)


#%% Floats - type float - decimale getallen. Zie het variable explorer venster!
print() # print nieuwe lijn - leeg
print("Floats: decimale getallen")

var3 = 2/3
print ("var3 =", var3)
print ('type var3 =', type(var3)) # type is een python functie

# opgepast met afrondingsfouten bij floats!
a = 0.1
b = 0.2
# multiline string, wordt geprint zoals het er staat, drie "
print ("""
Afrondingsfouten zijn een gevolg van de omzetting van 
decimaal (wat wij gebruiken om te rekenen, 0-9) naar 
binair (wat de computer gebruikt) en terug.
Iets om te onthouden als je werkt met floats""")
# de f in het print statement staat voor format!
# wat tussen {} wordt uitgevoerd, de rest wordt zo geprint.
print (f'a={a}, b={b}, a+b={a+b}') 
# gebruik de functie round() om af te ronden
print (f'a={a}, b={b}, met round: a+b={round(a+b, 3)}')


#%% Complexe getallen - type complex - voor de wiskundige geesten
# De meeste programmeertalen ondersteunen geen complexe getallen, out 
# of the box, python dus wel. 
print ()
print("Complexe getallen.")
var4 = 4.6 + 8.2j
var5 = 3+2j

print('var4 =', var4, 'var5 =', var5)

print('+', var4+var5)
print('-', var4-var5)
print('*', var4*var5)
print('/', var4/var5)
print('**', var4**var5)


#%% wetenschappelijke notatie - voor grote en kleine getallen
print ()
print("Wetenschappelijke notatie.")

print('5000 is ook te schrijven als 5*10**3 of 5e3')
var6 = 5e3 # e3 is een korte notatie voor * 10**3 
print (var6)
print('0.03 is ook te schrijven als 3*10**(-2) of 3e-2')
var7 = 3e-2 # e-2 is een korte notatie voor * 10**(-2) 
print (var7)

lichtsnelheid = 3e8 # in m/s
afstandAardeZon = 1.5e11 # in m
# variabele bestaande uit meerdere woorden in "CamelCase"
# ik prefereer camelcase
tijdNodigVoorZonlichtOmAardeTeBereiken = afstandAardeZon/lichtsnelheid
print()
print ("Tijd nodig voor licht van de zon om de aarde te bereiken:", 
       tijdNodigVoorZonlichtOmAardeTeBereiken, "seconden, of", 
       tijdNodigVoorZonlichtOmAardeTeBereiken/60, "minuten.")

# variabele bestaande uit meerdere woorden gescheiden door underscore teken
# dit is wat de meeste python programmeurs gebruiken, maar het is niet meer 
# dan een overeenkomst
gravitatieconstante = 6.674e-11 # constante van Cavendish in N*m**2/kg**2
diameter_aarde = 12.750e6 # in m
massa_aarde = 5.9722e24 # in kg

kracht_op_1_kg = gravitatieconstante*massa_aarde/(diameter_aarde/2)**2
# F=m*g -> g=F/m met m = 1kg
g = kracht_op_1_kg

print()
print ("Kracht uitgeoefend op 1 kg =", kracht_op_1_kg, 'N')
print ("Valversnelling g =", g, 'm/s**2')


#%% Strings - type str - letter, woorden en zinnen. Zie het variable explorer venster!
print ()
print("Strings: letters, woorden en zinnen.")

str1 = 'rudy'
print('concatenatie:', str1 + 'tje')
print('vermenigvuldiging:', str1*4)

# je kunt zowel enkele als dubbele quotes gebruiken
# maar...
str2 = "Rudy's boeken"
print (str2)
# de backslash \ staat bekend als het escape karakter!
str3 ='Rudy\'s boeken'
print (str3)
str4 = 'Dit is een quote: "The problem with quotes found on the internet is that they\'re often not true." - Abraham Lincoln.'
print (str4)


#%% Slicing - niet alleen voor strings!
# string = ketting!
print()
print("Slicing - niet alleen voor strings!")
str5 = 'ongeloofelijk'

# we tellen vanaf 0!!!
print (str5[0]) # 1e karakter (positie 0)
print (str5[3:6]) # 4e, 5e en 6e karakter (resp. positie 3, 4 en 5)
print (str5[::2]) # vanaf positie 0, elk 2e karakter
print (str5[::3]) # vanaf positie 0, elk 3e karakter
print (str5[::-1]) # omgekeerd
print (str5[::-3]) # vanaf laatste positie, elk 3e karakter, omgekeerd
print (str5[-1]) # laatste letter
print (str5[-2]) # voorlaatste letter
print ('lengte van deze string =', len(str5)) # functie len geeft lengte string
print (str5[-3:len(str5)]) # laatste 3 letters


#%% Object georiënteerd
# Python is een object georiënteerde taal.
# Alles in python is een object!
# Oproepen van functies met de punt- of dotnotatie!
print()
print("Object georiënteerd")

str6='fantastisch'

print (str6)
print (str6.capitalize())
print (str6.capitalize) # altijd de haakjes gebruiken bij functie!
print (str6.upper()) 

str7 = '123'
str8 = '456'
print(str7.isnumeric()) # dit geeft een boolean terug True/False
print (str7+str8) # concatenatie
# cast naar int 
print (int(str7)+int(str8)) # optelling van de numerieke waardes van de strings
print (float(str7)/float(str8))

print ("Optelling, een beetje anders:", (3).__add__(2))


#%% Object georiënteerd - meer van dat
print()
print("Object georiënteerd - meer van dat")

a = int(3)
b = float(3.1415926)
c = complex(2,5)
d = str('een zinnetje')
t1 = bool(1) # alles wat niet 0 is, is true!
f1 = bool(0)
t2 = True
f2 = False

test1 = (a == b)
test2 = (a != b)

print ('a =', a)
print ('b =', b)
print ('c =', c)
print ('d =', d)
print ('t1 =', t1)
print ('f1 =', f1)
print ('t2 =', t2)
print ('f2 =', f2)
print ('test1 =', test1)
print ('test2 =', test2)


#%% Input van gebruikers
print()
print("Input van gebruikers...")

invoer = input("Typ hier iets en druk op enter: ")

print(type(invoer))

print(int(invoer) + 3)

naam = input("Wat is uw naam? ")
print (f'Hallo, dag {naam}!')