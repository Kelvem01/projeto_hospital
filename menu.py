from cadastro import *

import sqlite3
conexao = sqlite3.connect("gestaoHospitalar.sqlite3")

#Oi do Sherlon

while True:
	print("---- Gestão Hospitalar ----")
	print("O que você deseja fazer?")
	print("1) Cadastro de Usuários")
	print("2) Procedimentos")
	print("3) Cadastar Materiais e Equipamentos")
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
		print("Opções: 1) Cadastrar, 2) Listar, 3) Desmarcar")
		tipo_procedimento = int(input("Digite o a operação desejada: "))
		if tipo_procedimento == 1:
			cadastrar_procedimento(conexao)
		elif tipo_procedimento == 2:
			listar_dados(conexao, "Procedimento")
		elif tipo_procedimento == 3:
			desmarcar_procedimento(conexao)
		else:
			print("Opção inválida!")
	elif opcao == 3:
		print("Opções: 1) Cadastrar, 2) Listar, 3) Atualizar estoque ")
		tipo_procedimento = int(input("Digite o a operação desejada: "))
		if tipo_procedimento == 1:
			cadastrar_materiais_equipamentos(conexao)
		elif tipo_procedimento == 2:
			listar_dados(conexao, "MateriaisEquipamentos")
		elif tipo_procedimento == 3:
			atualizar_materias_equipamentos(conexao)
		else:
			print("Opção inválida!")
		
	else:
		print("Opção inválida!")

conexao.commit()
conexao.close()