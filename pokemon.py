import sqlite3
import time
import random

conn = sqlite3.connect('pokemon.db')
c = conn.cursor()
id = 0


def dynamic_data_entry():

    name = input ("Name: ")
    health = input ("Health: ")
    stage = input ("Stage:")
    ptype = input("Type: ")
    retreat = input ("Retreat: ")
    year = input ("Year: ")

    c.execute("INSERT INTO pm VALUES ( ?,?,?,?,?,?,? )",
          (id,name,health,stage,ptype,retreat,year))

    conn.commit()

    
for i in range(600):
    dynamic_data_entry()
    time.sleep(1)
    id += 1

c.close
conn.close()
