from tkinter import *
from tkinter import messagebox
import mysql.connector

def login(user, passwd):
        con = mysql.connector.connect(user='root', password='trolldevelopers',
                               host='localhost',
                               database='darkspear')
        curs = con.cursor()
        curs.execute("select (count(*)) "
                     "from Player "
                     "where username = %s and pswd = %s",
                     (user, passwd))

        #thingy = curs.fetchall()
        thingy = {}
        for item in curs:
                thingy[0] = item
        con.close()

        return thingy

class LoginPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.configure(bg="gray8")

        # initialize frames
        logo_frame = Frame(self)
        logo_frame.config(bg="gray8")
        logo_frame.pack()

        form_frame = Frame(self)
        form_frame.config(bg="gray8", highlightbackground="midnight blue",
                          highlightcolor="midnight blue", highlightthickness=3)
        form_frame.pack()

        # initialize logo
        logo = PhotoImage(file="images/narwhal.png")
        logo_label = Label(logo_frame, image=logo)
        # keep image as a reference to Tikinter object
        logo_label.image = logo
        # pack logo and configure options
        logo_label.config(bg="gray8")
        logo_label.pack()

        # initialize login form fields
        usr_name_txt = Label(form_frame, text="User Name:", font="bold")
        usr_name_txt.config(bg="gray8", fg="lawn green", justify="right")
        usr_name_txt.grid(row=0, column=0)

        pw_txt = Label(form_frame, text="Password:", font="bold")
        pw_txt.config(bg="gray8", fg="lawn green")
        pw_txt.grid(row=1, column=0)

        usr_name = Entry(form_frame)
        usr_name.config(bg="gray8", fg="lawn green")
        usr_name.grid(row=0, column=1)

        pw = Entry(form_frame, show="*")
        pw.config(bg="gray8", fg="lawn green")
        pw.grid(row=1, column=1)

        # submit login and quit application buttons
        login_sub = Button(form_frame, text="Login", bg="midnight blue", fg="snow",
                           command=lambda: self.login_auth(controller, pw.get(), usr_name.get()))
        login_sub.grid(row=2, column=0, sticky="E")

        quit_sub = Button(form_frame, text="exit Darkspear", bg="midnight blue",
                          fg="snow", command=lambda: self.confirm_quit())
        quit_sub.grid(row=2, column=1, sticky="E")

        create_sub = Button(form_frame, text="Create account", bg="midnight blue",
                          fg="snow", command=lambda: self.create_account(pw.get(), usr_name.get()))
        create_sub.grid(row=3, column=1, sticky="SW")

    def login_auth(self, controller, passwd, user):
        number = login(user, passwd)
        controller.set_username(user)
        if int(number[0][0]) == 1:
            controller.show_frame(HomePage)
        else:
            messagebox.showinfo("Error", "Username or Password entered "
                                "incorrectly please try again")

    def confirm_quit(self):
        if messagebox.askyesno("verify", "really quit?"):
            quit()
        else:
            messagebox.showinfo("no", "quit has been canceled")

    def create_account(self, passwd, user):
        con = mysql.connector.connect(user='root',
                                      password='trolldevelopers',
                                      host='localhost',
                                      database='darkspear')
        cur = con.cursor()

        cur.execute("insert into Player (username, pswd) "
                    "values(%s, %s)", (user, passwd))
        con.commit()
        con.close()

from pages.HomePage import HomePage
from pages.ClanPage import ClanPage
from pages.FriendsPage import FriendsPage
