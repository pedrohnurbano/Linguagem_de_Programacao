-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: gerenciamento_processos
-- ------------------------------------------------------
-- Server version	5.5.20-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `processo`
--

DROP TABLE IF EXISTS `processo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `processo` (
  `numero` int(11) NOT NULL,
  `situacao` varchar(45) NOT NULL,
  `inicio_processo` date NOT NULL,
  `valor_causa` decimal(10,0) NOT NULL,
  `natureza` varchar(45) NOT NULL,
  `codcliente` int(11) NOT NULL,
  `codadvogado` int(11) NOT NULL,
  `parte_passiva_cli` varchar(45) NOT NULL,
  `parte_passiva_adv` varchar(45) NOT NULL,
  PRIMARY KEY (`numero`),
  KEY `codcliente` (`codcliente`),
  KEY `codadvogado` (`codadvogado`),
  CONSTRAINT `processo_ibfk_1` FOREIGN KEY (`codcliente`) REFERENCES `cliente` (`codigo`),
  CONSTRAINT `processo_ibfk_2` FOREIGN KEY (`codadvogado`) REFERENCES `advogado` (`numero_oab`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `processo`
--

LOCK TABLES `processo` WRITE;
/*!40000 ALTER TABLE `processo` DISABLE KEYS */;
INSERT INTO `processo` VALUES (1,'Arquivado','2024-11-26',1250,'Criminal',1,123456,'Abigail Jeremias Silva','Nelson Willians'),(2,'Aberto','2024-05-24',3520,'Cível',2,789159,'Jones Mendes','Marcus Uggioni'),(3,'Encerrado','2024-09-16',5890,'Tributário',3,846237,'Mariane Joaquim Melo','Arthur Andrade Junior');
/*!40000 ALTER TABLE `processo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-26 17:02:50
