```python
import psycopg2
from psycopg2 import sql
import json

class DataStorage:

    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="your_database",
            user="your_username",
            password="your_password",
            host="your_host"
        )
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS investor_data (
                InvestorEmail TEXT PRIMARY KEY,
                OpenStatus BOOLEAN,
                ClickStatus BOOLEAN,
                ResponseStatus BOOLEAN,
                CustomizationData JSON
            )
        """)
        self.conn.commit()

    def insert_data(self, InvestorEmail, OpenStatus, ClickStatus, ResponseStatus, CustomizationData):
        query = sql.SQL("""
            INSERT INTO investor_data (InvestorEmail, OpenStatus, ClickStatus, ResponseStatus, CustomizationData)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (InvestorEmail) DO UPDATE 
            SET OpenStatus = excluded.OpenStatus, 
                ClickStatus = excluded.ClickStatus, 
                ResponseStatus = excluded.ResponseStatus, 
                CustomizationData = excluded.CustomizationData
        """)
        self.cursor.execute(query, (InvestorEmail, OpenStatus, ClickStatus, ResponseStatus, json.dumps(CustomizationData)))
        self.conn.commit()

    def get_data(self, InvestorEmail):
        query = sql.SQL("""
            SELECT * FROM investor_data WHERE InvestorEmail = %s
        """)
        self.cursor.execute(query, (InvestorEmail,))
        return self.cursor.fetchone()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
```