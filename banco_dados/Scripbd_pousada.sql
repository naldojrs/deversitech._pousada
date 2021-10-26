-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema bd_pousada
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema bd_pousada
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `bd_pousada` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `bd_pousada` ;

-- -----------------------------------------------------
-- Table `bd_pousada`.`clientes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bd_pousada`.`clientes` (
  `id` INT NOT NULL,
  `nome` VARCHAR(250) NULL DEFAULT NULL,
  `CPF` INT NULL DEFAULT NULL,
  `endereco` VARCHAR(250) NULL DEFAULT NULL,
  `telefone` INT NULL DEFAULT NULL,
  `status_c` VARCHAR(15) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `bd_pousada`.`quartos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bd_pousada`.`quartos` (
  `id` INT NOT NULL,
  `tipo` VARCHAR(25) NULL DEFAULT NULL,
  `numQuarto` INT NULL DEFAULT NULL,
  `acomodacao` VARCHAR(250) NULL DEFAULT NULL,
  `status_q` VARCHAR(15) NULL DEFAULT NULL,
  `check_in` DATE NULL DEFAULT NULL,
  `check_out` DATE NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `bd_pousada`.`reservas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bd_pousada`.`reservas` (
  `id` INT NOT NULL,
  `cliente_id` INT NULL DEFAULT NULL,
  `quarto_id` INT NULL DEFAULT NULL,
  `Status` VARCHAR(15) NULL DEFAULT NULL,
  `date` DATE NULL DEFAULT NULL,
  `fk_clientes_id` INT NULL DEFAULT NULL,
  `fk_quartos_id` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `FK_reservas_2` (`fk_clientes_id` ASC) VISIBLE,
  INDEX `FK_reservas_3` (`fk_quartos_id` ASC) VISIBLE,
  CONSTRAINT `FK_reservas_2`
    FOREIGN KEY (`fk_clientes_id`)
    REFERENCES `bd_pousada`.`clientes` (`id`)
    ON DELETE RESTRICT,
  CONSTRAINT `FK_reservas_3`
    FOREIGN KEY (`fk_quartos_id`)
    REFERENCES `bd_pousada`.`quartos` (`id`)
    ON DELETE RESTRICT)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
