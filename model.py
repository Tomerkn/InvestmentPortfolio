import sqlite3

class Model:
    """
    מחלקה לניהול מסד הנתונים של תיק השקעות.
    """
    def __init__(self, db_name="portfolio.db"):
        self.conn = sqlite3.connect(db_name)  # יצירת חיבור למסד הנתונים
        self.cursor = self.conn.cursor()  # יצירת קרסור לביצוע שאילתות
        self._create_tables()  # יצירת טבלאות במסד הנתונים

    def _create_tables(self):
        """
        יצירת טבלת ניירות ערך אם היא לא קיימת.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS securities (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                price REAL NOT NULL,
                variance REAL NOT NULL,
                security_type INTEGER NOT NULL,
                quantity INTEGER NOT NULL
            )
        ''')
        self.conn.commit()

    def add_security(self, name, price, variance, security_type, quantity):
        """
        הוספת נייר ערך חדש או עדכון הכמות אם כבר קיים.
        """
        self.cursor.execute('SELECT * FROM securities WHERE name = ?', (name,))
        existing = self.cursor.fetchone()
        if existing:
            new_quantity = existing[5] + quantity
            self.update_quantity(name, new_quantity)
        else:
            self.cursor.execute('''
                INSERT INTO securities (name, price, variance, security_type, quantity)
                VALUES (?, ?, ?, ?, ?)
            ''', (name, price, variance, security_type, quantity))
        self.conn.commit()

    def update_quantity(self, name, new_quantity):
        """
        עדכון כמות של נייר ערך קיים.
        """
        self.cursor.execute('''
            UPDATE securities SET quantity = ? WHERE name = ?
        ''', (new_quantity, name))
        self.conn.commit()

    def update_price(self, name, new_price):
        """
        עדכון המחיר של נייר ערך קיים.
        """
        self.cursor.execute('''
            UPDATE securities SET price = ? WHERE name = ?
        ''', (new_price, name))
        self.conn.commit()

    def get_portfolio(self):
        """
        שליפת כל המידע מתיק ההשקעות.
        """
        self.cursor.execute('SELECT * FROM securities')
        return self.cursor.fetchall()

    def clear_portfolio(self):
        """
        ניקוי כל הרשומות בתיק ההשקעות.
        """
        self.cursor.execute('DELETE FROM securities')
        self.conn.commit()

    def get_portfolio_for_graph(self):
        """
        שליפת שם וכמות ייחודיים עבור גרף.
        """
        self.cursor.execute('SELECT name, SUM(quantity) FROM securities GROUP BY name')
        return self.cursor.fetchall()
