from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import customtkinter as ctk
import re
from urllib.parse import urlparse
import tldextract
import sqlite3
import random
import string
from datetime import datetime
from cryptography.fernet import Fernet
from realpass2 import*
import subprocess
import platform
import sys
from pyzbar.pyzbar import decode
import time
import cv2
import threading
import qrcode

current_winfo = ["Dashboard"]
pass_style = ["AlphaNumeric"]
pass_char = [True]
qr_content = []

class StaticColor:
    def __init__(self, btn, img):
        self.label = btn
        self.image = img

        self.image_pass= Image.open(self.image).resize((24, 24))
        self.button_image = ctk.CTkImage(light_image=self.image_pass,size=(24, 24))

        self.label.configure(text_color = "White", image = self.button_image, fg_color = "#1410DB")
    
    def resetColor(self, prev):
        self.prev_label = prev
        self.cwd = os.getcwd

        if self.prev_label == "Dashboard":
            self.image_path = os.path.join(cwd, "Assets", "Buttons", "home1.png") #cwd+"\\Assets\\Buttons\\home1.png"
            self.image_pass1= Image.open(self.image_path).resize((24, 24))
            self.button_image1 = ctk.CTkImage(light_image=self.image_pass1,size=(24, 24))
            home_btn.configure(text_color = "black", image = self.button_image1, fg_color = "white")

        elif self.prev_label == "Password":

            self.image_path = os.path.join(cwd, "Assets", "Buttons", "password.png") #cwd+"\\Assets\\Buttons\\password.png"
            self.image_pass1= Image.open(self.image_path).resize((24, 24))
            self.button_image1 = ctk.CTkImage(light_image=self.image_pass1,size=(24, 24))
            pass_btn.configure(text_color = "black", image = self.button_image1, fg_color = "white")

        elif self.prev_label == "Generate":

            self.image_path = os.path.join(cwd, "Assets", "Buttons", "seedbl.png") #cwd+"\\Assets\\Buttons\\seedbl.png"
            self.image_pass1= Image.open(self.image_path).resize((24, 24))
            self.button_image1 = ctk.CTkImage(light_image=self.image_pass1,size=(24, 24))
            passgen_btn.configure(text_color = "black", image = self.button_image1, fg_color = "white")
        
        elif self.prev_label == "QR":

            self.image_path = os.path.join(cwd, "Assets", "Buttons", "qrbl.png") #cwd+"\\Assets\\Buttons\\qrbl.png"
            self.image_pass1= Image.open(self.image_path).resize((24, 24))
            self.button_image1 = ctk.CTkImage(light_image=self.image_pass1,size=(24, 24))
            qr_btn.configure(text_color = "black", image = self.button_image1, fg_color = "white")


        elif self.prev_label == "wifi":

            self.image_path = os.path.join(cwd, "Assets", "Buttons", "wifibl.png") #cwd+"\\Assets\\Buttons\\wifibl.png"
            self.image_pass1= Image.open(self.image_path).resize((24, 24))
            self.button_image1 = ctk.CTkImage(light_image=self.image_pass1,size=(24, 24))
            wifi_btn.configure(text_color = "black", image = self.button_image1, fg_color = "white")
        
        elif self.prev_label == "Settings":

            self.image_path = os.path.join(cwd, "Assets", "Buttons", "settbl.png") #cwd+"\\Assets\\Buttons\\settbl.png"
            self.image_pass1= Image.open(self.image_path).resize((24, 24))
            self.button_image1 = ctk.CTkImage(light_image=self.image_pass1,size=(24, 24))
            settings_btn.configure(text_color = "black", image = self.button_image1, fg_color = "white")
        
