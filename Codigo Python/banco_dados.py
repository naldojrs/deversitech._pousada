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


def cadastra_cliente(cursor, nome, cpf, telefone):
    comando = f'''
    INSERT INTO `pousada`.`cliente`(      # mudei de locadora para pousada
        `nome`,
        `cpf`,
        `telefone`
    ) VALUES (
        "{nome}",
        "{cpf}",
        "{telefone}"
    );
    '''

    cursor.execute(comando)
    print('Cadastro executado com sucesso!')
    print(f'Cliente {nome} cadastrado!')
    # return None


def consulta_cliente(cursor):
    comando = '''
    SELECT * FROM cliente
    '''

    cursor.execute(comando)

    resultado = cursor.fetchall()
    for dic in resultado:
        print('-' * 50)
        print('ID: ', dic['id'])
        print('Nome: ', dic['nome'])
        print(f"CPF: {dic['cpf']}")
        print(f'Telefone: {dic["telefone"]}')

    return None

# cadastro_quarto = ''                ajustes de ortografia
# cadastro_reserva = ''

# cursor.execute(cadastro_cliente)
# print('Cadastro executado com sucesso!')
# print(f'Cliente {nome} cadastrado!')
# conexao.commit()

# Deleção
# remocao_quarto =
# remocao_cliente =

# Consulta
# consulta_cliente = f'''
# SELECT *
# FROM cliente
# WHERE nome = "{nome}"
# ;
# '''
# print(consulta_cliente)

# cursor.execute(consulta_cliente)
# resultado = cursor.fetchall()

# print('Consulta executada com sucesso!')
# print('Resultado: ')
# print(resultado)