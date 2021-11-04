#Connections to the database and send the cursor on its way. 
import sqlite3
import pandas as pd
#Connect to DB
connection = sqlite3.connect('rpg_db.sqlite3')

#make cursor

cursor = connection.cursor()

#create querry
query = 'SELECT * FROM charactercreator_character;'

# execute qurey on cursor

cursor.execute(query)

# pull results from cusor

results = cursor.fetchall()

df = pd.DataFrame(data=results)

print(df)
