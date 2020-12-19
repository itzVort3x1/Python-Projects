from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
#----------------------------------------PASSOWRD GENERATOR------------------------------------------#
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    # print(f"Your password is: {password}")
    password_entry.insert(0, password)
    pyperclip.copy(password)


#----------------------------------------SAVE PASSWORD-------------------------------------------#

def save():
    website_name = website_entry.get()
    email_id = email_entry.get()
    password = password_entry.get()

    if len(website_name) == 0 or len(email_id) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave and fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_name, message=f"These are the details entered: \nEmail: {email_id} "
                                                       f"\nPassword: {password} \nIs it ok to save?")

        if is_ok:
            # a = append it appends to the data present
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website_name} | {email_id} | {password}\n")
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)



#----------------------------------------UI SETUP--------------------------------------------#
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#labels
website_label = Label(text = "Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#entriers
website_entry = Entry()
website_entry.config(width=52)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)
email_entry = Entry()
email_entry.config(width=52)
email_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry()
password_entry.config(width=33)
password_entry.grid(column=1, row=3)

#buttons
generate_passowrd_button = Button(text="Generate Password", command= generate_password)
generate_passowrd_button.grid(column=2, row=3)

add_button = Button(text="ADD", command=save)
add_button.config(width=44)
add_button.grid(column=1, row=4, columnspan=2)






window.mainloop()