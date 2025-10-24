""" Create a DB Schema + Tables Webpage Notes 
    -> outline
        -> introduction
        -> how to create a database schema in MySQL
            -> a database schema refers to how the tables in a relational database are connected
                -> e.g, by their columns
        -> how to add a table using MySQL: create table
            -> MySQL is an application for Relational Database Management (RDBMS)
            -> the language it uses to query the database is SQL (Structured Query Language)
            -> MySQL can be run in the CLI, or using an open-source application called MySQL Workbench
                -> this contains a GUI
        -> Summary: create a database schema and table in MySQL
    -> we are following the instructions on the course webpage, at: https://codingnomads.com/mysql-create-database-schema-mysql-create-table-tutorial
    -> this tutorial use MySQL Workbench
        -> this uses a GUI
    -> it is equivalent to running MySQL in the terminal, which asks for SQL commands
        -> and then running this entire SQL script in it (they give this to you at the end of the tutorial webpage):

            CREATE DATABASE  IF NOT EXISTS SocialDB /*!40100 DEFAULT CHARACTER SET latin1 */;
            USE SocialDB;
            -- Host: 127.0.0.1    Database: SocialDB
            --------------------------------------------------------
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
            -- Table structure for table Images
            --
            DROP TABLE IF EXISTS Images;
            /*!40101 SET @saved_cs_client     = @@character_set_client */;
            /*!40101 SET character_set_client = utf8 */;
            CREATE TABLE Images (
            ImageId int(11) NOT NULL AUTO_INCREMENT,
            ImageURL varchar(250) NOT NULL,
            Date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            PRIMARY KEY (ImageId)
            ) ENGINE=InnoDB DEFAULT CHARSET=latin1;
            /*!40101 SET character_set_client = @saved_cs_client */;
            --
            -- Dumping data for table Images
            --
            LOCK TABLES Images WRITE;
            /*!40000 ALTER TABLE Images DISABLE KEYS */;
            /*!40000 ALTER TABLE Images ENABLE KEYS */;
            UNLOCK TABLES;
            --
            -- Table structure for table Posts
            --
            DROP TABLE IF EXISTS Posts;
            /*!40101 SET @saved_cs_client     = @@character_set_client */;
            /*!40101 SET character_set_client = utf8 */;
            CREATE TABLE `Posts` (
            `PostId` int(11) NOT NULL AUTO_INCREMENT,
            `UserId` int(11) NOT NULL,
            `PostText` blob NOT NULL,
            `ImageId` int(11) DEFAULT NULL,
            `Date` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            PRIMARY KEY (`PostId`),
            KEY `UserId_idx` (`UserId`),
            CONSTRAINT `UserId` FOREIGN KEY (`UserId`) REFERENCES `Users` (`UserId`) ON DELETE CASCADE ON UPDATE CASCADE
            ) ENGINE=InnoDB DEFAULT CHARSET=latin1;
            /*!40101 SET character_set_client = @saved_cs_client */;
            --
            -- Dumping data for table `Posts`
            --
            LOCK TABLES `Posts` WRITE;
            /*!40000 ALTER TABLE `Posts` DISABLE KEYS */;
            /*!40000 ALTER TABLE `Posts` ENABLE KEYS */;
            UNLOCK TABLES;
            --
            -- Table structure for table `Users`
            --
            DROP TABLE IF EXISTS `Users`;
            /*!40101 SET @saved_cs_client     = @@character_set_client */;
            /*!40101 SET character_set_client = utf8 */;
            CREATE TABLE `Users` (
            `UserId` int(11) NOT NULL AUTO_INCREMENT,
            `FirstName` varchar(100) NOT NULL,
            `LastName` varchar(100) NOT NULL,
            `Email` varchar(100) NOT NULL,
            `DateCreated` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            PRIMARY KEY (`UserId`)
            ) ENGINE=InnoDB DEFAULT CHARSET=latin1;
            /*!40101 SET character_set_client = @saved_cs_client */;
            --
            -- Dumping data for table `Users`
            --
            LOCK TABLES `Users` WRITE;
            /*!40000 ALTER TABLE `Users` DISABLE KEYS */;
            /*!40000 ALTER TABLE `Users` ENABLE KEYS */;
            UNLOCK TABLES;
            --
            -- Table structure for table `Users_Friends`
            --
            DROP TABLE IF EXISTS `Users_Friends`;
            /*!40101 SET @saved_cs_client     = @@character_set_client */;
            /*!40101 SET character_set_client = utf8 */;
            CREATE TABLE `Users_Friends` (
            `Id` int(11) NOT NULL AUTO_INCREMENT,
            `UserId_1` int(11) NOT NULL,
            `UserId_2` int(11) NOT NULL,
            `Date` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            PRIMARY KEY (`Id`),
            KEY `UserId_1_idx` (`UserId_1`),
            KEY `UserId_2_idx` (`UserId_2`),
            CONSTRAINT `UserId_1` FOREIGN KEY (`UserId_1`) REFERENCES `Users` (`UserId`) ON DELETE CASCADE ON UPDATE CASCADE,
            CONSTRAINT `UserId_2` FOREIGN KEY (`UserId_2`) REFERENCES `Users` (`UserId`) ON DELETE CASCADE ON UPDATE CASCADE
            ) ENGINE=InnoDB DEFAULT CHARSET=latin1;
            /*!40101 SET character_set_client = @saved_cs_client */;
            --
            -- Dumping data for table `Users_Friends`
            --
            LOCK TABLES `Users_Friends` WRITE;
            /*!40000 ALTER TABLE `Users_Friends` DISABLE KEYS */;
            /*!40000 ALTER TABLE `Users_Friends` ENABLE KEYS */;
            UNLOCK TABLES;
            /*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;
            /*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
            /*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
            /*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
            /*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
            /*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
            /*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
            /*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
"""