from tkinter import *
from tkinter.messagebox import *
import pymysql


def register_window():
    root.destroy()
    import register


def signin():
    if Usernameentry.get() == '' or passentry.get() == '':
        showerror('Error', 'All Fields Are Required')

    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='Naili123#', database='register')
            cur = con.cursor()
            cur.execute('select * from student where Username=%s and password=%s', (Usernameentry.get(), passentry.get()))
            row = cur.fetchone()

            if row == None:
                showerror('error', 'Invalid Username or Password')


            else:
                showinfo('Success', 'Welcome')
                import homepage
            con.close()
        except Exception as e:
            showerror('Error', f"Error due to: {e}")


root = Tk()
root.geometry('900x600+50+50')
root.title('Login Page')
bglogin = PhotoImage(file='loginbg.png')
bgloginLabel = Label(root, image=bglogin)
bgloginLabel.place(x=0, y=0)

frame = Frame(root, bg='white', width=560, height=320)
frame.place(x=180, y=140)

userimage = PhotoImage(file='user.png')
userimageLabel = Label(frame, image=userimage, bg='white')
userimageLabel.place(x=10, y=50)
UsernameLabel = Label(frame, text='Username', font=('arial', 22, 'bold'), bg='white', fg='black')
UsernameLabel.place(x=220, y=32)
Usernameentry = Entry(frame, font=('arial', 22,), bg='white', fg='grey')
Usernameentry.place(x=220, y=70)

passLabel = Label(frame, text='Password', font=('arial', 22, 'bold'), bg='white', fg='black')
passLabel.place(x=220, y=120)
passentry = Entry(frame, font=('arial', 22,), bg='white', fg='grey',show="*")
passentry.place(x=220, y=160)
regbutton = Button(frame, text='Signup New Account?', font=('arial', 12,), bd=0, fg='gray20', bg='white',
                   cursor='hand2',command=register_window,
                   activebackground='white', activeforeground='gray20')
regbutton.place(x=220, y=200)

loginbutton2 = Button(frame, text='Login', font=('arial', 18, 'bold'), fg='white', bg='gray20', cursor='hand2',
                      activebackground='gray20', activeforeground='white', command=signin)
loginbutton2.place(x=450, y=240)

root.mainloop()