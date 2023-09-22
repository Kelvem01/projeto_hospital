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
		print(f"""
        #############################################################################
        | ID:{dado[0]}                                                              
        | Material:{dado[1]}             || Descrição do material:{dado[2]} 
        | Quantidade:{dado[3]}                                                
        | Valor:{dado[4]}                                                           
        #############################################################################
        """)

def faturamento(conn):
	cursor = conn.cursor()
	listar_dados(conn, "Cliente")
	cliente_id = int(input("Selecione o ID do Cliente: "))
	status_pagamento = False #Inicializa como "Não pago"
	comando = f"""INSERT INTO Faturamento (cliente_id, status_pagamento) VALUES (?,?)"""
	valores = [cliente_id, status_pagamento]
	cursor.execute(comando,valores)
	conn.commit()

def faturamento_procedimento(conn):
	cursor = conn.cursor()
	listar_dados(conn, "Faturamento")
	faturamento_id = int(input("Selecione o ID do Faturamento: "))
	listar_dados(conn, "Procedimento")
	procedimento_id = int(input("Selecione o ID do Procedimento: "))
	qtdHorasSala = int(input("Selecione o tempo cirurgico(em minutos): "))
	valorAnestesista = float (input('Digite o valor da anestesia: '))
	comando = f"""INSERT INTO FaturamentoProcedimento (faturamento_id, procedimento_id, qtdHorasSala, valorAnestesista) VALUES (?,?,?,?)"""
	valores = [faturamento_id, procedimento_id, qtdHorasSala, valorAnestesista]
	cursor.execute(comando,valores)
	conn.commit()

def contabiliza_faturamento(conn):
	cursor = conn.cursor()
	listar_dados(conn, "Faturamento")
	faturamento_id = int(input("Digite o id do Faturamento: "))

	comando = f"""
		SELECT
			Faturamento.id,
			Faturamento.cliente_id,
			FaturamentoProcedimento.faturamento_id,
			FaturamentoProcedimento.procedimento_id,
			FaturamentoProcedimento.qtdHorasSala,
			FaturamentoProcedimento.valorAnestesista
		FROM Faturamento
		INNER JOIN FaturamentoProcedimento
			ON Faturamento.id = FaturamentoProcedimento.faturamento_id
		WHERE Faturamento.id = {faturamento_id}
	"""
	cursor.execute(comando)
	dados_fatur_proced = cursor.fetchall()
	
	valor_sala = 0.0
	valor_hora = 18.75
	valor_anestesista = 0.0
	for dado in dados_fatur_proced:
		print(dado)
		hora_minutos = dado[4]
		valor_sala += (hora_minutos/60) * valor_hora
		valor_atual_anestesista = dado[5]
		valor_anestesista += valor_atual_anestesista
	print(f"Valor SALA a ser cobrado (TOTAL): R${valor_sala:.2f}")
	print(f"Valor ANESTESISTA a ser cobrado (TOTAL): R${valor_anestesista:.2f}")
	
	faturamento_total = valor_sala + valor_anestesista
	print(f"Faturamento (TOTAL): R${faturamento_total:.2f}")
	#Faltou somarmos o total de materiais
	#Faltou atualizarmos o faturamento como PAGO (True)
	#Podemos melhorar esta implementação usando SQL Puro