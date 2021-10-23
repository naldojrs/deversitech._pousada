-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema dbPousada
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema dbPousada
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dbPousada` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `dbPousada` ;

-- -----------------------------------------------------
-- Table `dbPousada`.`clilentes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbPousada`.`clilentes` (
  `id` INT NOT NULL,
  `Nome` VARCHAR(250) NULL DEFAULT NULL,
  `CPF` INT NULL DEFAULT NULL,
  `Endereco` VARCHAR(250) NULL DEFAULT NULL,
  `Telefone` INT NULL DEFAULT NULL,
  `Status` VARCHAR(15) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `dbPousada`.`reserva`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbPousada`.`reserva` (
  `id` INT NOT NULL,
  `Status` VARCHAR(15) NULL DEFAULT NULL,
  `fk_Clilentes_id` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `FK_Reserva_2` (`fk_Clilentes_id` ASC) VISIBLE,
  CONSTRAINT `FK_Reserva_2`
    FOREIGN KEY (`fk_Clilentes_id`)
    REFERENCES `dbPousada`.`clilentes` (`id`)
    ON DELETE RESTRICT)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `dbPousada`.`quartos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbPousada`.`quartos` (
  `id` INT NOT NULL,
  `numQuarto` INT NULL DEFAULT NULL,
  `tipo` VARCHAR(25) NULL DEFAULT NULL,
  `Acomodacao` VARCHAR(250) NULL DEFAULT NULL,
  `Status` VARCHAR(15) NULL DEFAULT NULL,
  `Checkin` DATE NULL DEFAULT NULL,
  `Checkout` DATE NULL DEFAULT NULL,
  `fk_Reserva_id` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `FK_Quartos_2` (`fk_Reserva_id` ASC) VISIBLE,
  CONSTRAINT `FK_Quartos_2`
    FOREIGN KEY (`fk_Reserva_id`)
    REFERENCES `dbPousada`.`reserva` (`id`)
    ON DELETE RESTRICT)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
