/* merLogicoPousada: */

CREATE TABLE reservas (
    id int(3) PRIMARY KEY,
    cliente_id int(3),
    quarto_id int(3),
    status varchar(15),
    date date,
    fk_clientes_id int(3),
    fk_quartos_id int(3)
);

CREATE TABLE quartos (
    id int(3) PRIMARY KEY,
    tipo varchar(25),
    num_quarto int(5),
    acomodacao varchar(250),
    status_q varchar(15),
    check_in date,
    check_out date
);

CREATE TABLE clientes (
    id int(3) PRIMARY KEY,
    nome varchar(250),
    CPF int(11),
    endereco varchar(250),
    telefone int(14),
    status_c varchar(15)
);
 
ALTER TABLE reservas ADD CONSTRAINT FK_reservas_2
    FOREIGN KEY (fk_clientes_id)
    REFERENCES clientes (id)
    ON DELETE RESTRICT;
 
ALTER TABLE reservas ADD CONSTRAINT FK_reservas_3
    FOREIGN KEY (fk_quartos_id)
    REFERENCES quartos (id)
    ON DELETE RESTRICT;