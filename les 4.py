# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 11:59:14 2021

@author: rudy
"""
#%% Functies zijn objecten - zoals alles in Python
print()
print('Functies zijn objecten')

# kunnen toegewezen worden aan een variabele
p = print

p()
p('print functie in variabele p')
p('hello')
p(p)
print(print)

# functies in een dictionary
functieDict = {
    'lower': str.lower,
    'print': print,
    'range': range,
    'tel': len
    }

p()
functieDict['print']('Functies in een dictionary')
functieDict['print'](functieDict['lower']('RUDY'))
functieDict['print'](functieDict['tel']('RUDY'))


#%% Scope - nonlocal
"""
Scope - nonlocal, dit is een tussenlevel van scope, tussen global (beschikbaar                                                          ) 
voor het ganse programma) en local (enkel beschikbaar voor het huidige code
block). De variabele is nonloval voor een functie als die functie in een 
andere functie vervat zit, en de variabele gedefinieerd is in die buitenste 
functie.                                    
"""
print()
print('Scope - nonlocal')

def buitensteFunctie():
    # test variable
    test = 'Python'  # nonlocal variabele voor binnensteFunctie
    
    def binnensteFunctie():
        # gebruik keyword nonlocal om aan te geven dat we de variabele 
        # buiten de scope van binnenstefunctie gebruiken
        # gelijkaardig aan global (les 3.2), maar de scope van test is nu 
        # die van de buitensteFunctie
        nonlocal test # je wil de oorspronkelijke variabele gebruiken
        test = 'Scope' # hier creëer je een nieuwe variabele zonder nonlocal
        print('In binnenste functie: ', test)
    # probeer te veranderen door binnensteFunctie op te roepen
    binnensteFunctie()
    # controleer 
    print('In buitenste functie: ', test)

buitensteFunctie()



#%% Closure
"""
Closure: het intern geheugen van een geneste functie. 
Bevat al de nonlocal variabelen (een scope tussen global en local) 
die nodig zijn om de functie te runnen, in een tuple. 
Eens een variabele in een closure zit, kun je die wel gebruiken, maar 
niet wijzigen, zelfs niet als het origineel verwijderd of gewijzigd wordt. 
"""
print()
print('Closure')

def buitensteFunctie(tekst):
    extra = 'zomaar iets'
    def binnensteFunctie():
        e = extra + '!' # extra niet gebruiken, niet bijgehouden
        print (tekst)
    return binnensteFunctie # zonder de haakjes! Geeft reference naar functie

print()
a = buitensteFunctie('Hallo!')
a() # met de haakjes is een functie call (oproep)
print(a.__closure__)
print()
for cell in a.__closure__:
    print ('in cell ', cell.cell_contents)

print()
del buitensteFunctie # functie deleten
# buitensteFunctie('Hallo!') # functie aanroepen geeft nu een fout
a() # de tekst werd onthouden in binnensteFunctie


#%% Decorators - principe
"""
Decorators omhullen een functie en wijzigen het gedrag zonder de code van 
de functie te wijzigen. 
"""
print()
print('Decorators - principe')

def decoratorFunctie(functieAlsParameter):
    def omhulselFunctie():
        print('#='*10+'#')
        functieAlsParameter()
        print('*-'*10+'*')
        
    return omhulselFunctie # zonder de haakjes! Geeft reference naar functie

def halloFunctie1():
    print('Hello World!')
 
print()
hallo1 = decoratorFunctie(halloFunctie1)
hallo1()

@ decoratorFunctie
def halloFunctie2():
    print('Hello World too!')

print()
hallo2 = halloFunctie2()

hallo3 = decoratorFunctie(halloFunctie2)
print()
hallo3()

def decorator1(functieAlsParameter):
    def omhulselFunctie():
        print('1'*20)
        functieAlsParameter()
        print('1'*20)
        
    return omhulselFunctie # zonder de haakjes!!!


def decorator2(functieAlsParameter):
    def omhulselFunctie():
        print('2'*20)
        functieAlsParameter()
        print('2'*20)
        
    return omhulselFunctie # zonder de haakjes!!!

@ decorator1
@ decorator2
def halloFunctie3():
    print('Hello World 3!')
    
@ decorator2
@ decorator1
def halloFunctie4():
    print('Hello World 4!')
    
print()
halloFunctie3()

print()
halloFunctie4()

 
#%% Decorators - praktischer
print()
print('Decorators - praktischer')

def delingDecorator(functieAlsParameter):
    def omhulsel(x, y):
        print(x, 'gedeeld door', y)
        if y==0:
            print('Deling door nul niet toegestaan!')
            return 'onbepaald'
        return x/y
    
    return omhulsel

@ delingDecorator
def deling(a, b):
    return a/b

print()
print('Deling')
print (deling(10, 5))
print (deling(10, 0))


#%% Decorators - timing
print()
print('Decorators - timing')

from time import time_ns

def meetTijd (teTimenFunctie):
    def omhulsel(*args, **kwargs):
        start = time_ns()
        result = teTimenFunctie(*args, **kwargs)
        stop = time_ns()
        print('Start =', start, "stop =", stop)
        print('Tijd gemeten: {} seconden'.format((stop-start)/10e9))
    
        return result
    
    return omhulsel

@ meetTijd
def teller1(getal):
    som = 0
    for i in range(getal + 1):
        som += i
        
    return som

def teller2(getal):
    som = 0
    for i in range(getal + 1):
        som += i
        
    return som

print()
print('Met annotatie op de functie')
print(teller1(20000))
print(teller1(200000))
print(teller1(2000000))

print()
print('Zonder annotatie op de functie')
t = meetTijd(teller2)
t(20000)
t(200000)
t(2000000)


#%% Inner functies - praktischer
print()
print('Inner functies - praktischer')

def machtN(exponent):
    def totDeMacht(basis):
        return pow(basis, exponent)
    
    return totDeMacht

tweedeMacht = machtN(2) # zet het één keer op

print()
print('Power')

print()


print(tweedeMacht(2)) # zet het één keer op, blijf het gebruiken
print(tweedeMacht(3)) # zet het één keer op, blijf het gebruiken
print(tweedeMacht(4)) # zet het één keer op, blijf het gebruiken

derdeMacht = machtN(3) # flexibel, andere parameter

print()
print(derdeMacht(2))
print(derdeMacht(3))
print(derdeMacht(4))

print(tweedeMacht(2))
   
