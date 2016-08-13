class PokeIterator(object):
    def __init__(self):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        pass

    next = __next__

# Sqlite3 usage
import sqlite3
conn = sqlite3.connect('pokemon.db')
c = conn.cursor()

c.execute("SELECT * FROM pokemon;")
res1 = c.fetchone()
print(res1)