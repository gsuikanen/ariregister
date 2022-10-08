import sqlite3

db = 'database.db'

def getList(db, listname):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("SELECT key, label, CASE WHEN allowed = 1 THEN 'TRUE' ELSE 'FALSE' END as allowed FROM lists WHERE list_name = '{0}'".format(listname))
    list = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.connection.close()
    return list if len(list) > 0 else 'ERROR: list {0} not found'.format(listname)
