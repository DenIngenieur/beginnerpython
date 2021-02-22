# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 11:19:45 2021

@author: rudy
"""
#%% OS- folders en files

# import de os module
import os

print()
print ('OS- folders en files')

print()
print ('huidige directory (folder):', os.getcwd())

print()
# de . staat voor huidige folder, de folder waarin we nu werken
print ('Inhoud van huidige folder:', os.listdir(path='.'))

# maak een nieuwe folder in de huidige folder
# exist_ok=True zorgt ervoor dat je geen fout krijgt als de folder al bestaat
os.makedirs('demo', exist_ok=True)
print()
print ('Inhoud van huidige folder, met nieuwe folder:', os.listdir(path='.'))

# maak de demo folder de huidige directory
os.chdir('demo')
print()
print ('huidige directory (folder):', os.getcwd())

# maak nieuwe folder test in de huidige directory
os.makedirs('test', exist_ok=True)
print()
print ('Inhoud van huidige folder, met nieuwe folder:', os.listdir(path='.'))

#%%
#verwijder de folder test
os.rmdir('test')
print()
print ('Inhoud van huidige folder, na verwijdering', os.listdir(path='.'))

# wat is de directory separator op uw systeem? 
print()
print ('directory separator =', os.sep)

# maak een geldige path naam 
path = os.path.join('foldernaam', 'filenaam')
print()
print ('pad 1 =', path)

path = 'foldernaam' + os.path.sep +  'filenaam'
print()
print ('pad 2 =', path)

# de volgende twee zijn af te raden
path = r'foldernaam\filenaam'
print()
print ('pad 3 (afgeraden) =', path)

path = 'C:\\Files\\foldernaam\\filenaam\\test.txt'
print()
print ('pad 4 (afgeraden) =', path)

# een manier om de filenaam te bekomen
print()
print ('pad =', path)
print ('file =', os.path.basename(path))

# het is gewoon een string, je kunt dus alle string bewerkingen gebruiken
pathOnderdelen = os.getcwd().split(os.path.sep)
print()
print (pathOnderdelen)
# maak een geldige path naam 
path = pathOnderdelen[0] + os.path.sep # de drive letter krijgt geen slash !
for deel in pathOnderdelen[1::]:
    path = os.path.join(path, deel)
path = os.path.join(path, 'filenaam')
print()
print ('pad =', path)


#%% Lezen en schrijven van en naar files

print()
print ('Lezen en schrijven van en naar files')

"""
OPTIES voor het openen van een file:
    
r = read (default) - geeft fout als file niet bestaat!
r+ = read & write
w = write - maakt file als ze niet bestaat, overschrijft bestaande file
w+ = write & read
a = append - schrijft bij in een bestaande file
b = binary - voorbeeld van binary file is een foto
"""

# probeer te lezen - niet bestaande file
print()
try:
    fileHandler = open('test.txt', 'r')
except FileNotFoundError:
    print ("Foute file naam!")        


# open file om te schrijven, maakt nieuwe file als niet bestaat
fileHandler = open('demo.txt', 'w')
fileHandler.write('Deze tekst komt in het tekstbestand!')
# zeer belangrijk om altijd de file te sluiten!!!
fileHandler.close()


#%% 
try:
    fileHandler = open('demo.txt', 'w')
    fileHandler.write('Deze tekst overschrijft het tekstbestand!')
finally:
    # zeer belangrijk om altijd de file te sluiten!!!
    fileHandler.close()
    
#%% zelfde als voorgaande, andere syntax

# de fileHandler.close() gebeurt automatisch bij deze vorm!
with open('demo.txt', 'w') as fileHandler:
    fileHandler.write('Deze tekst overschrijft het tekstbestand ook!')
    
    
#%% os line separator
"""
windows gebruik de karakters '\r\n' voor een nieuwe lijn
linux gebruikt '\n'
https://docs.python.org/3/library/os.html
Do not use os.linesep as a line terminator when writing files opened 
in text mode (the default); use a single '\n' instead, on all platforms.
"""
print()
os.linesep # probeer dit in de console!

with open('demo.txt', 'w') as fileHandler:
    for i in range(10):
        fileHandler.write(f'Dit is lijn {i+1}!\n')
    
    
#%% append
with open('demo.txt', 'a') as fileHandler:
    fileHandler.write('\nEven iets toevoegen!\n\n')
    for i in range(10):
        fileHandler.write(f'Dit is lijn {i+1}!\n')
        
        
#%% Lezen van een file
print()
print ('Lezen van een file')

# lezen is de default, je kunt ook expliciet 'r' toevoegen
with open('demo.txt') as fileHandler:
    # print (fileHandler.read())
    # print ('type =', type(fileHandler.read())) # geeft een string terug
    # print ('een paar karakters =', fileHandler.read(7))
    # print ('een lijn =', fileHandler.readline())
    # print ('nog een lijn =', fileHandler.readline())
    lijst = fileHandler.readlines() # maakt een lijst van alle lijnen
    print ('lijst =', lijst)
    print ('lijn 7 =', lijst[6])
    

#%% JSON Java Script Object Notation
"""
Wordt erg veel gebruikt voor datauitwisseling. 
Op het internet, maar niet alleen daar. 
Soort van dict voor javascript.
Je kunt alle soorten types converteren naar json, uitgezonderd sets
"""

# importeer de json bibliotheek
import json

mijnDict = {
        'id' : 1,
        'naam' : 'Rudy',
        'woonplaats' : 'Leuven',
        'lengte' : 1.72
    }

print()
print ('dump :', json.dumps(mijnDict))
print ('dump :', json.dumps(mijnDict, indent = 3))
print ('dump sorted :', json.dumps(mijnDict, indent = 3, sort_keys=True))

with open('demo.json', 'w') as fileHandler:
    fileHandler.write(json.dumps(mijnDict, indent = 3 ))
    

#%% JSON lezen

with open('demo.json', 'r') as fileHandler:
    jsonString = fileHandler.read()
    
jsonValue = json.loads(jsonString)
print()
print ('jsonValue:', jsonValue)
print ('jsonValue - naam:', jsonValue['naam'])

