import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap import constants

from src.controllers import TabController
from src.window import TKWindow
from src.models import Register, Consult


if __name__ == '__main__':
   window = TKWindow()
   tab_app = TabController(window)
   Consult(window).consult_client(tab_app.consult_tab)
   Register(window).client_register(tab_app.register_tab)
   Register(window).service_register(tab_app.register_tab)
   window.mainloop()
