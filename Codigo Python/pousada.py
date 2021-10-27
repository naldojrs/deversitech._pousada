import os

import banco_dados

conexao = banco_dados.conecta_bd()
cursor = conexao.cursor()

# MENU


def menu():
    os.system('cls')
    op = ''
    print('='*35)
    print('       SISTEMA DE RESERVA')
    print('='*35)
    print()
    while op != '12':  # Sai quando a op é 5
        print('       TESTES DAS DEF_S:')
        print('=' * 35)
        print('    1  - CADASTRO DE CLIENTE')
        print('    2  - CADASTRO DE QUARTO')
        print('    3  - CONSULTAR CLIENTE')
        print('    4  - CONSULTAR QUARTO')
        print('    5  - CONSULTAR RESERVA')
        print('    6  - EXCLUIR CLIENTE')
        print('    7  - EXCLUIR QUARTO')
        print('    8  - RESERVA - CHECK_OUT')
        print('    9  - RESERVA - CHECK_IN')
        print('    10 - RELATÓRIO CLIENTES')
        print('    11 - RELATÓRIO QUARTOS')
        print('    12 - SAIR')

        op = input('Opção: ')
        if op == '1':
            # CADASTRA CLIENTE()
            os.system('cls')
            print('='*19)
            print('CADASTRA CLIENTE')
            print('='*19)

            nome = input('Nome: ')
            CPF = input('CPF: ')
            telefone = input('Telefone: ')
            endereco = input('Endereço: ')

            banco_dados.cadastra_cliente(cursor, nome, CPF, telefone, endereco)
            print(type(conexao))
            conexao.commit()  # se não exe commit as alterações não são salva
            os.system('cls')
            print('-'*50)
            print(f'Usuário {nome} cadastrado com sucesso!')
            print('-'*50)
            input('Aperte Enter para voltar: ')

        elif op == '2':
            # CADASTRA QUARTO()
            os.system('cls')
            print('='*19)
            print('CADASTRA QUARTO')
            print('='*19)
            acomodacao = input('Acomodação: ')
            tipo = input('Tipo: ')
            numQuarto = input('Número: ')
            status_q = input('Status: ')
            banco_dados.cadastra_quarto(
                cursor, numQuarto, tipo, acomodacao, status_q)
            print(type(conexao))
            conexao.commit()
            os.system('cls')
            print('-'*50)
            print(f'Quarto {numQuarto} Cadstrado com Sucesso!')
            print('-'*50)
            input('Aperte Enter para voltar: ')
            os.system('cls')

        elif op == '3':
            # CONSULTA CLIENTES()
            os.system('cls')
            print('='*19)
            print('CONSULTA CLIENTES')
            print('='*19)
            nome = input('Nome: ')

            banco_dados.consulta_clientes(cursor, nome)
            print('-'*50)
            input('Aperte Enter para voltar: ')
            os.system('cls')

        elif op == '4':
            # CONSULTA QUARTO()
            os.system('cls')
            print('='*19)
            print('CONSULTA QUARTO')
            print('='*19)

            numQuarto = input('Número: ')
            banco_dados.consulta_quarto(cursor, numQuarto)
            os.system('cls')
            print('-'*50)
            input('Aperte Enter para voltar: ')
            print('-'*50)
            os.system('cls')

        elif op == '5':
            # CONSULTA RESERVA()
            os.system('cls')
            print('='*19)
            print('CONSULTA RESERVA')
            print('='*19)
            cliente_id = input('Nome: ')
            banco_dados.consultar_reserva(cursor, cliente_id)
            cliente_id = input('CÓDIGO: ')
            print(f'RESERVA {cliente_id}')

        elif op == '6':
            # EXCLUIR CLIENTE()
            os.system('cls')
            print('='*19)
            print('EXCLUIR CLIENTE')
            print('='*19)
            nome = input('NOME DO CLIENTE:')
            banco_dados.excluir_cliente(cursor, nome)
            conexao.commit()
            print(f'Cliente {nome} excluido com sucesso!')
            os.system('cls')
            print('-'*50)
            input('Aperte Enter para voltar: ')
            print('-'*50)
            os.system('cls')

        elif op == '7':
            # EXCLUIR QUARTO()
            os.system('cls')
            print('='*19)
            print('EXCLUIR QUARTO')
            print('='*19)
            numQuarto = input('NUMERO DO QUARTO: ')
            banco_dados.excluir_quarto(cursor, numQuarto)
            conexao.commit()
            os.system('cls')
            print('-'*50)
            input('Aperte Enter para voltar: ')
            print('-'*50)
            os.system('cls')

        elif op == '8':
            # RESERVA - CHECK OUT()
            os.system('cls')
            print('='*19)
            print('CHECK OUT - RESERVA')
            print('='*19)
            numero = input('NUMERO DO QUARTO: ')
            print(f'Quarto {numero} Check Out com sucesso!')

        elif op == '9':
            # RESERVA - CHECK_IN ()
            os.system('cls')
            print('='*19)
            print('RESERVA - CHECK_IN')
            print('='*19)
            numQuarto = input('Número do Quarto: ')

            banco_dados.reserva_check_in(cursor, numQuarto)
            print('-'*50)
            input('Aperte Enter para voltar: ')
            os.system('cls')

        elif op == '10':
            # RELAToRIO CLIENTES()
            os.system('cls')
            print('='*19)
            print('Relatório Clientes')
            print('='*19)
            banco_dados.relatorio_cliente(cursor)
            print('-'*50)
            print('Relatório emitido com sucesso!')
            print('-'*50)
            input('Aperte Enter para voltar: ')
            print('-'*50)
            os.system('cls')

        elif op == '11':
            # RELAToRIO QUARTOS()
            os.system('cls')
            print('='*19)
            print('Relatório Quartos')
            print('='*19)
            banco_dados.relatorio_quarto(cursor)
            print('-'*50)
            print('Relatório emitido com sucesso!')
            print('-'*50)
            input('Aperte Enter para voltar: ')
            print('-'*50)
            os.system('cls')

        elif op == '12':
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

    return
