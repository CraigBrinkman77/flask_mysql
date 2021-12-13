-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Survey_Schema
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Survey_Schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Survey_Schema` DEFAULT CHARACTER SET utf8 ;
USE `Survey_Schema` ;

-- -----------------------------------------------------
-- Table `Survey_Schema`.`dojos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Survey_Schema`.`dojos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `location` VARCHAR(45) NULL,
  `language` VARCHAR(45) NULL,
  `comment` TEXT NULL,
  `crated_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
dojos