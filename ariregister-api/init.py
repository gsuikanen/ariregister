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
        code        text NOT NULL
    );

    CREATE TABLE IF NOT EXISTS relation (
        id          integer PRIMARY KEY AUTOINCREMENT,
        company_id  integer NOT NULL,
        owner_id    integer NOT NULL,
        role        text NOT NULL,
        amount      integer NOT NULL,
        FOREIGN KEY (company_id) REFERENCES company (id),
        FOREIGN KEY (owner_id)   REFERENCES owner   (id)
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

conn.commit()
conn.close()