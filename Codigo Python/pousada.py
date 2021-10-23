import os

from mysql.connector import cursor

import banco_dados

conexao = banco_dados.conecta_bd()
cursor = conexao.cursor()


def menu(conexao=cursor):
    os.system('cls')
    op = ''
    print('='*35)
    print('       SISTEMA DE RESERVA')
    print('='*35)
    print()
    while op != '7':  # Sai quando a op é 5
        print('    ESCOLHA A OPÇÃO DESEJADA:')
        print('=' * 35)
        print('    1 - CADASTRO DE CLIENTE')
        print('    2 - CADASTRO DE QUARTO')
        print('    3 - EXCLUIR CLIENTE')
        print('    4 - EXCLUIR QUARTO')
        print('    5 - RESERVA')
        print('    6 - Relatório')
        print('    7 - Sair')
        op = input('Opção: ')
        if op == '1':
            os.system('cls')
            print('='*19)
            print('CADASTRA CLIENTE')
            print('='*10)

            nome = input('Nome: ')
            cpf = input('CPF: ')
            telefone = input('Telefone: ')

            banco_dados.cadastra_cliente(cursor, nome, cpf, telefone)
            conexao.commit()  # se não executar commit as alterações não são salvas
            os.system('cls')
            print(f'Usuário {nome} cadastrado com sucesso!')
        elif op == '2':
            # CADASTRA QUARTO()
            print('CADASTRA QUARTO()')
            os.system('cls')
            acomodacao = input('Acomodação:')
            tipo = input('Tipo:')
            numero = input('Número:')
            status = input('Status:')

            print(f'Cadastro Quarto({acomodacao}, {tipo}, {numero},{status}')
            os.system('cls')
            print(f'Quarto {numero} Cadstrado com Sucesso!')
        elif op == '3':
            # EXCLUIR CLIENTE ()
            print('CLIENTE EXCLUIDO()')
        elif op == '4':
            # EXCLUIR QUARTO()
            print('QUARTO EXCLUIDO()')
        elif op == '5':
            # RESERVA()
            print('RESERVA()')
        elif op == '4':
            os.system('cls')
            banco_dados.consulta_cliente(cursor)
            print('-'*50)
            input('Aperte Enter para voltar: ')
            os.system('cls')

        elif op == '7':
            os.system('cls')
            cursor.close()
            conexao.close()
            print('Obrigado!')
            print('Volte Sempre!')
        else:
            os.system('cls')
            print('Opção Inválida!')
            print('Por favor')

    print('Fim do Progama!')

    return None

# menu()
