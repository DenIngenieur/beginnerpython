# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 18:41:16 2021

@author: rudy
"""
# Als tkinter niet geïnstalleerd is kun je dat op dezelfde manier 
# installeren als pyinstaller, zoals getoond in de video.

# importeer GUI module tkinter en noem het tk
import tkinter as tk

#%% snelle test om te zien of tkinter werkt
tk._test()


#%% Eerste GUI applicatie

# dit is een tk object, en het is het hoofdvenster
venster = tk.Tk()

# zet een titel voor je toepassing
venster.title("Eerste GUI app")

# we plaatsen een knop in het venster
# componenten zoals knoppen worden widgets genoemd
tk.Button(venster, text="TkInter zegt hallo!").grid()

# dit zorgt ervoor dat je venster opent en blijft lopen
# er wordt continue gecheckt of er iets gebeurd in het venster,
# zoals klikken op een knop
venster.mainloop()


#%% Veel verschillende widgets 
"""
Button, Label, Canvas, Menu, Text, Scale, OptionMenu, Frame,
CheckButton, LabelFrame, MenuButton, PanedWindow, Entry, ListBox,
Message, RadioButton, ScrollBar, Bitmap, SpinBox, Image
"""

venster = tk.Tk()

# frame widgets zijn containers en bevatten andere widgets
frame = tk.Frame(venster)

# gebruik een TkInter variabele voor het label tekst zodat
# we het kunnen aanpassen met set
labelTekst = tk.StringVar()

label = tk.Label(frame, textvariable=labelTekst)
knop = tk.Button(frame, text="Klik op mij!")

# verander de tekst van het label 
labelTekst.set("Ik ben een label!")

# pack positioneert de widgets in het venster
# het is een simpele zogenaamde "geometry manager"
label.pack()
knop.pack()
frame.pack()

venster.mainloop()



#%% Pack manager
"""
Pack positioneert widgets door hen hun positie te laten opgeven
(Top, Right, Bottom, Left) en hun opvulling of rek (X, Y, BOTH, NONE) 
binnen een andere widget (of het venster, of een frame, of ...).
"""

venster = tk.Tk()

frame = tk.Frame(venster)

# waar plaatsen en hoe die plaats opvullen
tk.Label(frame, text="Een bende knoppen.").pack()
tk.Button(frame, text="Knop 1").pack(side=tk.LEFT, fill=tk.Y)
tk.Button(frame, text="Knop 2").pack(side=tk.TOP, fill=tk.X)
tk.Button(frame, text="Knop 3").pack(side=tk.RIGHT, fill=tk.X) # rechts!!!
tk.Button(frame, text="Knop 4").pack(side=tk.LEFT, fill=tk.X)

frame.pack()

venster.mainloop()


#%% Grid manager
"""
De grid manager is te vergelijken met een spreadsheet.
Elke cel heeft een rij en een kolom, en bevat een widget.
Je maakt dus feitelijk een tabel van widgets en kunt zo de positie van 
die widgets bepalen. 
Een widget kan zich over meerdere cellen uitstrekken.
Het is zeer goed te vergelijken met een tabel in HTML.
"""

venster = tk.Tk()
venster.configure(background='#97F3F4')

# rijen en kolommen starten met 0, niet 1, zoals gewoonlijk in programmeren
# sticky definieert hoe het widget strekt (N, NE, E, SE, S, SW, W, NW)
# padx en pady geven de hoeveelheid padding rond het widget aan
tk.Label(venster, text="Voornaam: ").grid(row=0, column=0, sticky=tk.W, padx=4)
tk.Entry(venster).grid(row=0, column=1, sticky=tk.E, padx=4, pady=4) # input veld

tk.Label(venster, text="Familienaam: ").grid(row=1, column=0, sticky=tk.W, padx=4)
tk.Entry(venster).grid(row=1, column=1, sticky=tk.E, padx=4, pady=4) # input veld

tk.Button(venster, text="VERZENDEN").grid(row=2, column=0, sticky=tk.S, columnspan=2)

venster.mainloop()


#%% Meer grid... en events

# hulpfunctie
def klik(waarde):
    print (waarde)

venster = tk.Tk()

tk.Label(venster, text="Beschrijving produkt: ").grid(row=0, column=0, sticky=tk.W)
tk.Entry(venster, width=50).grid(row=0, column=1)
tk.Button(venster, text="VERZEND").grid(row=0, column=3)

rbVar = tk.IntVar() # zorgt ervoor dat we de keuze kunnen aanspreken 
tk.Label(venster, text="Staat van het produkt:").grid(row=1, column=0, sticky=tk.W)
tk.Radiobutton(venster, text="Nieuw", variable=rbVar, value=1, 
               command=lambda: klik(rbVar.get())).grid(row=2, column=0, sticky=tk.W)
tk.Radiobutton(venster, text="Goed", variable=rbVar, value=2,
               command=lambda: klik(rbVar.get())).grid(row=3, column=0, sticky=tk.W)
tk.Radiobutton(venster, text="Redelijk", variable=rbVar, value=3,
               command=lambda: klik(rbVar.get())).grid(row=4, column=0, sticky=tk.W)
tk.Radiobutton(venster, text="Kapot", variable=rbVar, value=4, 
               command=lambda: klik(rbVar.get())).grid(row=5, column=0, sticky=tk.W)
tk.Radiobutton(venster, text="Onherstelbaar", variable=rbVar, value=5, 
               command=lambda: klik(rbVar.get())).grid(row=6, column=0, sticky=tk.W)

cbVar1 = tk.StringVar() # zorgt ervoor dat we de keuze kunnen aanspreken 
cbVar2 = tk.StringVar() # zorgt ervoor dat we de keuze kunnen aanspreken 
cbVar3 = tk.StringVar() # zorgt ervoor dat we de keuze kunnen aanspreken 
# zet de standaard waarden
cbVar1.set("NGV")
cbVar2.set("NBC")
cbVar3.set("NMOS")

tk.Label(venster, text="Extra: ").grid(row=1, column=1, sticky=tk.W)
c1 = tk.Checkbutton(venster, variable=cbVar1, text="Gratis verzending",
               onvalue="GV", offvalue="NGV", command=lambda: klik(cbVar1.get()))
c1.grid(row=2, column=1, sticky=tk.W)
c2 = tk.Checkbutton(venster, variable=cbVar2, text="Bonus cadeau",
               onvalue="BC", offvalue="NBC", command=lambda: klik(cbVar2.get()))
c2.grid(row=3, column=1, sticky=tk.W)
c3 = tk.Checkbutton(venster, variable=cbVar3, text="Meename oude spullen",
               onvalue="MOS", offvalue="NMOS", command=lambda: klik(cbVar3.get()))           
c3.grid(row=4, column=1, sticky=tk.W)
c1.deselect()
c2.deselect()
c3.deselect()


venster.mainloop()

#%% Events - nog meer 

def som(event):
    # haal de waarden uit de inputvelden
    getal1 = int(getal1Invoer.get())
    getal2 = int(getal2Invoer.get())
    totaal = getal1 + getal2
    
    # eerst deleten, anders wordt er gewoon bijgeschreven
    totaalUitvoer.delete(0, "end")

    # dan waarde tonen
    totaalUitvoer.insert(0, totaal)

venster = tk.Tk()

getal1Invoer = tk.Entry(venster)
getal1Invoer.pack(side=tk.LEFT)

tk.Label(venster, text="+").pack(side=tk.LEFT)

getal2Invoer = tk.Entry(venster)
getal2Invoer.pack(side=tk.LEFT)

isGelijkKnop = tk.Button(venster, text="=")

# linkse muisknop geklikt => roep functie op
isGelijkKnop.bind("<Button-1>", som)

isGelijkKnop.pack(side=tk.LEFT)

totaalUitvoer = tk.Entry(venster)
totaalUitvoer.pack(side=tk.LEFT)

venster.mainloop()