import tkinter as tk
from tkinter import Label, font as tkfont
from tkinter.constants import LEFT
from PIL import ImageTk, Image
import os


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        menu(self)

        self.title("ValeFarma")
        origin_path = os.path.abspath(os.getcwd())
        self.iconbitmap(origin_path + "\\images\\diamante.ico")

        

        self.title_font = tkfont.Font(family='Helvetica', size=12, slant="italic")
        self.geometry("{}x{}+{}+{}".format(400,600, 200, 200))
        self.resizable(False, False)
        container = tk.Frame(self)
        
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (login_page, menu_principal, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("login_page")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class login_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        
        origin_path = os.path.abspath(os.getcwd())
        tkimage = ImageTk.PhotoImage(Image.open(origin_path + "\\images\\diamante.png").resize([100, 100]))
        label = tk.Label(self, image=tkimage)
        label.image = tkimage
        label.pack(side = "top", pady= 50)

        usuario = tk.Label(self, 
                            text="Nome de usuario", 
                            font=controller.title_font, 
                            justify= "left", 
                            anchor= "w")
        usuario.pack(side="top")

        campo_user = tk.Entry(self, width= 50)
        campo_user.pack(pady= 10)


        senha = tk.Label(self, text="Senha", font=controller.title_font, justify= "left", anchor= "w")
        senha.pack(side="top")

        campo_user = tk.Entry(self, width= 50)
        campo_user.pack(pady= 10)

        bt_entrar = tk.Button(self, 
                    text="Entrar",
                    width= 10,
                    command=lambda: controller.show_frame("menu_principal"))
        bt_entrar.pack(pady= 10)

        bt_registrar = tk.Button(self,
                            text="Registrar",
                            width= 10,
                            command=lambda: controller.show_frame("Registrar"))

        bt_registrar.pack(pady= 10)


class menu_principal(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        origin_path = os.path.abspath(os.getcwd())
        tkimage = ImageTk.PhotoImage(Image.open(origin_path + "\\images\\valefarma.png").resize([200, 100]))
        label = tk.Label(self, image=tkimage)
        label.image = tkimage
        label.pack(side = "top", pady= 30)

        vendas_button = tk.Button(self, text="VENDAS", width= 100, height= 3)
        vendas_button.pack(side = "top", padx= 20, pady= 5)

        clientes_button = tk.Button(self, text="CLIENTES", width= 100, height= 3)
        clientes_button.pack(side = "top", padx= 20, pady= 5)

        produtos_button = tk.Button(self, text="PRODUTOS", width= 100, height= 3)
        produtos_button.pack(side = "top", padx= 20, pady= 5)




class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class menu:
	def __init__(self, master):
            menubar = tk.Menu(master)
            filemenu = tk.Menu(menubar, tearoff=0)
            filemenu.add_command(label="Sair", command=master.quit)
            sobremenu = tk.Menu(menubar, tearoff = 0)
            sobremenu.add_command(label = "Sobre o aplicativo")
            menubar.add_cascade(label="Arquivo", menu=filemenu)
            menubar.add_cascade(label = "Sobre", menu= sobremenu)
            master.config(menu=menubar)



if __name__ == "__main__":
    app = App()
    app.mainloop()

