import pymysql.cursors
import getpass


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

    print('Banco de dados conectado com sucesso!')
    return conexao


def cadastra_cliente(cursor, nome, cpf, telefone, endereco):
    comando = f'''
    INSERT INTO `dbpousada`.`clientes`(
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


def cadastra_quartos(cursor, numero, tipo, acomodacao, status):
    comando = f'''INSERT INTO `quartos`(`numero`,
                                  `tipo`,
                                  `acomodacao`
                                  `status`
                                  )
                                  VALUES (
        {numero},
        "{tipo}",
        "{acomodacao}",
        "{status}"
    );
    '''
    cursor.execute(comando)
    print('Cadastro executado com sucesso!')
    print(f'Quarto {numero} cadastrado!')
    # return None


def reserva_check_in(cursor):
    comando = ''' SELECT * FROM reservas
    '''
    cursor.execute(comando)


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
        print(f"CPF: {dic['cpf']}")
        print(f'Telefone: {dic["telefone"]}')

    return None
