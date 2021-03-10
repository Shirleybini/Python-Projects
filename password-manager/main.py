from tkinter import *
from tkinter import messagebox
import random
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def Generate_Password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    password_list = []
    
    password_letters = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for char in range(random.randint(2,4))]
    password_numbers = [random.choice(numbers) for char in range(random.randint(2,4))]
    
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    
    password = ""
    for char in password_list:
      password += char
      
    password_input.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def Add_data():
    Website = website_input.get()
    Username = username_input.get()
    Password = password_input.get()
    new_data = {
        Website:
            {"email":Username,
             "password":Password,
             }
        }
    
    if len(Website)==0 or len(Password)==0:
        messagebox.showwarning(title="Oops!",message="Don't leave any field empty")
    else:
        #if file already exists
        try:
            with open("mypassword.json", "r") as f:
                #reading old data
                data = json.load(f)
        
        #if file doesnt exits-error        
        except FileNotFoundError:
            with open("mypassword.json","w") as f:    
                json.dump(new_data,f,indent = 4)
        
        #if there is no error
        else:
            #updating old data with new data
            data.update(new_data)
            
            with open("mypassword.json","w") as f:    
                #saving updated data
                json.dump(data,f,indent = 4)
        
        #run no matter what
        finally:
            website_input.delete(0,END)
            password_input.delete(0,END)
            
            
def Search():
    Website = website_input.get()
    try:
        with open("mypassword.json","r") as my_file:
            Data = json.load(my_file)
            messagebox.showinfo(title=Website,message=f"Email: {Data[Website]['email']} \n Password: {Data[Website]['password']}")
    except FileNotFoundError:
        messagebox.showinfo(title = "File Error",message="No such file exists.")






# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password")
window.config(padx = 50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100,100,image = logo_img)
canvas.grid(row = 0, column = 1)

Website = Label(text = "Website:")
Website.grid(row=1, column = 0)

username = Label(text="Email/Username:")
username.grid(row=2,column = 0)

password = Label(text = "Password:")
password.grid(row=3,column = 0)

website_input = Entry()
website_input.insert(END,string="")
website_input.grid(row=1,column=1,sticky="EW")
website_input.focus()

username_input = Entry()
username_input.insert(END,string="")
username_input.grid(row=2,column=1,columnspan=2,sticky="EW")
username_input.insert(0,"shirley****@gmail.com")  #Add your email

password_input = Entry()
#password_input.insert(END,string="")
password_input.grid(row=3,column=1,sticky="EW")

generate_button = Button(text = 'Generate Password',command = Generate_Password)
generate_button.grid(row = 3,column = 2)

add_button = Button(text = 'Add',command = Add_data)
add_button.grid(row = 4,column = 1,columnspan=2,sticky="EW")

search_button = Button(text = 'Search',command=Search)
search_button.grid(row = 1,column = 2,sticky="EW")

window.mainloop()
