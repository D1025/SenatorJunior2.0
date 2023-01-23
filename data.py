import sqlite3
import difflib

def ifInDataBase(cursor, author):
    cursor.execute("SELECT characters FROM USERS WHERE id = ?", (author,))
    row = cursor.fetchone()
    if row:
        return True
    return False

def ifCharCheck(cursor, author, id):
    cursor.execute("SELECT characters FROM USERS WHERE id = ?", (str(author.id),))
    fetchId = cursor.fetchall()[0][0]
    
    if id<=0:
        return False
    if fetchId<id:
        return False
    return True

def allRases(cursor):
    cursor.execute("SELECT name FROM RASE")
    fetchId = cursor.fetchall()
    listRase = []
    for row in fetchId:
        listRase.append(row[0])
    return listRase

def allClass(cursor):
    cursor.execute("SELECT name FROM CLASS")
    fetchId = cursor.fetchall()
    listClass = []
    for row in fetchId:
        listClass.append(row[0])
    return listClass

def allSubclasses(cursor, klasa):
    cursor.execute("SELECT name FROM SUBCLASS WHERE class = (SELECT class_id FROM CLASS WHERE name = ? LIMIT 1)", (str(klasa),))
    fetchId = cursor.fetchall()
    listSubclass = []
    for row in fetchId:
        listSubclass.append(row[0])
    return listSubclass


def checkRase(cursor, word):
    if word == "Random":
        return "Random"
    rase=allRases(cursor)
    match = difflib.get_close_matches(word, rase, n=1, cutoff=0.6)
    if match:
        return match[0]
    else:
        return "Random"
    
    
def checkClass(cursor, word):
    if word == "Random":
        return "Random"
    classes=allClass(cursor)
    match = difflib.get_close_matches(word, classes, n=1, cutoff=0.6)
    if match:
        return match[0]
    else:
        return "Random"

def checkSubclass(cursor, klasa, subclasa):
    klasa = checkClass(cursor, klasa)
    if klasa == "Random":
        return klasa, "Random"
    subclasses=allSubclasses(cursor, klasa)
    match = difflib.get_close_matches(subclasa, subclasses, n=1, cutoff=0.6)
    if match:
        return klasa, match[0]
    else:
        return klasa, "Random"
    