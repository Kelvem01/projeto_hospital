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

def contabiliza_pagamento(conn):
	print("------------ Dados Recuperados ------------")
	cursor = conn.cursor()
	comando = """SELECT * FROM MateriaisEquipamentos"""
	cursor.execute(comando)
	dados = cursor.fetchall()
	for dado in dados:
		print(dado)

def faturamento(conn):
	cursor = conn.cursor()
	listar_dados(conn, "Cliente")
	cliente_id = int(input("Selecione o ID do Cliente: "))
	listar_dados(conn, "Procedimento")
	procedimento_id = int(input("Selecione o ID do Procedimento: "))
	qtdHorasSala = int(input("Selecione o tempo cirurgico(em minutos): "))
	valorAnestesista = float (input('Digite o valor da anestesia: '))
	status_pagamento = False #Inicializa como "Não pago"
	comando = f"""INSERT INTO Faturamento (cliente_id, procedimento_id, qtdHorasSala, valorAnestesista, status_pagamento) VALUES (?,?,?,?,?)"""
	valores = [cliente_id, procedimento_id, qtdHorasSala, valorAnestesista, status_pagamento]

	cursor.execute(comando,valores)
	conn.commit()