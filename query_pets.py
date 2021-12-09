# -*- coding: utf-8 -*-
import sqlite3
con = sqlite3.connect("pets.db")
print("Connection with pets.db established")
person_id =  int(input("Please enter person's ID number: "))
while person_id != -1:
    cursor = con.cursor()
    cursor.execute("Select * from person where id="+ str(person_id))
    cursor = cursor.fetchall()
    if len(cursor) > 0:
        for row in cursor:
            first_name =  row[1]
            last_name =  row[2]
            age =  row[3]
            print(f"{first_name} {last_name}, {age} years old.")
            new_cursor = con.execute("Select pet_id from person_pet where person_id ="+ str(person_id)) 
            for new_row in new_cursor:
                pet_id = new_row[0]
                pet_cursor = con.execute("Select * from pet where id ="+ str(pet_id)) 
                if pet_cursor:
                    for pet_row in pet_cursor:
                        pet_name = pet_row[1]
                        breed = pet_row[2]
                        pet_age = pet_row[3]
                        pet_dead= pet_row[4]
                        if pet_dead == 0:
                             print(f"{first_name} {last_name}, owned a {pet_name}, a {breed}, that is {pet_age} year(s) old.")
                        else:
                             print(f"{first_name} {last_name}, owned a {pet_name}, a {breed}, that was {pet_age} year(s) old.")
    else:
        print(f"There is no person with Person ID {person_id}")
    person_id =  int(input("Please enter person's ID number: "))
con.close()
print("Bye")

