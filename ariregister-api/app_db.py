import sqlite3

db = 'database.db'

def getList(db, listname):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("SELECT key, label, CASE WHEN allowed = 1 THEN 'TRUE' ELSE 'FALSE' END as allowed FROM lists WHERE list_name = '{0}'".format(listname))
    list = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.connection.close()
    return list if len(list) > 0 else {'ERROR': 'List {0} not found'.format(listname)} 

def getCompanyBasicData(db, id):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute('''
        SELECT c.id, c.name, c.code, c.reg_dt, count(r.owner_id) as owners, sum(r.amount) as capital
        FROM company c
        LEFT JOIN relation r ON r.company_id = c.id
        WHERE c.id = {0}'''.format(id))
    list = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
    resp = list[0]
    print(resp)
    cur.connection.close()
    return resp if type(resp['name']) == "str" else {'ERROR': 'Company with id {0} not found'.format(id)}

def getSearchedCompanies(db, str):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute('''
        SELECT c.id, c.name, c.code, '' as owner
        FROM company c
        WHERE c.code = '{0}' OR lower(c.name) LIKE lower('%{0}%')
        UNION
        SELECT c.id, c.name, c.code, trim(o.name || ' ' || o.surname) as owner
        FROM company c, relation r, owner o
        WHERE c.id = r.company_id
        AND r.owner_id = o.id
        AND (lower(o.name) = lower('{0}') OR lower(o.surname) = lower('{0}'))'''.format(str))
    list = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.connection.close()
    return list if len(list) > 0 else {'ERROR': 'No company found matching the following search: {0}'.format(str)}

def getCompanyOwners(db, id):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute('''
        SELECT o.id, trim(o.name || ' ' || o.surname) as name, o.type, o.code, r.role, r.amount
        FROM relation r
        LEFT JOIN owner o ON o.id = r.owner_id
        WHERE r.company_id = {0}'''.format(id))
    list = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.connection.close()
    return list if len(list) > 0 else {'ERROR': 'Company with id {0} not found'.format(id)}