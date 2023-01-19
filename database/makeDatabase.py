import json
import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('database/SenatorJunior.db')

# Create a cursor object
c = conn.cursor()

conn.execute("BEGIN")

# Execute a SQL command to create a table
c.executescript(
    '''CREATE TABLE USERS (
	id integer,
	name varchar,
	characters integer
);

CREATE TABLE TRAITS (
	trait varchar);

CREATE TABLE CHARACTERS (
	id integer PRIMARY KEY AUTOINCREMENT,
	whoes integer,
	name varchar,
	sex varchar,
	class integer,
	subclass integer,
	rase integer,
	subrase integer,
	stats integer,
	traits varchar
);

CREATE TABLE RASE (
	rase_id integer PRIMARY KEY AUTOINCREMENT,
	name varchar,
	bonus_stats integer
);

CREATE TABLE SUBRASE (
	subrase_id integer PRIMARY KEY AUTOINCREMENT,
	name varchar,
	rase integer,
	bonus_stats integer
);

CREATE TABLE CLASS (
	class_id integer PRIMARY KEY AUTOINCREMENT,
	name varchar,
	primary_att varchar
);

CREATE TABLE SUBCLASS (
	subclass_id integer PRIMARY KEY AUTOINCREMENT,
	name varchar,
	class integer
);

CREATE TABLE FEMELE_NAMES (
	name varchar
);

CREATE TABLE MELE_NAMES (
	name varchar
);

CREATE TABLE LAST_NAMES (
	name varchar
);

CREATE TABLE STATS (
	stats_id integer PRIMARY KEY AUTOINCREMENT,
	strength integer,
	dexterity integer,
	constitution integer,
	intelligence integer,
	wisdom integer,
	charisma integer,
	other integer
);''')




with open("generator/femele.txt","r") as file:
    
    for i in file.readlines():
        c.execute("insert into FEMELE_NAMES (name) values (?)",(i,))
        
        
        
with open("generator/male.txt","r") as file:

    for i in file.readlines():
        c.execute("insert into MELE_NAMES (name) values (?)",(i,))
        
        
with open("generator/last.txt","r") as file:

    for i in file.readlines():
        c.execute("insert into LAST_NAMES (name) values (?)",(i,))



cr = open("json/clases.json")
class_ressult = json.load(cr)
for row in class_ressult['results']:
    c.execute("INSERT INTO CLASS (name, primary_att) VALUES (?, ?)", (row['name'],row['primary']))
    c.execute("SELECT last_insert_rowid()")
    new_id = c.fetchone()[0]
    for nextrow in row['archetype']:
        c.execute("INSERT INTO SUBCLASS (name, class) VALUES (?, ?)", (nextrow['name'], new_id))
cr.close()


rr = open("json/newrases.json")
rase_result = json.load(rr)
for row in rase_result['results']:
    bonus_stats = {"Strength":0,"Dexterity":0,"Constitution":0,"Intelligence":0,"Wisdom":0,"Charisma":0,"Other":0}
    name = row['name']
    for nextrow in row['asi']:
        bonus_stats[str(nextrow['attributes'][0])] += nextrow['value']
    c.execute("INSERT INTO STATS (strength, dexterity, constitution, intelligence, wisdom, charisma, other) VALUES (?,?,?,?,?,?,?)", 
              (bonus_stats['Strength'],bonus_stats['Dexterity'],bonus_stats['Constitution'],bonus_stats['Intelligence'],bonus_stats['Wisdom'],bonus_stats['Charisma'],bonus_stats['Other']))
    c.execute("SELECT last_insert_rowid()")
    new_id = c.fetchone()[0]
    c.execute("INSERT INTO RASE (name, bonus_stats) VALUES (?, ?)", (name, new_id))

        
rr.close()


tr = open("json/traits.json")
trait_resssult = json.load(tr)
for row in trait_resssult['personality']:
    c.execute("INSERT INTO TRAITS (trait) VALUES (?)", (row,))



# Commit the changes and close the connection
conn.commit()
conn.close()