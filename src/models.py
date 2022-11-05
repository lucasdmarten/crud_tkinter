from src.controllers import ButtonController, FormsController
import tkinter as tk
from ttkbootstrap import constants
from tkinter import ttk, messagebox


class Register(tk.Frame, FormsController, ButtonController):


    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.button_methods = ButtonController

    def client_register(self, register):
        container = ttk.Frame(register)
        container.grid(row=0, column=0, sticky="w")
        ttk.Label(master=container, text="CLIENT").grid(row=0, column=0, sticky="nw")
        self.create_form_entry("name", tk.StringVar, container, 1, 0)
        self.create_form_entry("email", tk.StringVar, container, 2, 0)
        self.create_form_entry("phone", tk.StringVar, container, 3, 0)
        self.create_form_entry("birthday", tk.StringVar, container, 4, 0)
        ttk.Button(master=container,text="client_add", command=self.button_methods.register_client,
                    bootstyle=constants.SUCCESS,width=10,).grid(row=9, column=0, pady=15, padx=15, sticky="n")

    def service_register(self, register_tab):
        container = ttk.Frame(register_tab)
        container.grid(row=1, column=0, sticky="w")
        ttk.Label(master=container, text="SERVICE").grid(row=5, column=0, sticky="nw")
        self.create_form_entry("client_name", tk.StringVar, container, 6, 0)
        self.create_form_entry("placa", tk.StringVar, container, 7, 0)
        self.create_form_entry("modelo", tk.StringVar, container, 8, 0)
        self.create_form_entry("descrição", tk.StringVar, container, 9, 0)
        ttk.Button(master=container, text="service_add", command=self.button_methods.register_service,
                    bootstyle=constants.SUCCESS, width=10).grid(row=18, column=0, pady=15, padx=15, sticky="n")


class Consult(tk.Frame, FormsController, ButtonController):


    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.button_methods = ButtonController

    def consult_client(self, consult_tab):
        container = ttk.Frame(consult_tab)
        container.grid(row=0, column=0, sticky="w")
        ttk.Label(master=container, width=20, text="SEARCH DATABASE").grid(row=0, column=0, sticky="e")
        self.create_form_entry("name", tk.StringVar, container, 1, 0)
        ttk.Button(master=container, text="SEARCH", command=self.button_methods.consult_client,
                   bootstyle=constants.SUCCESS, width=20, ).grid(row=9, column=0, pady=15, padx=15, sticky="nw")

