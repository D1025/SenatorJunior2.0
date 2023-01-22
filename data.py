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


def checkRase(cursor, word):
    if word == "Random":
        return "Random"
    rase=allRases(cursor)
    match = difflib.get_close_matches(word, rase, n=1, cutoff=0.6)
    if match:
        return match[0]
    else:
        return "Random"
    
    
    