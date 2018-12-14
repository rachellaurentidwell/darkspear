from tkinter import *
import mysql.connector
from tkinter import messagebox
from datetime import datetime


class FriendsPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.configure(bg="gray8")

        # connect to db and query for info
        conn = mysql.connector.connect(user='root', password='trolldevelopers',
                                       host='127.0.0.1',
                                       database='darkspear')
        mycursor = conn.cursor()
        mycursor.execute("select    username "
                         "FROM      player")
        myresult = list(mycursor)

        player_list = []
        i = 0
        for name in myresult:
            # player_list.append(name)
            player_list = player_list + list(name)
            i = i+1

        # initialize frames
        nav_frame = Frame(self)
        nav_frame.configure(bg="gray8")
        nav_frame.pack(side="left")

        content_frame = Frame(self)
        content_frame.configure(bg="gray8")
        content_frame.pack()

        friends_frame = Frame(content_frame)
        friends_frame.configure(bg="gray8")
        friends_frame.grid(row=2, column=0)

        txt_frame = Frame(self)
        txt_frame.configure(bg="gray8", highlightbackground="deep pink",
                            highlightcolor="deep pink", highlightthickness=3)
        txt_frame.pack()

        # initialize nav bar
        home = Button(nav_frame, text="home", bg="midnight blue", fg="snow",
                      command=lambda: controller.show_frame(HomePage))
        home.grid(row=1, column=0, pady=10)

        clan = Button(nav_frame, text="clan", bg="midnight blue", fg="snow",
                      command=lambda: controller.show_frame(ClanPage))
        clan.grid(row=2, column=0, pady=10)

        quit_sub = Button(nav_frame, text="exit Darkspear", bg="midnight blue",
                          fg="snow", command=lambda: self.confirm_quit())
        quit_sub.grid(row=8, column=0, pady=10)

        # initialize content

        txt = ""

        user = 'Zuroke'
        self.receiver = ""
        # populate the list of friends
        i = 0
        for friend in player_list:
            user_button = Button(friends_frame, text=friend, bg="midnight blue",
                                 fg="snow", command=lambda friend=friend: self.get_txt(user,
                                                                                       friend, content_frame,))
            user_button.grid(row=i, column=0)
            i = i + 1

        chat = Text(content_frame, height=40, width=100)
        chat.configure(wrap="word", yscrollcommand="scroll.set", bg="grey8", fg="lawn green")
        if txt == "":
            chat_txt = "this is just a general palceholder to hold a list " \
                    "of the clan's chat"
        else:
            chat_txt = txt
        chat.insert(END, chat_txt)
        chat.grid(row=1, column=1, rowspan=2)
        # make a scroll bar for the chat
        scroll = Scrollbar(content_frame)
        scroll.grid(row=1, column=2, rowspan=2, sticky="N E S W")
        scroll.configure(command=chat.yview)

        # initialize chat entry

        usr = Label(txt_frame, text="user's name: ")
        usr.config(bg="midnight blue", fg="snow")
        usr.pack(side="left")

        entry_txt = StringVar()
        usr_txt = Entry(txt_frame, textvariable=entry_txt)
        # entry_txt = usr_txt.get()
        usr_txt.configure(width=130, bg="gray8", fg="lawn green")
        usr_txt.pack(fill=X)

        txt_sub = Button(txt_frame, text="Submit", bg="midnight blue", fg="snow",
                         command=lambda: self.update_txt(usr_txt.get(), user, self.receiver))
        txt_sub.pack(side="right")
        conn.close()

    def update_txt(self, entry_txt, user, receiver):
        # connect to the database
        conn = mysql.connector.connect(user='root', password='trolldevelopers',
                                       host='127.0.0.1',
                                       database='darkspear')
        mycursor = conn.cursor()

        # generate insert
        sql = ("INSERT INTO F_chat (p1_username, p2_username, sender, message) "
               "VALUES (%s, %s, %s, %s)")

        val = (user, receiver, user, entry_txt)
        mycursor.execute(sql, val)
        conn.commit()
        conn.close()

    def get_txt(self, player1, player2, content_frame):
        self.receiver = player2
        # create query for chat
        conn = mysql.connector.connect(user='root', password='trolldevelopers',
                                       host='127.0.0.1',
                                       database='darkspear')
        mycursor = conn.cursor()
        chat_stmt = ("select    sender, message, msg_time " 
                     "from      f_chat " 
                     "where     p1_username = %s and " 
                     "          p2_username = %s " 
                     "order by  msg_time")
        data = (player1, player2)
        mycursor.execute(chat_stmt, data)
        fchat_txt = []
        myresult = list(mycursor)
        for txt in myresult:
            fchat_txt.append(txt)

        chat = Text(content_frame, height=40, width=100)
        chat.configure(wrap="word", yscrollcommand="scroll.set", bg="gray8", fg="lawn green")
        if fchat_txt == "":
            chat_txt = "this is just a general palceholder to hold a list " \
                       "of the friends chat"
        else:
            chat_txt = fchat_txt
        chat.insert(END, chat_txt)
        chat.grid(row=1, column=1, rowspan=2)
        conn.close()

    def confirm_quit(self):
        if messagebox.askyesno("verify", "really quit?"):
            quit()
        else:
            messagebox.showinfo("no", "quit has been canceled")

    def find_friend(self):
        messagebox.showinfo("soon", "to be implemented later")

from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from pages.ClanPage import ClanPage
