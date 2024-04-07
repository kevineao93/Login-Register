import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from PIL import Image, ImageTk

class Container(tk.Frame):
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.controlador = controlador
        self.pack()
        self.place(x=0, y=0, width=1100, height=650)
        self.config(bg="#C6D9E3")
        self.widgets()

    def show_frames(self, container):
        top_level = tk.Toplevel(self)
        frame = container(top_level)
        frame.config(bg="#C6D9E3")
        frame.pack(fill="both", expand=True)
        top_level.geometry("1100x650")
        #top_level.pack(fill="both", expand=True)
        #top_level.state("zoomed")
        top_level.resizable(False, False)

    def widgets(self):  
        
#==============Frame superior=======================================================================================================#
        frame1 = tk.Frame(self, bg="#dddddd",highlightbackground="gray", highlightthickness=1)
        frame1.pack()
        frame1.place(x=0, y=0, width=1100, height=100)
        
        lblframe1=tk.Label(frame1, text="LOGIN & REGISTER", font="sans 30 bold", bg="#dddddd", anchor="center")
        lblframe1.place(x=3, y=5, width=1095, height=90)
        