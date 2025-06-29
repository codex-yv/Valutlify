from tkinter import *
from tkinter import messagebox
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

current_winfo = ["Dashboard"]

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
            self.image_path = cwd+"\\Assets\\Buttons\\home1.png"
            self.image_pass1= Image.open(self.image_path).resize((24, 24))
            self.button_image1 = ctk.CTkImage(light_image=self.image_pass1,size=(24, 24))
            home_btn.configure(text_color = "black", image = self.button_image1, fg_color = "white")

        elif self.prev_label == "Password":

            self.image_path = cwd+"\\Assets\\Buttons\\password.png"
            self.image_pass1= Image.open(self.image_path).resize((24, 24))
            self.button_image1 = ctk.CTkImage(light_image=self.image_pass1,size=(24, 24))
            pass_btn.configure(text_color = "black", image = self.button_image1, fg_color = "white")

        elif self.prev_label == "Generate":

            self.image_path = cwd+"\\Assets\\Buttons\\seedbl.png"
            self.image_pass1= Image.open(self.image_path).resize((24, 24))
            self.button_image1 = ctk.CTkImage(light_image=self.image_pass1,size=(24, 24))
            passgen_btn.configure(text_color = "black", image = self.button_image1, fg_color = "white")
        
        elif self.prev_label == "QR":

            self.image_path = cwd+"\\Assets\\Buttons\\qrbl.png"
            self.image_pass1= Image.open(self.image_path).resize((24, 24))
            self.button_image1 = ctk.CTkImage(light_image=self.image_pass1,size=(24, 24))
            qr_btn.configure(text_color = "black", image = self.button_image1, fg_color = "white")


        elif self.prev_label == "wifi":

            self.image_path = cwd+"\\Assets\\Buttons\\wifibl.png"
            self.image_pass1= Image.open(self.image_path).resize((24, 24))
            self.button_image1 = ctk.CTkImage(light_image=self.image_pass1,size=(24, 24))
            wifi_btn.configure(text_color = "black", image = self.button_image1, fg_color = "white")
        
        elif self.prev_label == "Settings":

            self.image_path = cwd+"\\Assets\\Buttons\\settbl.png"
            self.image_pass1= Image.open(self.image_path).resize((24, 24))
            self.button_image1 = ctk.CTkImage(light_image=self.image_pass1,size=(24, 24))
            settings_btn.configure(text_color = "black", image = self.button_image1, fg_color = "white")
        

def open_home():
    mainframe.pack_forget()
    home_frame.pack(fill='both', expand=True)

def on_enter_home(e):
    global current_winfo
    if current_winfo[0] != "Dashboard":
        image_path = cwd+"\\Assets\\Buttons\\home.png"
        image_pass= Image.open(image_path).resize((24, 24))
        button_image = ctk.CTkImage(light_image=image_pass,size=(24, 24))
        home_btn.configure(text_color = "White", image = button_image, fg_color = "#1410DB")

def on_leave_home(e):
    global current_winfo
    if current_winfo[0] != "Dashboard":
        image_path = cwd+"\\Assets\\Buttons\\home1.png"
        image_pass= Image.open(image_path).resize((24, 24))
        button_image = ctk.CTkImage(light_image=image_pass,size=(24, 24))
        home_btn.configure(text_color = "Black", image = button_image, fg_color = "White")

def on_enter_pass(e):
    global current_winfo
    if current_winfo[0] != "Password":
        image_path = cwd+"\\Assets\\Buttons\\lock.png"
        image_pass= Image.open(image_path).resize((24, 24))
        button_image = ctk.CTkImage(light_image=image_pass, size=(24, 24))
        pass_btn.configure(text_color = "White", image = button_image, fg_color = "#1410DB")

def on_leave_pass(e):
    global current_winfo
    if current_winfo[0] != "Password":
        image_path = cwd+"\\Assets\\Buttons\\password.png"
        image_pass= Image.open(image_path).resize((24, 24))
        button_image = ctk.CTkImage(light_image=image_pass,size=(24, 24))
        pass_btn.configure(text_color = "Black", image = button_image, fg_color = "White")

def on_enter_passgen(e):
    global current_winfo
    if current_winfo[0] != "Generate":
        image_path = cwd+"\\Assets\\Buttons\\seedling.png"
        image_pass= Image.open(image_path).resize((24, 24))
        button_image = ctk.CTkImage(light_image=image_pass, size=(24, 24))
        passgen_btn.configure(text_color = "White", image = button_image, fg_color = "#1410DB")

