# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 11:50:13 2020

@author: rudy
"""
#%% Optionele argumenten
print('Functies - optionele argumenten')

def kaas(naam, gaten = None):
    if gaten is None: 
         resultaat = naam + ' is een type kaas zonder gaten'
    else: 
         resultaat = 'Aantal gaten in ' + naam + ' = ' + str(gaten) + '.' 
    print(resultaat)
 
# met gaten: 
kaas('Emmenthal', 1258) 
# zonder gaten:
kaas('Ricotta')

def functie(naam, *punten, **score):
    print(naam)
    print(punten)
    print(score)
    
functie('rudy')
functie('rudy', 1, 2, 3)
functie('rudy', fysica=10, biologie=9)


#%% Scope + try blocks
print()
print('Functies - scope & try')

def f1(arg):
    arg = arg * 5
    return arg

print()
x = 5
print ('return f1: ', f1(x))
print('x =', x)
# print('arg = ', arg)

try:
    print('arg = ', arg)
    #10/0
except NameError: # specifiek, kijkt alleen naar fouten van type NameError
    print('de variabele is niet gedefinieerd')
except: # alle mogelijke fouten, optioneel als specifieke fout except
    print('er was een fout')
else: # optioneel, wordt uitgevoerd als er geen fouten zijn
    print('alles ging goed!')
finally: # optioneel, wordt altijd uitgevoerd, fout of geen fout
    print('dit wordt sowieso geprint...')


# arg en arg zijn verschillend! Lokaal vs globaal
def f2(arg):
    arg = arg * 5
    return arg
 
print()
arg = 5
# de return wordt niet toegekend aan arg
x = f2(arg)
# arg is niet gewijzigd
print('arg = ', arg, ' en x =', x)
# de return wordt wel toegekend aan arg
arg = f2(arg)
print('arg = ', arg)


# defineer een functievariabele als globaal - TE VERMIJDEN!!!
def f3():
    global x 
    x = 10
    
print()
x = 5
f3()
print('x =', x)


# dit geeft een error
# x is reeds een lokale variabele: f4(x)
# def f4(x):
#     global x 
#     x = 10
    
# print()    
# x = 5
# f4(x)
# print('x =', x)

# by reference, by value...
# Datastructuren - list, tuple, dict, set, ... worden meegeven by reference
# dat wil zeggen, de variabele in de functie is een alias voor de doorgegeven
# structuur.
# Simpele variabelen worden doorgegeven by value, de variabele in de functie
# krijgt de waarde van de doorgegeven variabele. 
def f5(arg):
    arg.append(1)
 
print()
x = [5]
f5(x)
print('x =', x)


# het kan verwarrend worden...
def f6(arg):
    arg = arg * 2 # deze arg is lokaal en gelijk aan arg*2
    arg.append(1)
    print('arg in functie =', arg)

print()
x = [5]
f6(x)
print('x =', x)


# strings aijn in feite immutable, alle bewerkingen geven een nieuwe string
def f7(arg):
    arg.upper()
    print('arg upper in functie =', arg.upper())
    print('arg in functie =', arg)
 
print()
x = 'rudy'
f7(x)
print('x =', x)


#%% lambda functies - anonimous / oneline 
print()
print('Functies - lambda funties')

def dubbel(x):
    return 2 * x

def telOp(x,y):
    return x + y 

def maal(x,y,z):
    return x * y * z

print (dubbel(2))
print (telOp(2,3))
print (maal(2,3,4))

# herdefinieren

dubbel2 = lambda x : x * 2
telOp2 = lambda x,y : x + y
maal2 = lambda x,y,z : x * y * z

print()
print (dubbel2(2))
print (telOp2(2,3))
print (maal2(2,3,4))


#%% map - map(func, *iterables)
print()
print('Functies - map')

def fahrenheit(t):
  return round(9/5*t+32,1)
 
def celsius(t):
  return round(5/9*(t-32),1)
 
tempC = (36.5, 37, 37.5, 39)
tempF = (97.7, 98.6, 99.5, 102.2)
f = map(fahrenheit, tempC)
c = map(celsius, tempF) 

print()
# cast naar list voor gebruik
print(list(f))
print(tuple(c))

print() 
fahrenheit2 = map(lambda t: round(9/5*t+32, 1), tempC)
print('naar F met lambda', list(fahrenheit2))
 
celsius2 = map(lambda t: round(5/9*(t-32),1), tempF)
print('naar C met lambda:', tuple(celsius2))
print('2e keer naar C met lambda:', tuple(celsius2)) # slechts 1 keer te gebruiken!

celsius2 = map(lambda t: round(5/9*(t-32),1), tempF)
print('met __next__():', celsius2.__next__()) # private method
print('met __next__():', celsius2.__next__())
print('met __next__():', celsius2.__next__())
print('met __next__():', celsius2.__next__())

# returns een iterable, je kunt dus een loop gebruiken ook
celsius2 = map(lambda t: round(5/9*(t-32),1), tempF)
for t in celsius2:
    print('t =', t)


# bewerking op meerdere lijsten - zelfde lengte!!!
a = [1,2,3,4]
b = [17,12,11,10]
c = [-1,-4,5,9]

print()
resultaat = map(lambda x,y:x+y, a,b)  # resultaat = 1+17, 2+12, 3+11 and 4+10
print(list(resultaat))
 
resultaat = map(lambda x,y,z:x+y+z, a,b,c)
print(list(resultaat))
 
resultaat = map(lambda x,y,z:x+y-z, a,b,c) 
print(list(resultaat))


#%% filter - filter(function or None, iterable)
print()
print('Functies - filter')

fib = [0,1,1,2,3,5,8,13,21,34,55]
print()
resultaat = filter(lambda x: x % 2 , fib) # oneven%2 = 1 dus True
print('resultaat =', list(resultaat))

resultaat = filter(lambda x: x % 2 == 0 , fib) # even
print('resultaat =', list(resultaat))

# met if functie
resultaat = filter(lambda x: True if x>10 else False, fib)
print('resultaat met if =', list(resultaat))

# random lijst met waarden
randomLijst = [1, 'a', 0, False, True, '0']

gefilterd = filter(None, randomLijst) # zonder functie, kijkt naar de waarden

print()
print('originele lijst:', randomLijst)
print('gefilterde elementen:')
# returns een iterable, je kunt dus een loop gebruiken ook
for element in gefilterd:
    print(element)


# filter een lijst met letters, alle klinkers eruit
letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

def filterKlinkersUit(letter):
    klinkers = ['a', 'e', 'i', 'o', 'u']

    if(letter in klinkers):
        return False
    
    return True

gefilterd = filter(filterKlinkersUit, letters)

print()
print('originele lijst:', letters)
print('gefilterde elementen:')
for element in gefilterd:
    print(element)
    

#%% reduce - beter niet gebruiken: erg traag !!!
print()
print('Functies - reduce')

from functools import reduce

som = reduce(lambda x,y: x+y, [47,11,42,13])
print()
print('som =', som)

som = reduce(lambda x, y: x+y, range(1,101)) # 1 t.e.m. 100
print()
print('som =', som)

# lijst naar string met reduce()
strlijst=['I ', 'love ', 'Rudy']
resultaat = reduce(lambda x,y: x+y ,strlijst)
print()
print(resultaat)

nummers = [3, 5, 2, 4, 7, 1]

# eerst conventioneel...
# Minimum
# unpack de lijst in minimum en de lijst rest
minimum, *rest = nummers
for num in rest:
     if num < minimum:
         minimum = num
         
print()
print('minimum =', minimum)

# Maximum
# unpack de lijst in maximum en de lijst rest
maximum, *rest = nummers
for num in rest:
     if num > maximum:
         maximum = num

print('maximum =', maximum)


print()
print('met reduce:')
minimum = reduce(lambda a, b: a if a < b else b, nummers)
maximum = reduce(lambda a, b: a if a > b else b, nummers)
print(minimum, maximum)

print()
print('Check of alle waarden True geven:')
print(reduce(lambda a, b: bool(a and b), [0, 0, 1, 0, 0]))
print(reduce(lambda a, b: bool(a and b), [1, 1, 1, 2, 1]))
print(reduce(lambda a, b: bool(a and b), [], True)) 