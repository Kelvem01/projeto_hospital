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

	#comando = f"""
	#	SELECT
	#		MateriaisEquipamentosProcedimento.MateriaisEquipamentos_id,
	#		MateriaisEquipamentosProcedimento.qtd_utilizada,
	#		MateriaisEquipamentos.valor,
	#		MateriaisEquipamentosProcedimento.Procedimento_id,
	#		Procedimento.id,
	#		Procedimento.tipo,
	#		Procedimento.cliente_id,
	#		SUM(MateriaisEquipamentosProcedimento.qtd_utilizada*MateriaisEquipamentos.valor)
    #
	#	FROM MateriaisEquipamentosProcedimento
	#	INNER JOIN MateriaisEquipamentos
	#		ON MateriaisEquipamentosProcedimento.MateriaisEquipamentos_id = MateriaisEquipamentos.id
	#	INNER JOIN Procedimento
	#		ON MateriaisEquipamentosProcedimento.Procedimento_id = Procedimento.id
	#	GROUP BY Procedimento.id;
	#"""
	#
	#cursor.execute(comando)  ## Realizar uma nova Checagem no sql para realizar a contabilidade do procedimento com os materiais,
	#dados = cursor.fetchall()
	#for dado in dados:
    #		print(f"""
     #       ID:{dado[0]} |Tipo Material:{dado[2]}
      ##      Quantidade Utilizada:{dado[3]}
       #     Valor Mateial : R$ {dado[4]}
        #    ID Procedimento:{dado[6]}| Procedimento :{dado[7]} | ID Clinte :{dado[8]} 
         #   Total:R$ {dado[9]}
         #   """)
		#print(dado)
		#print(f""" Id Cliente: {dado[8]}
        #Id material: {dado[1]} | Material: {dado[2]}
        #Quantidade Utilizada: {dado[3]}
		#Valor: {dado[4]}
		#Id procedimento: {dado[6]} | Procedimento: {dado[7]}
    	#""") #Mostra a tupla recuperada do BD
############################################################################## opção com o nome do cliente
	comando = """
    SELECT 
        Cliente.cliente_id,
        Cliente.nome AS nome_cliente,
        Procedimento.id AS id_procedimento,
        Procedimento.tipo AS tipo_procedimento,
        Cirurgiao.id AS id_cirurgiao,
        Cirurgiao.nome AS nome_cirurgiao,
        MateriaisEquipamentosProcedimento.Procedimento_id AS id_procedimento_material,
        SUM(MateriaisEquipamentosProcedimento.qtd_utilizada * MateriaisEquipamentos.valor) AS custo_total_material
    FROM Cliente
    INNER JOIN Procedimento ON Cliente.Procedimento_id = Procedimento.id
    INNER JOIN Cirurgiao ON Procedimento.Cirurgiao_id = Cirurgiao.id
    INNER JOIN MateriaisEquipamentosProcedimento ON Procedimento.id = MateriaisEquipamentosProcedimento.Procedimento_id
    INNER JOIN MateriaisEquipamentos ON MateriaisEquipamentosProcedimento.MateriaisEquipamentos_id = MateriaisEquipamentos.id
    GROUP BY Procedimento.id, Cliente.cliente_id, Cliente.nome, Procedimento.id, Procedimento.tipo, Cirurgiao.id, Cirurgiao.nome, MateriaisEquipamentosProcedimento.Procedimento_id;
"""

	
	cursor.execute(comando)  ## Realizar uma nova Checagem no sql para realizar a contabilidade do procedimento com os materiais,
	dados = cursor.fetchall()
	for dado in dados:
		print(dado)
     
    ###############################################################################################################
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
	
#Calcula o valor TOTAL por CLIENTE (TODOS OS PROCEDIMENTOS) | Obs.: Contabilizando pagamentos NÃO EFETUADOS apenas.
def exemplo_joins6(conn):
	print("------------ Dados Recuperados ------------")
	cursor = conn.cursor()

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
			SUM(MateriaisEquipamentosProcedimento.qtd_utilizada*MateriaisEquipamentos.valor),
			Faturamento.cliente_id,
			Faturamento.procedimento_id,
			Faturamento.qtdHorasSala,
			Faturamento.valorAnestesista,
			Faturamento.status_pagamento

		FROM MateriaisEquipamentosProcedimento
		INNER JOIN MateriaisEquipamentos
			ON MateriaisEquipamentosProcedimento.MateriaisEquipamentos_id = MateriaisEquipamentos.id
		INNER JOIN Procedimento
			ON MateriaisEquipamentosProcedimento.Procedimento_id = Procedimento.id
		INNER JOIN Faturamento
			ON Procedimento.cliente_id = Faturamento.cliente_id
		GROUP BY Faturamento.cliente_id;
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


def rodar_comandos_SQL(conn):
	cursor = conn.cursor()

	comando = f"""
	UPDATE MateriaisEquipamentosProcedimento
	SET qtd_utilizada = 7
	WHERE id = 2;
	"""

	#comando = f"""
	#SELECT * FROM Faturamento WHERE status_pagamento = FALSE;
	#"""
	
	cursor.execute(comando)
	
	#Listar dados quando houver um SELECT
	#dados = cursor.fetchall()
	#for dado in dados:
	#	print(dado)

	conn.commit()




#Calcula o valor TOTAL por PROCEDIMENTO
def exemplo_joins7(conn):
	print("------------ Dados Recuperados ------------")
	cursor = conn.cursor()

	comando = f"""
		SELECT MateriaisEquipamentosProcedimento.MateriaisEquipamentos_id, MateriaisEquipamentosProcedimento.Procedimento_id, MateriaisEquipamentosProcedimento.qtd_utilizada, Procedimento.id, Procedimento.tipo, MateriaisEquipamentos.id, MateriaisEquipamentos.tipo
		FROM MateriaisEquipamentosProcedimento
		INNER JOIN Procedimento
			ON MateriaisEquipamentosProcedimento.Procedimento_id = Procedimento.id;
		"""

	comando = f"""
		SELECT
			MateriaisEquipamentosProcedimento.MateriaisEquipamentos_id,
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
			ON MateriaisEquipamentosProcedimento.Procedimento_id = Procedimento.id
		WHERE Procedimento.cliente_id = {1}
	"""
	
	cursor.execute(comando)  ## Realizar uma nova Checagem no sql para realizar a contabilidade do procedimento com os materiais,
	dados = cursor.fetchall()
	for dado in dados:
		print(dado)