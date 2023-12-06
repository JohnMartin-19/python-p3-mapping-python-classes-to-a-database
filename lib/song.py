from config import CONN, CURSOR

class Song:
     all = []
     def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

     @classmethod
     def create_table(self):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """

        CURSOR.execute(sql)

        #creating a new song instance
     @classmethod
     def create(cls, name, album):
        song = Song(name, album)
        song.save()
        return song
     
     
#Inserting Class method
     def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.album))




Song.create_table()
hello = Song("Hello", "25")
hello.save()

despacito = Song("Despacito", "Vida")
despacito.save()
Song.all