# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 14:41:11 2021

@author: rudy
"""

from hashlib import sha256

def MaakHash(tekst):
    return sha256(tekst.encode("ascii")).hexdigest()

def zoeken(blokNummer, transacties, vorigeHash, prefix):
    prefixString = '0' * prefix
    nonce = 0 # https://en.bitcoin.it/wiki/Nonce
    
    while True:
        tekst = str(blokNummer) + transacties + vorigeHash + str(nonce)
        hashNummer = MaakHash(tekst)
        
        if hashNummer.startswith(prefixString):
            break
        
        nonce += 1
    
    print(f"Woehoe! Bitcoin nonce = {nonce} gevonden!")
    return hashNummer


# transacties =  '''
# Ann => Bob: 2 BTC
# Bob => Clara: 0.5 BTC
# Liesbet => Rudy: 3.25 BTC
# Jozef => Maria: 1.5 BTC
# '''

transacties =  '''
Liesbet => Rudy: 3.25 BTC
Jozef => Maria: 1.5 BTC
'''

# dit is het aantal nullen waarmee de hash moet beginnen
moeilijkheidsgraad = 4


import time
start = time.time()

hashNummer = zoeken(
    17895,
    transacties,
    '0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7', 
    moeilijkheidsgraad
)

print(f"Tijd verlopen: {time.time() - start} seconden.")
print()
print(hashNummer)