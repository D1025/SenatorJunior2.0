import sqlite3


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