from tkinter import *
import os



class login_page(Tk):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		

		#título e ícone
		self.title("ValeFarma")
		origin_path = os.path.abspath(os.getcwd())
		self.iconbitmap(origin_path + "\\images\\diamante.ico")

		window_height = 400
		window_width = 600
		
		self.geometry("{}x{}+{}+{}".format(window_height, window_width, 200, 200))
		self.resizable(False, False)
		activepage = 0
		container = Frame(self, width= 400, height= 600)

		container.pack(side= "top", fill="both", expand=True)

		# container.pack()
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)
		container.grid(row=0, column=0, sticky="nsew", pady= 20, padx= 20)

		user_label = Label(container, text="Usuários", justify= "center")
		user_label.grid(row=1, column=0, pady=10, padx=10)

		user_name = Entry(container, font=("Helvetica, 18"))
		user_name.grid(row=1, column=1, pady=10, padx=10)

		senha_label = Label(container, text="Senha")
		senha_label.grid(row=2, column=0, pady=10, padx=10)

		senha_name = Entry(container, font=("Helvetica, 18"))
		senha_name.grid(row=2, column=1, pady=10, padx=10)
		

