from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
web_entry = Entry(width=40)
web_entry.grid(column=1, columnspan=2, row=1)
web_entry.focus()
email_entry = Entry(width=40)
email_entry.grid(column=1, columnspan=2, row=2)
email_entry.insert(END, "vicmanuelr@gmail.com")
password_entry = Entry(width=28)
password_entry.grid(column=1, row=3)

# Buttons
gen_pass = Button(text="Generate PW", justify="left", width=9)
gen_pass.grid(column=2, row=3)
add_entry = Button(text="Add", width=38)
add_entry.grid(column=1, columnspan=2, row=4)

window.mainloop()