class ScrollableFrame(ctk.CTkScrollableFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.configure(border_width=1, scrollbar_button_color="#1410DB", fg_color = "#F7F7FE",
                       border_color = "black")


def open_home():
    mainframe.pack_forget()
    home_frame.pack(fill='both', expand=True)


def open_home2():
    cwd = os.getcwd()
    db_path = os.path.join(cwd, "Data", "logs.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    

    cursor.execute('SELECT username, password, key FROM users')
    user_data = cursor.fetchall()  # Returns a list of tuples

    # Close the connection
    conn.close()

    if username_entrys.get() == user_data[-1][0]:
        key = user_data[-1][2]
        encrypted_password = user_data[-1][1]
        cipher = Fernet(key)  # Convert string key to bytes
        decrypted_password = cipher.decrypt(encrypted_password).decode()
        if password_entrys.get() == decrypted_password:
            mainframe.pack_forget() 
            home_frame.pack(fill='both', expand=True)
        else:
            messagebox.showerror("password", "Wrong Password!")    
    else:
        messagebox.showerror("Username", "Invalid Username!")

def on_enter_home(e):
    global current_winfo
    if current_winfo[0] != "Dashboard":
        image_path = os.path.join(cwd, "Assets", "Buttons", "home.png") #cwd+"\\Assets\\Buttons\\home.png"
        image_pass= Image.open(image_path).resize((24, 24))
        button_image = ctk.CTkImage(light_image=image_pass,size=(24, 24))
        home_btn.configure(text_color = "White", image = button_image, fg_color = "#1410DB")

def on_leave_home(e):
    global current_winfo
    if current_winfo[0] != "Dashboard":
        image_path = os.path.join(cwd, "Assets", "Buttons", "home1.png") #cwd+"\\Assets\\Buttons\\home1.png"
        image_pass= Image.open(image_path).resize((24, 24))
        button_image = ctk.CTkImage(light_image=image_pass,size=(24, 24))
        home_btn.configure(text_color = "Black", image = button_image, fg_color = "White")

def on_enter_pass(e):
    global current_winfo
    if current_winfo[0] != "Password":
        image_path = os.path.join(cwd, "Assets", "Buttons", "lock.png") #cwd+"\\Assets\\Buttons\\lock.png"
        image_pass= Image.open(image_path).resize((24, 24))
        button_image = ctk.CTkImage(light_image=image_pass, size=(24, 24))
        pass_btn.configure(text_color = "White", image = button_image, fg_color = "#1410DB")

def on_leave_pass(e):
    global current_winfo
    if current_winfo[0] != "Password":
        image_path = os.path.join(cwd, "Assets", "Buttons", "password.png") #cwd+"\\Assets\\Buttons\\password.png"
        image_pass= Image.open(image_path).resize((24, 24))
        button_image = ctk.CTkImage(light_image=image_pass,size=(24, 24))
        pass_btn.configure(text_color = "Black", image = button_image, fg_color = "White")

def on_enter_passgen(e):
    global current_winfo
    if current_winfo[0] != "Generate":
        image_path = os.path.join(cwd, "Assets", "Buttons", "seedling.png") #cwd+"\\Assets\\Buttons\\seedling.png"
        image_pass= Image.open(image_path).resize((24, 24))
        button_image = ctk.CTkImage(light_image=image_pass, size=(24, 24))
        passgen_btn.configure(text_color = "White", image = button_image, fg_color = "#1410DB")

def on_leave_passgen(e):
    global current_winfo
    if current_winfo[0] != "Generate":
        image_path = os.path.join(cwd, "Assets", "Buttons", "seedbl.png") #cwd+"\\Assets\\Buttons\\seedbl.png"
        image_pass= Image.open(image_path).resize((24, 24))
        button_image = ctk.CTkImage(light_image=image_pass,size=(24, 24))
        passgen_btn.configure(text_color = "Black", image = button_image, fg_color = "White")


def on_enter_qr(e):
    global current_winfo
    if current_winfo[0] != "QR":
        image_path = os.path.join(cwd, "Assets", "Buttons", "qr-code.png") #cwd+"\\Assets\\Buttons\\qr-code.png"
        image_pass= Image.open(image_path).resize((24, 24))
        button_image = ctk.CTkImage(light_image=image_pass, size=(24, 24))
        qr_btn.configure(text_color = "White", image = button_image, fg_color = "#1410DB")

def on_leave_qr(e):
    global current_winfo
    if current_winfo[0] != "QR":
        image_path = os.path.join(cwd, "Assets", "Buttons", "qrbl.png") #cwd+"\\Assets\\Buttons\\qrbl.png"
        image_pass= Image.open(image_path).resize((24, 24))
        button_image = ctk.CTkImage(light_image=image_pass,size=(24, 24))
        qr_btn.configure(text_color = "Black", image = button_image, fg_color = "White")

def on_enter_wifi(e):
    global current_winfo
    if current_winfo[0] != "wifi":
        image_path = os.path.join(cwd, "Assets", "Buttons", "wifi.png") #cwd+"\\Assets\\Buttons\\wifi.png"
        image_pass= Image.open(image_path).resize((24, 24))
        button_image = ctk.CTkImage(light_image=image_pass, size=(24, 24))
        wifi_btn.configure(text_color = "White", image = button_image, fg_color = "#1410DB")

def on_leave_wifi(e):
    global current_winfo
    if current_winfo[0] != "wifi":
        image_path = os.path.join(cwd, "Assets", "Buttons", "wifibl.png") #cwd+"\\Assets\\Buttons\\wifibl.png"
        image_pass= Image.open(image_path).resize((24, 24))
        button_image = ctk.CTkImage(light_image=image_pass,size=(24, 24))
        wifi_btn.configure(text_color = "Black", image = button_image, fg_color = "White")

def on_enter_settings(e):
    global current_winfo
    if current_winfo[0] != "Settings":
        image_path = os.path.join(cwd, "Assets", "Buttons", "settings.png") #cwd+"\\Assets\\Buttons\\settings.png"
        image_pass= Image.open(image_path).resize((24, 24))
        button_image = ctk.CTkImage(light_image=image_pass, size=(24, 24))
        settings_btn.configure(text_color = "White", image = button_image, fg_color = "#1410DB")

def on_leave_settings(e):
    global current_winfo
    if current_winfo[0] != "Settings":
        image_path = os.path.join(cwd, "Assets", "Buttons", "settbl.png") #cwd+"\\Assets\\Buttons\\settbl.png"
        image_pass= Image.open(image_path).resize((24, 24))
        button_image = ctk.CTkImage(light_image=image_pass,size=(24, 24))
        settings_btn.configure(text_color = "Black", image = button_image, fg_color = "White")


def home_func():
    global current_winfo

    password_canvas.pack_forget()
    passgen_canvas.pack_forget()
    qr_canvas.pack_forget()
    wifi_canvas.pack_forget()
    settings_canvas.pack_forget()
    add_password_canvas.pack_forget()
    gen_qr_canvas.pack_forget()
    show_password_canvas.pack_forget()
    clear_scrollable_frame(password_frame)
    content_canvas.pack(fill='both', expand=True)
    clear_scrollable_frame(recent_password_frame)
    show_all_pass_recent()
    image_path = os.path.join(cwd, "Assets", "Buttons", "home.png") #cwd+"\\Assets\\Buttons\\home.png"
    static = StaticColor(home_btn, image_path)
    if current_winfo[0]!= "Dashboard":
        static.resetColor(current_winfo[0])

    current_winfo.insert(0, "Dashboard")


def pass_func():
    global current_winfo

    content_canvas.pack_forget()
    passgen_canvas.pack_forget()
    qr_canvas.pack_forget()
    wifi_canvas.pack_forget()
    settings_canvas.pack_forget()
    gen_qr_canvas.pack_forget()
    add_password_canvas.pack_forget()
    show_password_canvas.pack_forget()
    clear_scrollable_frame(password_frame)

    password_canvas.pack(fill='both', expand=True)

    image_path = os.path.join(cwd, "Assets", "Buttons", "lock.png") #cwd+"\\Assets\\Buttons\\lock.png"
    
    static = StaticColor(pass_btn, image_path)

    if current_winfo[0]!= "Password":
        static.resetColor(current_winfo[0])

    current_winfo.insert(0, "Password")

def passgen_func():
    global current_winfo
    content_canvas.pack_forget()
    password_canvas.pack_forget()
    qr_canvas.pack_forget()
    wifi_canvas.pack_forget()
    settings_canvas.pack_forget()
    add_password_canvas.pack_forget()
    gen_qr_canvas.pack_forget()
    show_password_canvas.pack_forget()
    clear_scrollable_frame(password_frame)
    passgen_canvas.pack(fill='both', expand=True)

    image_path = os.path.join(cwd, "Assets", "Buttons", "seedling.png") #cwd+"\\Assets\\Buttons\\seedling.png"
    
    static = StaticColor(passgen_btn, image_path)

    if current_winfo[0]!= "Generate":
        static.resetColor(current_winfo[0])

    current_winfo.insert(0, "Generate")

def qr_func():
    global current_winfo

    content_canvas.pack_forget()
    password_canvas.pack_forget()
    passgen_canvas.pack_forget()
    wifi_canvas.pack_forget()
    settings_canvas.pack_forget()
    gen_qr_canvas.pack_forget()
    add_password_canvas.pack_forget()
    show_password_canvas.pack_forget()
    clear_scrollable_frame(password_frame)
    qr_canvas.pack(fill='both', expand=True)

    image_path = os.path.join(cwd, "Assets", "Buttons", "qr-code.png") #cwd+"\\Assets\\Buttons\\qr-code.png"
    
    static = StaticColor(qr_btn, image_path)

    if current_winfo[0]!= "QR":
        static.resetColor(current_winfo[0])

    current_winfo.insert(0, "QR")

def gen_qr_func():
    qr_canvas.pack_forget()
    gen_qr_canvas.pack(fill='both', expand=True)

def gen_qr_back():
    gen_qr_canvas.pack_forget()
    qr_canvas.pack(fill='both', expand=True)

def wifi_func():
    global current_winfo
    content_canvas.pack_forget()
    password_canvas.pack_forget()
    passgen_canvas.pack_forget()
    qr_canvas.pack_forget()
    settings_canvas.pack_forget()
    add_password_canvas.pack_forget()
    show_password_canvas.pack_forget()
    gen_qr_canvas.pack_forget()
    clear_scrollable_frame(password_frame)
    wifi_canvas.pack(fill='both', expand=True)

    image_path = os.path.join(cwd, "Assets", "Buttons", "wifi.png") #cwd+"\\Assets\\Buttons\\wifi.png"
    
    static = StaticColor(wifi_btn, image_path)

    if current_winfo[0]!= "wifi":
        static.resetColor(current_winfo[0])

    current_winfo.insert(0, "wifi")

    
def setting_func():
    global current_winfo

    content_canvas.pack_forget()
    password_canvas.pack_forget()
    passgen_canvas.pack_forget()
    qr_canvas.pack_forget()
    add_password_canvas.pack_forget()
    show_password_canvas.pack_forget()
    gen_qr_canvas.pack_forget()
    clear_scrollable_frame(password_frame)
    wifi_canvas.pack_forget()

    settings_canvas.pack(fill='both', expand=True)

    image_path = os.path.join(cwd, "Assets", "Buttons", "settings.png") #cwd+"\\Assets\\Buttons\\settings.png"
    
    static = StaticColor(settings_btn, image_path)

    if current_winfo[0]!= "Settings":
        static.resetColor(current_winfo[0])

    current_winfo.insert(0, "Settings")

def add_new_pass_canvas():
    password_canvas.pack_forget()
    add_password_canvas.pack(fill='both', expand=True)

def fetch_credentials():
    # Connect to the SQLite database
    cwd = os.getcwd()
    db_path = os.path.join(cwd, "Data", "credentials.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Query all rows from the 'credentials' table
    try:
        cursor.execute("SELECT id, domain, username, password, strength, email, phone, key FROM credentials")
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

def Label_image(Image_path):
    pil_image = Image.open(Image_path)  # Replace with your image path
    ctk_image = ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=(20, 20))
    return ctk_image


def delete_cred(target_id):
    try:
        cwd = os.getcwd()
        db_path = os.path.join(cwd, "Data", "credentials.db")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Execute delete statement
        query = f"DELETE FROM credentials WHERE id = ?"
        cursor.execute(query, (target_id,))
        conn.commit()

        messagebox.showinfo("Success", "Deleted Successfully!")
        clear_scrollable_frame(password_frame)
        show_all_pass()
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        if conn:
            conn.close()


def update_cred(target_id):

    def update_exit():
        update_window.destroy()
    
    def upadte_clear():
        update_username_entry.delete(0, "end")
        update_password_entry.delete(0, "end")
        update_phone_entry.delete(0, "end")
        update_email_entry.delete(0, "end")
        update_url_entry.delete(0, "end")
        update_username_entry.configure(placeholder_text="Username")
        update_password_entry.configure(placeholder_text="Password")
        update_phone_entry.configure(placeholder_text="Phone Number")
        update_email_entry.configure(placeholder_text="Email")
        update_url_entry.configure(placeholder_text="URL")

    def update_cred_win():
        try:
            cwd = os.getcwd()
            db_path = os.path.join(cwd, "Data", "credentials.db")
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()

            # Update query
            

            if update_username_entry.get():
                query1 = f"UPDATE credentials SET username = ? WHERE id = ?"
                cursor.execute(query1, (update_username_entry.get().strip(), target_id))

            if update_password_entry.get():

                strength = password_strength(update_password_entry.get().strip())
                key = Fernet.generate_key()
                cipher = Fernet(key)
                updt_password_value = update_password_entry.get().strip().encode()
                password_encryp = cipher.encrypt(updt_password_value)

                query6 = f"UPDATE credentials SET key = ? WHERE id = ?"
                cursor.execute(query6, (key, target_id))

                query7 = f"UPDATE credentials SET strength = ? WHERE id = ?"
                cursor.execute(query7, (strength, target_id))

                query2 = f"UPDATE credentials SET password = ? WHERE id = ?"
                cursor.execute(query2, (password_encryp, target_id))
                
            if update_phone_entry.get():
                query3 = f"UPDATE credentials SET phone = ? WHERE id = ?"
                cursor.execute(query3, (update_phone_entry.get().strip(), target_id))

            if update_email_entry.get():
                validEmail = is_valid_email(update_email_entry.get().strip())
                if validEmail is True:
                    query4 = f"UPDATE credentials SET email = ? WHERE id = ?"
                    cursor.execute(query4, (update_email_entry.get().strip(), target_id))
                else:
                    messagebox.showerror('Invalid Email', "Please Enter the correct email!")

            if update_url_entry.get():
                validURL = is_valid_url(update_url_entry.get().strip())
                if validURL:
                    query5 = f"UPDATE credentials SET url = ? WHERE id = ?"
                    cursor.execute(query5, (update_url_entry.get().strip(), target_id))

                    domain = get_platform_name(update_url_entry.get().strip())

                    query8 = f"UPDATE credentials SET domain = ? WHERE id = ?"
                    cursor.execute(query8, (domain, target_id))
                else:
                    messagebox.showerror('Invaid URL', 'Please Enter the valid url')

            conn.commit()

            messagebox.showinfo('Success', 'Credentials updated successfully!')
            clear_scrollable_frame(password_frame)
            show_all_pass()
            update_dashboard()
            clear_scrollable_frame(recent_password_frame)
            show_all_pass_recent()

        except sqlite3.Error as e:
            messagebox.showerror('Updation Error', 'can not update the credentials.')
        finally:
            if conn:
                conn.close()
    update_window = Toplevel(win)
    update_window.title("Update Credentials")
    update_window.geometry("600x500")
    cwd = os.getcwd()
    path_ico = os.path.join(cwd, "Assets", "logo.ico")
    update_window.iconbitmap(path_ico)

    update_frame = Frame(update_window, bg="green", width=600)
    update_frame.propagate(False)
    update_frame.pack(fill=Y, expand=True, side='left', anchor='nw')

    update_password_canvas=Canvas(update_frame,bg='white',bd=0,highlightthickness=0, relief='ridge')
    update_password_canvas.propagate(False)
    update_password_canvas.pack(fill='both', expand=True)

    imagepath13=os.path.join(cwd, "Assets", "UIUX", "passdisplay.png") #cwd+"\\Assets\\UIUX\\passdisplay.png"
    openphoto13=Image.open(imagepath13).resize((600,500))
    bgimage13=ImageTk.PhotoImage(openphoto13)
    update_password_canvas.create_image(300,250, image=bgimage13)



    update_username_entry = ctk.CTkEntry(update_password_canvas, font=("poppins", 15), fg_color="white", bg_color="white",
                                text_color="black", border_width=0,placeholder_text="Username",
                                height=25)
    update_username_entry.place(x = 30, y = 96)

    update_password_entry = ctk.CTkEntry(update_password_canvas, font=("poppins", 15), fg_color="white", bg_color="white",
                                text_color="black", border_width=0,placeholder_text="Password",
                                height=25)
    update_password_entry.place(x = 230, y = 96)

    update_gen_pass_btn = ctk.CTkButton(update_password_canvas, text="Generate", font=("poppins", 12), fg_color="#8E8DF1",
                                bg_color="#F7F7FE", height=20, width=70, text_color='black', hover_color="#8E8DF1",
                                cursor = "hand2", command=insert_gen_pass)
    update_gen_pass_btn.place(x = 300, y = 130)


    update_phone_entry = ctk.CTkEntry(update_password_canvas, font=("poppins", 15), fg_color="white", bg_color="white",
                                text_color="black", border_width=0,placeholder_text="Phone Number",
                                height=25)
    update_phone_entry.place(x = 430, y = 96)


    update_email_entry = ctk.CTkEntry(update_password_canvas, font=("poppins", 15), fg_color="white", bg_color="white",
                                text_color="black", border_width=0,placeholder_text="Email",
                                height=25, width=365)
    update_email_entry.place(x = 30, y = 162)

    update_url_entry = ctk.CTkEntry(update_password_canvas, font=("poppins", 15), fg_color="white", bg_color="white",
                                text_color="black", border_width=0,placeholder_text="URL",
                                height=25, width=365)
    update_url_entry.place(x = 30, y = 227)

    update_password_btn = ctk.CTkButton(update_password_canvas, text="Update Credentials", font=("poppins", 15, 'bold'), 
                                    fg_color="#1410DB", bg_color="#F7F7FE", height=35, cursor = "hand2",
                                    width=110, command= update_cred_win)
    update_password_btn.place(x = 30, y = 277)

    update_clear_password_btn = ctk.CTkButton(update_password_canvas, text="Clear", font=("poppins", 15, 'bold'), 
                                    fg_color="#f34825", bg_color="#F7F7FE", height=35, cursor = "hand2",
                                    width=70, command=upadte_clear)
    update_clear_password_btn.place(x = 190, y = 277)

    update_exit_password_btn = ctk.CTkButton(update_password_canvas, text="Exit", font=("poppins", 15, 'bold'), 
                                    fg_color="#17ac00", bg_color="#F7F7FE", height=35, cursor = "hand2",
                                    width=70, command=update_exit)
    update_exit_password_btn.place(x = 275, y = 277)

    update_window.mainloop()
    

def show_all_pass():
    password_canvas.pack_forget()
    show_password_canvas.pack(fill='both', expand=True)
    credentials_dict = fetch_credentials()

    if not credentials_dict:
        ctk.CTkLabel(password_frame, text="No credentials found.", 
                    font=ctk.CTkFont("poppins", size=12, weight="bold"),
                    fg_color="#F7F7FE", corner_radius=20, bg_color="#F7F7FE", text_color="#1410DB").pack(pady=20)
    else:
        for row_id, data in credentials_dict.items():
            row = ctk.CTkFrame(password_frame, corner_radius=5, fg_color="#F7F7FE", border_color="black", border_width=1)
            row.pack(fill="x", pady=5, padx=5)

            # Domain
            cwd = os.getcwd()
            imspath = os.path.join(cwd, "Assets","Labels", "globe.png")
            domain_img = Label_image(imspath)

            domain_label = ctk.CTkLabel(row,image=domain_img ,text=f" {data['domain']}, ID: {row_id}", compound='left', font=ctk.CTkFont("poppins", size=12, weight="bold"),
                                        fg_color="#F7F7FE", corner_radius=20, bg_color="#F7F7FE", text_color="#1410DB")
            domain_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

            if data['strength'] == "Weak":
                tc = "red"
            elif data['strength'] == "Medium":
                tc = "orange"
            elif data['strength'] == "Strong":
                tc = "green"
            
            imspath = os.path.join(cwd, "Assets","Labels", "shield.png")
            strn_img = Label_image(imspath)

            strength_label = ctk.CTkLabel(row,image=strn_img ,text=f" Strength: {data['strength']}", compound='left', font=ctk.CTkFont("poppins", 12, "bold"),
                                        fg_color="#F7F7FE", corner_radius=20, bg_color="#F7F7FE", text_color=tc)
            strength_label.grid(row=0, column=1, padx=10, pady=(5, 5), sticky="w")

            # username + Copy Button
            imspath = os.path.join(cwd, "Assets","Labels", "user.png")
            username_img = Label_image(imspath)

            username_label = ctk.CTkLabel(row, image = username_img, text=f" {data['username']}", compound='left', font=ctk.CTkFont("poppins", size=12),
                                    fg_color="#F7F7FE", corner_radius=20, bg_color="#F7F7FE")
            username_label.grid(row=1, column=0, padx=10, sticky="w", pady = 5)

            username_copy = ctk.CTkButton(row, text="Copy usernmae", width=100, command=lambda p=data['password']: copy_to_clipboard(p),
                                    font=("poppins", 11, "bold"), fg_color="#1410DB", text_color="white", height=25)
            username_copy.grid(row=1, column=1, padx=5, pady = 5)

            # Password + Copy Button
            imspath = os.path.join(cwd, "Assets","Labels", "keypass.png")
            pwd_img = Label_image(imspath)

            pwd_label = ctk.CTkLabel(row, image = pwd_img, text=f" {data['password']}", compound='left', font=ctk.CTkFont("poppins", size=12),
                                    fg_color="#F7F7FE", corner_radius=20, bg_color="#F7F7FE")
            pwd_label.grid(row=2, column=0, padx=10, sticky="w", pady = 5)

            pwd_copy = ctk.CTkButton(row, text="Copy Password", width=100, command=lambda p=data['password']: copy_to_clipboard(p),
                                    font=("poppins", 11, "bold"), fg_color="#1410DB", text_color="white", height=25)
            pwd_copy.grid(row=2, column=1, padx=5, pady = 5)

            # Phone + Copy Button
            imspath = os.path.join(cwd, "Assets","Labels", "phone.png")
            phone_img = Label_image(imspath)

            phone_label = ctk.CTkLabel(row,image=phone_img ,text=f" {data['phone']}", compound='left', font=ctk.CTkFont("poppins", size=12),
                                    fg_color="#F7F7FE", corner_radius=20, bg_color="#F7F7FE")
            phone_label.grid(row=3, column=0, padx=10, sticky="w", pady = 5)

            phone_copy = ctk.CTkButton(row, text="Copy Phone", width=100, command=lambda p=data['phone']: copy_to_clipboard(p),
                                    font=("poppins", 11, "bold"), fg_color="#1410DB", text_color="white", height=25)
            phone_copy.grid(row=3, column=1, padx=5, pady = 5)

            # Email + Copy Button

            imspath = os.path.join(cwd, "Assets","Labels", "mail.png")
            email_img = Label_image(imspath)
            
            email_label = ctk.CTkLabel(row,image=email_img ,text=f" {data['email']}", compound='left', font=ctk.CTkFont("poppins", size=12),
                                    fg_color="#F7F7FE", corner_radius=20, bg_color="#F7F7FE")
            email_label.grid(row=4, column=0, padx=10, pady=(0, 5), sticky="w")

            email_copy = ctk.CTkButton(row, text="Copy Email", width=100, command=lambda e=data['email']: copy_to_clipboard(e),
                                    font=("poppins", 11, "bold"), fg_color="#1410DB", text_color="white", height=25)
            email_copy.grid(row=4, column=1, padx=5, pady = 5)

            update_copy = ctk.CTkButton(row, text="Update", width=60, command=lambda e=row_id: update_cred(e),
                                    font=("poppins", 14, "bold"), fg_color="green", text_color="white", height=25)
            update_copy.grid(row=4, column=2, padx=5, pady = 5)

            delete_copy = ctk.CTkButton(row, text="Delete", width=60, command=lambda e=row_id: delete_cred(e),
                                    font=("poppins", 14, "bold"), fg_color="#1410DB", text_color="white", height=25)
            delete_copy.grid(row=4, column=3, padx=5, pady = 5)


def clear_scrollable_frame(scrollable_frame):
    for widget in scrollable_frame.winfo_children():
        widget.destroy()

def is_valid_email(email):
 
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    if re.match(pattern, email):
        return True
    else:
        return False

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme in ("http", "https"), result.netloc])
    except Exception:
        return False
    
