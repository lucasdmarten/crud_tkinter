import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import os
import yaml


class DataEntryForm(ttk.Frame):

    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)

        # form variables
        self.name = ttk.StringVar(value="")
        self.email = ttk.StringVar(value="")
        self.phone = ttk.StringVar(value="")
        self.idate = ttk.StringVar(value="")
        self.fdate = ttk.StringVar(value="")
        self.description = ttk.StringVar(value="")
        self.total = ttk.StringVar(value="")

        # form header
        hdr_txt = "Please enter your contact information"
        hdr = ttk.Label(master=self, text=hdr_txt, width=50)
        hdr.pack(fill=X, pady=10)

        # form entries
        self.create_form_entry("name", self.name)
        self.create_form_entry("email", self.email)
        self.create_form_entry("phone", self.phone)
        self.create_form_entry("idate", self.idate)
        self.create_form_entry("fdate", self.fdate)
        self.create_form_entry("description", self.description)
        self.create_form_entry("total", self.total)
        self.create_buttonbox()

    def load_yaml(self):
        with open(f'./database/{self.name.get()}.yaml', 'r') as yfile:
            current_yaml = yaml.safe_load(yfile)
        return current_yaml

    def create_form_entry(self, label, variable):
        """Create a single form entry"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=10)
        lbl.pack(side=LEFT, padx=5)

        ent = ttk.Entry(master=container, textvariable=variable)
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)

    def create_buttonbox(self):
        """Create the application buttonbox"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=(15, 10))

        create_btn = ttk.Button(
            master=container,
            text="Submit",
            command=self.create,
            bootstyle=SUCCESS,
            width=6,
        )
        create_btn.pack(side=RIGHT, padx=5)
        create_btn.focus_set()

        del_btn = ttk.Button(
            master=container,
            text="Delete",
            command=self.update,
            bootstyle=DANGER,
            width=6,
        )
        del_btn.pack(side=RIGHT, padx=5)

        update_btn = ttk.Button(
            master=container,
            text="Update",
            command=self.update,
            bootstyle=WARNING,
            width=6,
        )
        update_btn.pack(side=RIGHT, padx=5)

        read_btn = ttk.Button(
            master=container,
            text="Read",
            command=self.on_cancel,
            bootstyle=INFO,
            width=6,
        )
        read_btn.pack(side=RIGHT, padx=5)

    def output_data_fn(self):
        output_data = {
            'name':self.name.get(),
            'email':self.email.get(),
            'phone':self.phone.get(),
            'idate':self.idate.get(),
            'fdate':self.fdate.get(),
            'description': self.description.get(),
            'total':self.total.get()
        }
        return output_data

    def create(self):
        #def create_btn():
        if not self.name.get():
            return self.messagebox.showinfo('message', f'Hi! field name is required.')
        os.makedirs('./database/', exist_ok=True)
        is_file = os.path.isfile(f"./database/{self.name.get()}.yaml")

        if is_file:
            self.messagebox.showinfo('message', f'Hi! a client with same name already registered')
        if not is_file:
            with open(f'./database/{self.name.get()}.yaml', 'w+') as yfile:
                yaml.dump(
                    self.output_data_fn(), yfile,
                    allow_unicode=True, default_flow_style=False
                )

        return

    def update(self):
        data_entry = self.output_data_fn()
        if not self.name.get():
            return self.messagebox.showinfo('message', f'Hi! field name is required.')
        is_file = os.path.isfile(f"./database/{self.name.get()}.yaml")
        if is_file:
            if self.name.get():
                current_yaml = self.load_yaml()
                for key, value in data_entry.items():
                    if value:
                        current_yaml[key] = value
                with open(f'./database/{self.name.get()}.yaml', 'w+') as yfile:
                    yaml.dump(
                        current_yaml, yfile,
                        allow_unicode=True, default_flow_style=False
                    )
            else:
                self.messagebox.showinfo('message', f'necessary a name.')
        else:
            self.messagebox.showinfo('message', f'file not exist.')

    def on_cancel(self):
        """Cancel and close the application."""
        self.quit()


if __name__ == "__main__":

    app = ttk.Window("Data Entry", "superhero", resizable=(False, False))
    DataEntryForm(app)
    app.mainloop()