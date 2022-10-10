import sqlite3
from app_db import db

conn = sqlite3.connect(db)
cur = conn.cursor()

#Step 1 - creating tables
cur.executescript('''
    CREATE TABLE IF NOT EXISTS lists (
        id          integer PRIMARY KEY AUTOINCREMENT,
        list_name   text NOT NULL,
        key         text NOT NULL,
        label       text NOT NULL,
        allowed     boolean NOT NULL CHECK (allowed IN (0, 1)) DEFAULT "1",
        CONSTRAINT  unq UNIQUE (list_name, key)
    );

    CREATE TABLE IF NOT EXISTS company (
        id          integer PRIMARY KEY AUTOINCREMENT,
        name        text NOT NULL UNIQUE,
        code        text NOT NULL UNIQUE,
        reg_dt      text NOT NULL
    );

    CREATE TABLE IF NOT EXISTS owner (
        id          integer PRIMARY KEY AUTOINCREMENT,
        name        text NOT NULL,
        surname     text,
        type        text NOT NULL,
        code        text NOT NULL,
        CONSTRAINT  unq UNIQUE (name, surname, code)
    );

    CREATE TABLE IF NOT EXISTS relation (
        id          integer PRIMARY KEY AUTOINCREMENT,
        company_id  integer NOT NULL,
        owner_id    integer NOT NULL,
        role        text NOT NULL,
        amount      integer NOT NULL,
        FOREIGN KEY (company_id) REFERENCES company (id),
        FOREIGN KEY (owner_id)   REFERENCES owner   (id),
        CONSTRAINT  unq UNIQUE (company_id, owner_id)
    );
''')

#Step 2 - prepopulating DB with lists
cur.executescript('''
    INSERT INTO lists (list_name, key, label) VALUES
    ('ownerRole', 'found', 'Founder'),
    ('ownerRole', 'own', 'Owner'),
    ('ownerType', 'priv', 'Private person'),
    ('ownerType', 'bus', 'Business');
''')

#Step 3 - prepopulating DB with dummy data
i = 0
answer = ""
while True:
    i += 1
    answer = input("Prepopulate DB with dummy data? (y/n) ").lower()
    if answer == 'yes' or answer == 'y':
        answer = True
        break
    if answer == 'no' or answer == 'n' or i >= 3:
        answer = False
        break

if answer:
    print('Prepopulating DB with dummy data')
    cur.executescript('''
        INSERT INTO company (name, code, reg_dt) VALUES
            ('MEES JA KOER OÜ', '1211762', '2011-06-08'),
            ('BASOLUTION OÜ', '1433731', '2017-09-21');

        INSERT INTO owner (name, surname, type, code) VALUES
            ('Andre', 'Esna', 'priv', '3800308****'),
            ('Georgi', 'Suikanen', 'priv', '3931223****'),
            ('Jana', 'Suikanen', 'priv', '4940610****');
        
        INSERT INTO relation (company_id, owner_id, role, amount) VALUES
            (1, 1, 'found', 2500),
            (2, 2, 'found', 2500),
            (2, 3, 'found', 1000);
    ''')

conn.commit()
conn.close()