def get_platform_name(url):
    ext = tldextract.extract(url)
    domain = ext.domain.lower()

    return domain

def password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score < 3:
        return "Weak"
    elif score == 3 or score == 4:
        return "Medium"
    else:
        return "Strong"

def add_credential(domain, username, password, strength=None, phone=None, email=None, url=None, key = None):
    date_time = datetime.now().strftime("%d/%m/%Y")

    cwd = os.getcwd()
    db_path = os.path.join(cwd, "Data", "credentials.db")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO credentials (domain, username, password, strength, phone, email, url, date_time, key)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (domain, username, password, strength, phone, email, url, date_time, key))

    conn.commit()
    conn.close()
    update_dashboard()
    show_all_pass_recent()
    messagebox.showinfo('Success', "Credentials added successfully.")

def add_pass_db():
    cwd = os.getcwd()
    db_path = os.path.join(cwd, "Data", "credentials.db")
    conn = sqlite3.connect(db_path)

    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS credentials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            domain TEXT NOT NULL,
            username TEXT ,
            password TEXT NOT NULL,
            strength TEXT,
            phone TEXT,
            email TEXT,
            url TEXT,
            date_time TEXT,
            key TEXT
        )
    ''')

    conn.commit()
    conn.close()

    should_add = True

    username_val = username_entry.get().strip()
    password_val = password_entry.get().strip()
    phone_val = phone_entry.get().strip()
    email_val = email_entry.get().strip()
    url_val = url_entry.get().strip()

    username_val = username_val if username_val else None
    password_val = password_val if password_val else None
    phone_val = phone_val if phone_val else None
    email_val = email_val if email_val else None
    url_val = url_val if url_val else None
    

    if password_val is None:
        messagebox.showerror("Empty Password", "No password Provided")
        should_add = False
    else:
        strength = password_strength(password_val)
        key = Fernet.generate_key()
        cipher = Fernet(key)
        password_value = password_val.encode()
        password_encryp = cipher.encrypt(password_value)
        if email_val is not None:
            validEmail = is_valid_email(email_val)
            if validEmail is True:
                pass
            else:
                messagebox.showerror("Incorrect Email", "The email format is not correct.")
                should_add = False

        if url_val is not None:
            validURL = is_valid_url(url_val)
            if validURL:
                domain = get_platform_name(url_val)
            else:
                messagebox.showerror("Invalid URL", "URL is invalid")
                should_add = False
        else:
            domain = None

        try:
            if phone_val is not None:
                phone_val = int(phone_val)
        except ValueError:
            messagebox.showerror("Invalid PhoneNumber", "Phone Number should be integer!")
            should_add = False
        
    if should_add is True:
        add_credential(domain = domain, username = username_val, password = password_encryp, strength=strength,
                        phone=phone_val, email=email_val, url= url_val, key=key)
    else:
        should_add = True
        
                
            
def generate_password():
    length = 12 
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = "@#!*"

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special)
    ]

    all_chars = lowercase + uppercase + digits + special
    password += random.choices(all_chars, k=length - len(password))

    random.shuffle(password)

    return ''.join(password)

def insert_gen_pass():
    password_entry.delete(0, "end")
    password = generate_password()
    password_entry.insert(0, password)  


def customPassword():
    global pass_style
    if an_var.get():
        a_var.set(0)
        n_var.set(0)
        pass_style.insert(0, 'AlphaNumeric')
    elif a_var.get():
        an_var.set(0)
        n_var.set(0)
        pass_style.insert(0, 'Alpha')
    elif n_var.get():
        an_var.set(0)
        a_var.set(0)
        pass_style.insert(0, 'Numeric')
    else:
        pass_style.insert(0, 'AlphaNumeric')

def customChar():
    global pass_char
    if yes_var.get():
        no_var.set(0)
        pass_char.insert(0, True)
    elif no_var.get():
        yes_var.set(0)
        pass_char.insert(0, False)
    else:
        pass_char.insert(0, True)
def Generate_custom_password():
    global pass_style, pass_char

    numm = 3
    
    mod = mods.get()

    if mods.get() == "Select":
        mod = "Anime_Characters"
    try:
        minn = int(min_entry.get())
        if int(min_entry.get())<6:
            minn = 6
        maxx = int(max_entry.get())
        
        if int(max_entry.get()) >25:
            maxx = 25

        if pass_style[0] == "Numeric":
            numm = minn
    except ValueError:
        minn = 6
        maxx = 25
        if pass_style[0] == "Numeric":
            numm = minn
        messagebox.showinfo('Invalid Input', 'Invalid Min or Max input Random Custom Password is generated.')
    
    cstm_passwd = BasicSecurity(password_lenght_limit=(minn,maxx), style=(pass_style[0], numm), premods=mod,
                                special_chars=pass_char[0])
    cstmgenpass_dis.configure(state = NORMAL)
    cstmgenpass_dis.delete(0, "end")
    valuee = cstm_passwd.get_password()
    if valuee is None:
        messagebox.showerror('Length Error', "Try different minimum and maximum value or Mods")
    else:
        cstmgenpass_dis.insert(0, valuee)
    cstmgenpass_dis.configure(state = "readonly")

def add_pass_clear():
    username_entry.delete(0, "end")
    password_entry.delete(0, "end")
    phone_entry.delete(0, "end")
    email_entry.delete(0, "end")
    url_entry.delete(0, "end") 
    username_entry.configure(placeholder_text="Username")
    password_entry.configure(placeholder_text="Password")
    phone_entry.configure(placeholder_text="Phone Number")
    email_entry.configure(placeholder_text="Email")
    url_entry.configure(placeholder_text="URL")

def pass_save_back():
    add_password_canvas.pack_forget()
    password_canvas.pack(fill='both', expand=True)


def get_wifi_credentials():
    os_name = platform.system()
    creds = []
    try:
        if os_name == "Windows":
            out = subprocess.check_output(
                ["netsh", "wlan", "show", "profiles"],
                stderr=subprocess.STDOUT, encoding="utf-8"
            )
            ssids = [line.split(":")[1].strip() for line in out.splitlines() if "All User Profile" in line]
            for ssid in ssids:
                try:
                    pwd_out = subprocess.check_output(
                        ["netsh", "wlan", "show", "profile", ssid, "key=clear"],
                        stderr=subprocess.STDOUT, encoding="utf-8"
                    )
                    pwd = next((ln.split(":")[1].strip() for ln in pwd_out.splitlines() if "Key Content" in ln), "N/A")
                    creds.append((ssid, pwd))
                except subprocess.CalledProcessError:
                    creds.append((ssid, "N/A"))
        elif os_name == "Darwin":
            out = subprocess.check_output(
                ["security", "find-generic-password", "-D", "AirPort network password", "-a", ""],
                stderr=subprocess.DEVNULL, encoding="utf-8"
            )
            ssids = [ln.split('"')[1] for ln in out.splitlines() if "acct" in ln]
            for ssid in ssids:
                try:
                    pwd = subprocess.check_output(
                        ["security", "find-generic-password", "-D", "AirPort network password", "-a", ssid, "-w"],
                        stderr=subprocess.STDOUT, encoding="utf-8"
                    ).strip() or "N/A"
                    creds.append((ssid, pwd))
                except subprocess.CalledProcessError:
                    creds.append((ssid, "N/A"))
        elif os_name == "Linux":
            out = subprocess.check_output(
                ["nmcli", "-t", "-f", "NAME", "connection", "show"],
                stderr=subprocess.STDOUT, encoding="utf-8"
            )
            ssids = out.strip().splitlines()
            for ssid in ssids:
                try:
                    pwd_out = subprocess.check_output(
                        ["nmcli", "-s", "-g", "802-11-wireless-security.psk", "connection", "show", ssid],
                        stderr=subprocess.STDOUT, encoding="utf-8"
                    )
                    pwd = pwd_out.strip() or "N/A"
                    creds.append((ssid, pwd))
                except subprocess.CalledProcessError:
                    creds.append((ssid, "N/A"))
        else:
            raise NotImplementedError(f"Unsupported OS: {os_name}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch Wi‑Fi credentials:\n{e}")
    return creds

def copy_to_clipboard(text):
    win.clipboard_clear()
    win.clipboard_append(text)
    messagebox.showinfo("Copied", f"Content copied to clipboard:\n{text}")

def qr_scanner():
    global qr_content
    try:
        cam = cv2.VideoCapture(0)
        if not cam.isOpened():
            raise IOError("Cannot open webcam")
    except Exception as e:
        messagebox.showerror(f"Error initializing camera:", f"{e}")
        exit(1)

    # Set resolution with error handling
    try:
        cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    except Exception as e:
        messagebox.showerror(f"Error setting camera resolution", f"{e}")
    detected_qr_codes = set()
    last_detection_time = {}

    try:
        while True:
            try:
                success, frame = cam.read()
                if not success or frame is None:
                    print("")
                    messagebox.showerror(f"Failed to capture frame from camera. Retrying...", f"Try Again")
                    time.sleep(0.5)
                    continue

                decoded_objects = decode(frame)
                message_displayed = False

                for obj in decoded_objects:
                    try:
                        qr_data = obj.data.decode("utf-8")
                        qr_type = obj.type
                    except Exception as e:
         
                        messagebox.showerror(f"Error decoding QR data", f"{e}")
                        continue

                    points = obj.polygon
                    if len(points) > 4:
                        try:
                            hull = cv2.convexHull(points)
                            hull = list(map(tuple, hull.reshape(-1, 2)))
                        except Exception as e:
                            messagebox.showerror(f"Error processing polygon hull", f"{e}")
                            hull = points
                    else:
                        hull = points

                    n = len(hull)
                    for j in range(n):
                        pt1 = tuple(map(int, hull[j]))
                        pt2 = tuple(map(int, hull[(j + 1) % n]))
                        cv2.line(frame, pt1, pt2, (0, 255, 0), 3)

                    current_time = time.time()

                    if qr_data in detected_qr_codes:
                        last_seen = last_detection_time.get(qr_data, 0)
                        if current_time - last_seen > 5:
                            last_detection_time[qr_data] = current_time
                            message_displayed = True
                    else:
                        qr_content = []
                        qr_Data = f"Detected QR data: \n{qr_data}"
                        qr_textbox.configure(state = NORMAL)
                        qr_textbox.delete("1.0", "end")
                        qr_textbox.insert("end", qr_Data)
                        qr_textbox.configure(state = DISABLED)
                        detected_qr_codes.add(qr_data)
                        qr_content.insert(0, qr_data)
                        last_detection_time[qr_data] = current_time

                cv2.imshow("QR-Scanner (Press 'q' to exit)", frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            except Exception as e:
                messagebox.showerror(f"Unexpected error during frame processing", f"{e}")
                time.sleep(0.5)

    except KeyboardInterrupt:
        pass

    finally:
        try:
            cam.release()
        except Exception as e:
            messagebox.showerror(f"Error releasing camera", f"{e}")

        try:
            cv2.destroyAllWindows()
        except Exception as e:
            messagebox.showerror(f"Error closing windows", f"{e}")

def scanQR():
    thread = threading.Thread(target=qr_scanner, daemon=True).start()

def copyqr():
    global qr_content
    copy_to_clipboard(qr_content[0])
    
def generate_qr_func():
    # Get text from textbox
    input_text = gen_qr_textbox.get("1.0", END).strip()
    if not input_text:
        messagebox.showerror("No-Input", "Give message to convert to QR")
        return

    # Generate QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(input_text)
    qr.make(fit=True)

    coloropt=["#641e16",'#512e5f','#4a235a','#154360','#1b4f72','#0b5345','#f1c40f','#f39c12','#F08080']
    color=random.choice(coloropt)
    qr_img = qr.make_image(fill_color=color, back_color="white")

    # Save the image
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Image", "*.png")])
    if save_path:
        qr_img.save(save_path)

        # Display image
        img = Image.open(save_path)
        img = img.resize((200, 200))
        img_tk = ImageTk.PhotoImage(img)
        qr_img_label.configure(image=img_tk, text="")
        qr_img_label.image = img_tk  # keep a reference!

def clear_qr():
    gen_qr_textbox.delete("1.0", END)


def update_dashboard():
    try:
        cwd = os.getcwd()
        db_path = os.path.join(cwd, "Data", "credentials.db")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        query = f"SELECT COUNT(*) FROM credentials"
        cursor.execute(query)

        row_count = cursor.fetchone()[0]

        if row_count:
            total_pass_label.configure(text = str(row_count))
        else:
            total_pass_label.configure(text = "00")

        query = "SELECT strength FROM credentials"
        cursor.execute(query)

        values = [row[0] for row in cursor.fetchall()]

        weak = values.count("Weak")
        mid = values.count("Medium")
        strong = values.count("Strong")

        total_weak_pass.configure(text = str(weak))
        total_mid_pass.configure(text = str(mid))
        total_strong_pass.configure(text = str(strong))
        
    except sqlite3.Error as e:
        error = e
    finally:
        if conn:
            conn.close()

def fetch_credentials_resent():
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
        print("Empty Password Data First add some password!")

def show_all_pass_recent():
    credentials_dict = fetch_credentials_resent()

    if not credentials_dict:
        ctk.CTkLabel(recent_password_frame, text="No credentials found.", 
                    font=ctk.CTkFont("poppins", size=12, weight="bold"),
                    fg_color="#F7F7FE", corner_radius=20, bg_color="#F7F7FE", text_color="#1410DB").pack(pady=20)
    else:
        for row_id, data in credentials_dict.items():
            row = ctk.CTkFrame(recent_password_frame, corner_radius=5, fg_color="#F7F7FE", border_color="black", border_width=1)
            row.pack(fill="x", pady=5, padx=5)

            # Domain
            cwd = os.getcwd()
            imspath = os.path.join(cwd, "Assets","Labels", "globe.png")
            domain_img = Label_image(imspath)

            domain_label = ctk.CTkLabel(row,image=domain_img ,text=f" {data['domain']}, ID: {row_id}", compound='left', font=ctk.CTkFont("poppins", size=12, weight="bold"),
                                        fg_color="#F7F7FE", corner_radius=20, bg_color="#F7F7FE", text_color="#1410DB")
            domain_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

            if data['strength'] == "Weak":
                tc = "red"
            elif data['strength'] == "Medium":
                tc = "yellow"
            elif data['strength'] == "Strong":
                tc = "green"
            
            imspath = os.path.join(cwd, "Assets","Labels", "shield.png")
            strn_img = Label_image(imspath)

            strength_label = ctk.CTkLabel(row,image=strn_img ,text=f" Strength: {data['strength']}", compound='left', font=ctk.CTkFont("poppins", 12, "bold"),
                                        fg_color="#F7F7FE", corner_radius=20, bg_color="#F7F7FE", text_color=tc)
            strength_label.grid(row=0, column=1, padx=10, pady=(5, 5), sticky="w")

            # username + Copy Button
            imspath = os.path.join(cwd, "Assets","Labels", "user.png")
            username_img = Label_image(imspath)

            username_label = ctk.CTkLabel(row, image = username_img, text=f" {data['username']}", compound='left', font=ctk.CTkFont("poppins", size=12),
                                    fg_color="#F7F7FE", corner_radius=20, bg_color="#F7F7FE")
            username_label.grid(row=1, column=0, padx=10, sticky="w", pady = 5)

            username_copy = ctk.CTkButton(row, text="Copy usernmae", width=100, command=lambda p=data['password']: copy_to_clipboard(p),
                                    font=("poppins", 11, "bold"), fg_color="#1410DB", text_color="white", height=25)
            username_copy.grid(row=1, column=1, padx=5, pady = 5)

            # Password + Copy Button
            imspath = os.path.join(cwd, "Assets","Labels", "keypass.png")
            pwd_img = Label_image(imspath)

            pwd_label = ctk.CTkLabel(row, image = pwd_img, text=f" {data['password']}", compound='left', font=ctk.CTkFont("poppins", size=12),
                                    fg_color="#F7F7FE", corner_radius=20, bg_color="#F7F7FE")
            pwd_label.grid(row=2, column=0, padx=10, sticky="w", pady = 5)

            pwd_copy = ctk.CTkButton(row, text="Copy Password", width=100, command=lambda p=data['password']: copy_to_clipboard(p),
                                    font=("poppins", 11, "bold"), fg_color="#1410DB", text_color="white", height=25)
            pwd_copy.grid(row=2, column=1, padx=5, pady = 5)

            # Phone + Copy Button
            imspath = os.path.join(cwd, "Assets","Labels", "phone.png")
            phone_img = Label_image(imspath)

            phone_label = ctk.CTkLabel(row,image=phone_img ,text=f" {data['phone']}", compound='left', font=ctk.CTkFont("poppins", size=12),
                                    fg_color="#F7F7FE", corner_radius=20, bg_color="#F7F7FE")
            phone_label.grid(row=3, column=0, padx=10, sticky="w", pady = 5)

            phone_copy = ctk.CTkButton(row, text="Copy Phone", width=100, command=lambda p=data['phone']: copy_to_clipboard(p),
                                    font=("poppins", 11, "bold"), fg_color="#1410DB", text_color="white", height=25)
            phone_copy.grid(row=3, column=1, padx=5, pady = 5)

            # Email + Copy Button

            imspath = os.path.join(cwd, "Assets","Labels", "mail.png")
            email_img = Label_image(imspath)
            
            email_label = ctk.CTkLabel(row,image=email_img ,text=f" {data['email']}", compound='left', font=ctk.CTkFont("poppins", size=12),
                                    fg_color="#F7F7FE", corner_radius=20, bg_color="#F7F7FE")
            email_label.grid(row=4, column=0, padx=10, pady=(0, 5), sticky="w")

            email_copy = ctk.CTkButton(row, text="Copy Email", width=100, command=lambda e=data['email']: copy_to_clipboard(e),
                                    font=("poppins", 11, "bold"), fg_color="#1410DB", text_color="white", height=25)
            email_copy.grid(row=4, column=1, padx=5, pady = 5)


def save_credentials():
    username = username_entry2.get()
    password = password_entry2.get()

    keys = Fernet.generate_key()
    ciphers = Fernet(keys)
    password_values = password.encode()
    password_encryp = ciphers.encrypt(password_values)
    if username and password:
        cwd = os.getcwd()
        db_path = os.path.join(cwd, "Data", "logs.db")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Create the table if it does not already exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                key TEXT NOT NULL
            )
        ''')

        # Insert data into the users table
        cursor.execute('''
            INSERT INTO users (username, password, key)
            VALUES (?, ?, ?)
        ''', (username, password_encryp, keys))

        # Commit changes and close connection
        conn.commit()
        conn.close()
        messagebox.showinfo("Logged In", "Account created succesfully!")

        username_entry.delete(0, ctk.END)
        password_entry.delete(0, ctk.END)
    else:
        messagebox.showinfo("Error", "Please enter both fields")           

