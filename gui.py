from tkinter import *
import tkinter as tk
import customtkinter
from tkinter import ttk
from tkinter_webcam import webcam
import ttkthemes
import time
from camera_manager import CameraManager
import cv2


class GUI(Tk):

    def __init__(self):
        Tk.__init__(self)

        color_1 = '#1a1a1c'
        color_2 = '#2b2b2e'

        self.current_cam = 'default'

        self.__camera_manager = CameraManager('camera_data.json')

        # pre display settings
        self.title('Security Camera Viewer')
        icon = PhotoImage(file='assets/camera_icon.png')
        self.iconphoto(True, icon)
        # self.minsize(width=300, height=150)
        # self.geometry("600x400")  # setting default size of the window

        style = ttkthemes.ThemedStyle()
        style.theme_use("equilux")

        self.configure(bg=color_2)
        self.menu_frame = Frame(self)
        self.menu_frame.pack(padx=75, pady=40)
        # self.menu_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.menu_frame.configure(bg=color_2)
        # self.menu_frame.tkraise()

        self.cam_names = ['default']
        # order of camera names must match order of file for correct data processing
        self.cam_names += [e['Name'] for e in self.__camera_manager.get_entries().values()]

        print(self.cam_names)
        self.cams = []  # list of active cams. As of now this should only ever have one item

        self.lab1 = Label(self.menu_frame, text='Select a Camera to View', bg=color_2, fg='white',
                          font='Helvetica 10 bold')
        self.lab1.pack()

        self.cam_select = ttk.Combobox(self.menu_frame, values=self.cam_names)
        self.cam_select.pack(anchor='center')
        self.cam_select['state'] = 'readonly'
        self.cam_select.set('default')
        self.cam_select.bind(sequence='<<ComboboxSelected>>',
                             func=lambda event: self.cam_change(event, self.cam_select))

        # self.cam1 = Camera(self.menu_frame, self.get_current_cam())
        # self.cam1.pack(expand=True, fill='both')

        for cam in self.cams:
            cam.mainloop()

    def cam_change(self, e, box):
        print(f'Camera is Set To {box.get()}')
        self.current_cam = box.get()
        if box.get() != 'default':
            self.withdraw()
            self.update()
            time.sleep(0.1)
            self.cams.append(CamView(self, self.__camera_manager.get_entries(), self.current_cam))

    def get_current_cam(self):
        return self.current_cam

    def get_camera_manager(self):
        return self.__camera_manager


class CamView(tk.Toplevel):
    def __init__(self, parent: GUI, data, name: str = 'Camera 0'):
        Toplevel.__init__(self)

        self.__parent = parent
        self.__camera_data = get_data_from_name(name, data)
        # print(self.__camera_data)
        self.__camera_manager = parent.get_camera_manager()

        color_1 = '#1a1a1c'
        color_2 = '#393A3E'
        color_3 = '#2b2b2e'

        # pre display settings
        self.title(name)
        icon = PhotoImage(file='assets/camera_icon.png')
        self.iconphoto(True, icon)
        self.minsize(width=1280, height=720)

        # creating the navigation bar frame which is placed at the top
        self.nav_frame = Frame(self, bg=color_1, borderwidth=1, relief='solid')
        self.nav_frame.pack(side='top', fill='x')

        self.menu_image = PhotoImage(file="assets/hamburger_menu_button_white.png")
        self.menu_button = tk.Button(self.nav_frame, width=16, height=16, image=self.menu_image, bg=color_1,
                                     relief="solid", borderwidth=0, command=self.show_main_window)
        self.menu_button.pack(side="left", padx=10, pady=10)

        self.cam_title = Label(self.nav_frame, text=name, bg=color_1, fg='white', font='Helvetica 12 bold')
        self.cam_title.pack(expand=True, fill='x')

        # main frame holding the bottom section of the screen under the nav-bar
        self.main_frame = Frame(self, bg=color_2)
        self.main_frame.pack(expand=True, fill='both', anchor='s')

        # camera view goes here ---

        self.__camera_manager.get_frame()
        # load and display camera view here based on the camera selected in the gui

        # sidebar
        self.sidebar = Frame(self.main_frame, bg=color_3)
        self.sidebar.place(relx=0, rely=0, relwidth=0.2, relheight=1)

        self.title_frame = Frame(self.sidebar, bg=color_1)
        self.title_frame.pack(fill='x')
        self.sidebar_title = Label(self.title_frame, text='Camera Properties', bg=color_1, fg='white',
                                   font='Helvetica 11 bold')
        self.sidebar_title.pack(fill='x', pady=10)

        self.info_frame = Frame(self.sidebar, bg=color_3)
        self.info_frame.pack(fill='x', side='top')

        self.name_prop = Label(self.info_frame, text=self.__camera_data['Name'], bg=color_3, fg='white',
                               font='Helvetica 10 bold')
        self.name_prop.pack(side='top')
        # self.name_prop.insert(0, self.__camera_data['Name'])  # may need to redo camera data system, so as of now
        # this field is read only

        self.id_prop = Label(self.info_frame, text=f'CV_ID: {self.__camera_data['CV_ID']}', bg=color_3, fg='white',
                             font='Helvetica 10 bold')
        self.id_prop.pack(side='top')

        self.save_prop = Button(self.sidebar, text='Save Changes', bg=color_2, fg='white', font='Helvetica 10 bold')
        self.save_prop.pack(fill='x', side='bottom', pady=12, padx=12)

    def show_main_window(self):
        print('show main window')
        self.__parent.deiconify()
        self.destroy()


def get_data_from_name(name, data):
    # find the dictionary with the name value matching the input name then return

    for e in data.values():
        if e['Name'] == name:
            return e
    return None


def main():
    graphics = GUI()
    graphics.mainloop()

    # cam = CamView()
    # cam.mainloop()


main()
