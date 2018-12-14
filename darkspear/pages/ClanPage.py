from tkinter import *
from tkinter import messagebox
import mysql.connector


class ClanPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.configure(bg="gray8")

        # connect to db and query for clans
        conn = mysql.connector.connect(user='root', password='trolldevelopers',
                                       host='localhost',
                                       database='darkspear')
        mycursor = conn.cursor()
        mycursor.execute("select    clan_name "
                         "FROM      Clan")
        myresult = list(mycursor)

        clan_list = []
        i = 0
        for clan in myresult:
            clan_list = clan_list + list(clan)
            i = i+1

        # initialize frames
        self.nav_frame = Frame(self)
        self.nav_frame.configure(bg="gray8")
        self.nav_frame.pack(side="left")

        self.header_frame = Frame(self)
        self.header_frame.configure(bg="gray8")
        self.header_frame.pack()

        self.content_frame = Frame(self)
        self.content_frame.configure(bg="gray8")
        self.content_frame.pack()

        self.edit_frame = Frame(self.content_frame)
        self.edit_frame.configure(bg="gray8")
        self.edit_frame.grid(row=1, column=0)

        self.chat_frame = Frame(self)
        self.chat_frame.configure(bg="gray8")
        self.chat_frame.pack()

        self.text_frame = Frame(self)
        self.text_frame.configure(bg="gray8", highlightbackground="deep pink",
                                  highlightcolor="deep pink", highlightthickness=3)
        self.text_frame.pack()

        # initialize nav bar
        self.user = 'Zuroke'
        home = Button(self.nav_frame, text="home", bg="midnight blue",
                      fg="snow", command=lambda: controller.show_frame(HomePage))
        home.grid(row=0, column=0, pady=10)

        friends = Button(self.nav_frame, text="friends", bg="midnight blue",
                         fg="snow", command=lambda: controller.show_frame(FriendsPage))
        friends.grid(row=1, column=0, pady=10)

        quit_sub = Button(self.nav_frame, text="exit Darkspear", bg="midnight blue",
                          fg="snow", command=lambda: self.confirm_quit())
        quit_sub.grid(row=2, column=0, pady=10)

        i=0
        for clan in clan_list:
            clan_button = Button(self.nav_frame, text=clan, bg="midnight blue",
                                 fg="snow", command=lambda clan=clan: self.get_clan(clan))
            clan_button.grid(row=3+i, column=0, pady=10)
            i = i+1

        # initialize header
        self.header = Label(self.header_frame, text="Select Clan from Buttons on the left")
        self.header.configure(font="bold 20", bg="gray8", fg="deep pink")
        self.header.pack()

        # initialize content
        self.announcements = Text(self.content_frame, height=8, width=50)
        self.announcements.configure(bg="gray8", fg="lawn green", wrap="word")
        self.announcements_txt = 'Clan Announcements:'
        
        self.announcements.insert(END, self.announcements_txt)
        self.announcements.grid(row=0, column=0)

        self.events = Text(self.content_frame, height=8, width=50)
        self.events.configure(bg="gray8", fg="lawn green",wrap="word")
        self.events_txt= 'Clan Events:'
        self.events.insert(END, self.events_txt)
        self.events.grid(row=0, column=1)

        self.clan_bio = Text(self.content_frame, height=8, width=50)
        self.clan_bio.configure(bg="gray8", fg="lawn green",wrap="word")
        self.clan_bio_txt = 'Clan Bio:'
        self.clan_bio.insert(END, self.clan_bio_txt)
        self.clan_bio.grid(row=1, column=1)

        edit_announcements = Button(self.edit_frame, text="edit announcements",
                                    bg="midnight blue", fg="snow",
                                    command=lambda: self.update_annon(annon_txt.get(), self.clan_name))
        edit_announcements.grid(row=0, column=0)
        annon_txtv = StringVar()
        annon_txt = Entry(self.edit_frame, textvariable=annon_txtv)
        annon_txt.config(bg="gray8", fg="lawn green",width=40)
        annon_txt.grid(row=0, column=1)

        edit_events = Button(self.edit_frame, text="edit events", bg="midnight blue",
                             fg="snow")
        edit_events.grid(row=1, column=0)
        event_txtv = StringVar()
        event_txt = Entry(self.edit_frame, textvariable=event_txtv)
        event_txt.config(bg="gray8", fg="lawn green",width=40)
        event_txt.grid(row=1, column=1)

        self.chat = Text(self.chat_frame, height=20, width=100)
        self.chat.configure(bg="gray8", fg="lawn green",wrap="word", yscrollcommand="scroll.set")
        self.chat_txt = 'Clan Chat:'
        self.chat.insert(END, self.chat_txt)
        self.chat.pack(side="left")
        # make a scroll bar for the chat
        self.scroll = Scrollbar(self.chat_frame)
        self.scroll.pack(side="right", fill=Y)
        self.scroll.configure(command=self.chat.yview)

        # initialize chat box

        usr = Label(self.text_frame, text=self.user)
        usr.config(bg="midnight blue", fg="snow")
        usr.pack(side="left")

        entry_txt = StringVar()
        usr_txt = Entry(self.text_frame, textvariable=entry_txt)
        usr_txt.configure(bg="gray8", fg="lawn green",width=100)
        usr_txt.pack(fill=X)

        txt_sub = Button(self.text_frame, text="Submit", bg="midnight blue", fg="snow",
                         command=lambda: self.update_txt(self.clan_name, usr_txt.get()))
        txt_sub.pack(side="right")
        conn.close()

    def update_event(self, entry_txt, clan_name):
        # split the entry into column fields
        print(entry_txt, clan_name)
        word_list = entry_txt.split()
        event_name = ""
        description = ""
        event_time = ""

        i = 0
        for word in word_list:
            if i == 0:
                event_name = word
                i = i + 1
            elif (i + 1) == len(word_list):
                event_time = word
                i = i + 1
            elif i == len(word_list):
                event_time = event_time + " "
                event_time = event_time + word
                i = i + 1
            else:
                description = description + " "
                description = description + word
                i = i + 1

        i = 0
        desc = ""
        time = ""
        word_list = description.split()
        for word in word_list:
            if i == len(word_list):
                time += word
                i = i + 1
            elif (i + 1) == len(word_list):
                time += word
                i += 1
            else:
                desc = desc + " "
                desc = desc + word
                i = i + 1
        event_date = ""
        event_date += time
        event_date += " "
        event_date += event_time

        print(self.clan_name)
        conn = mysql.connector.connect(user='root', password='trolldevelopers',
                                       host='127.0.0.1',
                                       database='darkspear')
        mycursor = conn.cursor()
        sql = ("INSERT INTO Clan_event "
               "VALUES (%s, %s, %s, %s)")
        val = (clan_name, event_name, desc, event_date)
        mycursor.execute(sql, val)
        conn.commit()

        # conn.close()

    def update_annon(self, entry_txt, clan_name):
        conn = mysql.connector.connect(user='root', password='trolldevelopers',
                                       host='127.0.0.1',
                                       database='darkspear')
        mycursor = conn.cursor()
        sql = ("INSERT INTO Clan_announcement (clan_name, announcement) "
               "Values (%s, %s)")
        val = (clan_name, entry_txt)
        mycursor.execute(sql, val)
        conn.commit()

        conn.close()

    def update_txt(self, clan_name, entry_txt):
        conn = mysql.connector.connect(user='root', password='trolldevelopers',
                                       host='127.0.0.1',
                                       database='darkspear')
        mycursor = conn.cursor()

        # generate insert
        sql = ("INSERT INTO C_chat (poster_username, clan_name, message) "
               "Values (%s, %s, %s)")
        data = (self.user, clan_name, entry_txt)
        mycursor.execute(sql, data)
        conn.commit()

        self.chat_txt += "\n"
        self.chat_txt += self.user
        self.chat_txt += "{" + entry_txt + "}"
        self.chat.delete('1.0', END)
        self.chat.insert(END, self.chat_txt)

        conn.close()

    def get_clan(self, clan_name):
        self.clan_name = clan_name
        self.header['text'] = clan_name
        clan_name = str(clan_name)

        # connect to db and query for clans
        conn = mysql.connector.connect(user='root', password='trolldevelopers',
                                       host='localhost',
                                       database='darkspear')
        mycursor = conn.cursor()
        sql_stmt = ("SELECT     bio "
                    "FROM       clan "
                    "WHERE      clan_name = '%s'" % clan_name)
        data = clan_name
        mycursor.execute(sql_stmt)

        myresult = list(mycursor)
        new_bio = myresult[0]
        new_bio = str(new_bio)
        self.clan_bio.delete('1.0', END)
        self.clan_bio.insert(END, 'Clan Bio: \n')
        self.clan_bio.insert(END, new_bio)

        self.get_txt(clan_name)
        self.clan_announcements_query(clan_name)
        self.clan_events_query(clan_name)
        conn.close()

    def get_txt(self, clan_name):
        conn = mysql.connector.connect(user='root', password='trolldevelopers',
                                       host='localhost',
                                       database='darkspear')
        mycursor = conn.cursor()
        mycursor.execute("select    poster_username, message, msg_time "
                         "from      C_chat "
                         "where     clan_name = '%s'" % clan_name)
        chat_txt = []
        myresult = list(mycursor)
        for txt in myresult:
            chat_txt.append(txt)

        # self.chat = Text(self.chat_frame, height=20, width=100)
        # self.chat.configure(wrap="word")
        if chat_txt == "":
            chat_txt = "Clan Chat:"
        else:
            for word in chat_txt:
                for item in word:
                    self.chat_txt += str(item)

            this_string = "Clan Chat: \n"
            self.chat.delete('1.0', END)
            self.chat.insert(END, this_string)
            self.chat.insert(END, chat_txt)
            self.chat.pack(side="left")
        conn.close()

    def confirm_quit(self):
        if messagebox.askyesno("verify", "really quit?"):
            quit()
        else:
            messagebox.showinfo("no", "quit has been canceled")

    def clan_announcements_query(self, the_clan_name):
        con = mysql.connector.connect(user='root',
                                          password='trolldevelopers',
                                          host='localhost',
                                          database='darkspear')

        curs = con.cursor()


        stmt = ("select announcement, announcement_time "
                "from Clan_announcement "
                "where clan_name = '%s'" % the_clan_name) 
        
        curs.execute(stmt)

        clan_announcements = []
        result = list(curs)
        for item in result:
            clan_announcements.append(item)

        if clan_announcements == "":
            clan_announcements = "Clan Announcements:"
        else:
            this_string = "Clan Announcements: \n"
            self.announcements.delete('1.0', END)
            self.announcements.insert(END,this_string)
            self.announcements.insert(END, clan_announcements)
        con.close()

    def clan_events_query(self, the_clan_name):
        con = mysql.connector.connect(user='root',
                                          password='trolldevelopers',
                                          host='localhost',
                                          database='darkspear')
        curs = con.cursor()

        # query clan_events for name, description, event date
        stmt = ("select event_name, description, event_date "
                "from Clan_event "
                "where clan_name = '%s'" % the_clan_name) 
        
        curs.execute(stmt)

        clan_events = []
        result = list(curs)
        for item in result:
            clan_events.append(item)

        if clan_events == "":
            clan_events = "Clan Events:"
        else:
            this_string = "Clan Events: \n"
            self.events.delete('1.0', END)
            self.events.insert(END,this_string)
            self.events.insert(END, clan_events)
        con.close()
        
        


from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from pages.FriendsPage import FriendsPage
