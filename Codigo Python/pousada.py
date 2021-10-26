import os

import banco_dados

conexao = banco_dados.conecta_bd()
cursor = conexao.cursor()


def menu():
    os.system('cls')
    op = ''
    print('='*35)
    print('       SISTEMA DE RESERVA')
    print('='*35)
    print()
    while op != '11':  # Sai quando a op é 5
        print('       TESTES DAS DEF_S:')
        print('=' * 35)
        print('    1  - CADASTRO DE CLIENTE')
        print('    2  - CADASTRO DE QUARTO')
        print('    3  - RESERVA - CHECK_IN')
        print('    4  - CONSULTAR CLIENTE')
        print('    5  - CONSULTAR QUARTO')
        print('    6  - CONSULTAR RESERVA')
        print('    7  - EXCLUIR CLIENTE')
        print('    8  - EXCLUIR QUARTO')
        print('    9  - RESERVA - CHECK_OUT')
        print('    10 - RELATÓRIO')
        print('    11 - SAIR')
        op = input('Opção: ')
        if op == '1':
            # CADASTRA CLIENTE()
            os.system('cls')
            print('='*19)
            print('CADASTRA CLIENTE')
            print('='*19)

            nome = input('Nome: ')
            cpf = input('CPF: ')
            telefone = input('Telefone: ')
            endereco = input('Endereço')

            banco_dados.cadastra_cliente(cursor, nome, cpf, telefone, endereco)
            print(type(conexao))
            conexao.commit()  # se não exe commit as alterações não são salva
            os.system('cls')
            print(f'Usuário {nome} cadastrado com sucesso!')
        elif op == '2':
            # CADASTRA QUARTO()
            os.system('cls')
            print('='*19)
            print('CADASTRA QUARTO()')
            print('='*19)
            acomodacao = input('Acomodação: ')
            tipo = input('Tipo: ')
            numero = input('Número: ')
            status = input('Status: ')

            banco_dados.cadastra_quartos(
                cursor, numero, tipo, acomodacao, status)
            conexao.commit()
            os.system('cls')
            print(f'Quarto {numero} Cadstrado com Sucesso!')
        elif op == '3':
            # RESERVA - CHECK_IN ()
            os.system('cls')
            print('='*19)
            print('RESERVA - CHECK_IN()')
            print('='*19)

        elif op == '4':
            # CONSULTA CLIENTES()
            os.system('cls')
            print('CONSULTA CLIENTES()')
            nome = input('Nome: ')

            banco_dados.consulta_clientes(cursor, nome)
            print('-'*50)
            input('Aperte Enter para voltar: ')
            os.system('cls')
        elif op == '5':
            # CONSULTA QUARTO()
            print('CONSULTA QUARTO()')
            numero = input('Número:')

            print(f'QUARTO {numero}')
        elif op == '6':
            # CONSULTA RESERVA()
            print('CONSULTA RESERVA()')
            nome = input('NOME DO CLIENTE:')

            print(f'RESERVA {nome}')
        elif op == '7':
            # EXCLUIR CLIENTE()
            print('EXCLUIR CLIENTE ()')
            nome = input('NOME DO CLIENTE:')
            print(f'Cliente {nome} excluido com sucesso!')
        elif op == '8':
            # EXCLUIR QUARTO()
            numero = input('NUMERO DO QUARTO:')
            print(f'Quarto {numero} excluido com sucesso!')
        elif op == '9':
            # RESERVA - CHECK OUT()
            numero = input('NUMERO DO QUARTO:')
            print(f'Quarto {numero} Check Out com sucesso!')
        elif op == '10':
            # RELATORIO()
            print('Relatório emitido com sucesso!')
        elif op == '11':
            os.system('cls')
            cursor.close()
            conexao.close()
            print('Obrigado!')
            print('Volte Sempre!')
        elif op == '4':
            os.system('cls')
            banco_dados.consulta_cliente(cursor)
            print('-'*50)
            input('Aperte Enter para voltar: ')
            os.system('cls')
        else:
            os.system('cls')
            print('Opção Inválida!')
            print('Por favor')

    print('Fim do Progama!')

    return None
