import os
import sqlite3



cwd = os.getcwd()
db_path = os.path.join(cwd, "Data", "credentials.db")
conn = sqlite3.connect(db_path)

cursor = conn.cursor()

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS credentials (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         domain TEXT NOT NULL,
#         username TEXT NOT NULL,
#         password TEXT NOT NULL,
#         strength TEXT,
#         phone TEXT,
#         email TEXT,
#         url TEXT
#     )
# ''')

# conn.commit()
# conn.close()
try:
    cursor.execute("ALTER TABLE credentials ADD COLUMN date_time TEXT")
    print("Column 'date_time' added successfully.")
except sqlite3.OperationalError as e:
    if "duplicate column name" in str(e):
        print("Column 'date_time' already exists.")
    else:
        raise

# Commit and close
conn.commit()
conn.close()