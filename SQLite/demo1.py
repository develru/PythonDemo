##############################################
#                                            #
#      Author: Richard Ruzsa (develru)       #
#      Email: develru [at] me . com          #
#                                            #
##############################################

import sqlite3

conn = sqlite3.connect("demodatabase.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE albums (title text, artist text,
                    release_date text, publisher text, media_type text) """)

albums = [('Exodus', 'Andy Hunter', '7/9/2002', 'Sparrow Records', 'CD'),
          ('Until We Have Faces', 'Red', '2/1/2011', 'Essential Records', 'CD'),
          ('The End is Where We Begin', 'Thousand Foot Krutch', '4/17/2012', 'TFKmusic', 'CD'),
          ('The Good Life', 'Trip Lee', '4/10/2012', 'Reach Records', 'CD')]
cursor.executemany("INSERT INTO albums VALUES (?,?,?,?,?)", albums)
conn.commit()

print "\nHere's a listing of all the records in the table:\n"
for row in cursor.execute("SELECT rowid, * FROM albums ORDER BY artist"):
    print row
