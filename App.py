from Web_automation import InstaAnalyzer
from PIL import Image, ImageTk
import os
import tkinter as tk
from tkinter import *
from time import sleep

class GUI:
    #Sets up the canvas and stores local variables
    def __init__(self, Frame):
        self.Frame = Frame
        Frame.title('Instagram Unfollowers')
        self.canvas = tk.Canvas(Frame, width=250, height=250)
        self.instagram_image = PhotoImage(file='InstagramIcon.png')
        Frame.iconphoto(False, self.instagram_image)
        Frame.configure(bg="white smoke")
        self.background_label = tk.Label(Frame, image=self.instagram_image).grid(row=0, column=0)
        self.label = Label(self.Frame)
        self.start_button = Button(self.Frame , text="Start", width=10, bg="snow", command=self.login_screen).grid(row=0, column=0)

    #Makes the Login screen
    def login_screen(self):
        for widget in self.Frame.winfo_children():
            widget.destroy()

        # Username label and text entry box
        usernameLabel = Label(self.Frame, text="Username").grid(row=0, column=0)
        username = StringVar()
        usernameEntry = Entry(self.Frame, textvariable=username).grid(row=0, column=1)

        # Password label and text entry box
        passwordLabel = Label(self.Frame, text="Password").grid(row=2, column=0)
        password = StringVar()
        passwordEntry = Entry(self.Frame, show="*" ,textvariable=password).grid(row=2, column=1)


        loginButton = Button(self.Frame, text="Login", command= lambda: self.validateLogin(username, password)).grid(row=3, column=1)

    #Validates the login information and if it doesnt work, it brings you back to the login page
    def validateLogin(self, username, password):

        #Setting up a login profile for web automation
        Profile = InstaAnalyzer(username.get(), password.get())

        #Checks if the login information is correct
        if Profile.auto_login():
            #Gets a list of non followers that you follower
            non_followers = Profile.instaUnfollowers()

            self.showUsernames(non_followers)

        else:
            #Shows a error message and brings you back to the login page
            messagebox.showerror("Error", "Incorrect credentials. Please try again.")
            Profile.driver.close()
            self.login_screen()

    #Displays the lists of usernames on a textbox with a scrollbox.
    def showUsernames(self, non_followers):
        for widget in self.Frame.winfo_children():
            widget.destroy()

        #Setting up the frame
        self.Frame.geometry("150x200")

        w = Label(self.Frame, text='Insta Unfollowers',
                  font="50").pack()

        scroll_bar = Scrollbar(self.Frame)

        scroll_bar.pack(side=RIGHT,
                        fill=Y)

        mylist = Listbox(self.Frame,
                         yscrollcommand=scroll_bar.set)

        #Inserting the usernames into the list to display
        for line in range(len(non_followers)):
            mylist.insert(END, str(line+1) + ". " + non_followers[line])

        mylist.pack(side=LEFT, fill=BOTH)

        scroll_bar.config(command=mylist.yview)

