import pymysql.cursors
import getpass


def conecta_bd():
    print('=' * 35)
    print('  Conectando com o banco de dados')
    print('=' * 35)
    print('  Preencha as informações a seguir:')
    print('=' * 35)
    servidor = input('Servidor: ')
    usuario = input('Usuário: ')
    senha = getpass.getpass('Senha: ')
    banco = input('Banco: ')

    # Conexão com Banco de Dados
    conexao = pymysql.connect(
        host=servidor,  # ip ou o nome da maquina
        user=usuario,
        password=senha,
        database=banco,
        cursorclass=pymysql.cursors.DictCursor
    )

    print('Banco de dados conectado com sucesso!')
    return conexao

# Função Cadastrar clinetes


def cadastra_cliente(cursor, nome, CPF, telefone, endereco):
    comando = f'''
    INSERT INTO `bd_pousada`.`clientes`(
        `nome`,
        `CPF`,
        `telefone`,
        `endereco`

    ) VALUES (
        "{nome}",
        {CPF},
        {telefone},
        "{endereco}"
    );
    '''
    print(comando)
    cursor.execute(comando)
    print('Cadastro executado com sucesso!')
    print(f'Cliente {nome} cadastrado!')
    # return None

# Função Cadastrar Quartos


def cadastra_quarto(cursor, numQuarto, tipo, acomodacao, status_q):
    comando = f'''INSERT INTO `bd_pousada`.`quartos`(`numQuarto`,
                                  `tipo`,
                                  `acomodacao`,
                                  `status_q`
                                  )
                                  VALUES (
        {numQuarto},
        "{tipo}",
        "{acomodacao}",
        "{status_q}"
    );
    '''
    cursor.execute(comando)
    print('Cadastro executado com sucesso!')
    print(f'Quarto {numQuarto} cadastrado!')
    # return None

# Função Consultar clinetes


def consulta_clientes(cursor, nome):
    comando = f''' SELECT * FROM clientes where nome =  "{nome}"; '''

    cursor.execute(comando)
    print('Consulta executado com sucesso!')
    print(f'Cliente {nome}!')

    cursor.execute(comando)

    resultado = cursor.fetchall()
    for dic in resultado:
        print('-' * 50)
        print('ID: ', dic['id'])
        print('Nome: ', dic['nome'])
        print(f"CPF: {dic['CPF']}")
        print(f"Endereço: {dic['endereco']}")
        print(f'Telefone: {dic["telefone"]}')
        print(f"Status: {dic['status_c']}")

    return None

# Função Consultar quartos


def consulta_quarto(cursor, numQuarto):
    comando = f''' SELECT * FROM quartos where numQuarto =  {numQuarto}; '''

    cursor.execute(comando)
    print('Consulta executado com sucesso!')
    print(f'Quarto {numQuarto}!')

    cursor.execute(comando)

    resultado = cursor.fetchall()
    for dic in resultado:
        print('-' * 50)
        print('ID: ', dic['id'])
        print('Número: ', dic['numQuarto'])
        print(f"Tipo: {dic['tipo']}")
        print(f"Status: {dic['status_q']}")
        print(f'Check IN: {dic["check_in"]}')
        print(f"Check ON: {dic['check_on']}")

    return None

# Função Consultar reservas


def consultar_reserva(cursor, cliente_id):
    comando = f''' SELECT * FROM reservas where cliente_id = {cliente_id}; '''

    cursor.execute(comando)
    print('Consulta executado com sucesso!')
    print(f'Reserva {cliente_id}!')

    cursor.execute(comando)

    resultado = cursor.fetchall()
    for dic in resultado:
        print('-' * 50)
        print('ID: ', dic['id'])
        print('Cliente: ', dic['cliente_id'])
        print(f"Data: {dic['data']}")
        print(f"Status: {dic['status_r']}")

    return None

# Função excluir clinetes


def excluir_cliente(cursor, nome):
    comando = f''' DELETE FROM clientes where nome = "{nome}";'''

    cursor.execute(comando)
    print('Cliente excluido com sucesso!')
    print(f'Cliente {nome}!')

# Função excluir quartos


def excluir_quarto(cursor, numQuarto):
    comando = f''' DELETE FROM quartos where numQuarto = {numQuarto};'''

    cursor.execute(comando)
    print('Quarto excluido com sucesso!')
    print(f'Quarto {numQuarto}!')

# Função Check OUT Reservas


def reserva_check_out(cursor, numQuarto):
    comando = f''' SELECT * FROM reservas where numQuarto = {numQuarto};'''

    cursor.execute(comando)
    print('Consulta executado com sucesso!')
    print(f'Quarto {numQuarto}!')

# Função Check IN Reservas


def reserva_check_in(cursor, numQuarto):
    comando = f''' SELECT * FROM reservas where numQuarto = {numQuarto};'''

    cursor.execute(comando)
    print('Consulta executado com sucesso!')
    print(f'Quarto {numQuarto}!')

# Função relatório clientes


def relatorio_cliente(cursor):
    comando = ''' SELECT * FROM clientes ; '''

    cursor.execute(comando)
    print('Consulta executado com sucesso!')

    cursor.execute(comando)

    resultado = cursor.fetchall()
    for dic in resultado:
        print('-' * 50)
        print('ID: ', dic['id'])
        print('Nome: ', dic['nome'])
        print(f"CPF: {dic['CPF']}")
        print(f"Status: {dic['status_c']}")

    return None

# Função relatório quartos


def relatorio_quarto(cursor):
    comando = ''' SELECT * FROM quartos ; '''

    cursor.execute(comando)
    print('Consulta executado com sucesso!')

    cursor.execute(comando)

    resultado = cursor.fetchall()
    for dic in resultado:
        print('-' * 50)
        print('ID: ', dic['id'])
        print('Número: ', dic['numQuarto'])
        print(f"Tipo: {dic['tipo']}")
        print(f"Status: {dic['status_q']}")
        print(f'Check IN: {dic["check_in"]}')
        print(f"Check ON: {dic['check_on']}")

    return None
