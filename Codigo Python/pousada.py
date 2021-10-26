import os
import mysql.connector
from mysql.connector import cursor
from datetime import date                                #add pensando no check-in/out

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

    while op != '11':
        print('=' * 80)
        print("BEM VINDO A POUSADA GAMA - ".center(80))
        data_atual = data_atual.strftime('%d/%m/%Y')
        print(data_atual.center(80))
        print('=' * 80)
        print('    ESCOLHA A OPÇÃO DESEJADA:')
 
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


#------------------------------------- CADASTRO DE CLIENTE ------------------------------------- 
    

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


#------------------------------------- RESERVA CHECK-IN ------------------------------------- 


        elif op == '3':
            # RESERVA - CHECK_IN ()
            os.system('cls')
            print('='*19)
            print('RESERVA - CHECK_IN()')
            print('='*19)
             
            print(f'RESERVA {nome}')


#------------------------------------- CONSULTA CLIENTES ------------------------------------- 


        elif op == '4':
            # CONSULTA CLIENTES()
            os.system('cls')
            print('CONSULTA CLIENTES()')
            nome = input('Nome: ')

            banco_dados.consulta_clientes(cursor, nome)
            print('-'*50)
            input('Aperte Enter para voltar: ')
            os.system('cls')


#------------------------------------- CONSULTA QUARTOS ------------------------------------- 


        elif op == '5':
            # CONSULTA QUARTO()
            print('CONSULTA QUARTO()')
            numero = input('Número:')

            print(f'QUARTO {numero}')

#------------------------------------- CONSULTA RESERVAS ------------------------------------- 


        elif op == '6':
            # CONSULTA RESERVA()
            print('CONSULTA RESERVA()')
            nome = input('NOME DO CLIENTE:')
  
            print('CADASTRA QUARTO()')
            acomodacao = input('Acomodação: ')               #oq seria acomodacao?
            tipo = input('Tipo:')
            num_quarto = input('Número: ')                   #troquei o nome de numero para num_quarto
            check_in = input('Check-in: ')                  #add precisa colocar sincronizado com data? não sei se entraria aqui
            check_out = input('Check-out: ')                #add
            status_q = input('Status Quarto: ')

            print(f'Cadastro Quarto({acomodacao}, {tipo}, {num_quarto},{check_in},{check_out},{status_q}')
            banco_dados.cadastra_quarto(cursor, acomodacao, tipo, num_quarto, check_in, check_out, status_q)  #assim que salva???
            conexao.commit()  # se não executar commit as alterações não são salvas
            os.system('cls')

            print(f'Quarto {num_quarto} Cadstrado com Sucesso!')


#------------------------------------- EXCLUIR CLIENTES ------------------------------------- 

        elif op == '7':
            # EXCLUIR CLIENTE()
            print('EXCLUIR CLIENTE ()')
            nome = input('NOME DO CLIENTE:')
            print(f'Cliente {nome} excluido com sucesso!')


    #    elif op == '7':           #pensei agora, não testei
            # EXCLUIR CLIENTE ()
    #        os.system('cls')
    #        print(' DIGITE O CPF PARA EXCLUIR O CLIENTE')
     #       #1 ideia
     #       #cpf_del = input('CPF: ')
     #       #del(cadastro_cliente['cpf'] == cpf_del)
     #       
    #        #2 ideia
    #        #for i in nomes:
    #        cpf_del = input('CPF: ')
    #        if(i == cpf_del):
    #            deleta(i)


            print('CLIENTE EXCLUIDO()')



            


#------------------------------------- EXCLUIR QUARTOS ------------------------------------- 

        elif op == '8':
            # EXCLUIR QUARTO()
            numero = input('NUMERO DO QUARTO:')
            print(f'Quarto {numero} excluido com sucesso!')

    #    elif op == '4':
    #        # EXCLUIR QUARTO()
    #       os.system('cls')
    #      print('QUARTO EXCLUIDO()')
            
            #Se der certo clientes, repetir em quartos


#------------------------------------- CHECK-OUT ------------------------------------- 


        elif op == '9':
            # RESERVA - CHECK OUT()
            numero = input('NUMERO DO QUARTO:')
            print(f'Quarto {numero} Check Out com sucesso!')


#------------------------------------- RELATÓRIOS ------------------------------------- 
            

        if op == '10':
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

        elif op == '11':
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

#------------------------------------- RESERVA ------------------------------------- 


    #    elif op == '5':
            # RESERVA() add aqui também
    #        os.system('cls')
    #        while status_q == "livre":
                #print(SELECT * FROM "cadastra_quarto" WHERE "status_q" == "livre" AND "tipo")            Para mostrar os quartos livres   
    #            cadastro_quarto[num_quarto] = input('Selecione o Número do quarto: ')  
                
            
            
            #Acho que o input do check-in/out seria agora
            #check_in = input('Check-in: ')                  #add precisa colocar sincronizado com data? não sei se entraria aqui
            #check_out = input('Check-out: ')                #add            
            
            
            
            
    #        cliente_id = input('Cliente:') #precisa trazer o input do cliente
            #SELECT * FROM cliente WHERE check_in LIKE yes 
            # alguma coisa assim, puxando do sql
    #        quarto_id = input('Quarto:')
            #SELECT * FROM quarato WHERE check_in LIKE yes 
            # alguma coisa assim, puxando do sql
    #        date = input('Data:')  
    #        status = input('Status Reserva: ')  #pensando ainda.. ainda não testei as fórmulas
    #        print('RESERVA()')

            #não consegui testar    