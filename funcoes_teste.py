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
		SELECT Faturamento.cliente_id, Faturamento.procedimento_id, Faturamento.valorAnestesista,
		Cliente.id, Cliente.nome, Procedimento.id, Procedimento.tipo ,Procedimento.Status
		FROM Faturamento
		INNER JOIN Cliente
			ON Faturamento.cliente_id = Cliente.id
		INNER JOIN Procedimento
			ON Faturamento.procedimento_id = Procedimento.id;
	"""

	cursor.execute(comando)
	dados = cursor.fetchall()
	for dado in dados: # recuperando os dados em foma de nota 
		#print(dado) #Mostra a tupla recuperada do BD  #recuperando todas as informações 
		print(f""" Cliente id : {dado [0]} Cliente: {dado[4]}
		Id Procedimento:{dado[5]}:Procedimento:{dado[6]}  
		Valor Anestesista: {dado[2]} Starus Cirurgico: {dado[7]}
		""")

def exemplo_joins2(conn):
	print("------------ Dados Recuperados ------------")
	cursor = conn.cursor()

	#comando = f"""
	#	SELECT MateriaisEquipamentosProcedimento.MateriaisEquipamentos_id, MateriaisEquipamentosProcedimento.Procedimento_id, MateriaisEquipamentosProcedimento.qtd_utilizada, Procedimento.id, Procedimento.tipo, MateriaisEquipamentos.id, MateriaisEquipamentos.tipo
	#	FROM MateriaisEquipamentosProcedimento
	#	INNER JOIN Procedimento
	#		ON MateriaisEquipamentosProcedimento.Procedimento_id = Procedimento.id;
	#	"""

	comando = f"""
		SELECT
			MateriaisEquipamentosProcedimento.MateriaisEquipamentos_id,
			MateriaisEquipamentos.id,
			MateriaisEquipamentos.tipo,
			MateriaisEquipamentosProcedimento.qtd_utilizada,
			MateriaisEquipamentos.valor,
			MateriaisEquipamentosProcedimento.Procedimento_id,
			Procedimento.id,
			Procedimento.tipo,
			Procedimento.cliente_id

		FROM MateriaisEquipamentosProcedimento
		INNER JOIN MateriaisEquipamentos
			ON MateriaisEquipamentosProcedimento.MateriaisEquipamentos_id = MateriaisEquipamentos.id
		INNER JOIN Procedimento
			ON MateriaisEquipamentosProcedimento.Procedimento_id = Procedimento.id;
	"""

	cursor.execute(comando)
	dados = cursor.fetchall()
	for dado in dados:
		print(f""" Id Cliente: {dado[8]}
        Id material: {dado[1]} | Material: {dado[2]}
        Quantidade Utilizada: {dado[3]}
		Valor: {dado[4]}
		Id procedimento: {dado[6]} | Procedimento: {dado[7]}
    """) #Mostra a tupla recuperada do BD

#Calcula o valor TOTAL por MATERIAL em PROCEDIMENTOS cadastrados em momentos diferentes
def exemplo_joins3(conn):
	print("------------ Dados Recuperados ------------")
	cursor = conn.cursor()

	#comando = f"""
	#	SELECT MateriaisEquipamentosProcedimento.MateriaisEquipamentos_id, MateriaisEquipamentosProcedimento.Procedimento_id, MateriaisEquipamentosProcedimento.qtd_utilizada, Procedimento.id, Procedimento.tipo, MateriaisEquipamentos.id, MateriaisEquipamentos.tipo
	#	FROM MateriaisEquipamentosProcedimento
	#	INNER JOIN Procedimento
	#		ON MateriaisEquipamentosProcedimento.Procedimento_id = Procedimento.id;
	#	"""

	comando = f"""
		SELECT
			MateriaisEquipamentosProcedimento.MateriaisEquipamentos_id,
			MateriaisEquipamentos.id,
			MateriaisEquipamentos.tipo,
			MateriaisEquipamentosProcedimento.qtd_utilizada,
			MateriaisEquipamentos.valor,
			MateriaisEquipamentosProcedimento.Procedimento_id,
			Procedimento.id,
			Procedimento.tipo,
			Procedimento.cliente_id,
			MateriaisEquipamentosProcedimento.qtd_utilizada*MateriaisEquipamentos.valor

		FROM MateriaisEquipamentosProcedimento
		INNER JOIN MateriaisEquipamentos
			ON MateriaisEquipamentosProcedimento.MateriaisEquipamentos_id = MateriaisEquipamentos.id
		INNER JOIN Procedimento
			ON MateriaisEquipamentosProcedimento.Procedimento_id = Procedimento.id;
	"""

	cursor.execute(comando)
	dados = cursor.fetchall()
	for dado in dados:
		print(dado)
		#print(f""" Id Cliente: {dado[8]}
        #Id material: {dado[1]} | Material: {dado[2]}
        #Quantidade Utilizada: {dado[3]}
		#Valor: {dado[4]}
		#Id procedimento: {dado[6]} | Procedimento: {dado[7]}
    	#""") #Mostra a tupla recuperada do BD

