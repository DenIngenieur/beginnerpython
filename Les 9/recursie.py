# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 11:14:31 2021

@author: rudy
"""
from time import time_ns

# decorator om tijd te meten. Zie les 4.
def meetTijd (teTimenFunctie):
    def omhulsel(*args, **kwargs):
        start = time_ns()
        result = teTimenFunctie(*args, **kwargs)
        stop = time_ns()
        print('Start =', start, "stop =", stop)
        print('Tijd gemeten: {} seconden'.format((stop-start)/10e9))
    
        return result
    
    return omhulsel


#%% recursie
# faculteit: vermenigvuldig alle getallen tot en met n
# 5! = 5*4*3*2*1

def faculteit(n):
    print ("De functie werd opgeroepen met n = " + str(n))
    if n == 0: # dit is de stop conditie
        print ("n = 0")
        return 1
    else:
        resultaat = n * faculteit(n-1) # recursieve oproep
        print ("tussentijds resultaat voor n= ", n, " * fuculteit(", n-1, "): ", resultaat)
    return resultaat


# alles wet je recursief kunt berekenen kun je ook zonder recursie doen
def iteratieveFaculteit(n): 
    resultaat = 1 
    for i in range(2,n+1): 
        resultaat  *= i 
    return resultaat

print('faculteit berekenen')
print ('faculteit(5) =', faculteit(5))
print 
print('iteratief faculteit berekenen')
print ('iteratieveFaculteit(5) =', iteratieveFaculteit(5))


#%% Memoization
# Fibonacci serie: 0,1,1,2,3,5,8,13,21,34,...som van de 2 voorgaande

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print('fibonacci nummer berekenen')
print ('fib(6) =',  fib(6))
f1 = meetTijd(fib) # gebruik de decorator meetTijd
print()
print ('fib(35) =',  f1(35))

# De memoization cache is een dictionary met als key n en als value de waarde
# die bij die n hoort. 
# We initialiseren de dictionary met de eerste 2 Fibonacci nummers: 
memo = {0:0, 1:1}
 
# De functie slaat de berekende waarde op in memo, als die er nog niet in zit.
def fibMemo(n):
    if not n in memo:
        memo[n] = fibMemo(n-1) + fibMemo(n-2)
    return memo[n]

print()
print('fibonacci nummer berekenen met memoization')
print ('fibMemo(6) =',  fibMemo(6))
print()
f2 = meetTijd(fibMemo) # gebruik de decorator meetTijd
print ('fibMemo(40) =',  f2(40)) 
print()
print ('fibMemo(42) =',  f2(42)) 
print()
print ('fibMemo(402) =',  f2(402)) 


#%% Memoization ingebouwd
# Fibonacci serie: 0,1,1,2,3,5,8,13,21,34,...som van de 2 voorgaande

from functools import lru_cache # import memoization

@lru_cache(maxsize = 5)
def fibLruCache(n):
    if n < 2:
        return n
    else:
        return fibLruCache(n-1) + fibLruCache(n-2)

print()
f3 = meetTijd(fibLruCache) # gebruik de decorator meetTijd
print()
print ('met lru cache fib(402) =',  f3(402))