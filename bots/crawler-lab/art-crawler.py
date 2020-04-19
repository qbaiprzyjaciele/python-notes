import sqlite3

conn = sqlite3.connect('art_entries.db')
c = conn.cursor()


class ArtEntryDao:

    def __init__(self, database):
        self.database = 'art_entries.db'
    

    def findByArtSourceAndId(self, source, id):
        conn = sqlite3.connect(self.database)
        c = self.conn.cursor()
        c.execute('SELECT * FROM art_entries WHERE source = ? and id = ?', (source, id))
        row = c.fetchone()
        if row == None:
            conn.close()
            return None
        print(row)
        conn.close()
    
    def saveArtEntry(self, art_entry):
        conn = sqlite3.connect(self.database)
        c = self.conn.cursor()
        #todo
        c.execute('INSERT INTO art_entries(source, id, title, img_link, link, category) values (?,?,?,?,?,?)',())




