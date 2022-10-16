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
    cur.connection.close()
    return resp if type(resp['name']) == str else {'ERROR': 'Company with id {0} not found'.format(id)}

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
    return list if len(list) > 0 else {'ERROR': 'No owners found for company with id {0}'.format(id)}

def getCompanyMatches(db, reg, name):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute('''
        SELECT c.name, c.code
        FROM company c
        WHERE c.code = '{0}' OR lower(c.name) = lower('{1}') '''.format(reg, name))
    list = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.connection.close()
    return len(list) > 0

def addCompany(db, name, code, regdt):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO company (name, code, reg_dt)
        VALUES ('{0}', '{1}', '{2}')'''.format(name, code, regdt))
    i = cur.lastrowid
    cur.connection.commit()
    cur.connection.close()
    return i

def addCompanyOwner(db, comp_id, name, surname, type, code, role, amount):
    own_id = getOwnerId(db, name, surname, type, code)
    if own_id == 0:
        own_id = addOwner(db, name, surname, type, code)
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO relation (company_id, owner_id, role, amount)
        VALUES ('{0}', '{1}', '{2}', {3})'''.format(comp_id, own_id, role, amount))
    cur.connection.commit()
    cur.connection.close()

def getOwnerId(db, name, surname, type, code):
    i = 0
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute('''
        SELECT id
        FROM owner
        WHERE lower(name) = lower('{0}') AND lower(surname) = lower('{1}') and type = '{2}' and code = '{3}' '''.format(name, surname, type, code))
    for row in cur:
        i = row[0]
    cur.connection.close()
    return i

def addOwner(db, name, surname, type, code):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO owner (name, surname, type, code)
        VALUES ('{0}', '{1}', '{2}', '{3}')'''.format(name, surname, type, code))
    i = cur.lastrowid
    cur.connection.commit()
    cur.connection.close()
    return i