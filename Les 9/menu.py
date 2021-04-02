# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 08:48:30 2021

@author: rudy
"""
import tkinter as tk


# In werkelijkheid heb je natuurlijk voor ieder commando
# een aparte functie nodig. Dit is enkel als demonstratie.
def CommandFunctie(waarde):
    tekst = 'Je klikte op: ' + waarde
    txtLabel = tk.Label(venster, text = tekst).pack()

# nepfunctie voor paste
def PasteFunctie():
    tekst = 'Je klikte op paste!'
    txtLabel = tk.Label(venster, text = tekst).pack()


# Maak hoofdvenster aan
venster = tk.Tk()
venster.title('Menu voorbeeld')
venster.geometry('560x330')

# Maak een menu aan
mijnMenu = tk.Menu(venster)
venster.config(menu = mijnMenu)

# Maak een menu item
fileMenu = tk.Menu(mijnMenu)
mijnMenu.add_cascade(label = "File", menu = fileMenu)
# voeg een commando toe
fileMenu.add_command(label = "New", command = lambda: CommandFunctie('new'))
# voeg een lijn toe
fileMenu.add_separator()
# voeg nog een commando toe
fileMenu.add_command(label = "Exit", command = venster.quit)

# Maak nog een menu item
editMenu = tk.Menu(mijnMenu)
mijnMenu.add_cascade(label = "Edit", menu = editMenu)
# voeg een commando toe
editMenu.add_command(label = "Copy", command = lambda: CommandFunctie('copy'))
# voeg nog een commando toe
editMenu.add_command(label = "Paste", command = PasteFunctie)


# Start programma
venster.mainloop()


