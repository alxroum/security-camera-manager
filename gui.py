from tkinter import *
import tkinter as tk
import customtkinter
from tkinter import ttk
from tkinter_webcam import webcam
import ttkthemes
import cv2


class GUI(Tk):

    def __init__(self):
        Tk.__init__(self)

        color_1 = '#1a1a1c'
        color_2 = '#2b2b2e'

        self.current_cam = 'default'

        # pre display settings
        self.title('Security Camera Viewer')
        icon = PhotoImage(file='assets/camera_icon.png')
        self.iconphoto(True, icon)
        self.minsize(width=300, height=150)
        # self.geometry("600x400")  # setting default size of the window

        style = ttkthemes.ThemedStyle()
        style.theme_use("equilux")

        self.menu_frame = Frame(self)
        self.menu_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.menu_frame.configure(bg=color_2)
        self.menu_frame.tkraise()

        self.cam_names = ['default', 'Camera 1', 'Camera 2', 'Camera 3']
        self.cams = []


        self.lab1 = Label(self.menu_frame, text='Select a Camera to View', bg=color_2, fg='white', font='Helvetica 10 bold')
        self.lab1.pack()

        self.cam_select = ttk.Combobox(self.menu_frame, values=self.cam_names)
        self.cam_select.pack(anchor='center')
        self.cam_select['state'] = 'readonly'
        self.cam_select.set('default')
        self.cam_select.bind(sequence='<<ComboboxSelected>>', func=lambda event: self.cam_change(event, self.cam_select))

        #self.cam1 = Camera(self.menu_frame, self.get_current_cam())
        #self.cam1.pack(expand=True, fill='both')

        for cam in self.cams:
            cam.mainloop()

    def cam_change(self, e, box):
        print(f'Camera is Set To {box.get()}')
        self.current_cam = box.get()
        if box.get() != 'default':
            self.cams.append(Camera(self.current_cam))


    def get_current_cam(self):
        return self.current_cam


class Camera(tk.Toplevel):
    def __init__(self, name: str = 'Camera 0'):
        Toplevel.__init__(self)

        color_1 = '#1a1a1c'
        color_2 = '#2b2b2e'

        # pre display settings
        self.title('Security Camera Viewer')
        icon = PhotoImage(file='assets/camera_icon.png')
        self.iconphoto(True, icon)
        self.minsize(width=300, height=150)

        # creating the navigation bar frame which is placed at the top
        self.nav_frame = Frame(self, bg=color_1, borderwidth=1, relief='solid')
        self.nav_frame.pack(side='top', fill='x')

        self.menu_image = PhotoImage(file="assets/hamburger_menu_button_white.png")
        self.menu_button = tk.Button(self.nav_frame, width=16, height=16, image=self.menu_image, bg=color_1,
                                     relief="solid", borderwidth=0)
        self.menu_button.pack(side="left", padx=10, pady=10)

        self.cam_title = Label(self.nav_frame, text=name, bg=color_1, fg='white', font='Helvetica 12 bold')
        self.cam_title.pack(expand=True, fill='y')

        # main frame holding the bottom section of the screen under the nav-bar
        self.main_frame = Frame(self, bg=color_2)
        self.main_frame.pack(expand=True, fill='both', anchor='s')

        # sidebar
        self.sidebar = Frame(self.main_frame, bg=color_1)
        self.sidebar.place(relx=0, rely=0, relwidth=0.2, relheight=1)
        self.sidebar_title = Label(self.sidebar, text='Camera Properties', bg=color_1, fg='white')
        self.sidebar_title.pack()

def main():
    graphics = GUI()
    graphics.mainloop()

    #cam = Camera()
    #cam.mainloop()


main()
