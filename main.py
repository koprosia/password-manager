from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for i in range(randint(8, 10))]
    password_symbols = [choice(symbols) for i in range(randint(2, 4))]
    password_numbers = [choice(numbers) for i in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_button_clicked():
    website_entry_text = website_entry.get()
    email_username_entry_text = email_username_entry.get()
    password_entry_text = password_entry.get()

    if len(website_entry_text) == 0 or len(password_entry_text) == 0:
        messagebox.showinfo("Oops", "Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_entry_text, message=f"There are the details entered:\n Email:{email_username_entry_text} \n"
                                                      f"Password: {password_entry_text} \n Is it ok to save?")
        if is_ok:
            f = open("data.txt", "a")
            f.write(f"{website_entry_text} | {email_username_entry_text} | {password_entry_text}\n")
            f.close()
            website_entry.delete(0, 'end')
            email_username_entry.delete(0, 'end')
            password_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


#Canvas
canvas = Canvas(width=180, height=180)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#Label "Website"
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

#Label "Email/Username"
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)
email_username_label.config()

#Label "Password"
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#Button "Generate password"
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

#Button "Add"
add_button = Button(text="Add", width=36, command=add_button_clicked)
add_button.grid(column=1, row=4, columnspan=2)

#Entry "Website"
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

#Entry "Email/Username"
email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "magda@gmail.com")

#Entry "Password"
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

window.mainloop()