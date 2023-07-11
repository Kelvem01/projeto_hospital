# Gestão Hospitalar

## Descrição
Este projeto de gestão hospitalar tem como objetivo facilitar a administração de um hospital, permitindo o gerenciamento eficiente de pacientes, médicos, consultas e registros médicos. O sistema é desenvolvido em Python e SQL, utilizando tecnologias como o Flask e o MySQL.

## Funcionalidades
O sistema de gestão hospitalar possui as seguintes funcionalidades principais:

- Cadastro e gerenciamento de pacientes, com informações pessoais, histórico médico e agendamento de consultas.
- Cadastro e gerenciamento de médicos, incluindo suas especialidades e horários de disponibilidade.
- Agendamento de consultas, considerando a disponibilidade dos médicos e dos pacientes.
- Registro e acesso a históricos médicos de pacientes, contendo informações sobre consultas, diagnósticos de cirurgia plastica.
- Geração de relatórios estatísticos sobre o fluxo de pacientes, número de consultas realizadas, entre outros.

## Tecnologias utilizadas
O projeto é desenvolvido utilizando as seguintes tecnologias:

- Python: Linguagem de programação utilizada para a lógica e funcionalidades do sistema.
- Flask: Framework web utilizado para criar o backend do sistema e fornecer APIs para interação com o frontend.
- SQL: Linguagem de consulta utilizada para manipulação e gerenciamento do banco de dados.
- MySQL: Sistema de gerenciamento de banco de dados relacional utilizado para armazenar as informações do sistema.
  
## Instalação e Execução
Siga as etapas abaixo para executar o projeto em sua máquina local:

1. Certifique-se de ter o Python 3 instalado corretamente: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Clone este repositório em sua máquina local.
3. Acesse o diretório do projeto e crie um ambiente virtual:
   ```
   $ python3 -m venv venv
   ```
4. Ative o ambiente virtual:
   - No Linux/Mac:
     ```
     $ source venv/bin/activate
     ```
   - No Windows:
     ```
     $ venv\Scripts\activate
     ```
5. Instale as dependências do projeto:
   ```
   $ pip install -r requirements.txt
   ```
6. Configuração do banco de dados:
   - Instale o MySQL e crie um banco de dados vazio.
   - No arquivo `config.py`, atualize as configurações do banco de dados com as informações do seu ambiente.
7. Execute as migrações do banco de dados para criar as tabelas necessárias:
   ```
   $ flask db upgrade
   ```
8. Inicie o servidor:
   ```
   $ flask run
   ```

## Contribuição
Contribuições para o aprimoramento deste projeto são bem-vindas. Se você quiser contribuir, siga estas etapas:

1. Faça um fork do repositório.
2. Crie um branch para a sua feature ou correção:
   ```
   $ git checkout -b feature/nova-feature
   ```
3. Faça as alterações desejadas e faça commit das mesmas:
   ```
   $ git commit -am 'Adiciona nova feature'
   ```
4. Envie as alterações para o repositório remoto:
   ```
   $ git push origin feature/nova-feature
   ```
5. Abra uma pull request no repositório original.

## Licença
Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).

## Contato
Para mais informações ou dúvidas sobre o projeto, entre em contato:

- Nome: Kelvem Ferreira 
- E-mail: kelvemdasilva16@gmail.com
