from funcoes_hospital import *

def cadastrar_procedimento(conn):
	cursor = conn.cursor()
	comando = f"""INSERT INTO Procedimento (tipo, cliente_id, cirurgiao_id, anestesista_id, sala, status) VALUES (?,?,?,?,?,?)"""	
	tipo  = input("Descreva o tipo de procedimento: ")

	#Listar os clientes e seus IDs
	listar_dados(conn, "Cliente")
	cliente_id = int(input("Selecione o cliente: "))

	#Listar os cirurgioes e seus IDs
	listar_dados(conn, "Cirurgiao")
	cirurgiao_id = int(input("Selecione o cirurgiao: "))

	#Listar os anestesistas e seus IDs
	listar_dados(conn, "Anestesista")
	anestesista_id = int(input("Selecione o anestesista: "))

	sala  = int(input("Digite a sala: "))
	values = [tipo, cliente_id, cirurgiao_id, anestesista_id, sala, "Agendado"]
	cursor.execute(comando, values)
	conn.commit()

def desmarcar_procedimento(conn):
	cursor = conn.cursor()
	listar_dados(conn, "Procedimento")
	id = int(input("Selecione o ID do procedimento a ser desmarcado: "))
	comando = f"""UPDATE Procedimento SET status = "Cancelado" WHERE id = {id};"""	
	cursor.execute(comando)
	conn.commit()