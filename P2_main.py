from tkinter import *
import psycopg2
import os

#stormy-depths-55799

origin_path = os.path.abspath(os.getcwd())

tela_login = Tk()

tela_login.title("ValeFarma")
tela_login.iconbitmap(origin_path + "\\images\\diamante.ico")
tela_login.geometry("300x500+200+200")
tela_login.resizable(True, True)
altura_app = 300
largura_app = 500
tela_login.minsize(altura_app, largura_app)
tela_login['bg'] = "gray"

def clear():
	f_name.delete(0, END)
	l_name.delete(0, END)

#configurando o postgres
def query():
    connection = psycopg2.connect(
        host = "ec2-52-45-179-101.compute-1.amazonaws.com",
        database = "dfteps5p12sa4o",
        user = "wtzpfamewvjhdo",
        password = "96baea9a68a850dde879d7133b9e648620b8521adb6910870391b15e40da7b8c",
        port = "5432",
    )

    conn = connection.cursor()

#criando a tabela
    conn.execute("CREATE TABLE IF NOT EXISTS tb_usuario (usuario VARCHAR, senha VARCHAR)")

    connection.commit()
    connection.close()

def submit():
	# Configure and connect to Postgres
	conn = psycopg2.connect(
		host = "ec2-18-211-41-246.compute-1.amazonaws.com", 
		database = "dalilo11l7p24t",
		user = "ikyumnardmfjok",
		password = "52d3b09a2480693c2649d8c8a6b10514ec9798d08126844f16a06342480e215b", 
		port = "5432",
		)

	# Create a cursor
	c = conn.cursor()

	# Insert data into table
	thing1 = f_name.get()
	thing2 = l_name.get()
	c.execute('''INSERT INTO customers (first_name, last_name)
		VALUES (%s, %s)''', (thing1, thing2)
		)
	
	conn.commit()	
	conn.close()
		
	update()
	clear()


def update():
    connection = psycopg2.connect(
        host = "ec2-52-45-179-101.compute-1.amazonaws.com",
        database = "dfteps5p12sa4o",
        user = "wtzpfamewvjhdo",
        password = "96baea9a68a850dde879d7133b9e648620b8521adb6910870391b15e40da7b8c",
        port = "5432",
    )

    conn = connection.cursor()

    #baixar valores do banco de dados

    conn.execute("SELECT * FROM tb_usuario")
    records = conn.fetchall()

    output = ''

    for record in records:
        output_label.config(text=f'{output}\n{record[0]} {record[1]}')
        output = output_label['text']




# Create The GUI For The App
my_frame = LabelFrame(tela_login, text="Postgres Example")
my_frame.pack(pady=20)

f_label = Label(my_frame, text="First Name:")
f_label.grid(row=0, column=0, pady=10, padx=10)

f_name = Entry(my_frame, font=("Helvetica, 18"))
f_name.grid(row=0, column=1, pady=10, padx=10)

l_label = Label(my_frame, text="Last Name:")
l_label.grid(row=1, column=0, pady=10, padx=10)

l_name = Entry(my_frame, font=("Helvetica, 18"))
l_name.grid(row=1, column=1, pady=10, padx=10)

submit_button = Button(my_frame, text="Submit", command=submit)
submit_button.grid(row=2, column=0, pady=10, padx=10)

update_button = Button(my_frame, text="Update", command=update)
update_button.grid(row=2, column=1, pady=10, padx=10)

output_label = Label(tela_login, text="")
output_label.pack(pady=50)


# #botao entrar
# btn = Button(tela_login, text = "login")
# btn.pack()

# # botao registrar
# btn = Button(tela_login, text = "login")
# btn.pack()

# #Largura da tela

# largura_tela = tela_login.winfo_screenwidth()

# altura_tela = tela_login.winfo_screenheight()

# #posicao do app

# # posicao_app = largura_tela / 2 - largu

# print(largura_tela, altura_tela)

# # tela_login.iconbitmap("x")

# tela_login.state("iconic")

query()

tela_login.mainloop()


