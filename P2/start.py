from tkinter import *
from menu import *
from function import *
import os
from function import _start





class start(Tk):
	def __init__(self, *args, **kwargs):
		Tk.__init__(self, *args, **kwargs)
		
		#barra de menu
		# login_menu(self)
		
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
		
		entrar_button = Button(container, text="ENTRAR", justify= "center", command= _start())
		entrar_button.grid(row=3, column=1, pady=10, padx=50)

		registrar_button = Button(container, 
								text="REGISTRAR", 
								justify= "center", 
								bd= 0, fg = "blue", 
								activeforeground= "navy", 
								cursor= "hand2")
								# command= fc.registrar())

		registrar_button.grid(row=4, column=1, pady=10, padx=50)



app = start()
app.mainloop()

