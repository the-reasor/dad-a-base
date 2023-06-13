import sqlite3
from dadjokes import Dadjoke

dadjoke = Dadjoke()
print(dadjoke.joke)


connection = sqlite3.connect("dadabase.db")

cursor = connection.cursor()

cursor.execute("CREATE TABLE jokes 
	(views INTEGER,
	ratings INTEGER,
	joke TEXT NOT NULL,
	joke_number INTEGER NOT NULL,
	UNIQUE(joke,joke_number)")


	(joke TEXT NOT NULL UNIQUE,
	 rating INTEGER NOT NULL,
	 )") #joke_number INTEGER NOT NULL UNIQUE
