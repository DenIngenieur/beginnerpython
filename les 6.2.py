# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 15:31:30 2021

@author: rudy
"""
# importeer GUI module tkinter en noem het tk
import tkinter as tk


# zie oefening 3.3
def IntegerNaarRomeins(getal):
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

# zie oefening 3.3
def RomeinsNaarInteger(romeinsGetal):
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
        
        if symbolen[huidigSymbool] > symbolen[vorigSymbool]:
            getal += symbolen[huidigSymbool] - 2 * symbolen[vorigSymbool]
        else:
            getal += symbolen[huidigSymbool]

        vorigSymbool = huidigSymbool
    
    return getal

    
#*************************************
# Hulpfuncties
#*************************************

def ToonFoutBoodschap(titel, boodschap):
    tk.messagebox.showerror(titel, boodschap)


def ControleInvoer():
    if invoerTekst.get() == '':
        ToonFoutBoodschap('Verplicht veld!', 'Vul het veld in, alstublieft.')
        return False
    return True


def ToonResultaat(romeins, getal):
        # wis invoerveld
        invoer.delete(0, tk.END)
        # voer de resultaten uit
        romeinsUitvoer.delete(0, tk.END)
        romeinsUitvoer.insert(tk.END, romeins.upper())       
        # decimaalUitvoer.delete(0, tk.END)
        # decimaalUitvoer.insert(tk.END, getal)
        decimaalTekst.set(getal)
        
    
    
#*************************************
# GUI Functies
#*************************************

def Romeins():
   # lijst.delete(0, tk.END)
    if ControleInvoer():
        try:
            getal = int(invoerTekst.get())
            romeins = IntegerNaarRomeins(getal)            
        except ValueError:
            ToonFoutBoodschap('Niet numeriek!', 'Invoer moet een getal zijn, groter dan 0 en kleiner dan 3999.')
            return
        
        ToonResultaat(romeins, getal)        
    return
            

def Decimaal():
    if ControleInvoer():
        try:
            romeins = invoerTekst.get()
            getal = RomeinsNaarInteger(romeins)       
        except ValueError:
            ToonFoutBoodschap('Ongeldig!', 'Dit is geen geldig Romeins getal.')
            return
        
        ToonResultaat(romeins, getal)      
    return
            

#*************************************
# BEGIN GUI programma
#*************************************

# Maak hoofdvenster aan
venster = tk.Tk()
venster.title('Omzetter')
venster.geometry('320x300')
venster.iconbitmap('les 6.2 SPQR.ico')
venster.configure(background='#F3F497')

# Invoer
invoerTekst = tk.StringVar()
invoerLabel = tk.Label(
    venster, text='Invoer (0<x<=3999): ', 
    font=('bold', 11), padx=15, pady=10, 
    background='#F3F497')
invoerLabel.grid(row=0, column=0, sticky=tk.E)
invoer = tk.Entry(venster, textvariable=invoerTekst)
invoer.grid(row=0, column=1)

# Knoppen definiëren
romeins = tk.Button(venster, text='ROMEINS', width=12, command=Romeins)
romeins.grid(row=1, column=0, padx=20, pady=10)

decimaal = tk.Button(venster, text='DECIMAAL', width=12, command=Decimaal)
decimaal.grid(row=1, column=1)

# Romeins
romeinsTekst = tk.StringVar()
romeinsLabel = tk.Label(venster, text='Romeins getal: ', 
                        font=('bold', 11), bg='#F3F497')
romeinsLabel.grid(row=2, column=0, sticky=tk.E)
romeinsUitvoer = tk.Entry(venster, textvariable=romeinsTekst)
romeinsUitvoer.grid(row=2, column=1)

# Decimaal
decimaalTekst = tk.StringVar()
decimaalLabel = tk.Label(venster, text='Decimaal getal: ', 
                         font=('bold', 11), bg='#F3F497')
decimaalLabel.grid(row=3, column=0, sticky=tk.E)
# decimaalUitvoer = tk.Entry(venster, textvariable=decimaalTekst)
decimaalUitvoer = tk.Label(venster, textvariable=decimaalTekst, 
                         font=('bold', 11), bg='#F3F497') 
decimaalUitvoer.grid(row=3, column=1, sticky=tk.W)
 
# Labels kunnen ook gebruikt worden voor figuren. 
prentje = tk.PhotoImage(file='les 6.2 SPQR.gif')
tk.Label(venster, image=prentje, bg='#F3F497').grid(row=4, column=0, columnspan=2, pady=20)

# Start programma
venster.mainloop()


# Om een executable te maken, installeer pyinstaller en run via command line.

# Gebruik eventueel de optie --onefile om alles in 1 file te krijgen 
# (die wordt dan wel reuzegroot!).

# Het werkt ook voor Mac, maar daar moet je een paar dingen toevoegen:
# --add-binary='-- pad naar Tk --/Tk.framework/Tk':'tk'
# --add-binary='-- pad naar Tcl --/Tcl.framework/Tcl':'tcl' 
# Waarbij je -- pad naar Tk -- en -- pad naar Tcl -- vervangt met
# het correcte pad naar die files, uiteraard.

# Mogelijks moet je hetzelfde doen voor Linux als voor Mac...

