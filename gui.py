from tkinter import *
import tkinter as tk
import cv2


class GUI(Tk):

    def __init__(self, width, height):
        Tk.__init__(self)

        # variables
        self.width = width
        self.height = height

        self.geometry("600x400")  # setting default size of the window

        # fixing window size for now
        # self.minsize(self.width, self.height)
        # self.maxsize(self.width, self.height)

        # creating the main frame
        self.main_frame = Frame(self, bg="#2b2b2e")  # main background frame
        self.main_frame.pack(expand="yes", fill="both")

        # creating the navigation bar frame which is placed at the top
        self.nav_frame = Frame(self.main_frame, bg="#1a1a1c")
        self.nav_frame.pack(expand="yes", fill="x", side="top", anchor="n")

        self.side_bar = Frame(self.main_frame, bg="white")
        self.side_bar.pack(expand="yes", fill="y", side="bottom", anchor="w")



        self.menu_image = PhotoImage(file="assets/hamburger_menu_button_white.png")
        self.menu_button = tk.Button(self.nav_frame, image=self.menu_image, bg="#2b2b30")
        self.menu_button.pack(side="left", padx=10, pady=10)
        self.menu_button.bind('<Button-1>', lambda e: show_side_menu())  # opens expanded menu when button is clicked
        self.menu_button.bind('<Leave>', lambda e: hide_side_menu())  # exits when mouse leaves expanded menu


def main():
    graphics = GUI(1000, 600)
    graphics.mainloop()


def show_side_menu():
    print("showing side menu")

def hide_side_menu():
    print("hiding side menu")

main()
