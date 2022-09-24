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
canvas.pack()

window.mainloop()