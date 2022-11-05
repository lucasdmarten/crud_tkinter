import tkinter as tk
from tkinter import *
from tkinter import messagebox
import yaml
import os


def load_yaml(name):
	with open(f'./database/{name}.yaml', 'r') as yfile:
		current_yaml = yaml.safe_load(yfile)
	return current_yaml


def output_data_fn():
	fields = ('name','email','idate','fdate','description','total')
	return {f'{key}':eval(f'{key}.get()') for key in fields}


def update_btn():
	output_data = output_data_fn()
	if not name.get():
		return messagebox.showinfo('message', f'Hi! field name is required.')
	is_file = os.path.isfile(f"./database/{name.get()}.yaml")
	if is_file:
		update_yaml(output_data)
	else:
		messagebox.showinfo('message', f'file not exist.')


def create_btn():
	if not name.get():
		return messagebox.showinfo('message', f'Hi! field name is required.')
	os.makedirs('../database/', exist_ok=True)
	is_file = os.path.isfile(f"./database/{name.get()}.yaml")
	output_data = output_data_fn()
	if is_file:
		messagebox.showinfo('message', f'Hi! a client with same name already registered')
	if not is_file:
		create_yaml(name.get(), output_data)


def delete_btn():
	is_file = os.path.isfile(f"./database/{name.get()}.yaml")
	if is_file:
		delete_yaml(name.get())
	else:
		messagebox.showinfo('message', f'not exist {name.get()}')


def read_btn():

	if name.get():
		is_file = os.path.isfile(f"./database/{name.get()}.yaml")
		if is_file:
			read_yaml(name.get())
		else:
			messagebox.showinfo('message', f'not exist {name.get()}')
	else:
		messagebox.showinfo('message', f'not exist {name.get()}')


def create_yaml(name, context):
	with open(f'./database/{name}.yaml', 'w+') as yfile:
		yaml.dump(
			context, yfile,
			allow_unicode=True, default_flow_style=False
		)
	return True


def update_yaml(context):
	if context['name']:
		current_yaml = load_yaml(context['name'])
		for key, value in context.items():
			if value:
				current_yaml[key] = value
		create_yaml(context['name'], current_yaml)


def delete_yaml(name):
	os.remove(f"./database/{name}.yaml")


def read_yaml(name):
	messagebox.showinfo('message', f"{load_yaml(name)}")

def make_form():
	fields = ('name', 'email', 'idate', 'fdate', 'description', 'total')
	for i, field in enumerate(fields):
		entry = tk.Entry(root, width=35)
		entry.grid(row=i, column=1)
		label = tk.Label(root, text=f"{field} -")
		label.grid(row=i, column=0)

root = tk.Tk()
width = 600 # Width
height = 300 # Height

screen_width = root.winfo_screenwidth()  # Width of the screen
screen_height = root.winfo_screenheight() # Height of the screen
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)

root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.title("Mecânica X")
root.eval('tk::PlaceWindow . center')


name = tk.Entry(root, width=35)
email = tk.Entry(root, width=35)
idate = tk.Entry(root, width=35)
fdate = tk.Entry(root, width=35)
description = tk.Entry(root, width=35)
total = tk.Entry(root, width=35)

name.grid(row=0,column=1)
email.grid(row=1,column=1)
idate.grid(row=2,column=1)
fdate.grid(row=3,column=1)
description.grid(row=4,column=1)
total.grid(row=5,column=1)


name_label = tk.Label(root, text="name -")
email_label = tk.Label(root, text="email -")
idate_label = tk.Label(root, text="idate -")
fdate_label = tk.Label(root, text="fdate -")
description_label = tk.Label(root, text="description -")
total_label = tk.Label(root, text="total -")

name_label.grid(row=0,column=0)
email_label.grid(row=1,column=0)
idate_label.grid(row=2,column=0)
fdate_label.grid(row=3,column=0)
description_label.grid(row=4,column=0)
total_label.grid(row=5,column=0)


submitbtn = tk.Button(root, text="Create",
                      bg='red', command=create_btn)
submitbtn.grid(row=6,column=0)

updtbtn = tk.Button(root, text="Update",
                      bg='green', command=update_btn)
updtbtn.grid(row=6,column=1)



readbtn = tk.Button(root, text="Read",
                      bg='blue', command=read_btn)
readbtn.grid(row=7,column=0)

deletebtn = tk.Button(root, text="Delete",
                      bg='red', command=delete_btn)
deletebtn.grid(row=7,column=1)

root.mainloop()