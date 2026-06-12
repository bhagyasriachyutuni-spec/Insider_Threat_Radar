-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: threat
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `admin_alerts`
--

DROP TABLE IF EXISTS `admin_alerts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin_alerts` (
  `id` int NOT NULL AUTO_INCREMENT,
  `message` text,
  `created_at` datetime DEFAULT NULL,
  `status` varchar(20) DEFAULT 'unread',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_alerts`
--

LOCK TABLES `admin_alerts` WRITE;
/*!40000 ALTER TABLE `admin_alerts` DISABLE KEYS */;
INSERT INTO `admin_alerts` VALUES (1,'⚠️ Behavior mismatch detected for user: vinay',NULL,'unread'),(2,'⚠️ Behavior mismatch detected for user: bhagyashree',NULL,'unread'),(3,'⚠️ Behavior mismatch detected for user: bhagyashree',NULL,'unread'),(4,'⚠️ Behavior mismatch detected for user: bhagyashree',NULL,'unread'),(5,'⚠️ Behavior mismatch detected for user: bhagyashree',NULL,'unread'),(6,'? Suspicious activity detected!\nUser: bhagyashree\nRisk Score: 92.5',NULL,'unread');
/*!40000 ALTER TABLE `admin_alerts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notifications`
--

DROP TABLE IF EXISTS `notifications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notifications` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` varchar(50) DEFAULT NULL,
  `message` text,
  `status` varchar(20) DEFAULT NULL,
  `timestamp` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notifications`
--

LOCK TABLES `notifications` WRITE;
/*!40000 ALTER TABLE `notifications` DISABLE KEYS */;
INSERT INTO `notifications` VALUES (1,'ajay','⚠️ ALERT: User ajay marked as HIGH RISK','unread','2026-03-01 00:47:15'),(2,'ajay','⚠️ ALERT: User ajay marked as HIGH RISK','unread','2026-03-02 12:37:46'),(3,'bhagyashree','⚠️ ALERT: User bhagyashree marked as HIGH RISK','unread','2026-03-11 15:49:00'),(4,'bhagyashree','⚠️ ALERT: User bhagyashree marked as HIGH RISK','unread','2026-03-11 16:21:12'),(5,'bhagyashree','⚠️ ALERT: User bhagyashree marked as HIGH RISK','unread','2026-03-11 16:21:59'),(6,'bhagyashree','⚠️ ALERT: User bhagyashree marked as HIGH RISK','unread','2026-03-11 16:24:23');
/*!40000 ALTER TABLE `notifications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `predictions`
--

DROP TABLE IF EXISTS `predictions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `predictions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` varchar(50) DEFAULT NULL,
  `input_data` text,
  `prediction` varchar(50) DEFAULT NULL,
  `risk_score` float DEFAULT NULL,
  `risk_level` varchar(20) DEFAULT NULL,
  `timestamp` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `predictions`
--

LOCK TABLES `predictions` WRITE;
/*!40000 ALTER TABLE `predictions` DISABLE KEYS */;
INSERT INTO `predictions` VALUES (1,'ajay','{\'total_emails\': 4711.0, \'total_attachments\': 1780.0, \'avg_email_size\': 30020.0, \'off_hour_emails\': 499.0, \'weekend_emails\': 0.0, \'O\': 36.0, \'C\': 30.0, \'E\': 14.0, \'A\': 50.0, \'N\': 29.0}','Normal',0,'Low','2026-03-01 00:11:06'),(2,'ajay','{\'total_emails\': 7519.0, \'total_attachments\': 4531.0, \'avg_email_size\': 29953.61, \'off_hour_emails\': 1219.0, \'weekend_emails\': 2092.0, \'O\': 13.0, \'C\': 15.0, \'E\': 40.0, \'A\': 44.0, \'N\': 33.0}','Suspicious',92.5,'High','2026-03-01 00:47:15'),(3,'ajay','{\'total_emails\': 4711.0, \'total_attachments\': 1780.0, \'avg_email_size\': 30020.0, \'off_hour_emails\': 499.0, \'weekend_emails\': 0.0, \'O\': 36.0, \'C\': 30.0, \'E\': 14.0, \'A\': 50.0, \'N\': 29.0}','Normal',0,'Low','2026-03-02 12:35:58'),(4,'ajay','{\'total_emails\': 7519.0, \'total_attachments\': 4531.0, \'avg_email_size\': 29953.0, \'off_hour_emails\': 1219.0, \'weekend_emails\': 2092.0, \'O\': 13.0, \'C\': 15.0, \'E\': 40.0, \'A\': 18.0, \'N\': 27.0}','Suspicious',90,'High','2026-03-02 12:37:46'),(5,'ajay','{\'total_emails\': 4711.0, \'total_attachments\': 1780.0, \'avg_email_size\': 30020.0, \'off_hour_emails\': 499.0, \'weekend_emails\': 0.0, \'O\': 36.0, \'C\': 30.0, \'E\': 14.0, \'A\': 50.0, \'N\': 29.0}','Normal',0,'Low','2026-03-04 12:17:14'),(6,'vinay','{\'total_emails\': 4711.0, \'total_attachments\': 1780.0, \'avg_email_size\': 30020.0, \'off_hour_emails\': 499.0, \'weekend_emails\': 0.0, \'O\': 36.0, \'C\': 30.0, \'E\': 14.0, \'A\': 50.0, \'N\': 29.0}','Normal',0,'Low','2026-03-04 13:40:04'),(7,'bhagyashree','{\'total_emails\': 7519.0, \'total_attachments\': 4531.0, \'avg_email_size\': 29953.0, \'off_hour_emails\': 1219.0, \'weekend_emails\': 2092.0, \'O\': 13.0, \'C\': 15.0, \'E\': 40.0, \'A\': 44.0, \'N\': 33.0}','Suspicious',91.5,'High','2026-03-11 15:49:00'),(8,'bhagyashree','{\'total_emails\': 7519.0, \'total_attachments\': 4531.0, \'avg_email_size\': 29953.0, \'off_hour_emails\': 1219.0, \'weekend_emails\': 2092.0, \'O\': 13.0, \'C\': 15.0, \'E\': 40.0, \'A\': 44.0, \'N\': 33.0}','Suspicious',91.5,'High','2026-03-11 16:21:12'),(9,'bhagyashree','{\'total_emails\': 7519.0, \'total_attachments\': 4531.0, \'avg_email_size\': 29953.61, \'off_hour_emails\': 1219.0, \'weekend_emails\': 2092.0, \'O\': 13.0, \'C\': 15.0, \'E\': 40.0, \'A\': 44.0, \'N\': 33.0}','Suspicious',92.5,'High','2026-03-11 16:21:59'),(10,'bhagyashree','{\'total_emails\': 7519.0, \'total_attachments\': 4531.0, \'avg_email_size\': 29953.61, \'off_hour_emails\': 1219.0, \'weekend_emails\': 2092.0, \'O\': 13.0, \'C\': 15.0, \'E\': 40.0, \'A\': 44.0, \'N\': 33.0}','Suspicious',92.5,'High','2026-03-11 16:24:23'),(11,'bhagyashree','{\'total_emails\': 7519.0, \'total_attachments\': 4531.0, \'avg_email_size\': 29953.61, \'off_hour_emails\': 1219.0, \'weekend_emails\': 2092.0, \'O\': 13.0, \'C\': 15.0, \'E\': 40.0, \'A\': 44.0, \'N\': 33.0}','Suspicious',92.5,'High','2026-03-11 16:37:01');
/*!40000 ALTER TABLE `predictions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` varchar(50) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `role` enum('admin','user') DEFAULT NULL,
  `security_question` varchar(255) DEFAULT NULL,
  `security_answer` varchar(255) DEFAULT NULL,
  `status` enum('active','archived') DEFAULT 'active',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('admin','admin@gmail.com','admin','admin','admin_q','admin_a','active'),('ajay','ajay@gmail.com','123456','user','animal','dog','active'),('bhagyashree','bhagyashree@savantis.com','123456','user','animal','dog','active'),('naresh','naresh@savantis.com','123456','user','animal','dog','active'),('noore','noore@savantis.com','123456','user','animal','dog','active'),('santhosh','santhosh@savantis.com','123456','user','animal','dog','active'),('shiva','ajay@savantis.com','123456','user','animal','dog','active'),('vinay','vinay@savantis.com','123456','user','animal','dog','active');
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

-- Dump completed on 2026-03-11 17:15:06