win=Tk()
win.geometry("800x500+150+110")
win.title("Vaultify")
win.minsize(800, 500)
win.maxsize(800, 500)
cwd = os.getcwd()
path_ico = os.path.join(cwd, "Assets", "logo.ico")
win.iconbitmap(path_ico)


mainframe=Frame(win,height=770,width=1400,bg='red')
mainframe.propagate(False)
mainframe.pack()


stratup_canvas=Canvas(mainframe,height=770,width=1400,bg='white',bd=0,highlightthickness=0, relief='ridge')
stratup_canvas.propagate(False)
stratup_canvas.pack()

cwd = os.getcwd()
db_path = os.path.join(cwd, "Data", "logs.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute('SELECT COUNT(*) FROM users')
row_counts = cursor.fetchone()[0]
if row_counts == 0:
    imagepath= os.path.join(cwd, "Assets", "UIUX", "nologinentry.png") #cwd+"\\Assets\\UIUX\\nologinentry.png"
    openphoto=Image.open(imagepath).resize((800,500))
    bgimage=ImageTk.PhotoImage(openphoto)
    stratup_canvas.create_image(400,250, image=bgimage)

    continue_button = ctk.CTkButton(stratup_canvas, text="Continue", font=("poppins", 15, 'bold'), bg_color="white",
                                    fg_color="#1410DB", text_color="white", corner_radius=10, height=30, width=100,
                                    command=open_home)
    continue_button.place(relx = 0.5, rely = 0.6, anchor = 'center')
else:
    imagepath= os.path.join(cwd, "Assets", "UIUX", "signin.png") #cwd+"\\Assets\\UIUX\\nologinentry.png"
    openphoto=Image.open(imagepath).resize((800,500))
    bgimage=ImageTk.PhotoImage(openphoto)
    stratup_canvas.create_image(400,250, image=bgimage)

    username_entrys = ctk.CTkEntry(stratup_canvas, font=("poppins", 15), fg_color="white", bg_color="white",
                              text_color="black", border_width=0,placeholder_text="Username",
                              height=25, width=160)
    username_entrys.place(relx = 0.46, rely = 0.5, anchor = 'center')

    password_entrys = ctk.CTkEntry(stratup_canvas, font=("poppins", 15), fg_color="white", bg_color="white",
                                text_color="black", border_width=0,placeholder_text="Password",
                                height=25, width=160)
    password_entrys.place(relx = 0.46, rely = 0.63, anchor = 'center')

    continue_button = ctk.CTkButton(stratup_canvas, text="Continue", font=("poppins", 15, 'bold'), bg_color="white",
                                    fg_color="#1410DB", text_color="white", corner_radius=10, height=30, width=100,
                                    command=open_home2)
    continue_button.place(relx = 0.5, rely = 0.75, anchor = 'center')




home_frame = Frame(win, bg="yellow")
home_frame.propagate(False)

side_frame = Frame(home_frame, bg='#F7F7FE', width=200, relief='groove', bd=2)
side_frame.propagate(False)
side_frame.pack(fill=Y, expand=True, side='left',anchor='nw')

content_frame = Frame(home_frame, bg="green", width=600)
content_frame.propagate(False)
content_frame.pack(fill=Y, expand=True, side='left', anchor='nw')
# --------------------------------------------------------------------------------------------------------------
image_path1 = os.path.join(cwd, "Assets", "Buttons", "home.png") #cwd+"\\Assets\\Buttons\\home.png"
image_home = Image.open(image_path1).resize((24, 24))
button_image1 = ctk.CTkImage(light_image=image_home,size=(24, 24))

home_btn = ctk.CTkButton(side_frame, text="Home", image=button_image1, height=30, font=("poppins",16, 'bold'),
                         fg_color="#1410DB", bg_color="white",compound='left',
                         text_color="white", anchor='w', cursor = "hand2", command=home_func)
home_btn.pack(pady=10, fill="x", padx=10)
home_btn.bind("<Enter>", on_enter_home)
home_btn.bind("<Leave>", on_leave_home)
# --------------------------------------------------------------------------------------------------------------
image_path2 = os.path.join(cwd, "Assets", "Buttons", "password.png") #cwd+"\\Assets\\Buttons\\password.png"
image_pass= Image.open(image_path2).resize((24, 24))
button_image2 = ctk.CTkImage(light_image=image_pass,size=(24, 24))

pass_btn = ctk.CTkButton(side_frame, text="Password", image=button_image2, height=30, font=("poppins",16, 'bold'),
                         fg_color="white", bg_color="white",compound='left',
                         anchor='w',text_color="black", cursor = "hand2", command = pass_func)
pass_btn.pack(pady=10, fill="x", padx=10)

pass_btn.bind("<Enter>", on_enter_pass)
pass_btn.bind("<Leave>", on_leave_pass)
# --------------------------------------------------------------------------------------------------------------

image_path3 = os.path.join(cwd, "Assets", "Buttons", "seedbl.png") #cwd+"\\Assets\\Buttons\\seedbl.png"
image_pass3= Image.open(image_path3).resize((24, 24))
button_image3 = ctk.CTkImage(light_image=image_pass3,size=(24, 24))

passgen_btn = ctk.CTkButton(side_frame, text="Generate", image=button_image3, height=30, font=("poppins",16, 'bold'),
                         fg_color="white", bg_color="white",compound='left',
                         anchor='w',text_color="black", cursor = "hand2", command=passgen_func)
passgen_btn.pack(pady=10, fill="x", padx=10)

passgen_btn.bind("<Enter>", on_enter_passgen)
passgen_btn.bind("<Leave>", on_leave_passgen)
# --------------------------------------------------------------------------------------------------------------

image_path4 = os.path.join(cwd, "Assets", "Buttons", "qrbl.png")  #cwd+"\\Assets\\Buttons\\qrbl.png"
image_pass4= Image.open(image_path4).resize((24, 24))
button_image4 = ctk.CTkImage(light_image=image_pass4,size=(24, 24))

qr_btn = ctk.CTkButton(side_frame, text="QR Codes", image=button_image4, height=30, font=("poppins",16, 'bold'),
                         fg_color="white", bg_color="white",compound='left',
                         anchor='w',text_color="black", cursor = "hand2", command=qr_func)
qr_btn.pack(pady=10, fill="x", padx=10)

qr_btn.bind("<Enter>", on_enter_qr)
qr_btn.bind("<Leave>", on_leave_qr)
# --------------------------------------------------------------------------------------------------------------

image_path5 =os.path.join(cwd, "Assets", "Buttons", "wifibl.png") #cwd+"\\Assets\\Buttons\\wifibl.png"
image_pass5= Image.open(image_path5).resize((24, 24))
button_image5 = ctk.CTkImage(light_image=image_pass5,size=(24, 24))

wifi_btn = ctk.CTkButton(side_frame, text="Wi-Fi", image=button_image5, height=30, font=("poppins",16, 'bold'),
                         fg_color="white", bg_color="white",compound='left',
                         anchor='w',text_color="black", cursor = "hand2", command=wifi_func)
wifi_btn.pack(pady=10, fill="x", padx=10)

wifi_btn.bind("<Enter>", on_enter_wifi)
wifi_btn.bind("<Leave>", on_leave_wifi)

# --------------------------------------------------------------------------------------------------------------
image_path6 = os.path.join(cwd, "Assets", "Buttons", "settbl.png") #cwd+"\\Assets\\Buttons\\settbl.png"
image_pass6= Image.open(image_path6).resize((24, 24))
button_image6 = ctk.CTkImage(light_image=image_pass6,size=(24, 24))

settings_btn = ctk.CTkButton(side_frame, text="Settings", image=button_image6, height=30, font=("poppins",16, 'bold'),
                         fg_color="white", bg_color="white",compound='left',
                         anchor='w',text_color="black", cursor = "hand2", command=setting_func)
settings_btn.pack(pady=10, fill="x", padx=10)

settings_btn.bind("<Enter>", on_enter_settings)
settings_btn.bind("<Leave>", on_leave_settings)
# --------------------------------------------------------------------------------------------------------------

content_canvas=Canvas(content_frame,bg='white',bd=0,highlightthickness=0, relief='ridge')
content_canvas.propagate(False)
content_canvas.pack(fill='both', expand=True)

imagepath7=os.path.join(cwd, "Assets", "UIUX", "dashboard.png") #cwd+"\\Assets\\UIUX\\dashboard.png"
openphoto7=Image.open(imagepath7).resize((600,500))
bgimage7=ImageTk.PhotoImage(openphoto7)
content_canvas.create_image(300,250, image=bgimage7)


total_pass_label = ctk.CTkLabel(content_canvas, text="00", font=("poppins", 15, "bold"), width=30, fg_color="white",
                                bg_color="white", text_color="black")
total_pass_label.place(x = 520, y = 35)

total_weak_pass = ctk.CTkLabel(content_canvas, text="00", font=("poppins", 15, "bold"), width=30, fg_color="white",
                                bg_color="white", text_color="red")
total_weak_pass.place(x = 520, y = 60)

total_mid_pass = ctk.CTkLabel(content_canvas, text="00", font=("poppins", 15, "bold"), width=30, fg_color="white",
                                bg_color="white", text_color="orange")
total_mid_pass.place(x = 520, y = 87)

total_strong_pass = ctk.CTkLabel(content_canvas, text="00", font=("poppins", 15, "bold"), width=30, fg_color="white",
                                bg_color="white", text_color="green")
total_strong_pass.place(x = 520, y = 115)
update_dashboard()

recent_password_frame = ScrollableFrame(content_canvas, width=480, height=200)
recent_password_frame.pack(padx=10, pady=(235, 10), fill="both", expand=True)
show_all_pass_recent()
# --------------------------------------------------------------------------------------------------------------

password_canvas=Canvas(content_frame,bg='white',bd=0,highlightthickness=0, relief='ridge')
password_canvas.propagate(False)

imagepath8=os.path.join(cwd, "Assets", "UIUX", "password_init.png") #cwd+"\\Assets\\UIUX\\password_init.png"
openphoto8=Image.open(imagepath8).resize((600,500))
bgimage8=ImageTk.PhotoImage(openphoto8)
password_canvas.create_image(300,250, image=bgimage8)

add_new_pass_btn = ctk.CTkButton(password_canvas, text="Add New Password", font=("poppins", 15, 'bold'), 
                                 fg_color="#1410DB", bg_color="white", text_color="white", width=157,
                                 command=add_new_pass_canvas)
add_new_pass_btn.pack(side = 'left', padx = (135, 0))
# --------------------------------------------------------------------------------------------------------------


add_password_canvas=Canvas(content_frame,bg='white',bd=0,highlightthickness=0, relief='ridge')
add_password_canvas.propagate(False)


imagepath13=os.path.join(cwd, "Assets", "UIUX", "passdisplay.png") #cwd+"\\Assets\\UIUX\\passdisplay.png"
openphoto13=Image.open(imagepath13).resize((600,500))
bgimage13=ImageTk.PhotoImage(openphoto13)
add_password_canvas.create_image(300,250, image=bgimage13)



username_entry = ctk.CTkEntry(add_password_canvas, font=("poppins", 15), fg_color="white", bg_color="white",
                              text_color="black", border_width=0,placeholder_text="Username",
                              height=25)
username_entry.place(x = 30, y = 96)

password_entry = ctk.CTkEntry(add_password_canvas, font=("poppins", 15), fg_color="white", bg_color="white",
                              text_color="black", border_width=0,placeholder_text="Password",
                              height=25)
password_entry.place(x = 230, y = 96)

gen_pass_btn = ctk.CTkButton(add_password_canvas, text="Generate", font=("poppins", 12), fg_color="#8E8DF1",
                             bg_color="#F7F7FE", height=20, width=70, text_color='black', hover_color="#8E8DF1",
                             cursor = "hand2", command=insert_gen_pass)
gen_pass_btn.place(x = 300, y = 130)


phone_entry = ctk.CTkEntry(add_password_canvas, font=("poppins", 15), fg_color="white", bg_color="white",
                              text_color="black", border_width=0,placeholder_text="Phone Number",
                              height=25)
phone_entry.place(x = 430, y = 96)


email_entry = ctk.CTkEntry(add_password_canvas, font=("poppins", 15), fg_color="white", bg_color="white",
                              text_color="black", border_width=0,placeholder_text="Email",
                              height=25, width=365)
email_entry.place(x = 30, y = 162)

url_entry = ctk.CTkEntry(add_password_canvas, font=("poppins", 15), fg_color="white", bg_color="white",
                              text_color="black", border_width=0,placeholder_text="URL",
                              height=25, width=365)
url_entry.place(x = 30, y = 227)

add_password_btn = ctk.CTkButton(add_password_canvas, text="Add Password", font=("poppins", 15, 'bold'), 
                                 fg_color="#1410DB", bg_color="#F7F7FE", height=35, cursor = "hand2",
                                 width=110, command= add_pass_db)
add_password_btn.place(x = 30, y = 277)

clear_password_btn = ctk.CTkButton(add_password_canvas, text="Clear", font=("poppins", 15, 'bold'), 
                                 fg_color="#f34825", bg_color="#F7F7FE", height=35, cursor = "hand2",
                                 width=70, command=add_pass_clear)
clear_password_btn.place(x = 160, y = 277)

back_password_btn = ctk.CTkButton(add_password_canvas, text="Back", font=("poppins", 15, 'bold'), 
                                 fg_color="#17ac00", bg_color="#F7F7FE", height=35, cursor = "hand2",
                                 width=70, command=pass_save_back)
back_password_btn.place(x = 245, y = 277)

# --------------------------------------------------------------------------------------------------------------


show_all_password = ctk.CTkButton(password_canvas, text="Show all Passwords", font=("poppins", 15, 'bold'), 
                                 fg_color="#1410DB", bg_color="white", text_color="white", command= show_all_pass)
show_all_password.pack(side = 'left', padx = 18)

show_password_canvas=Canvas(content_frame,bg='white',bd=0,highlightthickness=0, relief='ridge')
show_password_canvas.propagate(False)

imagepath14=os.path.join(cwd, "Assets", "UIUX", "passwordss.png") #cwd+"\\Assets\\UIUX\\passwordss.png"
openphoto14=Image.open(imagepath14).resize((600,500))
bgimage14=ImageTk.PhotoImage(openphoto14)
show_password_canvas.create_image(300,250, image=bgimage14)

password_frame = ScrollableFrame(show_password_canvas, width=480, height=480)
password_frame.pack(padx=10, pady=(70, 10), fill="both", expand=True)

# --------------------------------------------------------------------------------------------------------------

passgen_canvas=Canvas(content_frame,bg='white',bd=0,highlightthickness=0, relief='ridge')
passgen_canvas.propagate(False)

imagepath9=os.path.join(cwd, "Assets", "UIUX", "custompass3.png") #cwd+"\\Assets\\UIUX\\custompass3.png"
openphoto9=Image.open(imagepath9).resize((600,500))
bgimage9=ImageTk.PhotoImage(openphoto9)
passgen_canvas.create_image(300,250, image=bgimage9)


min_entry = ctk.CTkEntry(passgen_canvas, font=("poppins", 12), placeholder_text="Min 6", fg_color="white", bg_color="white",
                         text_color="black", border_width=1, corner_radius=5, border_color="black", 
                         width=80, height=25)
min_entry.place(x = 140, y = 197)

max_entry = ctk.CTkEntry(passgen_canvas, font=("poppins", 12), placeholder_text="Max 25", fg_color="white", bg_color="white",
                         text_color="black", border_width=1, corner_radius=5, border_color="black", 
                         width=80, height=25)
max_entry.place(x = 140, y = 253)
an_var = IntVar()

an_cb = ctk.CTkCheckBox(passgen_canvas, text="Alpha Numeric", font=('poppins', 14 ), fg_color="#1410DB", bg_color="white",
                        text_color="black", checkmark_color="white", checkbox_height=24, checkbox_width=24,
                        command= customPassword, variable=an_var)
an_cb.place(x =240, y = 187 )

a_var = IntVar()
a_cb = ctk.CTkCheckBox(passgen_canvas, text="Alpha", font=('poppins', 14 ), fg_color="#1410DB", bg_color="white",
                        text_color="black", checkmark_color="white", checkbox_height=24, checkbox_width=24,
                        command= customPassword, variable=a_var)
a_cb.place(x =240, y = 220 )

n_var = IntVar()
n_cb = ctk.CTkCheckBox(passgen_canvas, text="Numeric", font=('poppins', 14 ), fg_color="#1410DB", bg_color="white",
                        text_color="black", checkmark_color="white", checkbox_height=24, checkbox_width=24,
                        command= customPassword, variable=n_var)
n_cb.place(x =240, y = 250 )

yes_var = IntVar()
spchar_cb_yes = ctk.CTkCheckBox(passgen_canvas, text="Yes", font=('poppins', 14 ), fg_color="#1410DB", bg_color="white",
                        text_color="black", checkmark_color="white", checkbox_height=24, checkbox_width=24,
                        variable=yes_var, command=customChar)
spchar_cb_yes.place(x =380, y = 187 )

no_var = IntVar()
spchar_cb_no = ctk.CTkCheckBox(passgen_canvas, text="No", font=('poppins', 14 ), fg_color="#1410DB", bg_color="white",
                        text_color="black", checkmark_color="white", checkbox_height=24, checkbox_width=24,
                        variable=no_var, command=customChar)
spchar_cb_no.place(x =380, y = 240 )

value = ['Fruits','Flowers','Animals','Movies','Celebrities','Anime_Characters','Gaming_ID']
mods = ctk.CTkOptionMenu(passgen_canvas, values=value, fg_color="#1410DB", text_color="white",
                         height=30, width=150, bg_color="white")
mods.place(relx = 0.46, rely = 0.675, anchor = 'center')
mods.set("Select")

cstmgenpass_dis = ctk.CTkEntry(passgen_canvas, font=("poppins",12), fg_color="white", bg_color="white",
                               border_width=1, border_color='black', state=DISABLED)
cstmgenpass_dis.place(relx = 0.65, rely = 0.785, anchor = 'center')


gen_btn = ctk.CTkButton(passgen_canvas, text="Generate", font=("poppins", 12, "bold"), fg_color="#1410DB",
                        bg_color="white", text_color="white", command=Generate_custom_password)
gen_btn.place(relx = 0.5, rely = 0.9, anchor = "center")
# --------------------------------------------------------------------------------------------------------------

qr_canvas=Canvas(content_frame,bg='white',bd=0,highlightthickness=0, relief='ridge')
qr_canvas.propagate(False)

imagepath10=os.path.join(cwd, "Assets", "UIUX", "qrqr.png") #cwd+"\\Assets\\UIUX\\qrqr.png"
openphoto10=Image.open(imagepath10).resize((600,500))
bgimage10=ImageTk.PhotoImage(openphoto10)
qr_canvas.create_image(300,250, image=bgimage10)

qr_textbox = ctk.CTkTextbox(qr_canvas, font=("poppins", 12), height=190, width=218, border_width=0, border_color="black",
                            scrollbar_button_color="#1410DB", state = DISABLED)
qr_textbox.pack(pady = (125, 0))

scan_qr_btn = ctk.CTkButton(qr_canvas,text="Scan QR-Code", bg_color="white", fg_color="#1410DB", font=("poppins", 12, "bold"),
                            text_color="white", cursor = "hand2", command=scanQR, width=100)

scan_qr_btn.place(relx = 0.4, rely = 0.7, anchor = 'center')

copy_qr = ctk.CTkButton(qr_canvas,text="Copy QR-Code", bg_color="white", fg_color="green", font=("poppins", 12, "bold"),
                            text_color="white", cursor = "hand2", width=100, command=copyqr)

copy_qr.place(relx = 0.6, rely = 0.7, anchor = 'center')

generate_qr = ctk.CTkButton(qr_canvas,text="Generate QR-Code", bg_color="white", fg_color="white", font=("poppins", 12, "bold"),
                            text_color="black", cursor = "hand2", width=100, border_color="black", border_width=1,
                            command=gen_qr_func)

generate_qr.place(relx = 0.5, rely = 0.9, anchor = 'center')

gen_qr_canvas=Canvas(content_frame,bg='white',bd=0,highlightthickness=0, relief='ridge')
gen_qr_canvas.propagate(False)

imagepath15=os.path.join(cwd, "Assets", "UIUX", "genqr.png") #cwd+"\\Assets\\UIUX\\genqr.png"
openphoto15=Image.open(imagepath15).resize((600,500))
bgimage15=ImageTk.PhotoImage(openphoto15)
gen_qr_canvas.create_image(300,250, image=bgimage15)

qr_store_frame = ctk.CTkFrame(gen_qr_canvas, fg_color="white", bg_color="white", height=200,
                              width=200, border_color="black", border_width=1)
qr_store_frame.place(x = 40, y = 140)

qr_img_label = Label(qr_store_frame)
qr_img_label.pack(fill='both', expand=True)

gen_qr_textbox = ctk.CTkTextbox(gen_qr_canvas, font=("poppins", 12), height=190, width=218, border_width=0, border_color="black",
                            scrollbar_button_color="#1410DB")
gen_qr_textbox.pack(pady = (137, 0), padx = (285, 0))

gen_qr_btn = ctk.CTkButton(gen_qr_canvas,text="Generate QR-Code", bg_color="white", fg_color="#1410DB", font=("poppins", 12, "bold"),
                            text_color="white", cursor = "hand2", command= generate_qr_func, width=100)

gen_qr_btn.place(relx = 0.64, rely = 0.74, anchor = 'center')

gen_clear_tb = ctk.CTkButton(gen_qr_canvas,text="Clear Textbox", bg_color="white", fg_color="green", font=("poppins", 12, "bold"),
                            text_color="white", cursor = "hand2", width=100, command=clear_qr)

gen_clear_tb.place(relx = 0.84, rely = 0.74, anchor = 'center')

qr_back = ctk.CTkButton(gen_qr_canvas,text="Back", bg_color="white", fg_color="white", font=("poppins", 12, "bold"),
                            text_color="black", cursor = "hand2", width=100, border_color="black", border_width=1,
                            command=gen_qr_back)

qr_back.place(relx = 0.5, rely = 0.9, anchor = 'center')

# --------------------------------------------------------------------------------------------------------------

wifi_canvas=Canvas(content_frame,bg='white',bd=0,highlightthickness=0, relief='ridge')
wifi_canvas.propagate(False)

imagepath12=os.path.join(cwd, "Assets", "UIUX", "passwordss.png") #cwd+"\\Assets\\UIUX\\passwordss.png"
openphoto12=Image.open(imagepath12).resize((600,500))
bgimage12=ImageTk.PhotoImage(openphoto12)
wifi_canvas.create_image(300,250, image=bgimage12)

wifi_frame = ScrollableFrame(wifi_canvas, width=480, height=480)
wifi_frame.pack(padx=10, pady=(70, 10), fill="both", expand=True)

creds = get_wifi_credentials()

if not creds:
    ctk.CTkLabel(wifi_frame, text="No Wi‑Fi profiles found.", font=ctk.CTkFont("poppins",size=12, weight="bold"),fg_color="#F7F7FE", corner_radius=20, bg_color="#F7F7FE", text_color="#1410DB").pack(pady=20)
else:
    for ssid, pwd in creds:
        row = ctk.CTkFrame(wifi_frame, corner_radius=5, fg_color="#F7F7FE", border_color="black", border_width=1)
        row.pack(fill="x", pady=5)
        label_ssid = ctk.CTkLabel(row, text=f"📶 {ssid}", font=ctk.CTkFont("poppins",size=12, weight="bold"),
                                  fg_color="#F7F7FE", corner_radius=20, bg_color="#F7F7FE", text_color="#1410DB")
        label_ssid.pack(side="left", padx=10, pady=8)
        label_pwd = ctk.CTkLabel(row, text=f"{pwd}", font=ctk.CTkFont("poppins",size=12),
                                 fg_color="#F7F7FE", corner_radius=20, bg_color="#F7F7FE")
        label_pwd.pack(side="left", padx=10)
        btn = ctk.CTkButton(row, text="Copy", width=60, command=lambda p=pwd: copy_to_clipboard(p), font=("poppins", 12, "bold"),
                            fg_color="#1410DB", text_color="white")
        btn.pack(side="right", padx=10)
# --------------------------------------------------------------------------------------------------------------


settings_canvas=Canvas(content_frame,bg='white',bd=0,highlightthickness=0, relief='ridge')
settings_canvas.propagate(False)

imagepath11=os.path.join(cwd, "Assets", "UIUX", "settingsdis.png") #cwd+"\\Assets\\UIUX\\passwordss.png"
openphoto11=Image.open(imagepath11).resize((600,500))
bgimage11=ImageTk.PhotoImage(openphoto11)
settings_canvas.create_image(300,250, image=bgimage11)


username_label = ctk.CTkLabel(settings_canvas, text="Username:", font=("poppins", 15, "bold"))
username_label.place(x = 10, y = 120)
username_entry2 = ctk.CTkEntry(settings_canvas, font=("poppins", 13), width=150, placeholder_text="Username" )
username_entry2.place(x = 100, y = 120)

# Password label and entry
password_label = ctk.CTkLabel(settings_canvas, text="Password:", font=("poppins", 15, "bold"))
password_label.place(x = 10, y = 170)
password_entry2 = ctk.CTkEntry(settings_canvas, font=("poppins", 13), width=150, placeholder_text="Password")
password_entry2.place(x = 100, y = 170)

# Save button
save_button = ctk.CTkButton(settings_canvas, text="Save", font=("poppins", 15, "bold"),fg_color="#1410DB",
                            bg_color="white", text_color="white", command=save_credentials)
save_button.place(x = 50, y = 220 )



win.mainloop()