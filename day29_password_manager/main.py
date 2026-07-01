from tkinter import *
from tkinter import messagebox
import secrets
import string

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(13))
    password_input.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website)==0 or len(email)==0 or len(password)==0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left anything blanc.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmal: {email}\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            website_input.delete(0, END)
            password_input.delete(0,END)
            with open("passwords.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image = logo)

# Labels
website_label = Label(text="Website:")
email_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

# Buttons
generate_password_btn = Button(text="Generate Password", command=generate_password)
add_btn = Button(text="Add", width=36, command=save_password)

# Input
website_input = Entry(width=35)
website_input.focus()
email_input = Entry(width=35)
password_input = Entry(width=21)

# Layout
canvas.grid(row=0, column=1)
website_label.grid(row=1, column=0)
website_input.grid(row=1, column=1, columnspan=2, sticky="ew")
email_label.grid(row=2, column=0)
email_input.grid(row=2, column=1, columnspan=2, sticky="ew")
password_label.grid(row=3, column=0)
password_input.grid(row=3, column=1, sticky="ew")
generate_password_btn.grid(row=3, column=2)
add_btn.grid(row=4, column=1, columnspan=2, sticky="ew")





window.mainloop()
