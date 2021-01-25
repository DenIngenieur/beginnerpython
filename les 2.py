# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 15:05:17 2020

@author: rudy
"""

#%% beslissingen
print('Beslissingen')

a = 1
print('a =', a)
print('a == 1:', a == 1)
print('a != 1:',a != 1)
print('a < 1:',a < 1)
print('a > 1:',a > 1)
print('a <= 1:',a <= 1)
print('a >= 1:',a >= 1)

if(a==1):
    print('dit is een code block') 
    print('a is gelijk aan 1')
    print('nog steeds in het code block')
print('uit het code block')
    
# anders...
a += 1
if(a!=1):
    print('a is niet gelijk aan 1')
else:
    print('a is gelijk aan 1')
    
c = '123'
d = '456'
# d = 'abc'

if (c.isnumeric()):
    print('c bevat een numerieke waarde')
if (d.isnumeric()):
    print('d bevat een numerieke waarde')

if (c.isnumeric() or d.isnumeric()):
    print('c OF d bevatten een numerieke waarde')
    
if(c.isnumeric()):
    if(d.isnumeric()):
        print('c EN d bevatten een numerieke waarde')

# bovenstaande is identiek aan:
if(c.isnumeric() and d.isnumeric()):
    print('c EN d bevatten een numerieke waarde')
    
# anders...
if(d.isnumeric()):
    print('d bevat een numerieke waarde')
else:
    print("d bevat GEEN numerieke waarde")
    
# anders anders...
a = 0

if (a == 1):
    print("a is gelijk aan 1")
elif (a == 2):
    print("a is gelijk aan 2")
elif (a >= 3):
    print("a is gelijk aan of groter dan 3")
else:
    print("geen idee wat a is...")
        


# %% for loops
print()
print("Loops - for loops")
str1 = 'ongeloofelijk'

print('Er is een o in ongeloofelijk:', 'o' in str1)
print('Er is een a in ongeloofelijk:', 'a' in str1)

print()

# de letters i, j en k worden frequent gebruikt in loops!
# i krijgt eerst de eerste waarde in range, zijnde 0, dan
# wordt er 1 bij opgeteld, net zolang i kleiner is dan
# de lengte van de string str1
for i in range(0, len(str1)):
    print(str1[i], end=", ")

print()
# de 0 is niet noodzakelijk in de range als je van 0 begint
for i in range(len(str1)-1):
    print(str1[i], end=", ")
print(str1[-1])  # laatste waarde -> slicing!

print()
print("niet vanaf het begin:")
# python is de enige programmeertaal die ik ken waar een 
# else voorkomt bij loops!
for i in range(3, len(str1)-1):
    print(str1[i], end=", ")
else:
    print(str1[i+1])  # i+1 -> geen slicing!
    
print()
print("met gebruik van het keyword in:")
for letter in str1:
    print(letter, end=" ")
else:
    print()
            
print()
print("met gebruik van enumerate")
for i, letter in enumerate(str1):
    print(f'str1[{i}] = "{letter}"', end=" ")
print()
    
    
#%% break en continue    
print()
print('else block niet uitgevoerd bij een break!')
for i in range(11):
    print(i, end=' ')
else:
    print("Einde!")
print("Dit wordt altijd geprint!")
    
# break
for i in range(11):
    print(i, end=' ')
    if(i==6):
        print('Oeps, een break!')
        break
else:
    print("Einde!")
print("Dit wordt altijd geprint!")

# continue
for i in range(len(str1)):
    if (i>3 and i<6):
        continue
    print(i, str1[i])


# %% while loops
print()
print("Loops - while loops")
str2 = 'fantastisch'

print('i=', i)
# belangrijk om de loop variabele te initialiseren !!!
i = 0
while (i < len(str2)):
    print(i, str2[i])
    i += 1 # niet vergeten !!!!
# else:
#     print('klaar')
    
print()
print('oneindig loopen...')
while True:
    print(i)
    i += 1 # niet vergeten !!!!
    if (i > 15):
        break


#%% lists
print()
print('Lists')

# variabelen worden gebruikt om een waarde op te slaan
# wat als we vele waarden hebben? 
# een kleurfoto van slechts 100x100 pixels bevat 10000x3 = 30000 waardes!

lijst = [] # lege list
fruitLijst1 = ["appels", "peren", "bananen"]

print()
for i in range(len(fruitLijst1)):
    print(fruitLijst1[i])

for fruit in fruitLijst1:
    print(fruit)
    
for i, fruit in enumerate(fruitLijst1):
    print(f'[{i}] = {fruit}')
   
print()
print('slicing werkt ook:', fruitLijst1[-1])

fruitLijst2 = ['sinaasappelen', 'druiven']

print()
print (fruitLijst1 + fruitLijst2)

print()
print (fruitLijst2 * 3)

print()
print (fruitLijst1.index('peren'))

# f is een alias! Geen kopie!
f = fruitLijst1
f.reverse()
f.append('bosbessen')

print()
print(fruitLijst1)

# nu is f een kopie!
f = fruitLijst1.copy()

f.sort()
print()
print("fruitLijst1 =", fruitLijst1)
print("f =", f)

f.remove("bosbessen")
print()
print(f)

f.pop()
print()
print(f)

f.insert(1,"bosbessen")
print()
print(f)

# lists kunnen meerdere dimensies hebben, 
# en verschillende soorten data bevatten
lijstVanLijsten = [[1,2,3,4],['a','b','c'],[1,3.1415,'Rudy']]
print()
print(lijstVanLijsten)
print(lijstVanLijsten[2][2])


#%% tuples - lists die immutable zijn
"""
Tuples zijn hetzelfde als lists, buiten dat ze immutable zijn, 
dat wil zeggen, overanderbaar. Eens gemaakt, kun je ze niet meer 
aanpassen. Tuples zijn sneller dan lists, en je kunt ze ook gebruiken 
om verschillende variabelen in te pakken (en weer uit te pakken nadien).
"""

print()
print('Tuples')

t = ('appels', 'bananen', 'peren', 'appels')
print(t.count('appels'))

# tuple met maar 1 element:
t1 = (5,)

# uitpakken
f1,f2,f3,f4 = t
print (f2)


#%% dictionary - dict
"""
Dicts zijn een soort lijsten, die een key - value paar hebben, oftewel
een sleutel - waarde. Dit is handig om data op te slaan en snel terug 
op te halen aan de hand van de sleutel. 
"""

print()
print('Dicts')

maanden = {
    1 :'Januari',
    2 : 'Februari',
    3 : 'Maart',
    4 : 'April',
    5 : 'Mei',
    6 : 'Juni',
    7 : 'Juli',
    8 : 'Augustus',
    9 : 'September',
    10 : 'Oktober',
    11 : 'November',
    12 : 'December'        
}

kleuren = {'rood' : '#ff0000', 'groen' : '#00ff00', 'blauw' : '#0000ff'}

print()
print(maanden[3])

print()
print(kleuren['rood'])

print()
for key in maanden:
    print(f'sleutel = {key}, waarde = {maanden[key]}')
  
print()
for kleur in kleuren.items(): # geeft tuples terug!
    print(kleur)

print()
# je kunt de tuples ook uitpakken!
for kleurNaam, kleurCode in kleuren.items():
    print(f'naam = {kleurNaam}, code = {kleurCode}')
    
kleuren['r'] = '#ff000'

print()
print(kleuren.keys())
print(kleuren.values())

k = kleuren.pop('r')
print()
print(kleuren.keys())
print(kleuren.values())
print(k)

## sets
"""
Sets zijn vergelijkbaar met verzamelingen uit de wiskunde.
Ze kunnen allerlei elementen bevatten, maar elk element slechts 
één keer. Je kunt sets dan ook gebruiken om dubbels uit te filteren. 
"""

print()
print('Sets')

print()
set1 = {1, 2, 3}
print(set1)

# set mixed 
set2 = {1.0, "Hello", (1, 2, 3)}
print(set2)

set1.add(4)
print()
print("4 toegvoegd, geeft:", set1)

set1.add(2)
print()
print("2 toegevoegd, geeft:", set1)

fruitLijst =  ["appels", "peren", "bananen", "appels"]
fruitSet = set(fruitLijst) # cast naar set!

print()
print("lijst:", fruitLijst)
print("set:", fruitSet)

s1 = fruitSet.copy()
fruitSet.add('druiven')
s2 = fruitSet.copy()

print()
print("set + druiven:", fruitSet)

print()
print("s1:", s1)
print("s2:", s2)
print("gemeenschappelijk:", s1.intersection(s2))
print("verschil:", s2.difference(s1))
print("verschil:", s1.difference(s2))

print()
print('Frozen Sets - niet aanpasbaar!')
"""
Frozen sets zijn immutable! 
"""

fruitSetFrozen = frozenset(fruitLijst) # cast naar frozenset!
print()
print(fruitSetFrozen)

# fruitSetFrozen.add('druiven') -> kan niet !!!!


#%% binair, octaal, hewadecimaal en ASCII karakters...
"""
binair: 0 en 1: de basis van de computer (base 2)
octaal: 0-7: samentrekking van 3 bits (base 8)
decimaal: 0-9: wat we normaal gebruiken (base 10)
hexadecimaal: 0-F: samentrekking van 4 bits (base 16), waarbij A=10,
B=11, C=12, D=13, E=14 en F=15

ASCII: 255 karakters, waarvan de eerste 32 controle karakters zijn.
Staat voor American Standard Code for Information Interchange.
"""

print()
print('decimaal, binair, octaal, hexadecimaal')

print()
for i in range(256):
    print(f'd: {i} \t b: {bin(i)} \t o: {oct(i)} \t h: {hex(i)}, ')

print()
# kontrole karakters:
# for i in range(32):
#     print(f'karakter {i} = {chr(i)}, ')
    
print()
print('normale karakters:')
for i in range(32,256):
    print(f'karakter {i} = "{chr(i)}"')
    # print(f'ascii karakter {i} = {(chr(i)).encode(encoding="ascii",errors="ignore")}')
    # print(f'utf-8 karakter {i} = {(chr(i)).encode(encoding="utf-8",errors="ignore")}')

txt = "Naam: Vebjørn Ståle"
print()
print(txt)
print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

print()
print ('ASCII code voor a:', ord('a'))
