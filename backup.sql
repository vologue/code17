-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: localhost    Database: Interract
-- ------------------------------------------------------
-- Server version	5.7.22-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Applicant`
--

DROP TABLE IF EXISTS `Applicant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Applicant` (
  `Aid` int(4) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `Name` varchar(45) DEFAULT NULL,
  `Email` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Aid`),
  UNIQUE KEY `Aid_UNIQUE` (`Aid`),
  UNIQUE KEY `Email_UNIQUE` (`Email`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Applicant`
--

LOCK TABLES `Applicant` WRITE;
/*!40000 ALTER TABLE `Applicant` DISABLE KEYS */;
INSERT INTO `Applicant` VALUES (0012,'vologue','vologue@volog.com'),(0014,'vologue','willtry@willtry.com'),(0015,'rahav','askj@sjdk'),(0016,'raghav','raghav.sp98@gmail.com'),(0017,'raghav','raghavp98@gmail.com'),(0019,'vologue','vologue@gmail.com'),(0020,'Arun','arun@gmail.com'),(0021,'dfg','eee@e.in');
/*!40000 ALTER TABLE `Applicant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Candidates`
--

DROP TABLE IF EXISTS `Candidates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Candidates` (
  `AID` int(10) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `Name` varchar(45) DEFAULT NULL,
  `Email` varchar(45) DEFAULT NULL,
  `Job-landed` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`AID`),
  UNIQUE KEY `AID_UNIQUE` (`AID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Candidates`
--

LOCK TABLES `Candidates` WRITE;
/*!40000 ALTER TABLE `Candidates` DISABLE KEYS */;
/*!40000 ALTER TABLE `Candidates` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Company`
--

DROP TABLE IF EXISTS `Company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Company` (
  `CID` int(3) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `Name` varchar(45) DEFAULT NULL,
  `Email` varchar(45) DEFAULT NULL,
  `PNO` varchar(15) DEFAULT NULL,
  `jopns` int(11) DEFAULT NULL,
  `HRname` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`CID`),
  UNIQUE KEY `CID_UNIQUE` (`CID`),
  UNIQUE KEY `Email_UNIQUE` (`Email`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Company`
--

LOCK TABLES `Company` WRITE;
/*!40000 ALTER TABLE `Company` DISABLE KEYS */;
INSERT INTO `Company` VALUES (001,'sajh','tra8il@trail.com','10928309238',0,'asd'),(003,'sajh','trail1@trail.com','10928309238',0,'asd'),(004,'sajh','trail2@trail.com','10928309238',0,'asd'),(005,'sajh','trail3@trail.com','10928309238',0,'asd'),(006,'sajh','trail4@trail.com','10928309238',0,'asd'),(007,'sajh','trail5@trail.com','10928309238',0,'asd'),(008,'sajh','trail6@trail.com','10928309238',0,'asd'),(010,'sajh','trail7@trail.com','10928309238',0,'asd'),(011,'sajh','trail9@trail.com','10928309238',0,'asd'),(012,'sajh','trail19@trail.com','10928309238',3,'asd'),(013,'xobin','xobinl@trail.com','832798739',34,'jdaf'),(016,'raghav','raghav@trail.com','asf',0,'asf'),(017,'Phone','phone@k.com','987526174',1,'Raghav'),(018,'final','final@trail.com','dsjf',2,'safkh');
/*!40000 ALTER TABLE `Company` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-06-22 17:30:52
