from tkinter import *
from tkinter.messagebox import *
import pymysql

def login_window():
    root.destroy()
    import main

def clear():
    entryemail.delete(0, END)
    entryDOB.delete(0, END)
    entrypassword.delete(0, END)
    entryUsername.delete(0, END)

def Signup():
    if entryUsername.get() == '' or entrypassword.get() == '' or  \
             entryemail.get() == '' or entryDOB.get() == '' :
        showerror('Error', "All Fields Are Required")
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='Naili123#', database='register')
            cur = con.cursor()
            cur.execute('select * from student where email=%s', entryemail.get())
            row = cur.fetchone()
            if row != None:
                showerror('Error', "User Already Exists")
            else:
                 cur.execute(
            'insert into student(Username,password,email,DOB) values(%s,%s,%s,%s)',
            (entryUsername.get(), entrypassword.get(), entryemail.get(),entryDOB.get()
              ))
                 con.commit()
                 con.close()
                 showinfo('Success', "Registration Successful")
                 clear()
                 root.destroy()
                 import main


        except Exception as e:
                showerror('Error', f"Error due to: {e}")



root = Tk()

root.geometry('1350x710+0+10')
root.title('Signup Page')

bg = PhotoImage(file='bg.png')
bgLabel = Label(root, image=bg)
bgLabel.place(x=0, y=0)


registerFrame = Frame(root, bg='white', width=650, height=650)
registerFrame.place(x=630, y=30)

titleLabel = Label(registerFrame, text='Signup now', font=('arial', 22, 'bold '), bg='white',
                   fg='red', )
titleLabel.place(x=200, y=5)

UsernameLabel = Label(registerFrame, text='User Name', font=('times new roman', 18, 'bold'), bg='white',
                       fg='gray20', )
UsernameLabel.place(x=20, y=80)
entryUsername = Entry(registerFrame, font=('times new roman', 18), bg='lightgray')
entryUsername.place(x=20, y=115, width=250)


passwordLabel = Label(registerFrame, text='Password', font=('times new roman', 18, 'bold'), bg='white',
                      fg='gray20', )
passwordLabel.place(x=20, y=200)
entrypassword = Entry(registerFrame, font=('times new roman', 18), bg='lightgray')
entrypassword.place(x=20, y=235, width=250)

emailLabel = Label(registerFrame, text='Email', font=('times new roman', 18, 'bold'), bg='white', fg='gray20', )
emailLabel.place(x=20, y=320)
entryemail = Entry(registerFrame, font=('times new roman', 18), bg='lightgray')
entryemail.place(x=20, y=355, width=250)


DOBLabel = Label(registerFrame, text='DOB', font=('times new roman', 18, 'bold'), bg='white',
                     fg='gray20', )
DOBLabel.place(x=20, y=440)

entryDOB = Entry(registerFrame, font=('times new roman', 18), bg='lightgray')
entryDOB.place(x=20, y=475, width=250)


button = PhotoImage(file='button.png')
Signupbutton = Button(registerFrame, image=button, bd=0, cursor='hand2', bg='white', activebackground='white'
                        , activeforeground='white', command=Signup)
Signupbutton.place(x=250, y=580)

loginimage = PhotoImage(file='login.png')
loginbutton1 = Button(root, image=loginimage, bd=0, cursor='hand2', bg='gold', activebackground='gold',
                      activeforeground='gold', command=login_window)
loginbutton1.place(x=240, y=330)

root.mainloop()
