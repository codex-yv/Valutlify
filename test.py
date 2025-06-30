import sqlite3
import os
from cryptography.fernet import Fernet
from tkinter import messagebox

def fetch_credentials():
    # Connect to the SQLite database
    cwd = os.getcwd()
    db_path = os.path.join(cwd, "Data", "credentials.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Query all rows from the 'credentials' table
    try:
        cursor.execute("SELECT id, domain, username, password, strength, email, phone, key FROM credentials ORDER BY id DESC LIMIT 3")
        rows = cursor.fetchall()

        # Create a dictionary with decrypted passwords
        credentials_dict = {}
        for row in rows:
            row_id = row[0]
            domain = row[1]
            username = row[2]
            encrypted_password = row[3]
            strength = row[4]
            email = row[5]
            phone = row[6]
            key = row[7]

            try:
                cipher = Fernet(key)  # Convert string key to bytes
                decrypted_password = cipher.decrypt(encrypted_password).decode()
            except Exception as e:
                print(f"Decryption failed for ID {row_id}: {e}")
                decrypted_password = None

            credentials_dict[row_id] = {
                "domain": domain,
                "username": username,
                "password": decrypted_password,
                "strength": strength,
                "email": email,
                "phone": phone,
                "key": key
            }

        # Close the connection
        conn.close()

        return credentials_dict
    except sqlite3.OperationalError:
        messagebox.showinfo("Empty Password Data", "First add some password!")


print(fetch_credentials())