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
	fields = ('name', 'email', 'idate', 'fdate', 'description', 'total')
	output_data = {f'{field}': entrys[field].get() for field in fields}
	return output_data

def update_btn():
	output_data = output_data_fn()
	if not entrys["name"].get():
		return messagebox.showinfo('message', f'Hi! field name is required.')
	is_file = os.path.isfile(f"./database/{entrys['name'].get()}.yaml")
	if is_file:
		update_yaml(output_data)
	else:
		messagebox.showinfo('message', f'file not exist.')

def create_btn():
	if not entrys['name'].get():
		return messagebox.showinfo('message', f'Hi! field name is required.')
	os.makedirs('../database/', exist_ok=True)
	is_file = os.path.isfile(f"./database/{entrys['name'].get()}.yaml")

	output_data = output_data_fn()

	if is_file:
		messagebox.showinfo('message', f'Hi! a client with same name already registered')
	if not is_file:
		create_yaml(entrys["name"].get(), output_data)

def delete_btn():
	is_file = os.path.isfile(f"./database/{entrys['name'].get()}.yaml")
	if is_file:
		delete_yaml(entrys['name'].get())
	else:
		messagebox.showinfo('message', f'not exist {entrys["name"].get()}')

def read_btn():
	if entrys['name'].get():
		is_file = os.path.isfile(f"./database/{entrys['name'].get()}.yaml")
		if is_file:
			read_yaml(entrys['name'].get())
		else:
			messagebox.showinfo('message', f'not exist {entrys["name"].get()}')
	else:
		messagebox.showinfo('message', f'not exist {entrys["name"].get()}')

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
	entrys, labels = dict(), dict()
	for i, field in enumerate(fields):
		entrys[field] = tk.Entry(root, width=35)
		entrys[field].grid(row=i, column=1)
		labels[field] = tk.Label(root, text=f"{field} -")
		labels[field].grid(row=i, column=0)
	return entrys, labels

def make_buttons():
	buttons = {"create": create_btn, "update": update_btn, "read": read_btn, "delete": delete_btn}
	for i, button in enumerate(buttons):
		btn = tk.Button(root, text=f"{button}", bg='red', command=buttons[button])
		btn.grid(row=6, column=i)

def set_screensize(root):
	width = 600  # Width
	height = 300  # Height
	screen_width = root.winfo_screenwidth()  # Width of the screen
	screen_height = root.winfo_screenheight()  # Height of the screen
	x = (screen_width / 2) - (width / 2)
	y = (screen_height / 2) - (height / 2)

	root.geometry('%dx%d+%d+%d' % (width, height, x, y))
	root.title("Mecânica X")
	root.eval('tk::PlaceWindow . center')


if '__main__' == __name__:

	root = tk.Tk()

	set_screensize(root)
	entrys, labels = make_form()
	make_buttons()

	root.mainloop()