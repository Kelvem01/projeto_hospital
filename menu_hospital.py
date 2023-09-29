from funcoes_hospital import *
from funcoes_teste import *
from funcoes_procedimento import *
from funcoes_equipamentos_materiais import *

import sqlite3
conexao = sqlite3.connect("gestaoHospitalar.sqlite3")

#Oi do Sherlon

while True:
	print("---- Gestão Hospitalar ----")
	print("O que você deseja fazer?")
	print("1) Cadastro de Usuários")
	print("2) Procedimentos")
	print("3) Cadastar Materiais e Equipamentos")
	print("4) Faturamento")
	print("5) Contabilizar pagamento")
	print("6) Listar Usuarios")
	print("7) Testes do sistema (Remover após o DEBUG)")
	print("0) Sair do Sistema")

	opcao = int(input("Digite a opcao desejada: "))
	if opcao == 0:
		print("Programa finalizado!")
		break
	elif opcao == 1:
		print("Opções: 1) Usuário, 2) Cliente, 3) Anestesista, 4) Cirurgiao")
		tipo_cadastro = int(input("Digite o tipo de cadastro: "))
		if tipo_cadastro == 1: #Cadastra um novo usuário no sistema
			cadastrar_usuario(conexao)
		elif tipo_cadastro == 2:
			cadastrar_cliente(conexao)
		elif tipo_cadastro == 3:
			cadastrar_medico(conexao, "Anestesista")
		elif tipo_cadastro == 4:
			cadastrar_medico(conexao, "Cirurgiao")
		else:
			print("Opção inválida!")
	elif opcao == 2:
		print("Opções: 1) Cadastrar, 2) Listar, 3) Desmarcar, 4) Registrar Materiais Utilizados")
		tipo_procedimento = int(input("Digite o a operação desejada: "))
		if tipo_procedimento == 1:
			cadastrar_procedimento(conexao)
		elif tipo_procedimento == 2:
			listar_dados(conexao, "Procedimento")
		elif tipo_procedimento == 3:
			desmarcar_procedimento(conexao)
		elif tipo_procedimento == 4:
			MateriaisEquipamentosProcedimento(conexao)
		else:
			print("Opção inválida!")
	elif opcao == 3:
		print("Opções: 1) Cadastrar, 2) Listar, 3) Atualizar estoque, 4) Atualizar tipo de Material")
		tipo_procedimento = int(input("Digite o a operação desejada: "))
		if tipo_procedimento == 1:
			cadastrar_materiais_equipamentos(conexao)
		elif tipo_procedimento == 2:
			listar_dados(conexao, "MateriaisEquipamentos")
		elif tipo_procedimento == 3:
			atualizar_materias_equipamentos(conexao)
		elif tipo_procedimento == 4:
			atualizar_nome_de_materiais(conexao)
		else:
			print("Opção inválida!")
	elif opcao == 4:
		print("Opções: 1) Criar Faturamento, 2) Cadastrar Procedimento, 3) Listar")
		tipo_procedimento = int(input("Digite o a operação desejada: "))
		if tipo_procedimento == 1:
			faturamento(conexao) #Cadastrar o faturamento			
		elif tipo_procedimento == 2:
			faturamento_procedimento(conexao) #Adiciona/relaciona o faturamento atual com os procedimentos realizados
		elif tipo_procedimento == 3:
			listar_dados(conexao, "Faturamento")
		else:
			print("Opção inválida!")
	elif opcao == 5:
		contabiliza_pagamento(conexao)
	elif opcao == 6:
		print("Opções: 1) Usuarios, 2) Clientes, 3) Cirurgiões, 4) Anestesistas")
		opcao = int(input("Digite o a operação desejada: "))
		if opcao == 1:
			listar_dados(conexao, "Usuario")
		elif opcao == 2:
			listar_dados(conexao, "Cliente")
		elif opcao == 3:
			listar_dados(conexao, "Cirurgiao")
		elif opcao == 4:
			listar_dados(conexao, "Anestesista")
		else:
			print("Opção inválida!")
	elif opcao == 7:
		#exemplo_joins(conexao)
		#exemplo_joins2(conexao)
		#exemplo_joins3(conexao)
		#exemplo_joins4(conexao) #VERIFICAR NA PRÓXIMA MONITORIA
		exemplo_joins7(conexao) #VERIFICAR NA PRÓXIMA MONITORIA
		#exemplo_joins5(conexao)
		#exemplo_joins6(conexao) #INCOMPLETO
		#rodar_comandos_SQL(conexao)

		#contabiliza_faturamento(conexao)
	else:
		print("Opção inválida!")

conexao.commit()
conexao.close()