def on_leave_passgen(e):
    global current_winfo
    if current_winfo[0] != "Generate":
        image_path = cwd+"\\Assets\\Buttons\\seedbl.png"
        image_pass= Image.open(image_path).resize((24, 24))
        button_image = ctk.CTkImage(light_image=image_pass,size=(24, 24))
        passgen_btn.configure(text_color = "Black", image = button_image, fg_color = "White")


def on_enter_qr(e):
    global current_winfo
    if current_winfo[0] != "QR":
        image_path = cwd+"\\Assets\\Buttons\\qr-code.png"
        image_pass= Image.open(image_path).resize((24, 24))
        button_image = ctk.CTkImage(light_image=image_pass, size=(24, 24))
        qr_btn.configure(text_color = "White", image = button_image, fg_color = "#1410DB")

def on_leave_qr(e):
    global current_winfo
    if current_winfo[0] != "QR":
        image_path = cwd+"\\Assets\\Buttons\\qrbl.png"
        image_pass= Image.open(image_path).resize((24, 24))
        button_image = ctk.CTkImage(light_image=image_pass,size=(24, 24))
        qr_btn.configure(text_color = "Black", image = button_image, fg_color = "White")

def on_enter_wifi(e):
    global current_winfo
    if current_winfo[0] != "wifi":
        image_path = cwd+"\\Assets\\Buttons\\wifi.png"
        image_pass= Image.open(image_path).resize((24, 24))
        button_image = ctk.CTkImage(light_image=image_pass, size=(24, 24))
        wifi_btn.configure(text_color = "White", image = button_image, fg_color = "#1410DB")

def on_leave_wifi(e):
    global current_winfo
    if current_winfo[0] != "wifi":
        image_path = cwd+"\\Assets\\Buttons\\wifibl.png"
        image_pass= Image.open(image_path).resize((24, 24))
        button_image = ctk.CTkImage(light_image=image_pass,size=(24, 24))
        wifi_btn.configure(text_color = "Black", image = button_image, fg_color = "White")

def on_enter_settings(e):
    global current_winfo
    if current_winfo[0] != "Settings":
        image_path = cwd+"\\Assets\\Buttons\\settings.png"
        image_pass= Image.open(image_path).resize((24, 24))
        button_image = ctk.CTkImage(light_image=image_pass, size=(24, 24))
        settings_btn.configure(text_color = "White", image = button_image, fg_color = "#1410DB")

def on_leave_settings(e):
    global current_winfo
    if current_winfo[0] != "Settings":
        image_path = cwd+"\\Assets\\Buttons\\settbl.png"
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
    content_canvas.pack(fill='both', expand=True)

    image_path = cwd+"\\Assets\\Buttons\\home.png"
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
    add_password_canvas.pack_forget()

    password_canvas.pack(fill='both', expand=True)

    image_path = cwd+"\\Assets\\Buttons\\lock.png"
    
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
    passgen_canvas.pack(fill='both', expand=True)

    image_path = cwd+"\\Assets\\Buttons\\seedling.png"
    
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
    add_password_canvas.pack_forget()
    qr_canvas.pack(fill='both', expand=True)

    image_path = cwd+"\\Assets\\Buttons\\qr-code.png"
    
    static = StaticColor(qr_btn, image_path)

    if current_winfo[0]!= "QR":
        static.resetColor(current_winfo[0])

    current_winfo.insert(0, "QR")

def wifi_func():
    global current_winfo
    content_canvas.pack_forget()
    password_canvas.pack_forget()
    passgen_canvas.pack_forget()
    qr_canvas.pack_forget()
    settings_canvas.pack_forget()
    add_password_canvas.pack_forget()
    wifi_canvas.pack(fill='both', expand=True)

    image_path = cwd+"\\Assets\\Buttons\\wifi.png"
    
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
    wifi_canvas.pack_forget()

    settings_canvas.pack(fill='both', expand=True)

    image_path = cwd+"\\Assets\\Buttons\\settings.png"
    
    static = StaticColor(settings_btn, image_path)

    if current_winfo[0]!= "Settings":
        static.resetColor(current_winfo[0])

    current_winfo.insert(0, "Settings")

