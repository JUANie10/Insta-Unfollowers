from Web_automation import InstaAnalyzer
from PIL import Image, ImageTk
import os
import tkinter as tk
from tkinter import *


class GUI:
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

    def validateLogin(self, username, password):

        for widget in self.Frame.winfo_children():
            widget.destroy()

        loading_image_1 = PhotoImage(file='Loading1.png')
        screen_label = tk.Label(self.Frame, image=loading_image_1).pack()


        Profile = InstaAnalyzer(username.get(), password.get())

        if Profile.auto_login():
            for widget in self.Frame.winfo_children():
                widget.destroy()

            loading_image_2 = PhotoImage(file='Loading2.png')
            screen_label = tk.Label(self.Frame, image=loading_image_2).pack()

            non_followers = Profile.instaUnfollowers()

            for widget in self.Frame.winfo_children():
                widget.destroy()

            loading_image_3 = PhotoImage(file='Loading3.png')
            screen_label = tk.Label(self.Frame, image=loading_image_3).pack()

            self.showUsernames(non_followers)


        else:
            messagebox.showerror("Error", "Incorrect credentials. Please try again.")
            Profile.driver.close()
            self.login_screen()

    def showUsernames(self, non_followers):
        for widget in self.Frame.winfo_children():
            widget.destroy()
        


