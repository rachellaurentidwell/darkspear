from tkinter import *
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from pages.ClanPage import ClanPage
from pages.FriendsPage import FriendsPage
from pages.Zombie import Zombie
from tkinter import messagebox
import mysql.connector

conn = mysql.connector.connect(user='root', password='trolldevelopers',
                               host='localhost',
                               database='darkspear')
mycursor = conn.cursor()

# define parent class that controls flow of pages
class Darkspear(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        # setup Frame
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # define library of pages
        for F in (LoginPage, HomePage, ClanPage, FriendsPage, Zombie):
            frame = F(container, self)
            self.frames[F] = frame
            self.configure(bg="gray8")
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginPage)

    def show_frame(self, context):
        frame = self.frames[context]
        frame.tkraise()

    def set_username(self, name):
        self.user = name

    def get_username(self):
        return self.user
conn.close()
app = Darkspear()
app.mainloop()
