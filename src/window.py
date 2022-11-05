import tkinter as tk
from ttkbootstrap import constants
from tkinter import ttk, messagebox


class TKWindow(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title("Test Application")
        container = tk.Frame(self, height=400, width=600)
        container.grid(row=0, column=0, padx=100, pady=100, ipadx=100, ipady=100)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)