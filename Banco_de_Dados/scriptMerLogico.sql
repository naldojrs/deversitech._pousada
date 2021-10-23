/* merLogico: */

CREATE TABLE Reserva (
    id int(3) PRIMARY KEY,
    Status varchar(15),
    fk_Clilentes_id int(3)
);

CREATE TABLE Quartos (
    id int(3) PRIMARY KEY,
    numQuarto int(5),
    tipo varchar(25),
    Acomodacao varchar(250),
    Status varchar(15),
    Checkin date,
    Checkout date,
    fk_Reserva_id int(3)
);

CREATE TABLE Clilentes (
    id int(3) PRIMARY KEY,
    Nome varchar(250),
    CPF int(11),
    Endereco varchar(250),
    Telefone int(14),
    Status varchar(15)
);
 
ALTER TABLE Reserva ADD CONSTRAINT FK_Reserva_2
    FOREIGN KEY (fk_Clilentes_id)
    REFERENCES Clilentes (id)
    ON DELETE RESTRICT;
 
ALTER TABLE Quartos ADD CONSTRAINT FK_Quartos_2
    FOREIGN KEY (fk_Reserva_id)
    REFERENCES Reserva (id)
    ON DELETE RESTRICT;