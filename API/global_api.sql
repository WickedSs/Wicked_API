﻿-- MySQL dump 10.13  Distrib 5.7.29, for Win64 (x86_64)
--
-- Host: localhost    Database: global_api
-- ------------------------------------------------------
-- Server version	5.7.29-log

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
-- Table structure for table `athletes`
--

DROP TABLE IF EXISTS `athletes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `athletes` (
  `id` smallint(6) DEFAULT NULL,
  `rfid` varchar(20) DEFAULT NULL,
  `fullname` varchar(28) DEFAULT NULL,
  `birthday` varchar(10) DEFAULT NULL,
  `photo` varchar(11) DEFAULT NULL,
  `telephone` varchar(11) DEFAULT NULL,
  `subscriptionStart` varchar(10) DEFAULT NULL,
  `subscriptionEnd` varchar(10) DEFAULT NULL,
  `sessions` smallint(6) DEFAULT NULL,
  `sessionLeft` smallint(6) DEFAULT NULL,
  `debts` smallint(6) DEFAULT NULL,
  `offer` varchar(14) DEFAULT NULL,
  `specialKey` varchar(12) DEFAULT NULL,
  `belongGroup` varchar(0) DEFAULT NULL,
  `gender` varchar(6) DEFAULT NULL,
  `timeline` varchar(29) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;



DROP TABLE IF EXISTS `cases`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cases` (
  `id` tinyint(4) DEFAULT NULL,
  `caseName` varchar(6) DEFAULT NULL,
  `key` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cases`
--

LOCK TABLES `cases` WRITE;
/*!40000 ALTER TABLE `cases` DISABLE KEYS */;
INSERT INTO `cases` VALUES (1,'Common','0xdeadcode');
/*!40000 ALTER TABLE `cases` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `categories` (
  `id` tinyint(4) DEFAULT NULL,
  `categoryName` varchar(9) DEFAULT NULL,
  `key` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES (1,'Common','0xdeadcode'),(2,'common','887cf5c2'),(3,'NonCommon','ebb92525');
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dailyincome`
--

DROP TABLE IF EXISTS `dailyincome`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dailyincome` (
  `id` smallint(6) DEFAULT NULL,
  `inDate` varchar(10) DEFAULT NULL,
  `inDebt` smallint(6) DEFAULT NULL,
  `inCase` mediumint(9) DEFAULT NULL,
  `inCome` mediumint(9) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;


DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employees` (
  `id` tinyint(4) DEFAULT NULL,
  `rfid` int(11) DEFAULT NULL,
  `fullname` varchar(18) DEFAULT NULL,
  `birthday` varchar(10) DEFAULT NULL,
  `avatar` varchar(11) DEFAULT NULL,
  `telephone` bigint(20) DEFAULT NULL,
  `employedAt` varchar(10) DEFAULT NULL,
  `monthlyPayment` smallint(6) DEFAULT NULL,
  `salary` mediumint(9) DEFAULT NULL,
  `specialKey` varchar(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` VALUES (1,10051997,'Souleymane Guerida','10-05-1997','default.png',664436207,'10-10-2016',1300,15000,'fcdb59e9');
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `expenses`
--

DROP TABLE IF EXISTS `expenses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `expenses` (
  `id` tinyint(4) DEFAULT NULL,
  `creditCard` varchar(18) DEFAULT NULL,
  `serviceName` varchar(6) DEFAULT NULL,
  `note` varchar(8) DEFAULT NULL,
  `amount` decimal(12,2) DEFAULT NULL,
  `imagePath` varchar(7) DEFAULT NULL,
  `type` varchar(7) DEFAULT NULL,
  `opDate` varchar(10) DEFAULT NULL,
  `key` varchar(10) DEFAULT NULL,
  `whichCase` varchar(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `expenses`
--

LOCK TABLES `expenses` WRITE;
/*!40000 ALTER TABLE `expenses` DISABLE KEYS */;
INSERT INTO `expenses` VALUES (3,'Common','Common','for that',1500.00,'#ac872d','Expense','22-12-2021','0xdeadcode','Case'),(9,'Souleymane Guerida','Common','for note',1300.00,'#9fbb78','Expense','22-12-2021','fcdb59e9','Employee');
/*!40000 ALTER TABLE `expenses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `intraining`
--

DROP TABLE IF EXISTS `intraining`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `intraining` (
  `id` tinyint(4) DEFAULT NULL,
  `rfid` bigint(20) DEFAULT NULL,
  `fullname` varchar(19) DEFAULT NULL,
  `photo` varchar(11) DEFAULT NULL,
  `trainingStarted` varchar(5) DEFAULT NULL,
  `trainingEnded` varchar(5) DEFAULT NULL,
  `status` tinyint(4) DEFAULT NULL,
  `date` varchar(10) DEFAULT NULL,
  `debts` decimal(12,2) DEFAULT NULL,
  `key` varchar(2) DEFAULT NULL,
  `specialKey` varchar(36) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;


DROP TABLE IF EXISTS `invoiceitems`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `invoiceitems` (
  `id` tinyint(4) DEFAULT NULL,
  `productName` varchar(12) DEFAULT NULL,
  `imagePath` varchar(14) DEFAULT NULL,
  `price` decimal(12,2) DEFAULT NULL,
  `quantity` tinyint(4) DEFAULT NULL,
  `total` decimal(12,2) DEFAULT NULL,
  `identifier` varchar(12) DEFAULT NULL,
  `respectiveBarcode` varchar(36) DEFAULT NULL,
  `isManual` tinyint(4) DEFAULT NULL,
  `reference` varchar(36) DEFAULT NULL,
  `color` varchar(36) DEFAULT NULL,
  `model` varchar(36) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `invoiceitems`
--

LOCK TABLES `invoiceitems` WRITE;
/*!40000 ALTER TABLE `invoiceitems` DISABLE KEYS */;
INSERT INTO `invoiceitems` VALUES (4,'Luna Lock','product_03.png',21000.00,2,42000.00,'ac3786000e80','SK00',1,'45erzer52','unknown_value_please_contact_support','unknown_value_please_contact_support'),(5,'Luna Lock','product_03.png',21000.00,1,21000.00,'0dd486fa4d66','SK00',1,'fer411','unknown_value_please_contact_support','unknown_value_please_contact_support'),(6,'Luna Lock','product_03.png',21000.00,5,105000.00,'5843059fc4d5','SK00',1,'qe11','unknown_value_please_contact_support','unknown_value_please_contact_support'),(7,'Luna Lock','product_03.png',21000.00,1,21000.00,'aa38b1880fe8','SK00',1,'erser445','unknown_value_please_contact_support','unknown_value_please_contact_support'),(8,'Luna Lock','product_03.png',21000.00,2,42000.00,'db053a6e38a5','SK00',1,'serser15516','unknown_value_please_contact_support','unknown_value_please_contact_support'),(9,'Luna Lock','product_03.png',21000.00,1,21000.00,'9490bbfccd38','SK00',1,'456sers51ef','unknown_value_please_contact_support','unknown_value_please_contact_support'),(10,'Luna Lock','product_03.png',21000.00,1,21000.00,'6127ca21423a','SK00',1,'se4r41fs5er41','unknown_value_please_contact_support','unknown_value_please_contact_support'),(11,'Luna Lock','product_03.png',21000.00,3,63000.00,'08f8f6d569ae','SK00',1,'s41ers513er','unknown_value_please_contact_support','unknown_value_please_contact_support'),(12,'Luna Lock','product_03.png',21000.00,1,21000.00,'eb5f0d7601c4','SK00',1,'se5rs5ef53','unknown_value_please_contact_support','unknown_value_please_contact_support'),(13,'Luna Lock','product_03.png',21000.00,2,42000.00,'e0205cd0251b','SK00',1,'se54rse5f1','unknown_value_please_contact_support','unknown_value_please_contact_support'),(16,'Luna Lock','product_03.png',16500.00,1,16500.00,'c4bc923a7792','SK00',1,'se54rs5er','unknown_value_please_contact_support','unknown_value_please_contact_support'),(17,'Hello','default.png',120.00,4,480.00,'56121337c843','unknown_value_please_contact_support',1,'unknown_value_please_contact_support','unknown_value_please_contact_support','unknown_value_please_contact_support'),(18,'Wicked','default.png',170.00,8,1360.00,'56121337c843','unknown_value_please_contact_support',1,'unknown_value_please_contact_support','unknown_value_please_contact_support','unknown_value_please_contact_support'),(22,'Luna Lock','product_03.png',18900.00,1,18900.00,'0d488d0c5702','SK00',0,'ghf51jy52y','unknown_value_please_contact_support','unknown_value_please_contact_support'),(23,'Wicked Chair','default.png',18900.00,1,18900.00,'0d488d0c5702','SK03',0,'unknown_value_please_contact_support','unknown_value_please_contact_support','unknown_value_please_contact_support'),(24,'Luna Lock','product_03.png',18900.00,1,18900.00,'efbc66ac4e2a','SK00',0,'ghf51jy52y','unknown_value_please_contact_support','unknown_value_please_contact_support'),(25,'Wicked Chair','default.png',21000.00,1,21000.00,'efbc66ac4e2a','SK03',0,'unknown_value_please_contact_support','unknown_value_please_contact_support','unknown_value_please_contact_support'),(26,'Luna Lock','product_03.png',22000.00,1,22000.00,'1a86ce9a597b','SK00',0,'ghf51jy52y','unknown_value_please_contact_support','unknown_value_please_contact_support'),(27,'Luna Lock','product_03.png',21000.00,2,42000.00,'cf15c69c10a0','SK00',0,'ghf51jy52y','unknown_value_please_contact_support','unknown_value_please_contact_support'),(28,'Wicked Chair','default.png',21000.00,3,63000.00,'cf15c69c10a0','SK02',0,'unknown_value_please_contact_support','unknown_value_please_contact_support','unknown_value_please_contact_support'),(29,'Hello','default.png',1500.00,5,7500.00,'56121337c843','',1,'','unknown_value_please_contact_support','unknown_value_please_contact_support');
/*!40000 ALTER TABLE `invoiceitems` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `invoices`
--

DROP TABLE IF EXISTS `invoices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `invoices` (
  `id` tinyint(4) DEFAULT NULL,
  `buyer` varchar(37) DEFAULT NULL,
  `opDate` varchar(10) DEFAULT NULL,
  `amount` decimal(12,2) DEFAULT NULL,
  `paid` decimal(12,2) DEFAULT NULL,
  `remaining` decimal(12,2) DEFAULT NULL,
  `identifier` varchar(12) DEFAULT NULL,
  `BC` tinyint(4) DEFAULT NULL,
  `BCdate` varchar(10) DEFAULT NULL,
  `BL` varchar(7) DEFAULT NULL,
  `BLdate` varchar(10) DEFAULT NULL,
  `factureNumber` varchar(7) DEFAULT NULL,
  `invoiceType` varchar(17) DEFAULT NULL,
  `validated` tinyint(4) DEFAULT NULL,
  `validationDate` varchar(36) DEFAULT NULL,
  `Note` varchar(38) DEFAULT NULL,
  `TVA` varchar(2) DEFAULT NULL,
  `FactureTVA` decimal(12,2) DEFAULT NULL,
  `Address` varchar(18) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;


DROP TABLE IF EXISTS `materials`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `materials` (
  `id` tinyint(4) DEFAULT NULL,
  `materialName` varchar(13) DEFAULT NULL,
  `materialType` varchar(4) DEFAULT NULL,
  `materialPrice` decimal(12,2) DEFAULT NULL,
  `materialQte` tinyint(4) DEFAULT NULL,
  `materialKey` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `materials`
--

LOCK TABLES `materials` WRITE;
/*!40000 ALTER TABLE `materials` DISABLE KEYS */;
INSERT INTO `materials` VALUES (1,'Bois round 15','Bois',1500.00,3,'3a6908bc8f'),(2,'Fer plat 10cm','Fer',150.00,5,'3a6908bc8f');
/*!40000 ALTER TABLE `materials` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `persistants`
--

DROP TABLE IF EXISTS `persistants`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `persistants` (
  `id` tinyint(4) DEFAULT NULL,
  `percentageOff` tinyint(4) DEFAULT NULL,
  `benefitPercentage` tinyint(4) DEFAULT NULL,
  `stcokOff` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `persistants`
--

LOCK TABLES `persistants` WRITE;
/*!40000 ALTER TABLE `persistants` DISABLE KEYS */;
INSERT INTO `persistants` VALUES (1,10,30,2);
/*!40000 ALTER TABLE `persistants` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products` (
  `id` int(10) DEFAULT NULL,
  `productName` varchar(50) DEFAULT NULL,
  `model` varchar(50) DEFAULT NULL,
  `barcode` varchar(50) DEFAULT NULL,
  `quantity` int(10) DEFAULT NULL,
  `imagePath` varchar(14) DEFAULT NULL,
  `price` decimal(12,2) DEFAULT NULL,
  `identifier` varchar(50) DEFAULT NULL,
  `dimensions` varchar(12) DEFAULT NULL,
  `sold` int(10) DEFAULT NULL,
  `bought` decimal(12,2) DEFAULT NULL,
  `market` decimal(12,2) DEFAULT NULL,
  `earned` decimal(12,2) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  `link` varchar(50) DEFAULT NULL,
  `priceL` varchar(1) DEFAULT NULL,
  `quantityL` varchar(2) DEFAULT NULL,
  `reference` varchar(14) DEFAULT NULL,
  `availableColors` varchar(500) DEFAULT NULL,
  `materialLink` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'Luna Lock','Model-0','1526512',5,'product_03.png',22400.00,'Example','120W 40D 20H',182,16000.00,16500.00,200000.00,'The Wicked Desk is a sleek and sturdy computer desk. Designed with curves and a slick wood look, Luna is a natural fit right in your office or home. The built-in USB ports make it easy to plug in your device for a seamless workflow, and easy to find a spot thatظآs just the right size.','HwhZSlNhQX','0','15','ghf51jy52y','Red','unknown_value_please_contact_support'),(2,'┘à┘╪▒╪ش ╪د┘┘â╪▒┘ê╪ذ','Model-0','14985554',20,'default.png',910.00,'book','',0,650.00,0.00,0.00,'\r\n','bc69d6fce1','0','20','tyffty551203ty','Green','unknown_value_please_contact_support'),(3,'Wicked Chair','Model-0','24149665',10,'default.png',21000.00,'Chair','',0,15000.00,0.00,0.00,'','HwhZSlNhQX','','','','Blue','3a6908bc8f'),(4,'Nebu Desk','Model-0','31846665',15,'default.png',21000.00,'Desk','',0,15000.00,0.00,0.00,'','67a2724f96','','','','White','2f36a04972'),(5,'Aurora Lamp','Model-0','44194484',13,'default.png',1750.00,'Lamp','',0,1250.00,0.00,0.00,'','301d54b13e','','','','Black','de4ebc0450'),(6,'Hope Table','Model-0','54892894',16,'default.png',26600.00,'Table','',0,19000.00,0.00,0.00,'','c3b5844805','','','','Red','8b29a7b2cf'),(7,'Asus Card','Model-0','64845485',1,'AsusCard.png',350.00,'Card','',0,250.00,0.00,0.00,'','7cbbce2cfd','','','','Black','e8f873806c'),(8,'Floppy Disk','Model-0','74185487',50,'FloppyDisk.png',140.00,'Disk','',0,100.00,60.00,0.00,'','f505d93006','','','','Blue','209b91c5c5'),(9,'Weight =','Model-0','154445251',10,'default.png',25200.00,'Protein','',0,18000.00,0.00,0.00,'','1241ddde52','','','','Weight','a413ec7cdb'),(14,'Protein C4','Model-0','10001',5,'default.png',19500.00,'Pre','',0,15000.00,0.00,0.00,'','121d61e080','','','','White','0a528d556f'),(15,'Protein Test','Model-0','10002',1,'default.png',19500.00,'Pre','',0,15000.00,0.00,0.00,'','421eb10a54','','','','White','d31bc20846'),(16,'Protein Test 02','Model-0','10003',2,'default.png',19500.00,'Pre','',0,15000.00,0.00,0.00,'','47a136ed5f','','','','White','cdadf0040d'),(17,'Protein Test V3','Model-0','10004',1,'default.png',19500.00,'Pre','',0,15000.00,0.00,0.00,'','723c2dc198','','','','White','b80d7e4f51');
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sqlite_sequence`
--

DROP TABLE IF EXISTS `sqlite_sequence`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sqlite_sequence` (
  `name` varchar(14) DEFAULT NULL,
  `seq` smallint(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sqlite_sequence`
--

LOCK TABLES `sqlite_sequence` WRITE;
/*!40000 ALTER TABLE `sqlite_sequence` DISABLE KEYS */;
INSERT INTO `sqlite_sequence` VALUES ('users',5),('Persistants',1),('Cases',1),('Categories',3),('dailyIncome',114),('invoices',19),('invoiceitems',29),('expenses',9),('Employees',1),('products',17),('Athletes',3621),('materials',2),('TrainingGroups',3),('inTraining',35);
/*!40000 ALTER TABLE `sqlite_sequence` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `traininggroups`
--

DROP TABLE IF EXISTS `traininggroups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `traininggroups` (
  `id` tinyint(4) DEFAULT NULL,
  `name` varchar(1) DEFAULT NULL,
  `members` varchar(18) DEFAULT NULL,
  `startTime` varchar(5) DEFAULT NULL,
  `endTime` varchar(5) DEFAULT NULL,
  `purpose` varchar(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `traininggroups`
--

LOCK TABLES `traininggroups` WRITE;
/*!40000 ALTER TABLE `traininggroups` DISABLE KEYS */;
INSERT INTO `traininggroups` VALUES (1,'A','Souleymane Guerida','20:00','22:00','Karat├ر'),(2,'B','','01:00','02:00','Females'),(3,'C','','14:00','16:00','Footbool');
/*!40000 ALTER TABLE `traininggroups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(10) DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `password_sha512` varchar(200) DEFAULT NULL,
  `userRole` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'root','1000:5b42403239366436353234:15614ffe49749472dfa2621a5bdb7f23a17608c102f3ce6fc46d67abece24683cad44723797059fad7477a16b93c3173ed2b15e49d6b3e7eb6c73b833fe8eca9','Admin'),(2,'Wicked','1000:5b42403537363564326639:26d12e71faa47c9a54ceedb2233d7d00da938292b3b3850e99ac975165a7529082f22ac869d2193412e423a3d6aef43a68e9e56788ee9df02b808af202067398','Employee'),(3,'Luna','1000:5b424064316136383136:c821da0b2a20daecfa8c0e65d2535a0d9fcac0cddbbadf441cc5c59789c5c67f6d89b3aeb55c8e29974ff7dfb5ca94a2bdb3fe56ef5c3dca937ccfbfe5e0b782','Employee'),(4,'Reone','1000:5b42403562376635623561:35e6f4bd99170c8b6f9b769c20f606d00ea90b0e6747ae0f549165513a82f4ce7f97d637b49f6267a48608a594af8f8dc57b67a7fd4b63dc92489d9b9b4bef41','Employee'),(5,'Aurora','1000:5b42403139636562663130:ace32b9ed31a4e998b9afdc89a693e3a51504b2bb37460744f9f62f57fb80d5826ffb9891a678f24f036077aae2eee03b5198da4e3aa5078d21cdf0e30582bce','Employee');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-09-17 17:59:40
