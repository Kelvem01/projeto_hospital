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
			print(f'Id:{dado[0]}\n Nome:{dado[2]}\n E-mail:{dado[3]} ')
   
def listar_dados_cirurgiao(conn, tabela):
	print("------------ Dados Recuperados ------------")
	cursor = conn.cursor()
	comando = f"""SELECT * FROM Cirurgiao"""
	cursor.execute(comando)
	dados = cursor.fetchall()
	for dado in dados:
    		print(f"""
            Cirurgião
            Id:{dado[0]}\n Nome:{dado[1]}\n Cpf:{dado[2]}\n CRM:{dado[3]}\n E-mail:{dado[4]}\n Telefone:{dado[5]}
            """)

def listar_dados_Anestesista(conn, tabela):
	print("------------ Dados Recuperados ------------")
	cursor = conn.cursor()
	comando = f"""SELECT * FROM Anestesista"""
	cursor.execute(comando)
	dados = cursor.fetchall()
	for dado in dados:
    		print(f"""
            Anestesista
            Id:{dado[0]}\n Nome:{dado[1]}\n CPF:{dado[2]}\n CRM:{dado[3]}\n E-mail:{dado[4]}\n Telefone:{dado[5]}
            """)
      
def listar_dados_procedimento(conn, tabela):
	print("------------ Dados Recuperados ------------")
	cursor = conn.cursor()
	comando = f"""
		SELECT 
		Cliente.id,
		Cliente.nome,
		Procedimento.id,
		Procedimento.tipo,
		Procedimento.cliente_id,
		Procedimento.status,
		Anestesista.id,
		Anestesista.nome,
		Anestesista.crm,
		Cirurgiao.id,
		Cirurgiao.nome,
		Cirurgiao.crm
	FROM Cliente
	INNER JOIN Procedimento
		ON Cliente.id = Procedimento.cliente_id
	INNER JOIN Anestesista
		ON Procedimento.anestesista_id = Anestesista.id
	INNER JOIN Cirurgiao
		ON Procedimento.Cirurgiao_id = Cirurgiao.id;
   		"""
	cursor.execute(comando)
	dados = cursor.fetchall()
	for dado in dados:
			print(f"""
         Status Cirurgico
         
         Id Paciente:{dado[0]}\n Nome:{dado[1]}\n Procedimento Cirurgico: {dado[3]}\n 
         Nome Anestesista:{dado[7]}  CRM:{dado[8]}
         Nome Cirurgiao: {dado[10]}	CRM:{dado[11]}
         Status Cirurgico:{dado[5]}
        """)

def listar_dados_materiais(conn, tabela):
	print("------------ Dados Recuperados ------------")
	cursor = conn.cursor()
	comando = f"""SELECT * FROM MateriaisEquipamentos"""
	cursor.execute(comando)
	dados = cursor.fetchall()
	for dado in dados:
			print(f"""
         Tabela Material
         Id:{dado[0]}
         Nome material:{dado[1]}
         Descrição do material:{dado[2]}
         Quantidade:{dado[3]}
         Valor:{dado[4]}
         """)
   
def listar_dados_Faturamento(conn, tabela):
	print("------------ Dados Recuperados ------------")
	cursor = conn.cursor()
	comando = f"""SELECT * FROM Faturamento"""
	cursor.execute(comando)
	dados = cursor.fetchall()
	for dado in dados:
			print(f'{dado}')