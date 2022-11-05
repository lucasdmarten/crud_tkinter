import re
import tkinter as tk
from tkinter import ttk
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import yaml
import os


class Client:
    def __init__(self, name, context):
        self.name = name
        self.context = context

    def output_data_fn(self):
        fields = (
            'name', 'email', 'idate', 'fdate', 'description', 'total'
        )
        return {f'{key}': eval(f'{key}.get()') for key in fields}

    def load_yaml(self):
        with open(f'./database/{self.name}.yaml', 'r') as yfile:
            current_yaml = yaml.safe_load(yfile)
        return current_yaml

    def save(self):
        with open(f'./database/{self.name}.yaml', 'w+') as yfile:
            yaml.dump(
                self.context, yfile,
                allow_unicode=True, default_flow_style=False
            )
        return True

    def update(self):
        if self.context['name']:
            current_yaml = self.load_yaml(self.context['name'])
            for key, value in self.context.items():
                if value:
                    current_yaml[key] = value
            self.save(self.name, current_yaml)
        return True