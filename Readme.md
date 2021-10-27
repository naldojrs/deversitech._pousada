# Sobre

#### Projeto de Software para hotel

---

###### Tecnologia utilizadas

- Python
- SQL Server
- SQL Workbench
- Github
- Metodologia Ágil

---

###### Requisitos do projeto

- Desenvolvimento de um software para gerenciar quartos, clientes e reservas. É importante que o sistema permita o cadastro de quartos e clientes, assim como sua deleção em caso de algum erro no cadastro.

- O sistema implementado irá gerenciar as reservas de quartos. Neste caso, as reservas só podem ser efetuadas se, quarto e clientes estiverem cadastrados e o quarto solicitado estiver livre.

- O sistema precisa exibir relatório com todos os quarto e seus respectivos status. Permitindo ao cliente escolher o quarto disponível, após a escolha do quarto o sistema realiza a reserva.

- O sistema precisa ter opção de check-in e check-out. O check-in só pode ser permitido se o quarto estiver reservado, e o check-out só é permitido se o quarto estiver com status ocupado. 

- O processo terá diversas etapas e status: Livre > Reservado > Realizando check-in > Ocupado > Realizando check-out > Livre.

  - Livre: Quarto disponível para reserva.
  - Reservado: Quarto reservado para um cliente.
  - Realizando check-in: Momento em que o cliente chega ao hotel para ocupar o quarto e se apresenta ao recepcionista.
  - Ocupado: Quarto ocupado pelo cliente.
  - Realizando check-out: momento em que o cliente está de saída, o mesmo deverá comparecer a recepção.
  - Livre: Após o check-out, o quarto ficará livre se não estiver reservado para outro cliente no mesmo dia. Se houver reserva do mesmo quarto para o mesmo dia, o quarto receberá o status de reservado.

  ---

###### Componentes do grupo


- Jefte Oliveira
- Josinaldo Rodrigues dos Santos
- Júlio Furtado
- Osiel Mesquita de Oliveira
- Thiago Batista Altoé

  ---

  ---

# Segue abaixo alguns detalhes do projeto:
  ---

## Menu exibido pelo software:

        1  - CADASTRO DE CLIENTE
        2  - CADASTRO DE QUARTO
        3  - RESERVA - CHECK_IN
        4  - CONSULTAR CLIENTE
        5  - CONSULTAR QUARTO
        6  - CONSULTAR RESERVA
        7  - EXCLUIR CLIENTE
        8  - EXCLUIR QUARTO
        9  - RESERVA - CHECK_OUT
        10 - RELATÓRIO
        11 - SAIR

  
  ---

# DER (Diagrama Entidade Relacionamento)

![DER do bando de dados](https://github.com/naldojrs/deversitech._pousada/blob/pousada/banco_dados/derPousada.png?raw=true)

  
  ---
# MER (Modelo Entidade Relacionamento)

![MER do bando de dados](https://github.com/naldojrs/deversitech._pousada/blob/pousada/banco_dados/merPousada.png?raw=true)




