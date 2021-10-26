import pymysql.cursors
import getpass

#------------------------------------- CONECTAR NO BANCO (OK) --------------------------------

def conecta_bd():
    print('=' * 31)
    print('Conectando com o banco de dados')
    print('=' * 31)
    print('Por favor, preencha as informações a seguir:')

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

    print('Banco de Dados Conectado com Sucesso!')
    return conexao

#------------------------------------- 1 CASDASTRO CLIENTE (OK) ------------------------------

def cadastra_clientes(cursor, nome, cpf, telefone, endereco):
    comando = f'''
    INSERT INTO `db_pousada`.`clientes`(
        `nome`,
        `cpf`,
        `telefone`,
        `endereco`

    ) VALUES (
        "{nome}",
        {cpf},
        {telefone},
        "{endereco}"
    );
    '''
    print(comando)
    cursor.execute(comando)
    print('Cadastro executado com sucesso!')
    print(f'Cliente {nome} cadastrado!')
    # return None

#------------------------------------- 2 CASDASTRO QUARTOS (OK) ------------------------------

def cadastra_quarto(cursor, numQuarto,tipo, acomodacao, status_q, check_in, check_out):
    comando = f'''INSERT INTO `quartos`(`numQuarto`,
        `tipo`, `acomodacao`, `status_q`, `check_in`, `check_out`)
        VALUES (
        {numQuarto},
        "{tipo}",
        "{acomodacao}",
        "{status_q}",
        "{check_in}",
        "{check_out}"
    );
    '''
    cursor.execute(comando)
    print('Cadastro executado com sucesso!')
    print(f'Quarto {numQuarto} cadastrado!')
    # return None

#------------------------------------- 3 RESERVA CHECK-IN ------------------------------------

def reserva_check_in(cursor):
    comando = ''' SELECT * FROM reservas
    '''
    cursor.execute(comando)

#------------------------------------- 4 CONSULTA CLIENTES -----------------------------------

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
        print(f'CPF: ', {dic['cpf']})
        print(f'Telefone: ', {dic["telefone"]})

    return None
