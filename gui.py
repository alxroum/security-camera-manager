from tkinter import *
import tkinter as tk
import customtkinter
from tkinter_webcam import webcam
import cv2


class GUI(Tk):

    def __init__(self, width, height):
        Tk.__init__(self)

        color_1 = '#1a1a1c'
        color_2 = '#2b2b2e'

        # variables
        self.width = width
        self.height = height

        self.side_menu_open = False

        # pre display settings
        self.title('Security Camera Viewer')
        icon = PhotoImage(file='assets/camera_icon.png')
        self.iconphoto(True, icon)
        self.geometry("600x400")  # setting default size of the window

        # creating the navigation bar frame which is placed at the top
        self.nav_frame = Frame(self, bg=color_1)
        self.nav_frame.pack(side='top', fill='x')

        self.menu_image = PhotoImage(file="assets/hamburger_menu_button_white.png")
        self.menu_button = tk.Button(self.nav_frame, width=16, height=16, image=self.menu_image, bg=color_1, relief="solid", borderwidth=0, command=self.side_menu)
        self.menu_button.pack(side="left", padx=10, pady=10)

        # main frame holding the bottom section of the screen under the nav-bar
        self.main_frame = Frame(self, bg=color_2)
        self.main_frame.pack(expand=True, fill='both', anchor='s')

        # sidebar
        self.sidebar = Frame(self.main_frame, bg=color_1)
        self.sidebar.place(relx=0, rely=0, relwidth=0.2, relheight=1)

        # creating the main camera display frame
        self.cam_frame = Frame(self.main_frame, bg=color_2)  # main background frame
        self.cam_frame.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)


        self.cam_1 = Frame(self.cam_frame, bg='blue')
        self.cam_1.grid(row=0, column=0, sticky="nsew", rowspan=2)
        self.img1 = PhotoImage(file='assets/hamburger_menu_button.png')
        self.label = Label(self.cam_1, image=self.img1)
        self.label.pack()

        self.cam_2 = Frame(self.cam_frame, bg='red')
        self.cam_2.grid(row=0, column=1, sticky="nsew")

        if self.side_menu_open:
            print('open')


    def side_menu(self):

        if self.side_menu_open:
            print("hiding side menu")
            self.side_menu_open = False

        if not self.side_menu_open:
            print("showing side menu")
            self.side_menu_open = True

    def cam_change(self, e):
        print(f'Camera Changed To {e}')



def main():
    graphics = GUI(1000, 600)
    graphics.mainloop()


main()
