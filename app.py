# import os
# from flask import Flask, request

# app = Flask(__name__)

# @app.route("/", methods = ["GET"])


# def hello():
#         return "testando a primeira rota"
# @app.route("/teste", methods = ["GET"])


# def teste():
#     return "Testando a segunda rota"

# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 5000))
#     app.run(host='0.0.0.0', port= port)
    


import psycopg2



def acesso():
    try:
        connection = psycopg2.connect(
            host = "ec2-52-45-179-101.compute-1.amazonaws.com",
            database = "dfteps5p12sa4o",
            user = "wtzpfamewvjhdo",
            password = "96baea9a68a850dde879d7133b9e648620b8521adb6910870391b15e40da7b8c",
            port = "5432",
        )
        return connection
    except Exception as erro:
        print (erro)
    

def cria_tabela(sql):
    connection = acesso()
    cur = connection.cursor()
    
    try:
        #cria a tabela se não existir
        cur.execute(sql) #"CREATE TABLE IF NOT EXISTS tb_usuario (usuario VARCHAR, senha VARCHAR)"

    except Exception as erro:
        print(erro)

    connection.commit()
    connection.close()


def clear():
    print("")
	# x1.delete(0, END)
	# x2.delete(0, END)

def submit():
	# Configure and connect to Postgres
    connection = acesso()

	# Create a cursor
    cur = connection.cursor()
    try:
	# Insert data into table
        thing1 = 0
        thing2 = 0
        cur.execute('''INSERT INTO customers (first_name, last_name) VALUES (%s, %s)''', (thing1, thing2))
    except Exception as erro:
        print(erro)

	cur.commit()	
	cur.close()
		
	atualizar()
	clear()

def atualizar():
    connection = acesso()

    cur = connection.cursor()

    #baixar valores do banco de dados

    cur.execute("SELECT * FROM tb_usuario")
    records = cur.fetchall()

    output = ''

    # for record in records:
    #     output_label.config(text=f'{output}\n{record[0]} {record[1]}')
    #     output = output_label['text']



