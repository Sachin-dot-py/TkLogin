import tkinter as tk
from tkinter import messagebox
def Login():
    alert = False; LoggedIn = False
    username = username_field.get()
    password = password_field.get()
    with open('Login.csv','r') as f:
        lines = [(line.replace('\n','').split(',')) for line in f.readlines()]
    for line in lines:
        if line[0] == username:
            if line[1] == password:
                tk.messagebox.showinfo(title='Login',message='Succesfully Logged in!')
                alert = True; LoggedIn = True
            else:
                tk.messagebox.showwarning(title='Login',message='Incorrect Password!')
                alert = True
    if not alert: tk.messagebox.showerror(title='Login',message='User not found!')

def CreateAccount():
    username = username_field.get()
    password = password_field.get()
    with open('Login.csv','a') as f:
        f.write(username+','+password+'\n')

def CreateAccountPage(event):
    global username_field,password_field,create_acc_frame
    login_frame.pack_forget()
    window.title("Create Account")
    create_acc_frame = tk.Frame(window)

    username_label = tk.Label(create_acc_frame,text="Enter a username: ")
    username_label.grid(row=0,column=0)
    username_field = tk.Entry(create_acc_frame)
    username_field.grid(row=0,column=1)

    password_label = tk.Label(create_acc_frame,text="Enter a password: ")
    password_label.grid(row=1,column=0)
    password_field = tk.Entry(create_acc_frame)
    password_field.grid(row=1,column=1)
    
    create_account = tk.Button(create_acc_frame,text="Create account!",command=CreateAccount)
    create_account.grid(row=2,columnspan=2)

    create_acc_frame.pack()

def LoginPage():
    global username_field,password_field,login_frame
    window.title("Login")
    login_frame = tk.Frame(window)

    username_label = tk.Label(login_frame,text="Username: ")
    username_label.grid(row=0,column=0)
    username_field = tk.Entry(login_frame)
    username_field.grid(row=0,column=1)

    password_label = tk.Label(login_frame,text="Password: ")
    password_label.grid(row=1,column=0)
    password_field = tk.Entry(login_frame)
    password_field.grid(row=1,column=1)

    login_button = tk.Button(login_frame,text="Login",command=Login)
    login_button.grid(row=2,columnspan=2)

    create_account_button = tk.Label(login_frame,text='Create a new account', fg="blue", cursor="hand2", underline=True)
    create_account_button.grid(row=3,columnspan=2)
    create_account_button.bind("<Button-1>", CreateAccountPage)
    login_frame.pack()

window = tk.Tk()
LoginPage()
window.mainloop()
