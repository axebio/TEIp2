from tkinter import *
import psycopg2
import os

origin_path = os.path.abspath(os.getcwd())

print()


tela_login = Tk()

tela_login.title("ValeFarma")
tela_login.iconbitmap(origin_path + "\\images\\diamante.ico")
tela_login.geometry("300x500+200+200")
tela_login.resizable(True, True)
altura_app = 300
largura_app = 500
tela_login.minsize(altura_app, largura_app)
tela_login['bg'] = "blue"

#botao entrar
btn = Button(tela_login, text = "login")
btn.pack()

# botao registrar
btn = Button(tela_login, text = "login")
btn.pack()

#Largura da tela

largura_tela = tela_login.winfo_screenwidth()

altura_tela = tela_login.winfo_screenheight()

#posicao do app

# posicao_app = largura_tela / 2 - largu

print(largura_tela, altura_tela)

# tela_login.iconbitmap("x")

tela_login.state("iconic")

tela_login.mainloop()