def add_new_pass_canvas():
    password_canvas.pack_forget()
    add_password_canvas.pack(fill='both', expand=True)

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

    username_val = username_entry.get()
    password_val = password_entry.get()
    phone_val = phone_entry.get()
    email_val = email_entry.get()
    url_val = url_entry.get()

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

win=Tk()
win.geometry("800x500+150+110")
win.title("Bazaro")
# win.iconbitmap('logo.ico')


mainframe=Frame(win,height=770,width=1400,bg='red')
mainframe.propagate(False)
mainframe.pack()


stratup_canvas=Canvas(mainframe,height=770,width=1400,bg='white',bd=0,highlightthickness=0, relief='ridge')
stratup_canvas.propagate(False)
stratup_canvas.pack()

cwd = os.getcwd()

imagepath=cwd+"\\Assets\\UIUX\\nologinentry.png"
openphoto=Image.open(imagepath).resize((800,500))
bgimage=ImageTk.PhotoImage(openphoto)
stratup_canvas.create_image(400,250, image=bgimage)

continue_button = ctk.CTkButton(stratup_canvas, text="Continue", font=("poppins", 15, 'bold'), bg_color="white",
                                fg_color="#1410DB", text_color="white", corner_radius=10, height=30, width=100,
                                command=open_home)
continue_button.place(relx = 0.5, rely = 0.6, anchor = 'center')

home_frame = Frame(win, bg="yellow")
home_frame.propagate(False)

side_frame = Frame(home_frame, bg='#F7F7FE', width=200, relief='groove', bd=2)
side_frame.propagate(False)
side_frame.pack(fill=Y, expand=True, side='left',anchor='nw')

content_frame = Frame(home_frame, bg="green", width=600)
content_frame.propagate(False)
content_frame.pack(fill=Y, expand=True, side='left', anchor='nw')
# --------------------------------------------------------------------------------------------------------------
image_path1 = cwd+"\\Assets\\Buttons\\home.png"
image_home = Image.open(image_path1).resize((24, 24))
button_image1 = ctk.CTkImage(light_image=image_home,size=(24, 24))

home_btn = ctk.CTkButton(side_frame, text="Home", image=button_image1, height=30, font=("poppins",16, 'bold'),
                         fg_color="#1410DB", bg_color="white",compound='left',
                         text_color="white", anchor='w', cursor = "hand2", command=home_func)
home_btn.pack(pady=10, fill="x", padx=10)
home_btn.bind("<Enter>", on_enter_home)
home_btn.bind("<Leave>", on_leave_home)
# --------------------------------------------------------------------------------------------------------------
image_path2 = cwd+"\\Assets\\Buttons\\password.png"
image_pass= Image.open(image_path2).resize((24, 24))
button_image2 = ctk.CTkImage(light_image=image_pass,size=(24, 24))

pass_btn = ctk.CTkButton(side_frame, text="Password", image=button_image2, height=30, font=("poppins",16, 'bold'),
                         fg_color="white", bg_color="white",compound='left',
                         anchor='w',text_color="black", cursor = "hand2", command = pass_func)
pass_btn.pack(pady=10, fill="x", padx=10)

pass_btn.bind("<Enter>", on_enter_pass)
pass_btn.bind("<Leave>", on_leave_pass)
# --------------------------------------------------------------------------------------------------------------

image_path3 = cwd+"\\Assets\\Buttons\\seedbl.png"
image_pass3= Image.open(image_path3).resize((24, 24))
button_image3 = ctk.CTkImage(light_image=image_pass3,size=(24, 24))

passgen_btn = ctk.CTkButton(side_frame, text="Generate", image=button_image3, height=30, font=("poppins",16, 'bold'),
                         fg_color="white", bg_color="white",compound='left',
                         anchor='w',text_color="black", cursor = "hand2", command=passgen_func)
passgen_btn.pack(pady=10, fill="x", padx=10)

passgen_btn.bind("<Enter>", on_enter_passgen)
passgen_btn.bind("<Leave>", on_leave_passgen)
# --------------------------------------------------------------------------------------------------------------

image_path4 = cwd+"\\Assets\\Buttons\\qrbl.png"
image_pass4= Image.open(image_path4).resize((24, 24))
button_image4 = ctk.CTkImage(light_image=image_pass4,size=(24, 24))

qr_btn = ctk.CTkButton(side_frame, text="QR Codes", image=button_image4, height=30, font=("poppins",16, 'bold'),
                         fg_color="white", bg_color="white",compound='left',
                         anchor='w',text_color="black", cursor = "hand2", command=qr_func)
