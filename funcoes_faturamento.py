from funcoes_hospital import *

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

#Calcula o valor total de um FATURAMENTO, dado o seu ID, somando os custos de SALA, ANESTESISTA e MATERIAIS.
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
	
	valor_sala = 0.0   #Deixar dinâmico no futuro
	valor_hora = 18.75 #Deixar dinâmico no futuro
	valor_anestesista = 0.0
	valor_procedimentos = 0.0
	for dado in dados_fatur_proced:
		print(dado)
		hora_minutos = dado[4]
		valor_sala += (hora_minutos/60) * valor_hora
		valor_atual_anestesista = dado[5]
		valor_anestesista += valor_atual_anestesista
		procedimento_id = dado[3]
		valor_procedimentos += contabiliza_procedimento(conn, procedimento_id) 
	print(f"Valor SALA a ser cobrado (TOTAL): R${valor_sala:.2f}")
	print(f"Valor ANESTESISTA a ser cobrado (TOTAL): R${valor_anestesista:.2f}")
	print(f"Valor PROCEDIMENTOS a ser cobrado (TOTAL): R${valor_procedimentos:.2f}")
	
	faturamento_total = valor_sala + valor_anestesista + valor_procedimentos
	print(f"Faturamento (TOTAL): R${faturamento_total:.2f}")
	
    #Atualiza o faturamento como PAGO (True)
	status = ""
	while status not in ["s", "n"]:
		status = input("Deseja definir o pagamento como efetuado? [S] Sim [N] Não: ").lower()
	if status == "s":
		realiza_pagamento_faturamento(conn, faturamento_id)

#Calcula o valor TOTAL de um PROCEDIMENTO, dado o seu ID
def contabiliza_procedimento(conn, procedimento_id):
	print("------------ Dados Recuperados ------------")
	cursor = conn.cursor()

	comando = f"""
		SELECT
			Procedimento.id,
			Procedimento.tipo,
			Procedimento.cliente_id,
			MateriaisEquipamentosProcedimento.Procedimento_id,
			MateriaisEquipamentosProcedimento.MateriaisEquipamentos_id,
			MateriaisEquipamentosProcedimento.qtd_utilizada,
			MateriaisEquipamentos.valor
    
		FROM MateriaisEquipamentosProcedimento
		INNER JOIN MateriaisEquipamentos
			ON MateriaisEquipamentosProcedimento.MateriaisEquipamentos_id = MateriaisEquipamentos.id
		INNER JOIN Procedimento
			ON MateriaisEquipamentosProcedimento.Procedimento_id = Procedimento.id
		WHERE Procedimento.id = {procedimento_id}
		ORDER BY Procedimento.id
	"""
	
	cursor.execute(comando)
	dados = cursor.fetchall()
	total_materiais = 0.0
	for dado in dados:
		print(dado)
		quantidade = dado[5]
		valor = dado[6]
		total_materiais += quantidade * valor
	return total_materiais

#Atualiza o faturamento como PAGO (True)
def realiza_pagamento_faturamento(conn, faturamento_id):
    cursor = conn.cursor()

    comando = f"""
        UPDATE Faturamento
        SET status_pagamento = True
        WHERE id = {faturamento_id};
	"""
	
    cursor.execute(comando)
    conn.commit()