# MENU POUSADA
import os
op = ''
print('='*35)
print('Bem vindo(a) ao Sistema de Locadora')
print('='*35)
print()
print('Para começar')
while op != '5': # Sai quando a op é 5
  print('Escolha uma das opções abaixo:')
  print('    1 - Cadastro Clientes')
  print('    2 - Cadastro Quartos')
  print('    3 - Reservas')
  print('    4 - Relatórios')
  print('    5 - Sair')
  op = input('Opção: ')
  if op == '1':
    #cadastra_clientes()
    os.system('clear')
    print('='*19)
    print('Cadastro de Clientes')
    print('='*10)
    nome = input('Nome: ')
    cpf = input('CPF: ')
    telefone = input('Telefone: ')
    print(f'cadastra_clientes({nome}, {cpf}, {telefone})')
    os.system('clear')
    print(f'Usuário {nome} cadastrado com sucesso!')
  elif op == '2':
    #cadastra_quartos()
    print('cadastra_quartos()')
  elif op == '3':
    #reserva()
    print('reservas()')
  elif op == '4':
    #relatorio()
    print('relatorios()')
  elif op == '5':
    os.system('clear')
    print('Obrigado!')
    print('Volte Sempre!')
  else:
    os.system('clear')
    print('Opção Inválida!')
    print('Por favor')

print('Fim do Progama!')