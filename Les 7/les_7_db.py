import sqlite3

def initialiseer(db):
    global connectie
    connectie = sqlite3.connect(db)
    global cursor
    cursor = connectie.cursor()
    sql = """
    CREATE TABLE IF NOT EXISTS onderdelen 
    (id INTEGER PRIMARY KEY, onderdeel text, 
    klant text, verkoper text, prijs text)
    """
    cursor.execute(sql) # handle
    connectie.commit()

def fetchAll():
    cursor.execute("SELECT * FROM onderdelen")
    rows = cursor.fetchall()
    return rows

def insert(onderdeel, klant, verkoper, prijs):
    cursor.execute("INSERT INTO onderdelen VALUES (NULL, ?, ?, ?, ?)",
                     (onderdeel, klant, verkoper, prijs))
    connectie.commit()

def remove(id):
    cursor.execute("DELETE FROM onderdelen WHERE id=?", (id,))
    connectie.commit()

def update(id, onderdeel, klant, verkoper, prijs):
    cursor.execute(
        "UPDATE onderdelen SET onderdeel = ?, klant = ?, verkoper = ?, prijs = ? WHERE id = ?",
        (onderdeel, klant, verkoper, prijs, id))
    connectie.commit()

def close():
    connectie.close()

def main():
    initialiseer('les_7_onderdelen.db')
    
    insert("Voeding 500w", "Vidal Sassoon", "Njam", "80")
    insert("8 GB DDR4 Ram", "Karen Vanginderachter", "Memory palace", "135")
    insert("Asus Moederbord", "Mary Thumas", "Mama Bord", "360")
    insert("Scherm 24 inch Philips", "Sam Son", "Vie Deo", "180")
    insert("Case", "Albert van Monaco", "Het computerhuis", "120")
    insert("4 GB DDR4 Ram", "Jules Destrooper", "Memory palace", "126")
    insert("GPU GeForceRTX 3090", "Mary Thumas", "Vie Deo", "679")
    insert("16 GB DDR4 Ram", "Karen Vanginderachter", "Memory palace", "169")
     
    close() 

if __name__ == "__main__":
    main()