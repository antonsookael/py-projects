import tkinter as tk
import random
import string
import json

top_window = [None]
lenght = "200"
savewindsize = f"300x{lenght}+500+200"


def clicked():
    chars = string.ascii_letters + string.digits
    password = "".join(random.choices(chars, k=12))
    gen_password.config(text=password)

def copy():
    window.clipboard_clear()
    window.clipboard_append(gen_password.cget("text"))
    copy_label.config(text="Copied!")

def save_pass():
    try:
        with open("passwords.json", "r") as f:
            passwords = json.load(f)
    except FileNotFoundError:
        passwords = []
    savcount = len(passwords)
    if savcount == 10:
        many_pass = tk.Label(window, text="Too many passwords saved.")
        many_pass.place(x=200, y=250)
    else:
        passwords.append(gen_password.cget("text"))
    
        with open("passwords.json", "w") as f:
            json.dump(passwords, f)
        copy_label.config(text="Saved!")
    
    if top_window[0] is not None and top_window[0].winfo_exists():
        top_window[0].destroy()
        show_passwords()

def delete_savpass(index):
    try:
        with open("passwords.json", "r") as f:
            passwords = json.load(f)
        passwords.pop(index)
        with open("passwords.json", "w") as f:
            json.dump(passwords, f)
    except FileNotFoundError:
        pass

def show_passwords():
    top_window[0] = tk.Toplevel(window)
    top_window[0].title("Saved Passwords")
    
    try:
        with open("passwords.json", "r") as f:
            passwords = json.load(f)
    except FileNotFoundError:
        passwords = []
    
    savcount = len(passwords)
    
    if savcount >= 9:
        length = "500"
    elif savcount >= 7:
        length = "400"
    elif savcount >= 5:
        length = "300"
    else:
        length = "200"
    
    top_window[0].geometry(f"300x{length}+500+200")
        
    def delete_and_refresh(idx):
        delete_savpass(idx)
        top_window[0].destroy()
        show_passwords()

    for i, p in enumerate(passwords, 0):
        tk.Label(top_window[0], text=f"{i+1}. {p}").pack()
        tk.Button(top_window[0], text="Delete", command=lambda idx=i: delete_and_refresh(idx)).pack()

window = tk.Tk()
window.title("Password Generator")
window.geometry("400x300")

label = tk.Label(window, text="Welcome to the password generator.")
label.place(x=100, y=20)

genbutton = tk.Button(window, text="Generate", command=clicked)
genbutton.place(x=100, y=150)

gen_password = tk.Label(window, text="", font=("Courier", 14))
gen_password.place(x=130, y=80)

copybutton = tk.Button(window, text="Copy", command=copy)
copybutton.place(x=180, y=150)

copy_label = tk.Label(window, text="")
copy_label.place(x=170, y=120)

savebutton = tk.Button(window, text="Save", command=save_pass)
savebutton.place(x=245, y=150)

showbutton = tk.Button(window, text="Saved", command=show_passwords)
showbutton.place(x=280, y=150)

window.mainloop()