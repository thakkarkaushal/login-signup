from tkinter import *
import sqlite3
import re
from tkinter import messagebox
from tkinter.messagebox import *

global login__root, name_var, ans1, ans2


def signup():
    global signup_root
    signup_root = Tk()
    login__root.withdraw()
    signup_root.configure(bg='black')
    app = SignUP(signup_root)
    signup_root.mainloop()


def login():
    login__root = Toplevel()
    signup_root.withdraw()
    login__root.configure(bg='black')
    app = Login(login__root)
    login__root.mainloop()


class Login:
    def __init__(self, login_root):
        self.login_root = login_root
        self.login_root.title("LOG IN")
        pad = 3
        self.login_root.geometry(
            "{0}x{1}+0+0".format(self.login_root.winfo_screenwidth() - pad, self.login_root.winfo_screenheight() - pad))

        self.label_frame = Frame(self.login_root)
        self.label_frame.configure(bg="#111212")
        self.label_frame.pack(side='top')

        self.login_frame = Frame(self.login_root)
        # self.login_frame.configure(bg='white')
        self.login_frame.pack(side='top')
        # login label
        Label(self.label_frame, font=('', 50), fg='#DE5D83', bg='black', text="LOGIN",
              anchor="center").grid(row=0, column=1, padx=3, pady=3)

        # Email label and entry
        self.email_var = StringVar()
        self.email_label = Label(self.login_frame, font=('', 20), fg='black', bg='white', text="EMAIL: ",
                                 anchor="center").grid(row=0, column=1, padx=3, pady=3)
        self.email_entry = Entry(self.login_frame, fg='black', cursor='ibeam', width=50, bg='white',
                                 textvar=self.email_var)
        self.email_entry.grid(row=0, column=2, padx=3, pady=3)

        # password label and entry
        self.password_var = StringVar()
        self.password_label = Label(self.login_frame, font=('', 20), fg='black', bg='white', text="PASSWORD: ",
                                    anchor="center").grid(row=1, column=1, padx=3, pady=3)
        self.password_entry = Entry(self.login_frame, fg='black', cursor='ibeam', width=50, bg='white', show='*',
                                    textvar=self.password_var)
        self.password_entry.grid(row=1, column=2, padx=3, pady=3)

        def login():
            global ans2
            global ans1
            while True:
                if self.email_entry.get() == '':
                    messagebox.showinfo("ERROR", "PLEASE ENTER EMAIL")
                    ans1= False
                    break
                else:
                    email = self.email_entry.get()
                    ans1 = True
                    break

            while True:
                if self.password_entry.get() == '':
                    messagebox.showinfo("ERROR", "PLEASE ENTER PASSWORD")
                    ans2= False
                    break
                else:
                    password = self.password_entry.get()
                    ans2 = True
                    break
            if ans1 == True and ans2 == True:
                conn = sqlite3.connect('Details.db')
                with conn:
                    cursor = conn.cursor()
                cursor.execute('CREATE TABLE IF NOT EXISTS Details (name TEXT, email TEXT, password TEXT)')
                with conn:
                    cursor.execute("SELECT email,password FROM Details")
                    ans = cursor.fetchall()
                    for i in ans:
                      
                        if email == i[0]:
                            if password == i[1]:
                                showinfo("Message", "LOGIN SUCCESS")
                                break
                            else:
                                showerror("ERROR", "Enter correct password")
                                continue
                    else:
                        showerror("ERROR", "Enter correct email id")


        # login button
        self.login_button = Button(self.login_frame, text='LOGIN', fg='black', bg='#3FEEE6', height=2, width=15,
                                   command=login).grid(
            row=2, column=2, padx=3, pady=3)

        # signup button
        self.signup_button = Button(self.login_frame, text='SIGNUP', fg='black', bg='#3FEEE6', height=2, width=15,
                                    command=signup).grid(row=2, column=1, padx=3, pady=3)


class SignUP:
    def __init__(self, master):
        self.master = master
        self.master.title("SIGN UP")
        pad = 3
        self.master.geometry(
            "{0}x{1}+0+0".format(self.master.winfo_screenwidth() - pad, self.master.winfo_screenheight() - pad))

        self.l_frame = Frame(self.master)
        self.l_frame.configure(bg="#111212")
        self.l_frame.pack(side='top')

        self.log_frame = Frame(self.master)
        self.log_frame.configure(bg='white')
        self.log_frame.pack(side='top')

        # login label
        Label(self.l_frame, font=('', 50), fg='#DE5D83', bg='black', text="SIGNUP",
              anchor="center").grid(row=0, column=1, padx=3, pady=3)

        # NAME label and entry
        self.name_var_signup = StringVar()
        self.name_label = Label(self.log_frame, font=('', 20), fg='black', bg='white', text="NAME: ",
                                anchor="center").grid(row=0, column=1, padx=3, pady=3)
        self.name_entry = Entry(self.log_frame, width=50, textvar=self.name_var_signup)
        self.name_entry.grid(row=0, column=2, padx=3, pady=3)

        # EMAIL label and entry
        self.email_var = StringVar()
        self.email_label = Label(self.log_frame, font=('', 20), fg='black', bg='white', text="EMAIL: ",
                                 anchor="center").grid(row=1, column=1, padx=3, pady=3)
        self.email_entry = Entry(self.log_frame, cursor='ibeam', width=50, textvar=self.email_var)
        self.email_entry.grid(row=1, column=2, padx=3, pady=3)

        # PASSWORD label and entry
        self.password_var = StringVar()
        self.password_label = Label(self.log_frame, font=('', 20), fg='black', bg='white', text="PASSWORD: ",
                                    anchor="center").grid(row=2, column=1, padx=3, pady=3)
        self.password_entry = Entry(self.log_frame, fg='black', cursor='ibeam', width=50, bg='white', show='*',
                                    textvar=self.password_var)
        self.password_entry.grid(row=2, column=2, padx=3, pady=3)

        def signup_user():
            global ans

            while True:
                if self.name_entry.get() is '':
                    messagebox.showerror("ERROR", "Please enter name")
                    break
                else:
                    name = self.name_entry.get()
                    break

            while True:
                if self.password_entry.get() is '':
                    messagebox.showerror("ERROR", "Please enter password")
                    break
                else:
                    password = self.password_entry.get()
                    break

            while True:
                regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

                if re.search(regex, self.email_entry.get()):
                    email = self.email_entry.get()
                    print(email)
                    ans = True
                    break
                else:
                    messagebox.showerror("ERROR", "PLEASE ENTER VALID EMAIL ID")
                    break

            if ans:
                conn = sqlite3.connect('Details.db')
                with conn:
                    cursor = conn.cursor()
                cursor.execute('CREATE TABLE IF NOT EXISTS Details (name TEXT, email TEXT, password TEXT)')
                cursor.execute('INSERT INTO Details (name,email,password) '
                               'VALUES(?,?,?)', (name, email, password))
                conn.commit()

                messagebox.showinfo("INFO", "SUCCESSFULLY SIGNUP")

        self.signup_button = Button(self.log_frame, text='SIGNUP', fg='black', bg='#3FEEE6', height=2, width=15,
                                    command=signup_user).grid(row=3, column=2, padx=3, pady=3)

        # login button
        self.login_button = Button(self.log_frame, text='LOGIN', fg='black', bg='#3FEEE6', height=2, width=15,
                                   command=login).grid(
            row=3, column=1, padx=3, pady=3)


# class Dictionary:
#     def __init__(self, dic_root):


if __name__ == '__main__':
    login__root = Tk()
    login__root.configure(bg='black')
    app = Login(login__root)
    login__root.mainloop()