qr_btn.pack(pady=10, fill="x", padx=10)

qr_btn.bind("<Enter>", on_enter_qr)
qr_btn.bind("<Leave>", on_leave_qr)
# --------------------------------------------------------------------------------------------------------------

image_path5 = cwd+"\\Assets\\Buttons\\wifibl.png"
image_pass5= Image.open(image_path5).resize((24, 24))
button_image5 = ctk.CTkImage(light_image=image_pass5,size=(24, 24))

wifi_btn = ctk.CTkButton(side_frame, text="Wi-Fi", image=button_image5, height=30, font=("poppins",16, 'bold'),
                         fg_color="white", bg_color="white",compound='left',
                         anchor='w',text_color="black", cursor = "hand2", command=wifi_func)
wifi_btn.pack(pady=10, fill="x", padx=10)

wifi_btn.bind("<Enter>", on_enter_wifi)
wifi_btn.bind("<Leave>", on_leave_wifi)

# --------------------------------------------------------------------------------------------------------------
image_path6 = cwd+"\\Assets\\Buttons\\settbl.png"
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

imagepath7=cwd+"\\Assets\\UIUX\\dashboard.png"
openphoto7=Image.open(imagepath7).resize((600,500))
bgimage7=ImageTk.PhotoImage(openphoto7)
content_canvas.create_image(300,250, image=bgimage7)


# --------------------------------------------------------------------------------------------------------------

password_canvas=Canvas(content_frame,bg='white',bd=0,highlightthickness=0, relief='ridge')
password_canvas.propagate(False)

imagepath8=cwd+"\\Assets\\UIUX\\password_init.png"
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


imagepath13=cwd+"\\Assets\\UIUX\\passdisplay.png"
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
                                 fg_color="#1410DB", bg_color="#F7F7FE", height=35, cursor = "hand2",
                                 width=70)
clear_password_btn.place(x = 160, y = 277)

back_password_btn = ctk.CTkButton(add_password_canvas, text="Back", font=("poppins", 15, 'bold'), 
                                 fg_color="#1410DB", bg_color="#F7F7FE", height=35, cursor = "hand2",
                                 width=70)
back_password_btn.place(x = 245, y = 277)

# --------------------------------------------------------------------------------------------------------------

show_all_password = ctk.CTkButton(password_canvas, text="Show all Passwords", font=("poppins", 15, 'bold'), 
                                 fg_color="#1410DB", bg_color="white", text_color="white")
show_all_password.pack(side = 'left', padx = 18)
# --------------------------------------------------------------------------------------------------------------

passgen_canvas=Canvas(content_frame,bg='white',bd=0,highlightthickness=0, relief='ridge')
passgen_canvas.propagate(False)

imagepath9=cwd+"\\Assets\\UIUX\\custompass2.png"
openphoto9=Image.open(imagepath9).resize((600,500))
bgimage9=ImageTk.PhotoImage(openphoto9)
passgen_canvas.create_image(300,250, image=bgimage9)




# --------------------------------------------------------------------------------------------------------------

qr_canvas=Canvas(content_frame,bg='white',bd=0,highlightthickness=0, relief='ridge')
qr_canvas.propagate(False)

imagepath10=cwd+"\\Assets\\UIUX\\qrqr.png"
openphoto10=Image.open(imagepath10).resize((600,500))
bgimage10=ImageTk.PhotoImage(openphoto10)
qr_canvas.create_image(300,250, image=bgimage10)

# --------------------------------------------------------------------------------------------------------------

wifi_canvas=Canvas(content_frame,bg='white',bd=0,highlightthickness=0, relief='ridge')
wifi_canvas.propagate(False)

imagepath12=cwd+"\\Assets\\UIUX\\passwordss.png"
openphoto12=Image.open(imagepath12).resize((600,500))
bgimage12=ImageTk.PhotoImage(openphoto12)
wifi_canvas.create_image(300,250, image=bgimage12)

# --------------------------------------------------------------------------------------------------------------


settings_canvas=Canvas(content_frame,bg='white',bd=0,highlightthickness=0, relief='ridge')
settings_canvas.propagate(False)

imagepath11=cwd+"\\Assets\\UIUX\\passwordss.png"
openphoto11=Image.open(imagepath11).resize((600,500))
bgimage11=ImageTk.PhotoImage(openphoto11)
settings_canvas.create_image(300,250, image=bgimage11)



win.mainloop()