CREATE TABLE Usuario (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nivel VARCHAR(30),
	nome  VARCHAR(100),
	email VARCHAR (30),
	senha VARCHAR (50)
);

CREATE TABLE Cliente (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nome VARCHAR (100),
	telefone VARCHAR (15),
	email VARCHAR (30),
	cpf VARCHAR (15),
	rg  VARCHAR (15),
	profissao VARCHAR (50)
);

CREATE TABLE Cirurgiao (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nome VARCHAR (100),
	cpf VARCHAR (15),
	crm VARCHAR (10),
	email VARCHAR (30),
	telefone VARCHAR (15)
);

CREATE TABLE Anestesista (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nome VARCHAR (100),
	cpf VARCHAR (15),
	crm VARCHAR (10),
	email VARCHAR (30),
	telefone VARCHAR (15)
);

CREATE TABLE MateriaisEquipamentos (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	tipo VARCHAR (20),
	descricao VARCHAR (300),
	quantidade INT,
	valor DECIMAL
);

CREATE TABLE Procedimento (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	tipo VARCHAR(50),
	cliente_id INT NOT NULL,
	cirurgiao_id INT NOT NULL,
	anestesista_id INT NOT NULL,
	sala INT,
	
	FOREIGN KEY (cliente_id) REFERENCES Cliente(id),
	FOREIGN KEY (cirurgiao_id)  REFERENCES Cirurgiao(id),
	FOREIGN KEY (anestesista_id)  REFERENCES Anestesista(id)
);

CREATE TABLE MateriaisEquipamentosProcedimento (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	MateriaisEquipamentos_id INT,
	Procedimento_id INT,

	FOREIGN KEY (MateriaisEquipamentos_id) REFERENCES MateriaisEquipamentos(id),
	FOREIGN KEY (Procedimento_id) REFERENCES Procedimento(id)
);

CREATE TABLE Faturamento (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	cliente_id INT NOT NULL,
	procedimento_id INT NOT NULL,
	qtdHorasSala INT,
	valorAnestesista DECIMAL,
	FOREIGN KEY (cliente_id) REFERENCES Cliente(id),
	FOREIGN KEY (procedimento_id) REFERENCES Procedimento(id)
);

#EXTRA Tabela Procedimentos
#EXTRA Tabela Profissões
#EXTRA Tabela Salas