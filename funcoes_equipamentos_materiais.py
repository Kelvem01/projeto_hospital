from funcoes_hospital import *

def cadastrar_materiais_equipamentos(conn):
	cursor = conn.cursor()
	comando = f"""INSERT INTO MateriaisEquipamentos (tipo, descricao, quantidade , valor) VALUES (?,?,?,?)"""
	tipo = input("Digite o tipo do material: ")
	descricao = input("Digite a descricao do material: ")
	quantidade = int(input("Digite a quantidade : "))
	valor = float(input('Digite o valor: '))
	values = [tipo, descricao, quantidade , valor]
	cursor.execute(comando, values)
	print('Material cadastrado com sucesso!  ')
	conn.commit()

def  atualizar_materias_equipamentos(conn):
	cursor = conn.cursor()
	listar_dados(conn, "MateriaisEquipamentos")
	id = int(input("Selecione o ID do material a ser atualizado: "))
	quantidade = int(input("Digite a nova quantidade : "))
	comando = f"""UPDATE MateriaisEquipamentos SET quantidade = {quantidade} WHERE id = {id}"""
	print('Cadastrado de nova quantidade realizado com sucesso!  ')
	
	cursor.execute(comando)
	conn.commit()

def retirada_de_materias_equipamentos(conn, id, quantidade):
	cursor = conn.cursor()
	listar_dados(conn, "MateriaisEquipamentos")
	comando = f"""UPDATE MateriaisEquipamentos SET quantidade = quantidade - {quantidade} WHERE id = {id}"""
	print('Cadastro de nova quantidade realizado com sucesso!  ')
	
	cursor.execute(comando)
	conn.commit()

def atualizar_nome_de_materiais(conn): # feito uma nova função para atualizar nomes de materiais
    cursor = conn.cursor()
    listar_dados(conn, "MateriaisEquipamentos")
    id = int(input("Selecione o ID do material a ser atualizado: "))
    material = input("Digite o nome do material: ")
    comando = f"""UPDATE MateriaisEquipamentos SET tipo = '{material}' WHERE id = {id}"""
    print (' Atualizado com sucesso! ') # adicionado para mostrar a atualização do nome 

    cursor.execute(comando)
    conn.commit()

def MateriaisEquipamentosProcedimento(conn):
	cursor = conn.cursor()
	listar_dados(conn, "MateriaisEquipamentos")
	MateriaisEquipamentos_id = int(input("Selecione o ID do Material "))
	listar_dados(conn, "Procedimento")
	Procedimento_id = int(input("Selecione o ID do Procedimento: "))
	qtd_utilizada = int(input("Selecione a quantidade utilizada deste material: "))
	
	#Atualiza no estoque a quantidade de materiais retirada (já usada)
	#Futuro: validar se existe a quantidade utilizada no estoque
	retirada_de_materias_equipamentos(conn, MateriaisEquipamentos_id, qtd_utilizada)
	
	comando = f"""INSERT INTO MateriaisEquipamentosProcedimento (MateriaisEquipamentos_id, Procedimento_id, qtd_utilizada) VALUES (?,?,?)"""
	valores = [MateriaisEquipamentos_id, Procedimento_id, qtd_utilizada]
	cursor.execute(comando,valores)
	conn.commit()