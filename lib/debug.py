#!/usr/bin/env python3

from config import CONN, CURSOR
from song import Song

all = []
if __name__ == '__main__':
    import ipdb; ipdb.set_trace()
def reset_db():
    Song.drop_table()
    Song.create_table()
    Song.create('My Time','TLS')
    Song.create('Better than ever', 'Decided2')

reset_db()
#Method for Getting data from db and converting it to python obj
@classmethod
def new_from_db(cls, row):
     song = cls(row[1], row[2])
     song.id = row[0]


#Method for getting all the records
@classmethod
def all(cls):
     sql = """
        SELECT * FROM songs
        """

     all = CURSOR.execute(sql).fetchall()

@classmethod
def get_all(cls):
        sql = """
            SELECT *
            FROM songs
        """

        all = CURSOR.execute(sql).fetchall()

        cls.all = [cls.new_from_db(row) for row in all]

@classmethod
def find_by_name(cls, name):
    sql = """
            SELECT *
            FROM songs
            WHERE name = ?
            LIMIT 1
        """

    song = CURSOR.execute(sql, (name,)).fetchone()

    return cls.new_from_db(song)
