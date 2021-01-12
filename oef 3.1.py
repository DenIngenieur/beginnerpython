# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 10:31:00 2021

@author: rudy
"""

def controleerTijd(tijdString):
    """
    Controleert of een gegeven input een correcte tijd is. 

    Parameters
    ----------
    tijdString : String
        Input van de vorm UxMM of UUxMM, waarbij U voor uur staat en M 
        voor minuut staat, de x is een willekeurig scheidingsteken. 
        Merk op dat we altijd 2 cijfers verwachten voor de minuten. 

    Raises
    ------
    ValueError
        Als de input niet het correcte formaat is, of als de ingegeven tijd
        niet correct is.

    Returns
    -------
    tijd : String
        4 karakters, van de vorm UUMM.
    uren : integer
        Aantal uren.
    minuten : integer
        Aantal minuten.
    """
    tijd = tijdString.strip()
    # 4 tekens, we gaan er van uit dat uur < 10
    if(len(tijd) == 4):
        # vul aan met een 0 vooraan, 9 wordt 09
        # belangrijk voor alfabetische vergelijking
        tijd = '0' + tijd 
    # string nu van de vorm UUxMM, 5 tekens, willekeurig karakter in 't midden
    if(len(tijd) != 5):
        raise ValueError # string te kort of te lang om correct te zijn

    # dit zal automatisch een ValueError geven als het niet lukt 
    uren = int(tijd[0:2])
    minuten = int(tijd[3::])
        
    # kunnen de opgegeven waarden wel? 
    if(uren < 0 or uren > 23):
        raise ValueError
    if(minuten < 0 or minuten > 59):
        raise ValueError
     
    # drop het willekeurig middelste karakter, voor alfabetische vergelijking
    tijd = tijd[0:2] + tijd[3::]
    
    return (tijd, uren, minuten)


def berekenEindTijd(begin, duur):
    """
    Berekent een eindtijd, gegeven een begintijd en een duur. 

    Parameters
    ----------
    begin : String
        Tijd in de vorm UxMM of UUxMM. Waarbij U = uur, M = minuut en x
        een willekeurig scheidingsteken.
    duur : String
        Tijd in de vorm UxMM of UUxMM.

    Returns
    -------
    uren : integer
        Aantal uren.
    minuten : integer
        Aantal minuten.
    """
    beginTijd, beginUren, beginMinuten = controleerTijd(begin)
    duurTijd, duurUren, duurMinuten = controleerTijd(duur)
    
    totaalUren = beginUren + duurUren
    totaalMinuten = beginMinuten + duurMinuten
    # tel bij als minuten > 60, // is gehele deling: 65 // 60 = 1
    uren = totaalUren + totaalMinuten // 60 
    minuten = totaalMinuten % 60 # rest na delen door 60, modulo
    
    return (uren, minuten)
    

def berekenVerschilTijd(begin, einde):
    """
    Berekent het verschil in uren en minuten tussen een gegeven begin en einde.
    Houdt rekening met overgang naar een volgende dag (als einde vroeger is 
    dan begin, dan wordt verondersteld dat we naar een volgende dag gaan).                                                             

    Parameters
    ----------
    begin : String
        Tijd in de vorm UxMM of UUxMM. Waarbij U = uur, M = minuut en x
        een willekeurig scheidingsteken.
    einde : String
        Tijd in de vorm UxMM of UUxMM.

    Returns
    -------
    uren : integer
        Aantal uren.
    minuten : integer
        Aantal minuten.
    """
    
    beginTijd, beginUren, beginMinuten = controleerTijd(begin)
    eindTijd, eindUren, eindMinuten = controleerTijd(einde)
    
    beginInMinuten = beginUren * 60 + beginMinuten
    eindInMinuten = eindUren * 60 + eindMinuten
    
    # vergelijk tijd alfabetisch ('10' < '2' = True, '10' < '02' = False) 
    # 1 komt voor 2, maar 0 komt voor 1, vandaar dat we 0 toevoegen aan 't begin
    # als beginTijd > eindTijd dan passeren we middernacht (22.00 naar 2.00)!
    if(beginTijd < eindTijd):    
        verschil = eindInMinuten - beginInMinuten
    else: 
        # aantal minuten tot middernacht + aantal minuten tot einde
        verschil = 24 * 60 - beginInMinuten + eindInMinuten
    
    uren = verschil // 60
    minuten = verschil % 60
    
    return (uren, minuten)
    

print()
start = '9u30'
duur = '2.15'
uren, minuten = berekenEindTijd(start, duur)
print(f'Start: {start}, duur: {duur}, einde : {uren:02d}:{minuten:02d}.')
start = '6h00'
duur = '2:05'
uren, minuten = berekenEindTijd(start, duur)
print(f'Start: {start}, duur: {duur}, einde : {uren:02d}:{minuten:02d}.')

try:
    uren, minuten = berekenEindTijd('9u3A', '2.15') # letter in tijd? 
except ValueError:
    print('Input is niet correct!')

try:
    uren, minuten = berekenEindTijd('25:30', '2.15') # uur 25?
except ValueError:
    print('Input is niet correct!')
        

print()
start = '10u30'
einde = '11.15'
uren, minuten = berekenVerschilTijd(start, einde)
print(f'Van {start} tot {einde}, duur : {uren} uur {minuten} minuten.')
start = '19u30'
einde = '2.15'
uren, minuten = berekenVerschilTijd(start, einde)
print(f'Van {start} tot {einde}, duur : {uren} uur {minuten} minuten.')
