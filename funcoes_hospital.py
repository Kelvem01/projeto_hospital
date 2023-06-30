import hashlib 

def cadastrar_usuario(conn):
	cursor = conn.cursor()
	comando = f"""INSERT INTO Usuario (nivel, nome, email, senha) VALUES (?,?,?,?)"""
	nivel = input("Digite o nivel de acesso: ") #1)basico, 2)parcial, 3)completo
	nome  = input("Digite o seu nome: ")
	email = input("Digite o seu email: ")
	
	while True:
		senha = input("Digite a sua senha: ")
		con_senha = input('confirme sua senha :')
		if con_senha == senha:
			print('cadastro realizado com sucesso!')
			break
		else:
			print('senha invalida!')

	values = [nivel, nome, email, senha]
	cursor.execute(comando, values)
	conn.commit()

def cadastrar_cliente(conn):
	cursor = conn.cursor()
	comando = f"""INSERT INTO Cliente (nome, telefone, email, cpf, rg, profissao) VALUES (?,?,?,?,?,?)"""
	nome  = input("Digite o seu nome: ")
	telefone  = input("Digite o seu telefone: ")
	email = input("Digite o seu email: ")
	cpf = input("Digite o seu CPF: ")
	rg = input("Digite o seu RG: ")
	profissao = input("Digite a sua profissao: ")
	values = [nome, telefone, email, cpf, rg, profissao]

	print('Cadastrado realizado com sucesso!  ')
	cursor.execute(comando, values)
	conn.commit()

def cadastrar_medico(conn, tabela):
	cursor = conn.cursor()
	comando = f"""INSERT INTO {tabela} (nome, cpf, email, crm, telefone) VALUES (?,?,?,?,?)"""
	nome  = input("Digite o seu nome: ")
	cpf = input("Digite o seu CPF: ")
	email = input("Digite o seu email: ")
	crm = input("Digite o seu CRM: ")
	telefone  = input("Digite o seu telefone: ")
	values = [nome, cpf, email, crm, telefone]
	print('Cadastrado realizado com sucesso!  ')
	cursor.execute(comando, values)
	conn.commit()

def listar_dados(conn, tabela):
	print("------------ Dados Recuperados ------------")
	cursor = conn.cursor()
	comando = f"""SELECT * FROM {tabela}"""
	cursor.execute(comando)
	dados = cursor.fetchall()
	for dado in dados:
		print(dado)

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

def atualizar_nome_de_materiais(conn): # feito uma nova função para atualizar nomes de materiais
    cursor = conn.cursor()
    listar_dados(conn, "MateriaisEquipamentos")
    id = int(input("Selecione o ID do material a ser atualizado: "))
    material = input("Digite o nome do material: ")
    comando = f"""UPDATE MateriaisEquipamentos SET tipo = '{material}' WHERE id = {id}"""
    print (f'Atualizado com sucesso! ') # adicionado para mostrar a atualização do nome 

    cursor.execute(comando)
    conn.commit()
