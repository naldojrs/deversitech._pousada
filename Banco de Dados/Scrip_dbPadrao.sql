/* merLogico: */

CREATE TABLE Reserva (
    id int(3) PRIMARY KEY,
    Status varchar(15),
    fk_Clilentes_id int(3)
);

CREATE TABLE Quarto (
    NumLeitos int(3),
    Ar_condicionado varchar(15),
    Status varchar(15),
    Checkin date,
    id int(3) PRIMARY KEY,
    Wifi int(3),
    Checkout date,
    fk_Reserva_id int(3)
);

CREATE TABLE Clilentes (
    id int(3) PRIMARY KEY,
    CPF int(11),
    Telefone int(14),
    Endereco varchar(250),
    Nome varchar(250),
    Status varchar(15)
);
 
ALTER TABLE Reserva ADD CONSTRAINT FK_Reserva_2
    FOREIGN KEY (fk_Clilentes_id)
    REFERENCES Clilentes (id)
    ON DELETE RESTRICT;
 
ALTER TABLE Quarto ADD CONSTRAINT FK_Quarto_2
    FOREIGN KEY (fk_Reserva_id)
    REFERENCES Reserva (id)
    ON DELETE RESTRICT;