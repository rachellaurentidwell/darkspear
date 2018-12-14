from tkinter import *
from tkinter import messagebox

class Zombie(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.configure(bg="gray8")

        # initialize frames
        self.head_frame = Frame(self)
        self.head_frame.configure(bg="gray8")
        self.head_frame.pack()

        self.txt_frame = Frame(self)
        self.txt_frame.configure(bg="gray8")
        self.txt_frame.pack()

        self.butt_frame = Frame(self)
        self.butt_frame.configure(bg="gray8")
        self.butt_frame.pack()

        self.sub_frame = Frame(self)
        self.sub_frame.configure(bg="gray8")
        self.sub_frame.pack()

        # initialize objects

        # header
        self.head = Label(self.head_frame, text="Hangover from Hell!!!")
        self.head.configure(bg="gray8", fg="deep pink")
        self.head.pack()

        back = Button(self.head_frame, text="Go Home", bg="midnight blue",
                      fg="snow", command=lambda: controller.show_frame(HomePage))
        back.pack(side="right", padx=20)

        # txt field
        self.txt = Text(self.txt_frame, height=30, width=50)
        self.txt.configure(wrap="word", bg="gray8", fg="lawn green")
        self.txtv = "You wake up still drunk from the party last night " \
                    "you look around in your drunken haze and see a sea of bodies. " \
                    "Gagging on the smell of rotting flesh, you slowly walk out your " \
                    "front door."
        self.txt.insert(END, self.txtv)
        self.txt.pack()

        # buttons
        self.but1 = Button(self.butt_frame, text="N/A", bg="midnight blue", fg="snow",
                           command=lambda: self.get_next(self.but1['text']))
        self.but2 = Button(self.butt_frame, text="N/A", bg="midnight blue", fg="snow",
                           command=lambda: self.get_next(self.but2['text']))
        self.but3 = Button(self.butt_frame, text="N/A", bg="midnight blue", fg="snow",
                           command=lambda: self.get_next(self.but3['text']))

        self.but1.grid(row=0, column=0, padx=5)
        self.but2.grid(row=0, column=1, padx=5)
        self.but3.grid(row=0, column=2, padx=5)

        # entry
        entry_sub = Button(self.sub_frame, text="Submit", bg="midnight blue", fg="snow",
                           command=lambda: self.get_next(entry.get()))
        entry_sub.pack(side="left")
        entry_txt = StringVar()
        entry = Entry(self.sub_frame, textvariable=entry_txt)
        entry.configure(width=50, bg="gray8", fg="lawn green")
        entry.pack(side="right", fill=X)

        self.job = ""
        self.weapon = ""

    def get_next(self, choice):
        # round 1
        if choice == 'first':
            self.txt.delete('1.0', END)
            new_txt = "What did you do before this hell you now call life?"
            self.txt.insert(END, new_txt)
            self.but1['text'] = "jerk cop"
            self.but2['text'] = "sleazy senator"
            self.but3['text'] = "hot nurse"
            return
        # round 2
        elif choice == 'jerk cop':
            self.txt.delete('1.0', END)
            new_txt = "Well you were a dick before zombies, you'll probably be a dick " \
                      "after them as well. Anyways, you notice a zombie shuffling around. " \
                      "what shall you do?"
            self.txt.insert(END, new_txt)
            self.but1['text'] = "attack it because yolo"
            self.but2['text'] = "hide and sneak around"
            self.but3['text'] = "N/A"
            self.job = "cop"
            return
        elif choice == "sleazy senator":
            self.txt.delete('1.0', END)
            new_txt = "Well you may not have much of a soul but at least you were winning " \
                      "in life. Lets see if that applies to the new world order. You " \
                      "notice a zombie shuffling around. What shall you do?"
            self.txt.insert(END, new_txt)
            self.but1['text'] = "attack it because yolo"
            self.but2['text'] = "hide and sneak around"
            self.but3['text'] = "N/A"
            self.job = "senator"
            return
        elif choice == "hot nurse":
            self.txt.delete('1.0', END)
            new_txt = "Thank God the hot chick lived. PLEASE PLEASE PLEASE live long enough " \
                      "for me to get some of that. Although I highly doubt you'll last long. " \
                      "You meet your first zombie, shuffling along, what shall you do?"
            self.txt.insert(END, new_txt)
            self.but1['text'] = "attack it because yolo"
            self.but2['text'] = "hide and sneak around"
            self.but3['text'] = "N/A"
            self.job = "nurse"
            return
        # round 3
        elif choice == "attack it because yolo":
            self.txt.delete('1.0', END)
            if self.job == "cop":
                new_txt = "Like the crazy son of a bitch you are, you running frantically " \
                          "at the zombie, screaming and waving your arms, you don't even have " \
                          "a weapon yet you noob. However, by some crazy stroke of luck, " \
                          "you crash into the zombie and it falls over crushing its head " \
                          "on a pole sticking out of the ground. You're not dead, but you " \
                          "need equipment if you're going to last long. Where would you like to go?"
                self.txt.insert(END, new_txt)
                self.but1['text'] = "arcade"
                self.but2['text'] = "drug store"
                self.but3['text'] = "home depot"
                return
            elif self.job == "senator":
                new_txt = "Well you made good choices in life but now you're dumb as a rock. " \
                          "You run at the zombie, screaming bloody murder and waving your hands. " \
                          "You have no weapon, and your eyes aren't even open. To no one's " \
                          "surprise this zombie reks you and eats your brains. You're dead gg"
                self.txt.insert(END, new_txt)
                self.but1['text'] = "N/A"
                self.but2['text'] = "N/A"
                self.but3['text'] = "N/A"
                return
            elif self.job == "nurse":
                new_txt = "You're super hot, but you're equally dumb. You run at the zombie, " \
                          "no weapon, take one look at it and drop to your knees in terror. " \
                          "Screaming in horror and looking up at the zombie, you see him slowly " \
                          "turn around and bite down right on your neck. You're dead. I really " \
                          "wanted you to live long enough to bang me but you're already dead."
                self.txt.insert(END, new_txt)
                self.but1['text'] = "N/A"
                self.but2['text'] = "N/A"
                self.but3['text'] = "N/A"
                return
        elif choice == "hide and sneak around":
            self.txt.delete('1.0', END)
            if self.job == "cop":
                new_txt = "Sneaking was never one of your strong suits. Apparently thinking " \
                          "isn't either. You attempt to sneak around the zombie by holding up " \
                          "a leaf and giggling. The leaf is just close enough to your face that " \
                          "you don't see the zombie walk up and bite your hands holding the leaf " \
                          "up. Well you certainly see him now. You're not dead yet, but you " \
                          "might as well be. Have fun slowly turning into a brainless monster, " \
                          "well I suppose you kinda already were"
                self.txt.insert(END, new_txt)
                self.but1['text'] = "N/A"
                self.but2['text'] = "N/A"
                self.but3['text'] = "N/A"
                return
            elif self.job == "senator":
                new_txt = "You were a snake while you were alive and you're a snake now. You " \
                          "gracefully wiggle your way right past the zombie. He never suspected " \
                          "a thing. Just like the authorities never suspected you for getting " \
                          "drunk and running over that hooker. You live, for now, but you need " \
                          "supplies, where do you go?"
                self.txt.insert(END, new_txt)
                self.but1['text'] = "arcade"
                self.but2['text'] = "drug store"
                self.but3['text'] = "home depot"
                return
            elif self.job == "nurse":
                new_txt = "You're super hot, but you're equally dumb. You attempt to sneak past " \
                          "the zombie in 6 inch heals and trip over a can of beans. You look up " \
                          "just in time to see him lunge at your face. I really hoped you'd live " \
                          "but I shouldn't have gotten my hopes up, the hot girl always dies " \
                          "in horror movies."
                self.txt.insert(END, new_txt)
                self.but1['text'] = "N/A"
                self.but2['text'] = "N/A"
                self.but3['text'] = "N/A"
                return
        # round 4
        elif choice == "arcade":
            self.txt.delete('1.0', END)
            new_txt = "What kind of idiot goes to an arcade when the whole world has gone to " \
                      "hell? Like seriously?! Well you run into a gang of rabid street kids. " \
                      "A horde of 9 year olds run at you and slice your legs with knives " \
                      "oddly large for such little kids. They spit on your face and piss in " \
                      "your hands because you have nothing of value on you. They leave you there " \
                      "to slowly bleed out. But you're a lucky bastard and instead a pack of " \
                      "zombies walk your way and tear out your intestines. They slowly munch on " \
                      "them while you're still alive. It takes hours for you to die and become one " \
                      "of them"
            self.txt.insert(END, new_txt)
            self.but1['text'] = "N/A"
            self.but2['text'] = "N/A"
            self.but3['text'] = "N/A"
            return
        elif choice == "drug store":
            self.txt.delete('1.0', END)
            new_txt = "Well its good thinking to load up on all the drugs you can before they " \
                      "are taken. However, it probably would have been smart to grab a weapon " \
                      "first. You walk into the drug store and find 5 skin heads smiling back at " \
                      "you. They decide to take turns slicing off body parts until you turn. " \
                      "Once you're a zombie, they push a leash around you and decide to keep you " \
                      "as a pet. The only thing worse than becoming a zombie is becoming a zombie " \
                      "slave. Good job scrub"
            self.txt.insert(END, new_txt)
            self.but1['text'] = "N/A"
            self.but2['text'] = "N/A"
            self.but3['text'] = "N/A"
            return
        elif choice == "home depot":
            self.txt.delete('1.0', END)
            new_txt = "Interesting choice. Its not fancy but you manage to find yourself a " \
                      "small axe designed for chopping wood. While you may not be in great shape, " \
                      "at least now you have a weapon. Lets get you moving on something faster " \
                      "though. What vehicle do you want?"
            self.txt.insert(END, new_txt)
            self.but1['text'] = "horse"
            self.but2['text'] = "big ass truck"
            self.but3['text'] = "flashy sports car"
            return
        # round 5
        elif choice == "horse":
            self.txt.delete('1.0', END)
            new_txt = "Well I guess you won't make much noise, and you won't have to worry " \
                      "about gas. Lets see how this turns out for you eh? You're riding along " \
                      "and you turn a corner. There is a group of zombies directly in front of you. " \
                      "your horse gets spooked and bucks you off. The good news is you bash your " \
                      "head and don't have to live through the zombies tearing you apart. The " \
                      "bad news is, the zombies tear you apart. You made it for a while, but " \
                      "it turns out you suck. GG"
            self.txt.insert(END, new_txt)
            self.but1['text'] = "N/A"
            self.but2['text'] = "N/A"
            self.but3['text'] = "N/A"
            return
        elif choice == "big ass truck":
            self.txt.delete('1.0', END)
            new_txt = "Its loud as fuck and every zombie in the area comes running as soon as you " \
                      "turn that bad boy on. Lucky for you this thing is basically a tank. You " \
                      "turn those zombies into road kill and GTFO. You live for now, but this was " \
                      "just day one. May the force be with you on your quest to not die. You win."
            self.txt.insert(END, new_txt)
            self.but1['text'] = "N/A"
            self.but2['text'] = "N/A"
            self.but3['text'] = "N/A"
            return
        elif choice == "flashy sports car":
            self.txt.delete('1.0', END)
            new_txt = "Its fast as hell but is equally loud. It draws every zombie in the area " \
                      "to you. You swerve in and out of zombies in your frantic attempt to control " \
                      "a car that has too much power for you to handle. You end up hitting a few " \
                      "and eventually one shatters through the windshield blocking your vision. " \
                      "You frantically jab at it with your weapon and kill it. But in the crazy " \
                      "struggle you crash and get ejected from the vehicle. You land a good " \
                      "distance from the zombies but your leg is broken. Will you manage to " \
                      "crawl away before any notice you? Maybe, but probably not so lets just " \
                      "call this gg now. You suck scrub."
            self.txt.insert(END, new_txt)
            self.but1['text'] = "N/A"
            self.but2['text'] = "N/A"
            self.but3['text'] = "N/A"
            return
        # catch all
        else:
            self.txt.delete('1.0', END)
            new_txt = "You fucking suck at life and now are zombie food. Have fun " \
                      "being dead ya nub"
            self.txt.insert(END, new_txt)


from pages.LoginPage import LoginPage
from pages.ClanPage import  ClanPage
from pages.FriendsPage import FriendsPage
from pages.HomePage import  HomePage