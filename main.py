from tkinter import *
from tkinter import messagebox
import random as rn
import pyperclip
import json


# ------------------------------ SEARCH PASSWORD -------------------------------- #
def search():
    web = web_entry.get().title()
    try:
        with open("data.json", mode="r") as f:
            # Reading old data
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Warning!", message="Empty database!")
    else:
        if web in data:
            mail = data[web]["email"]
            pwd = data[web]["password"]
            messagebox.showinfo(title=f"{web}", message=f"Your email: {mail}\nYour password: {pwd}")
            pyperclip.copy(pwd)
        else:
            messagebox.showinfo(title="No match!", message="No entries found!")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# From Password Generator Project: git@github.com:vicmanuelr/DAY5-PyPassword-Generator.git

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

NR_LETTERS = rn.randint(8, 10)
NR_SYMBOLS = rn.randint(2, 4)
NR_NUMBERS = rn.randint(2, 4)


def gen_password():
    password_entry.delete(0, END)
    # get random letters from list letters
    password_constructor = [rn.choice(letters) for _ in range(0, NR_LETTERS)]
    # get random symbols from list symbols
    password_constructor += [rn.choice(symbols) for _ in range(0, NR_SYMBOLS)]
    # get random numbers from list of numbers
    password_constructor += [rn.choice(numbers) for _ in range(0, NR_NUMBERS)]
    # shuffle or randomize password characters
    rn.shuffle(password_constructor)
    # join all passwords characters to deliver to user
    final_password = "".join(password_constructor)
    password_entry.insert(0, f"{final_password}")
    pyperclip.copy(final_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = web_entry.get()
    eml = email_entry.get()
    pw = password_entry.get()
    # creating new dictionary for our json format
    new_data = {
        web: {
            "email": eml,
            "password": pw,
        }
    }
    if len(web) == 0 or len(pw) == 0:
        messagebox.showinfo(title="oops", message="Please don't leave any fields empty!")
    else:
        answer = messagebox.askokcancel(title=web, message=f"These are the details entered: \nEmail: {eml}"
                                                           f" \nPassword: {pw} \nIts this ok?")
        if answer:
            try:
                with open("data.json", mode="r") as f:
                    # Reading old data
                    data = json.load(f)
                    # Updating old data
                    data.update(new_data)
            except FileNotFoundError:
                with open("data.json", mode="w") as f:
                    json.dump(new_data, f, indent=4)  # Creating new file if it doesn't exist
            else:
                with open("data.json", mode="w") as f:
                    # Saving updated data
                    json.dump(data, f, indent=4)  # Replaced with new data dictionary for json formatting
            finally:
                web_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Window related
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Canvas Related
lock_img = PhotoImage(file="logo.png")
canvas = Canvas(width=202, height=202)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
website = Label(text="Website:", justify="center")
website.grid(column=0, row=1)
email = Label(text="Email/Username:", justify="center")
email.grid(column=0, row=2)
password = Label(text="Password:", justify="center")
password.grid(column=0, row=3)

# Entries
web_entry = Entry(width=28)
web_entry.grid(column=1, row=1)
web_entry.focus()
email_entry = Entry(width=40)
email_entry.grid(column=1, columnspan=2, row=2)
email_entry.insert(0, "vicmanuelr@gmail.com")
password_entry = Entry(width=28)
password_entry.grid(column=1, row=3)

# Buttons
gen_pass = Button(text="Generate PW", justify="left", width=9, command=gen_password)
gen_pass.grid(column=2, row=3)
add_entry = Button(text="Add", width=38, command=save)
add_entry.grid(column=1, columnspan=2, row=4)
search_button = Button(text="Search", justify="center", width=9, command=search)
search_button.grid(column=2, row=1)

window.mainloop()
