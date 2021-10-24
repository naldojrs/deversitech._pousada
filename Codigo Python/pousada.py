import os
import mysql.connector
from mysql.connector import cursor
from datetime import date                                #add pensando no check-in/out

import banco_dados


conexao = banco_dados.conecta_bd()
cursor = conexao.cursor()


#------------------------------------- MENU (OK) ------------------------------------- 


def menu(conexao=cursor):
    os.system('cls')
    op = ''
    print('='*35)
    print('       SISTEMA DE RESERVA')
    print('='*35)
    print()

    while op != '7':  # Sai quando a op é 5
        print('=' * 80)
        print("BEM VINDO A POUSADA GAMA - ".center(80))
        data_atual = data_atual.strftime(‘%d/%m/%Y’)             #add pensando no check-in/out
        print(data_atual.center(80))                             #add 
        print('=' * 80)
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


#------------------------------------- CADASTRO DE CLIENTE ------------------------------------- 
    

        if op == '1':
            os.system('cls')
            print('='*19)
            print('CADASTRA CLIENTE')
            print('='*10)

            nome = input('Nome: ')
            cpf = input('CPF: ')
            telefone = input('Telefone: ')
            endereco = input('Endereço: ')                   #add de acordo com o SQL
            status_c = input('Status Cliente: ')

            print(f'Cadastro Cliente({nome}, {cpf}, {telefone},{endereco},{status_c}')
            banco_dados.cadastra_cliente(cursor, nome, cpf, telefone, endereco, status_c)
            conexao.commit()  # se não executar commit as alterações não são salvas
            os.system('cls')
            print(f'Usuário {nome} cadastrado com sucesso!')

# Não consegui testar, mas acho que está ok....


#------------------------------------- CADASTRO DOS QUARTOS ------------------------------------- 


        elif op == '2':
            # CADASTRA QUARTO()
            print('CADASTRA QUARTO()')
            os.system('cls')
            acomodacao = input('Acomodação:')
            tipo = input('Tipo:')
            num_quarto = input('Número:')                   #troquei o nome de numero para num_quarto
            check_in = input('Check-in: ')                  #add precisa colocar sincronizado com data?
            check_out = input('Check-out: ')                #add
            status_q = input('Status Quarto:')

            print(f'Cadastro Quarto({acomodacao}, {tipo}, {num_quarto},{check_in},{check_out},{status_q}')
            banco_dados.cadastra_quarto(cursor, acomodacao, tipo, num_quarto, check_in, check_out, status_q)  #assim que salva???
            conexao.commit()  # se não executar commit as alterações não são salvas
            os.system('cls')
            print(f'Quarto {num_quarto} Cadstrado com Sucesso!')


#------------------------------------- EXCLUIR CLIENTES ------------------------------------- 


        elif op == '3':
            # EXCLUIR CLIENTE ()
            # for 
            # if check_out > data_atual:
            #print('CLIENTE NO HOTEL')
            #os.system('cls')


            #tem q pensar em lista
            # data_atual > check_out, então o cliente será excluido pq não está mais no quarto
            # quando excluir o cliente aqui, tem que liberar o quarto também
            print('CLIENTE EXCLUIDO()')


#------------------------------------- EXCLUIR QUARTOS ------------------------------------- 


        elif op == '4':
            # EXCLUIR QUARTO()
            print('QUARTO EXCLUIDO()')


#------------------------------------- RESERVA ------------------------------------- 


        elif op == '5':
            # RESERVA() add aqui também
            os.system('cls')
            cliente_id = input('Cliente:') #precisa trazer o input do cliente
            #SELECT * FROM cliente WHERE check_in LIKE yes 
            # alguma coisa assim, puxando do sql
            quuarto_id = input('Quarto:')
            #SELECT * FROM quarato WHERE check_in LIKE yes 
            # alguma coisa assim, puxando do sql
            date = input('Data:')  
            status = input('Status Reserva: ')  #pensando ainda.. ainda não testei as fórmulas
            print('RESERVA()')

            #não consegui testar


#------------------------------------- RELATÓRIOS ------------------------------------- 
            

        if op == '6':
            os.system('cls')
            print('='*19)
            print('RELATÓRIOS'.center(19))
            print('='*19)
            
            #clientes
            #if check_in > 0:   #ainda não testei, só estou colocando para melhorar depois
            # SELECT * FROM 'clientes' ORDER BY 'status_c'[DESC]
            print('='*19)
            print('RELATÓRIO CLIENTES')
            print('='*19)
                


            #    cliente['nome'].value_counts()[:]  #acho q isso somaria os clientes
            #    print(cliente[nome, cpf, telefone])  #tem q fazer a lista dos clientes aparecer
            #print(sum)


            #quartos
            
            #quartos ocupados       
            #    print('='*19)
            #    print('RELATÓRIO QUARTOS')
            # SELECT COUNT * FROM 'quartos' WHERE 'status_q == ocupado    ??? não sei oq vai estar escrito em status_q para confirmar se está ocupado ou não
            # SELECT * FROM 'quartos' ORDER BY 'status_q'[DESC]
            #    print('='*19)
            #    porcentagem = 
            #    print()
            #    print(f'Quarto ocupados({acomodacao}, {tipo}, {numero},{status}')  #mostrar lista de quartos
            
         #   else:
         #       print('Hotel está vazio')

         #   conexao.commit()  # se não executar commit as alterações não são salvas
         #   os.system('cls')
         #   print(f'Relatório exibido com sucesso!')  
          

#------------------------------------- SAIR (OK) -------------------------------------  


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


# opção estava duplicada na ultima att do Josinaldo

 #       elif op == '4':
 #           os.system('cls')
 #           banco_dados.consulta_cliente(cursor)
 #           print('-'*50)
 #           input('Aperte Enter para voltar: ')
 #           os.system('cls')