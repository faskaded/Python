from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = [chr(i) for i in range(97, 123)]
    numbers = [str(i) for i in range(0, 10)]
    symbols = [chr(i) for i in range(33, 44)]

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(numbers) for _ in range(nr_symbols)]
    password_numbers = [random.choice(symbols) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    Password_enter.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def SavePassword():
    website = website_enter.get()
    email = Email_enter.get()
    password = Password_enter.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_enter.delete(0, END)
            Password_enter.delete(0, END)


def find_password():
    website = website_enter.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(width=800, height=800, padx=50, pady=50, bg="white")
window.resizable(False, False)
# ---------------------------- photo------------------------------- #
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
bg = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=bg)
canvas.grid(column=1, row=0)
# ---------------------------- label ------------------------------- #
label_web = Label(text="Website: ", bg="white")
label_web.grid(column=0, row=1)
label_email = Label(text="Email/Username: ", bg="white")
label_email.grid(column=0, row=2)
label_password = Label(text=f"Password: ", bg="white")
label_password.grid(column=0, row=3)
# ---------------------------- Enter ------------------------------- #
website_enter = Entry(width=21)
website_enter.grid(column=1, row=1)
website_enter.focus()
Email_enter = Entry(width=35)
Email_enter.grid(column=1, row=2, columnspan=2)
Email_enter.insert(0, "Savelka@yandex.ru")
Password_enter = Entry(width=21)
Password_enter.grid(column=1, row=3)
# ----------------------------Button ------------------------------- #
Generate_btn = Button(text="Generate password", command=gen_password)
Generate_btn.grid(column=2, row=3)
Search_btn = Button(text="Search", command=find_password)
Search_btn.grid(column=2, row=1, columnspan=2)
Add_btn = Button(text="Add", width=36, command=SavePassword)
Add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
