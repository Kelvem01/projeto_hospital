import hashlib

# realizar criptografia de senha teste**
def cadastrar_usuario(conn):
    cursor = conn.cursor()
    comando = f"""INSERT INTO Usuario (nivel, nome, email, senha) VALUES (?,?,?,?)"""
    nivel = input("Digite o nível de acesso: ")  # 1) básico, 2) parcial, 3) completo
    nome = input("Digite o seu nome: ")
    email = input("Digite o seu email: ")

    while True:
        senha = input("Digite a sua senha: ")
        con_senha = input('Confirme sua senha: ')
        if con_senha == senha:
            senha_hash = hashlib.sha256(senha.encode()).hexdigest()  # Criptografa a senha usando SHA256
            print('Cadastro realizado com sucesso!')
            break
        else:
            print('Senha inválida!')

    values = [nivel, nome, email, senha_hash]
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

def exemplo_joins(conn):
	print("------------ Dados Recuperados ------------")
	cursor = conn.cursor()
	#comando = f"""
	#	SELECT Faturamento.id, Cliente.id, Cliente.nome
	#	FROM Faturamento
	#	INNER JOIN Cliente ON Faturamento.id = Cliente.id;
	#"""

	#comando = f"""
	#	SELECT Faturamento.id, Procedimento.id, Procedimento.tipo
	#	FROM Faturamento
	#	INNER JOIN Procedimento ON Faturamento.id = Procedimento.id;
	#"""

	comando = f"""
		SELECT Faturamento.cliente_id, Faturamento.procedimento_id, Cliente.id, Cliente.nome, Procedimento.id, Procedimento.tipo
		FROM Faturamento
		INNER JOIN Cliente
			ON Faturamento.cliente_id = Cliente.id
		INNER JOIN Procedimento
			ON Faturamento.procedimento_id = Procedimento.id;
	"""

	cursor.execute(comando)
	dados = cursor.fetchall()
	for dado in dados:
		#print(dado) #Mostra a tupla recuperada do BD
		print(f"""Cliente: {dado[3]} | Procedimento: {dado[5]}""")

def contabiliza_pagamento(conn):
	print("------------ Dados Recuperados ------------")
	cursor = conn.cursor()
	comando = """SELECT * FROM MateriaisEquipamentos"""
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

def retirada_de_materias_equipamentos(conn, id, quantidade):
	cursor = conn.cursor()
	listar_dados(conn, "MateriaisEquipamentos")
	comando = f"""UPDATE MateriaisEquipamentos SET quantidade = quantidade - {quantidade} WHERE id = {id}"""
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

def faturamento(conn):
	cursor = conn.cursor()
	listar_dados(conn, "Cliente")
	cliente_id = int(input("Selecione o ID do Cliente: "))
	listar_dados(conn, "Procedimento")
	procedimento_id = int(input("Selecione o ID do Procedimento: "))
	qtdHorasSala = int(input("Selecione o tempo cirurgico(em minutos): "))
	valorAnestesista= float (input(' digite o valor da anestesia: '))
	comando = f"""INSERT INTO Faturamento (cliente_id, procedimento_id, qtdHorasSala, valorAnestesista) VALUES (?,?,?,?)"""
	valores = [cliente_id, procedimento_id, qtdHorasSala, valorAnestesista]

	cursor.execute(comando,valores)
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
