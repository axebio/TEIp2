from tkinter import *
from typing import Container
import psycopg2
import os


# from sql import insert_data

# postgresql-parallel-82683


def registrar(campo1, campo2, campo_saida):
	valores = "{}, {}".format(campo1.get(), campo2.get())
	output = Label(campo_saida, text= valores, font=("Helvetica, 18"), bg= "black", fg = "white")
	output.grid(row = 3, column= 1, pady=200, padx=10)
	clear(campo1, campo2)

def clear(campo1, campo2):
	campo1.delete(0, END)
	campo2.delete(0, END)

origin_path = os.path.abspath(os.getcwd())

class register_page(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)


		
		
		# Create The GUI For The App
		my_frame = Frame(self)
		my_frame.pack(pady=40)

		user_label = Label(my_frame, text="Usuários")
		user_label.grid(row=0, column=0, pady=10, padx=10)

		user_name = Entry(my_frame, font=("Helvetica, 18"))
		user_name.grid(row=0, column=1, pady=10, padx=10)

		senha_label = Label(my_frame, text="Senha")
		senha_label.grid(row=1, column=0, pady=10, padx=10)

		senha_name = Entry(my_frame, font=("Helvetica, 18"))
		senha_name.grid(row=1, column=1, pady=10, padx=10)

		entrar_button = Button(my_frame, text="REGISTRAR", command=lambda:[registrar(user_name, senha_name, my_frame)])
		entrar_button.grid(row=2, column=0, pady=10, padx=10)

		update_button = Button(my_frame, text="VOLTAR", command= lambda:controller.show_frame())
		update_button.grid(row=2, column=1, pady=10, padx=10)
