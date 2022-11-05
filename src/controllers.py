import tkinter as tk
from ttkbootstrap import constants
from tkinter import ttk, messagebox


class ButtonController:

    def __init__(self):
        pass

    @staticmethod
    def register_client():
        return messagebox.showinfo(title='register',message='register client callback')

    @staticmethod
    def register_service():
        return messagebox.showinfo(title='register', message='register service callback')

    @staticmethod
    def consult_client():
        return messagebox.showinfo(title='consult',message='consult client callback')


class TabController(ttk.Notebook):

    def __init__(self, parent, *args, **kwargs):
        ttk.Notebook.__init__(self, parent, *args, **kwargs)
        self.register_tab = ttk.Frame(self)
        self.consult_tab = ttk.Frame(self)
        self.add(self.register_tab, text=f'{"register":^20s}')
        self.add(self.consult_tab, text=f'{"consult":^20s}')
        self.grid(row=0, column=0, padx=100, pady=100, ipadx=100, ipady=100)




class FormsController:

    def __init__(self):
        pass

    def create_form_entry(self, label, variable, tab, i, j):
        container = ttk.Frame(tab)
        container.grid(row=i, column=j, sticky="w")
        lbl = ttk.Label(master=container, text=label.title(), width=5)
        lbl.grid(row=0, column=0, sticky="w")
        ent = ttk.Entry(master=container, textvariable=variable)
        ent.grid(row=0, column=1, sticky="w")

