
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
  print('    1 - Cadastro Cliente')
  print('    2 - Cadastro Quarto')
  print('    3 - Reserva')
  print('    4 - Relatório')
  print('    5 - Sair')
  op = input('Opção: ')
  if op == '1':
    #cadastra_cliente()
    os.system('clear')
    print('='*19)
    print('Cadastro de Cliente')
    print('='*10)
    nome = input('Nome: ')
    cpf = input('CPF: ')
    telefone = input('Telefone: ')
    print(f'cadastra_cliente({nome}, {cpf}, {telefone})')
    os.system('clear')
    print(f'Usuário {nome} cadastrado com sucesso!')
  elif op == '2':
    #cadastra_quarto()
    print('cadastra_quarto()')
  elif op == '3':
    #reserva()
    print('reserva()')
  elif op == '4':
    #relatorio()
    print('relatorio()')
  elif op == '5':
    os.system('clear')
    print('Obrigado!')
    print('Volte Sempre!')
  else:
    os.system('clear')
    print('Opção Inválida!')
    print('Por favor')

print('Fim do Progama!')