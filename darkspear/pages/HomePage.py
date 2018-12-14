from tkinter import *
from tkinter import messagebox
import mysql.connector

class HomePage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.configure(bg="gray8")

        # initialize frames
        nav_frame = Frame(self)
        nav_frame.configure(bg="gray8")
        nav_frame.pack(side="left")

        header_frame = Frame(self)
        header_frame.configure(bg="gray8")
        header_frame.pack()

        content_frame = Frame(self)
        content_frame.configure(bg="gray8")
        content_frame.pack()

        # initialize nav bar
        home = Button(nav_frame, text="home", bg="midnight blue", fg="snow",
                      command=lambda: controller.show_frame(HomePage))
        home.grid(row=1, column=0, pady=10)

        clan = Button(nav_frame, text="clan", bg="midnight blue", fg="snow",
                      command=lambda: controller.show_frame(ClanPage))
        clan.grid(row=2, column=0, pady=10)

        friends = Button(nav_frame, text="friends", bg="midnight blue", fg="snow",
                         command=lambda: controller.show_frame(FriendsPage))
        friends.grid(row=7, column=0, pady=10)

        zombie = Button(nav_frame, text="Zombie", bg="midnight blue", fg="snow",
                        command=lambda: controller.show_frame(Zombie))
        zombie.grid(row=8, column=0, pady=10)

        quit_sub = Button(nav_frame, text="exit Darkspear", bg="midnight blue",
                          fg="snow", command=lambda: self.confirm_quit())
        quit_sub.grid(row=9, column=0, pady=10)

        # initialize header
        user = self.get_user()

        header = Label(header_frame, text=user)
        header.configure(font="bold 20", bg="gray8", fg="deep pink")
        header.pack()

        # initialize content
        conn = mysql.connector.connect(user='root',
                                  password='trolldevelopers',
                                  host='localhost',
                                  database='darkspear')
        curs = conn.cursor()
        curs.execute("select bio "
                     "from Player "
                     "where username = '%s'" % user)
        user_bio = curs.fetchone()
        if type(user_bio) == tuple:
            user_bio = "User Bio:\n" + user_bio[0]
        else:
            user_bio = "No bio provided"

        self.bio = Text(content_frame, height=10, width=70)
        self.bio.configure(wrap="word", bg="gray8", fg="lawn green")
        self.bio_txt = user_bio

        self.bio.insert(END, self.bio_txt)
        self.bio.grid(row=0, column=0, rowspan=2, columnspan=3)

        bio_field = Entry(content_frame)
        bio_field.config(bg="gray8", fg="lawn green", justify="right")
        bio_field.grid(row=1, column=4, sticky="W")

        bio_edit = Button(content_frame, text="Edit Bio", bg="midnight blue", fg="snow",
                          command=lambda: self.update_bio(user, bio_field.get()))
        bio_edit.grid(row=1, column=3, sticky="E")

        curs.execute("select (game_name) "
                     "from Plays_game "
                     "where username = '%s'" % user)
        games = "Games played:\n"
        for item in curs:
            games += item[0] + "\n"
        if len(games) < 3:
            games = "No games listed."
        add_game = Button(content_frame, text="List Games", bg="midnight blue",
                          fg="snow", command=lambda: self.new_game(user))
        add_game.grid(row=2, column=0)
        self.game_list = Text(content_frame, height=25, width=30)
        self.game_list.configure(wrap="word", bg="gray8", fg="lawn green")
        self.game_list_txt = games

        self.game_list.insert(END, self.game_list_txt)
        self.game_list.grid(row=3, column=0, rowspan=5)

        new_game = Button(content_frame, text="Add Game", bg="midnight blue",
                           fg="snow", command=lambda: self.select_new_game(user))
        new_game.grid(row=10, column=0)

        curs.execute("select (clan_name) "
                     "from Player_in_clan "
                     "where username = '%s'" % user)
        clans = "Your clans:\n"
        clansarray = []
        for item in curs:
            clans += item[0] + "\n"
            clansarray.append(item[0])
        if len(clans) < 3:
            clans = "No clans listed."

        clan_game = Entry(content_frame)
        clan_game.config(bg="gray8", fg="lawn green")
        clan_game.grid(row=2, column=1)

        find_clan = Button(content_frame, text="Find Clan", bg="midnight blue",
                           fg="snow", command=lambda: self.new_clan(clan_game.get(), user))
        find_clan.grid(row=2, column=1, sticky="W")
        self.clan_list = Text(content_frame, height=25, width=30)
        self.clan_list.configure(wrap="word", bg="gray8", fg="lawn green")
        self.clan_list_txt = clans

        self.clan_list.insert(END, self.clan_list_txt)
        self.clan_list.grid(row=3, column=1, rowspan=5)

        announcments = "Clan announcements:\n"
        for item in clansarray:
            curs.execute("select announcement "
                         "from clan_announcement "
                         "where clan_name = '%s' and announcement_time = ( select max(announcement_time) "
                         "from clan_announcement "
                         "where clan_name = '%s')" % (item, item))
            parts = curs.fetchone()
            announcments += item +": " + "\n"
            if parts:
                announcments += parts[0]
            announcments += "\n\n"
        if len(announcments) < 3:
            announcments = "No announcments."
        clan_announcements = Text(content_frame, height=30, width=40)
        clan_announcements.configure(wrap="word", bg="gray8", fg="lawn green")
        clan_announcements_txt = announcments

        clan_announcements.insert(END, clan_announcements_txt)
        clan_announcements.grid(row=2, column=2, rowspan=6, columnspan=2)

        conn.close()

    def update_bio(self, user, msg):
        con = mysql.connector.connect(user='root',
                                      password='trolldevelopers',
                                      host='localhost',
                                      database='darkspear')
        cur = con.cursor()
        cur.execute("update Player "
                    "set bio = %s "
                    "where username = %s", (msg, user))

        self.bio.delete('1.0', END)
        self.bio.insert(END, 'User bio: \n')
        self.bio.insert(END, msg)

        con.commit()
        con.close()

    def get_user(self):
        return "Zuroke"

    def confirm_quit(self):
        if messagebox.askyesno("verify", "really quit?"):
            quit()
        else:
            messagebox.showinfo("no", "quit has been canceled")

    def select_new_game(self, user):
        games = []
        gamewin = Toplevel(self)
        display = Label(gamewin, text="Select a Game. Click [X] to close")
        display.pack()
        con = mysql.connector.connect(user='root',
                                      password='trolldevelopers',
                                      host='localhost',
                                      database='darkspear')
        cur = con.cursor()

        cur.execute("select game_name "
                    "from Game "
                    "where game_name not in (select game_name "
                    "from Plays_game "
                    "where username = '%s')" % user)
        for game in cur:
            games.append(game[0])
        for title in games:
            new_b = Button(gamewin, text=title, bg="midnight blue",
                           fg="snow", command=lambda title=title: self.add_game(user, title))
            new_b.pack()
        con.close()

    def add_game(self, user, game):
        con = mysql.connector.connect(user='root',
                                      password='trolldevelopers',
                                      host='localhost',
                                      database='darkspear')
        cur = con.cursor()

        cur.execute("insert into Plays_game "
                    "values (%s, %s)", (user, game))
        con.commit()

        self.game_list_txt += game + '\n'
        self.game_list.delete('1.0', END)
        self.game_list.insert(END, self.game_list_txt)
        con.close()

    def new_game(self, user):
        games = []
        gamewin = Toplevel(self)
        display = Label(gamewin, text="Select a Game. Click [X] to close")
        display.pack()
        con = mysql.connector.connect(user='root',
                                      password='trolldevelopers',
                                      host='localhost',
                                      database='darkspear')
        cur = con.cursor()

        cur.execute("select game_name "
                    "from Game")
        for game in cur:
            games.append(game[0])
        for title in games:
            new_b = Button(gamewin, text=title, bg="midnight blue",
                           fg="snow", command=lambda title=title: self.new_clan(title, user))
            new_b.pack()
        con.close()

    def new_clan(self, game, user):
        clans = []
        clanwin = Toplevel(self)
        display = Label(clanwin, text="Select a clan to join. Click the [X] to close")
        display.pack()
        con = mysql.connector.connect(user='root',
                                      password='trolldevelopers',
                                      host='localhost',
                                      database='darkspear')
        cur = con.cursor()

        cur.execute("select clan_name "
                    "from Clan_games "
                    "where game_name = %s "
                    "and clan_name not in (select clan_name "
                    "from Player_in_clan "
                    "where username = %s)", (game, user))
        for clan in cur:
            clans.append(clan[0])
        if not clans:
            display["text"] = "No clans available. Click [X] to close."
        else:
            for group in clans:
                new_b = Button(clanwin, text=group, bg="midnight blue",
                               fg="snow", command=lambda group=group: self.add_clan(user, group))
                new_b.pack()

        con.close()

    def add_clan(self, user, clan):
        con = mysql.connector.connect(user='root',
                                      password='trolldevelopers',
                                      host='localhost',
                                      database='darkspear')
        cur = con.cursor()
        cur.execute("insert into Player_in_clan "
                    "values (%s, %s)", (user, clan))
        con.commit()

        self.clan_list_txt += clan + '\n'
        self.clan_list.delete('1.0', END)
        self.clan_list.insert(END, self.clan_list_txt)
        con.close()


from pages.LoginPage import LoginPage
from pages.ClanPage import ClanPage
from pages.FriendsPage import FriendsPage
from pages.Zombie import Zombie
