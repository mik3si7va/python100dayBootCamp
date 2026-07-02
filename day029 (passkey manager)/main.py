from tkinter import *
from tkinter import messagebox
from os import path
import random
import pyperclip

directory = path.dirname(__file__)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"


def generate_password():
    password = "".join(random.choice(chars) for _ in range(16))
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)  # Copy the generated password to the clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please make sure you haven't left any fields empty."
        )
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered:\nFrom {website}: \nEmail: {email} "
            f"\nPassword: {password} \nIs it ok to save?",
        )
        if is_ok:
            with open(path.join(directory, "passkeys.txt"), "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Passkey Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)

logo = PhotoImage(file=path.join(directory, "logo.png"))


canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1, sticky=E)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky=E)

website_entry = Entry(width=61)
website_entry.grid(row=1, column=1, columnspan=2, sticky=E)
website_entry.focus()


email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky=E)

email_entry = Entry(width=61)
email_entry.grid(row=2, column=1, columnspan=2, sticky=E)
email_entry.insert(0, "mik3si7va@example.com")

pasword_label = Label(text="Password:")
pasword_label.grid(row=3, column=0, sticky=E)

password_entry = Entry(width=32)
password_entry.grid(row=3, column=1, sticky=W)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2, sticky=E)

add_button = Button(text="Add", width=51, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky=E)

window.bind("<Return>", lambda event: save())

window.mainloop()