#Calcula o valor TOTAL por PROCEDIMENTO
def exemplo_joins4(conn):
	print("------------ Dados Recuperados ------------")
	cursor = conn.cursor()

	#comando = f"""
	#	SELECT MateriaisEquipamentosProcedimento.MateriaisEquipamentos_id, MateriaisEquipamentosProcedimento.Procedimento_id, MateriaisEquipamentosProcedimento.qtd_utilizada, Procedimento.id, Procedimento.tipo, MateriaisEquipamentos.id, MateriaisEquipamentos.tipo
	#	FROM MateriaisEquipamentosProcedimento
	#	INNER JOIN Procedimento
	#		ON MateriaisEquipamentosProcedimento.Procedimento_id = Procedimento.id;
	#	"""

	comando = f"""
		SELECT
			MateriaisEquipamentosProcedimento.MateriaisEquipamentos_id,
			MateriaisEquipamentos.id,
			MateriaisEquipamentos.tipo,
			MateriaisEquipamentosProcedimento.qtd_utilizada,
			MateriaisEquipamentos.valor,
			MateriaisEquipamentosProcedimento.Procedimento_id,
			Procedimento.id,
			Procedimento.tipo,
			Procedimento.cliente_id,
			SUM(MateriaisEquipamentosProcedimento.qtd_utilizada*MateriaisEquipamentos.valor)

		FROM MateriaisEquipamentosProcedimento
		INNER JOIN MateriaisEquipamentos
			ON MateriaisEquipamentosProcedimento.MateriaisEquipamentos_id = MateriaisEquipamentos.id
		INNER JOIN Procedimento
			ON MateriaisEquipamentosProcedimento.Procedimento_id = Procedimento.id
		GROUP BY Procedimento.id;
	"""

	cursor.execute(comando)
	dados = cursor.fetchall()
	for dado in dados:
		print(dado)
		#print(f""" Id Cliente: {dado[8]}
        #Id material: {dado[1]} | Material: {dado[2]}
        #Quantidade Utilizada: {dado[3]}
		#Valor: {dado[4]}
		#Id procedimento: {dado[6]} | Procedimento: {dado[7]}
    	#""") #Mostra a tupla recuperada do BD

#Calcula o valor TOTAL por CLIENTE (TODOS OS PROCEDIMENTOS) | Obs.: É necessário melhorar a consulta para evitar pagamentos DUPLICADOS,
# mantendo apenas a contabilização de pagamentos NÃO EFETUADOS.
def exemplo_joins5(conn):
	print("------------ Dados Recuperados ------------")
	cursor = conn.cursor()

	#comando = f"""
	#	SELECT MateriaisEquipamentosProcedimento.MateriaisEquipamentos_id, MateriaisEquipamentosProcedimento.Procedimento_id, MateriaisEquipamentosProcedimento.qtd_utilizada, Procedimento.id, Procedimento.tipo, MateriaisEquipamentos.id, MateriaisEquipamentos.tipo
	#	FROM MateriaisEquipamentosProcedimento
	#	INNER JOIN Procedimento
	#		ON MateriaisEquipamentosProcedimento.Procedimento_id = Procedimento.id;
	#	"""

	comando = f"""
		SELECT
			MateriaisEquipamentosProcedimento.MateriaisEquipamentos_id,
			MateriaisEquipamentos.id,
			MateriaisEquipamentos.tipo,
			MateriaisEquipamentosProcedimento.qtd_utilizada,
			MateriaisEquipamentos.valor,
			MateriaisEquipamentosProcedimento.Procedimento_id,
			Procedimento.id,
			Procedimento.tipo,
			Procedimento.cliente_id,
			SUM(MateriaisEquipamentosProcedimento.qtd_utilizada*MateriaisEquipamentos.valor)

		FROM MateriaisEquipamentosProcedimento
		INNER JOIN MateriaisEquipamentos
			ON MateriaisEquipamentosProcedimento.MateriaisEquipamentos_id = MateriaisEquipamentos.id
		INNER JOIN Procedimento
			ON MateriaisEquipamentosProcedimento.Procedimento_id = Procedimento.id
		GROUP BY Procedimento.cliente_id;
	"""

	cursor.execute(comando)
	dados = cursor.fetchall()
	for dado in dados:
		print(dado)
		#print(f""" Id Cliente: {dado[8]}
        #Id material: {dado[1]} | Material: {dado[2]}
        #Quantidade Utilizada: {dado[3]}
		#Valor: {dado[4]}
		#Id procedimento: {dado[6]} | Procedimento: {dado[7]}
    	#""") #Mostra a tupla recuperada do BD