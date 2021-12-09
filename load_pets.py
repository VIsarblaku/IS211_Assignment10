# -*- coding: utf-8 -*-
import sqlite3

con = sqlite3.connect("pets.db")
con.execute("""Insert into person values  ( 1 ,'James', 'Smith', 41)""")
con.execute("""Insert into person values  ( 2 ,'Diana', 'Greene', 23)""")
con.execute("""Insert into person values  ( 3 ,'Sara', 'White', 27)""")
con.execute("""Insert into person values  ( 4 ,'William', 'Gibson', 23)""")
con. commit()
print("Data in person table inserted successfully.")

con.execute("""Insert into pet values  ( 1 ,'Rusty', 'dalmation', 4, 1)""")
con.execute("""Insert into pet values  ( 2 ,'Bella', 'Alaskan Malamute', 3, 0)""")
con.execute("""Insert into pet values  ( 3 ,'Max', 'Cocker Spaniel', 1, 0)""")
con.execute("""Insert into pet values  ( 4 ,'Rocky', 'Beagle', 7, 0)""")
con.execute("""Insert into pet values  ( 5 ,'Rufus', 'Cocker Spaniel', 1, 0)""")
con.execute("""Insert into pet values  ( 6 ,'Spot', 'Bloodhound', 2, 1)""")
con. commit()
print("Data in pet table inserted successfully.")

con.execute("""Insert into person_pet values  ( 1, 1)""")
con.execute("""Insert into person_pet values  ( 1, 2)""")
con.execute("""Insert into person_pet values  ( 2, 3)""")
con.execute("""Insert into person_pet values  ( 2, 4)""")
con.execute("""Insert into person_pet values  ( 3, 5)""")
con.execute("""Insert into person_pet values  ( 4, 6)""")
con. commit()
print("Data in person_pet table inserted successfully.")

con.close()
# 2. The purpose of creating person_pet table is to make relationship between person and the pet.


