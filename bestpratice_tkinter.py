import tkinter as tk
from tkinter import ttk
from ttkbootstrap import constants


class MainApplication(tk.Frame):


    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

    def create_form_entry(self, label, variable, tab, i, j):
        container = ttk.Frame(tab)
        container.grid(row=i, column=j, sticky="w")
        lbl = ttk.Label(master=container, text=label.title(), width=10)
        lbl.grid(row=0, column=0, sticky="w")
        ent = ttk.Entry(master=container, textvariable=variable)
        ent.grid(row=0, column=1, sticky="w")

    def client_register(self, register):
        container = ttk.Frame(register)
        container.grid(row=0, column=0, sticky="w")
        ttk.Label(master=container, text="CLIENT").grid(row=0, column=0, sticky="nw")
        self.create_form_entry("name", tk.StringVar, container, 1, 0)
        self.create_form_entry("email", tk.StringVar, container, 2, 0)
        self.create_form_entry("phone", tk.StringVar, container, 3, 0)
        self.create_form_entry("birthday", tk.StringVar, container, 4, 0)
        ttk.Button(master=container,text="client_add",# command=self.create,
                    bootstyle=constants.SUCCESS,width=6,).grid(row=9, column=1, sticky="w")

    def service_register(self, register):
        container = ttk.Frame(register)
        container.grid(row=1, column=0, sticky="w")
        ttk.Label(master=container, text="SERVICE").grid(row=5, column=0, sticky="nw")
        self.create_form_entry("client_name", tk.StringVar, container, 6, 0)
        self.create_form_entry("placa", tk.StringVar, container, 7, 0)
        self.create_form_entry("modelo", tk.StringVar, container, 8, 0)
        self.create_form_entry("descrição", tk.StringVar, container, 9, 0)
        ttk.Button(master=container, text="service_add",# command=self.create,
                    bootstyle=constants.SUCCESS, width=6).grid(row=18, column=1, sticky="w")


class TabController(ttk.Notebook):


    def __init__(self, parent, *args, **kwargs):
        ttk.Notebook.__init__(self, parent, *args, **kwargs)
        self.register_tab = ttk.Frame(self)
        self.consult_tab = ttk.Frame(self)
        self.add(self.register_tab, text=f'{"register":^20s}')
        self.add(self.consult_tab, text=f'{"consult":^20s}')
        self.pack(expand=1, fill='both')



if __name__ == '__main__':
   window = tk.Tk()
   window.title("Registrio GUI")

   tab_app = TabController(window)
   MainApplication(window).client_register(tab_app.register_tab)
   MainApplication(window).service_register(tab_app.register_tab)
   window.mainloop()
