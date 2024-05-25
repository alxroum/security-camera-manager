from tkinter import *
import tkinter as tk
import cv2

class GUI(Tk):

    def __init__(self, width, height):
        Tk.__init__(self)

        # variables
        self.width = width
        self.height = height

        # fixing window size for now
        self.minsize(self.width, self.height)
        self.maxsize(self.width, self.height)

        # creating the main frame
        self.main_frame = Frame(self)
        self.main_frame.pack(expand="yes", fill="both")

        # creating the button frame which is placed on the bottom
        self.button_frame = Frame(self.main_frame, bg="#1a1a1c")
        self.button_frame.pack(expand="yes", fill="x", side="bottom", anchor="s")

        # creating the buttons
        self.start_rec = tk.Button(self.button_frame, text="Start Recording", bg="#47a123")
        self.start_rec.pack(side="left", padx=15, pady=15)
        self.new_frame = tk.Button(self.button_frame, text="Display New Frame")
        self.new_frame.pack(side="left", fill="both", expand="yes", padx=20, pady=20)
        self.stop_rec = tk.Button(self.button_frame, text="Stop Recording", bg="#bf2222")
        self.stop_rec.pack(side="right", padx=15, pady=15)

    def start_recording(self):
        pass

    def stop_recording(self):
        pass

    def display_new_frame(self):
        pass


graphics = GUI(1000, 600)
graphics.mainloop()