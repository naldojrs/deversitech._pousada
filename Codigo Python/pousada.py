import os

import banco_dados

conexao = banco_dados.conecta_bd()
cursor = conexao.cursor()

#------------------------------------- MENU (OK) ------------------------------------- 
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

#------------------------------------- 1 CADASTRO DE CLIENTE (OK) -------------------------------------
        if op == '1':
            # CADASTRA CLIENTE()
            os.system('cls')
            print('='*19)
            print('CADASTRA CLIENTE')
            print('='*19)

            nome = input('Nome: ')
            cpf = input('CPF: ')
            telefone = input('Telefone: ')
            endereco = input('Endereço: ')

            banco_dados.cadastra_clientes(cursor, nome, cpf, telefone, endereco)
            print(type(conexao))
            conexao.commit()  # se não exe commit as alterações não são salva
            os.system('cls')
            print(f'Usuário {nome} cadastrado com sucesso!')

#------------------------------------- 2 CADASTRO DE QUARTOS (OK) -------------------------------------
        elif op == '2':
            # CADASTRA QUARTO()
            os.system('cls')
            print('='*19)
            print('CADASTRA QUARTO()')
            print('='*19)

            numQuarto = input('Número: ')
            tipo = input('Tipo: ')
            acomodacao = input('Acomodação: ')
            status_q = input('Status: ')
            check_in = input('Check-in: ')
            check_out = input('Check-out: ')

            banco_dados.cadastra_quarto(cursor, numQuarto, tipo, acomodacao, status_q, check_in, check_out)
            conexao.commit()
            os.system('cls')
            print(f'Quarto {numQuarto} Cadstrado com Sucesso!')

#------------------------------------- 3 RESERVA CHECK-IN ---------------------------------------
        elif op == '3':
            # RESERVA - CHECK_IN ()
            os.system('cls')
            print('='*19)
            print('RESERVA - CHECK_IN()')
            print('='*19)

#------------------------------------- 4 CONSULTA CLIENTES -------------------------------------
        elif op == '4':
            # CONSULTA CLIENTES()
            os.system('cls')
            print('='*19)
            print('CONSULTA CLIENTES()')
            print('='*19)
            
            nome = input('Nome: ')
            
            banco_dados.consulta_clientes(cursor, nome,cpf, telefone)
            print('-'*50)
            input('Aperte Enter para voltar: ')
            os.system('cls')

#------------------------------------- 5 CONSULTA QUARTOS -------------------------------------  
        elif op == '5':
            # CONSULTA QUARTO() - ACHO QUE PRECISA CADASTRAR UM QUARTO.
            os.system('cls')
            print('='*19)
            print('CONSULTA QUARTO()')
            print('='*19)
            numQuarto = input('Número: ')

            print(f'QUARTO {numQuarto}')

#------------------------------------- 6 CONSULTA RESERVA -------------------------------------
        elif op == '6':
            # CONSULTA RESERVA()
            os.system('cls')
            print('='*19)
            print('CONSULTA RESERVA()')
            print('='*19)

            nome = input('NOME DO CLIENTE: ')

            print(f'RESERVA {nome}')

#------------------------------------- 7 EXCLUIR CLIENTES -------------------------------------
        elif op == '7':
            # EXCLUIR CLIENTE()
            os.system('cls')
            print('='*19)
            print('EXCLUIR CLIENTE ()')
            print('='*19)

            nome = input('NOME DO CLIENTE: ')

            print(f'Cliente {nome} excluido com sucesso!')

#------------------------------------- 8 EXCLUIR QUARTOS -------------------------------------
        elif op == '8':
            # EXCLUIR QUARTO()
            os.system('cls')
            print('='*19)
            numQuarto = input('NUMERO DO QUARTO: ')
            print('='*19)

            print(f'Quarto {numQuarto} excluido com sucesso!')

#------------------------------------- 9 RESERVA CHECK-OUT ------------------------------------ 
        elif op == '9':
            # RESERVA - CHECK OUT()
            os.system('cls')
            print('='*19)
            numQuarto = input('RESERVA - CHECK OUT()')
            print('='*19)

            print(f'Quarto {numQuarto} Check Out com sucesso!')

#------------------------------------- 10 RELATÓRIOS -------------------------------------------
        elif op == '10':
            # RELATORIO()
            print('='*19)
            print('Relatório emitido com sucesso!')
            print('='*19)

#------------------------------------- 11 SAIR (OK) -------------------------------------
        elif op == '11':
            cursor.close()
            conexao.close()
            os.system('cls')
            print('='*19)
            print('Obrigado!')
            print('='*19)
            print('Volte Sempre!')
            print('='*19)
        elif op == '11':
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
    print('='*19)

    return None
