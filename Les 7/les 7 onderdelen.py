import tkinter as tk
import les_7_db as db

db.initialiseer('les_7_onderdelen.db')


def vulLijst():
    lijst.delete(0, tk.END)
    for row in db.fetchAll():
        lijst.insert(tk.END, row)


def VoegToeOnderdeel():
    if (onderdeelTekst.get() == '' or klantTekst.get() == '' or
            verkoperTekst.get() == '' or prijsTekst.get() == ''):
        tk.messagebox.showerror('Verplichte velden', 
                                'Vul alle velden in, alstublieft.')
        return
    db.insert(onderdeelTekst.get(), klantTekst.get(),
              verkoperTekst.get(), prijsTekst.get())
    lijst.delete(0, tk.END)
    lijst.insert(tk.END, (onderdeelTekst.get(), klantTekst.get(),
                            verkoperTekst.get(), prijsTekst.get()))
    wisVelden()
    vulLijst()


def selecteerOnderdeel(event):
    try:
        global geselecteerd
        index = lijst.curselection()[0]
        geselecteerd = lijst.get(index)

        onderdeelInvoer.delete(0, tk.END)
        onderdeelInvoer.insert(tk.END, geselecteerd[1])
        klantInvoer.delete(0, tk.END)
        klantInvoer.insert(tk.END, geselecteerd[2])
        verkoperInvoer.delete(0, tk.END)
        verkoperInvoer.insert(tk.END, geselecteerd[3])
        prijsInvoer.delete(0, tk.END)
        prijsInvoer.insert(tk.END, geselecteerd[4])
    except IndexError:
        pass


def verwijderOnderdeel():
    db.remove(geselecteerd[0])
    wisVelden()
    vulLijst()


def wijzigOnderdeel():
    db.update(geselecteerd[0], onderdeelTekst.get(), klantTekst.get(),
              verkoperTekst.get(), prijsTekst.get())
    vulLijst()


def wisVelden():
    onderdeelInvoer.delete(0, tk.END)
    klantInvoer.delete(0, tk.END)
    verkoperInvoer.delete(0, tk.END)
    prijsInvoer.delete(0, tk.END)


# Maak hoofdvenster aan
venster = tk.Tk()
venster.title('Onderdelen lijst')
venster.geometry('560x330')

# Onderdeel
onderdeelTekst = tk.StringVar()
onderdeelLabel = tk.Label(venster, text='Onderdeel', font=('bold', 12), pady=20)
onderdeelLabel.grid(row=0, column=0, sticky=tk.E)
onderdeelInvoer = tk.Entry(venster, textvariable=onderdeelTekst)
onderdeelInvoer.grid(row=0, column=1)

# Klant
klantTekst = tk.StringVar()
klantLabel = tk.Label(venster, text='Klant', font=('bold', 12))
klantLabel.grid(row=0, column=2, sticky=tk.E)
klantInvoer = tk.Entry(venster, textvariable=klantTekst)
klantInvoer.grid(row=0, column=3)

# Verkoper
verkoperTekst = tk.StringVar()
verkoperLabel = tk.Label(venster, text='Verkoper', font=('bold', 12))
verkoperLabel.grid(row=1, column=0, sticky=tk.E)
verkoperInvoer = tk.Entry(venster, textvariable=verkoperTekst)
verkoperInvoer.grid(row=1, column=1)

# Prijs
prijsTekst = tk.StringVar()
prijsLabel = tk.Label(venster, text='Prijs', font=('bold', 12))
prijsLabel.grid(row=1, column=2, sticky=tk.E)
prijsInvoer = tk.Entry(venster, textvariable=prijsTekst)
prijsInvoer.grid(row=1, column=3)

# Frame voor listbox en scrollbar
# Deze 2 samen in een frame om een mooi resultaat te hebben
lijstFrame = tk.Frame(venster)
lijstFrame.grid(row=3, column=0, columnspan=4, pady=15, padx=10)

# Scrollbar voor lijst
scrollbar = tk.Scrollbar(lijstFrame, orient=tk.VERTICAL)

# Lijst onderdelen (Listbox)
lijst = tk.Listbox(lijstFrame, height=8, width=80, border=1)

# Koppel scrollbar aan lijst
lijst.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lijst.yview)
# Bind select
lijst.bind('<<ListboxSelect>>', selecteerOnderdeel)

# Pack alles bijeen in het frame
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
lijst.pack()

# Knoppen definiëren
knopToevoegen = tk.Button(venster, text='Toevoegen', width=12, command=VoegToeOnderdeel)
knopToevoegen.grid(row=2, column=0, pady=20)

knopVerwijderen = tk.Button(venster, text='Verwijderen', width=12, command=verwijderOnderdeel)
knopVerwijderen.grid(row=2, column=1)

knopUpdate = tk.Button(venster, text='Wijzig', width=12, command=wijzigOnderdeel)
knopUpdate.grid(row=2, column=2)

knopLegen = tk.Button(venster, text='Input wissen', width=12, command=wisVelden)
knopLegen.grid(row=2, column=3)

# Lijst opvullen
vulLijst()

# Start programma
venster.mainloop()

# Database connecties altijd sluiten!
db.close()
