# -*- coding: utf-8 -*-
import sqlite3

con = sqlite3.connect("pets.db")
print("Connection with pets.db established")
con.execute('''CREATE TABLE person
         (id INT PRIMARY KEY NOT NULL,
         first_name TEXT NOT NULL,
         last_name TEXT NOT NULL,
         age int NOY NULL);''')
print ("person Table created successfully")

con.execute('''CREATE TABLE pet
         (id INT PRIMARY KEY NOT NULL,
          name TEXT NOT NULL,
          breed TEXT NOT NULL,
          age int NOY NULL,
          dead int NOT NULL);''')

print ("pet Table created successfully") 

con.execute('''CREATE TABLE person_pet
            (person_id int NOT NULL,
pet_id int NOT NULL
);''')

print ("person_pet Table created successfully")


con.close()

