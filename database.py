import sqlite3
from config import DATABASE_NAME


class Database:
    def __init__(self):
        self.conn = sqlite3.connect(DATABASE_NAME)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        # Entries Table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Entries(
                Date TEXT,
                CustName TEXT,
                ChitNo TEXT,
                Info TEXT,
                Weight TEXT,
                Status INTEGER,
                Months INTEGER,
                Principal REAL,
                InAmt REAL,
                InterAmt REAL,
                OutAmt REAL,
                Total REAL
            )
        """)

        # Available Table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Available(
                ChitNo TEXT,
                Info TEXT,
                Weight TEXT
            )
        """)

        # Customer Table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Customer(
                CID TEXT PRIMARY KEY,
                CName TEXT
            )
        """)

        self.conn.commit()

    def execute(self, query, values=()):
        self.cursor.execute(query, values)
        self.conn.commit()

    def fetchone(self, query, values=()):
        self.cursor.execute(query, values)
        return self.cursor.fetchone()

    def fetchall(self, query, values=()):
        self.cursor.execute(query, values)
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
