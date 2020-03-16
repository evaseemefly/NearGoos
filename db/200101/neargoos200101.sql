-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: neargoos
-- ------------------------------------------------------
-- Server version	5.7.17-log

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
-- Table structure for table `area_category_association`
--

DROP TABLE IF EXISTS `area_category_association`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `area_category_association` (
  `aid` int(11) NOT NULL,
  `tid` int(11) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `FK_ASSOCIATION_AREA` (`aid`) USING BTREE,
  KEY `FK_ASSOCIATION_CATEGORY` (`tid`) USING BTREE,
  CONSTRAINT `FK_ASSOCIATION_AREA` FOREIGN KEY (`aid`) REFERENCES `common_area` (`id`),
  CONSTRAINT `FK_ASSOCIATION_TYPE` FOREIGN KEY (`tid`) REFERENCES `product_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPACT;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `area_category_association`
--

LOCK TABLES `area_category_association` WRITE;
/*!40000 ALTER TABLE `area_category_association` DISABLE KEYS */;
INSERT INTO `area_category_association` VALUES (1,1,1),(2,1,2),(3,2,3),(2,2,4),(4,2,5),(5,3,6),(2,4,7),(3,4,8),(4,5,9);
/*!40000 ALTER TABLE `area_category_association` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `common_area`
--

DROP TABLE IF EXISTS `common_area`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `common_area` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pid` int(11) DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  `remark` varchar(300) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPACT;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `common_area`
--

LOCK TABLES `common_area` WRITE;
/*!40000 ALTER TABLE `common_area` DISABLE KEYS */;
INSERT INTO `common_area` VALUES (1,NULL,'ChinaSea','中国海'),(2,NULL,'Northwest',NULL),(3,NULL,'EastChinaSea',NULL),(4,NULL,'FarEast',NULL),(5,NULL,'Bohai',NULL);
/*!40000 ALTER TABLE `common_area` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `content_base_association`
--

DROP TABLE IF EXISTS `content_base_association`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `content_base_association` (
  `bid` int(255) NOT NULL,
  `cid` int(11) NOT NULL,
  PRIMARY KEY (`bid`,`cid`) USING BTREE,
  KEY `fk_content_base_bid` (`bid`) USING BTREE,
  KEY `fk_content_base_contentid` (`cid`) USING BTREE,
  CONSTRAINT `fk_content_base_bid` FOREIGN KEY (`bid`) REFERENCES `document_base` (`id`),
  CONSTRAINT `fk_content_base_contentid` FOREIGN KEY (`cid`) REFERENCES `document_content` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `content_base_association`
--

LOCK TABLES `content_base_association` WRITE;
/*!40000 ALTER TABLE `content_base_association` DISABLE KEYS */;
INSERT INTO `content_base_association` VALUES (1,1),(1,2),(1,3),(2,1);
/*!40000 ALTER TABLE `content_base_association` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `data_overview`
--

DROP TABLE IF EXISTS `data_overview`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `data_overview` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `gmt_create` datetime NOT NULL COMMENT '创建时间',
  `gmt_modified` datetime NOT NULL COMMENT '更新时间',
  `content` varchar(3000) DEFAULT NULL,
  `title` varchar(100) DEFAULT NULL,
  `is_delete` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data_overview`
--

LOCK TABLES `data_overview` WRITE;
/*!40000 ALTER TABLE `data_overview` DISABLE KEYS */;
INSERT INTO `data_overview` VALUES (1,'2019-10-10 10:22:55','2019-10-10 10:22:55','新测试屈远','标题',0);
/*!40000 ALTER TABLE `data_overview` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `document_base`
--

DROP TABLE IF EXISTS `document_base`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `document_base` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `is_del` tinyint(1) DEFAULT NULL,
  `pid` int(11) DEFAULT NULL,
  `page_area` varchar(45) DEFAULT NULL,
  `gmt_create` datetime DEFAULT NULL,
  `gmt_modified` datetime DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `document_base`
--

LOCK TABLES `document_base` WRITE;
/*!40000 ALTER TABLE `document_base` DISABLE KEYS */;
INSERT INTO `document_base` VALUES (1,'base_1',NULL,NULL,NULL,NULL,NULL),(2,'base_2',NULL,NULL,NULL,NULL,NULL),(3,'base_3',NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `document_base` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `document_content`
--

DROP TABLE IF EXISTS `document_content`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `document_content` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `document` varchar(100) DEFAULT NULL,
  `gmt_create` datetime DEFAULT NULL,
  `gmt_modified` datetime DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `document_content`
--

LOCK TABLES `document_content` WRITE;
/*!40000 ALTER TABLE `document_content` DISABLE KEYS */;
INSERT INTO `document_content` VALUES (1,'content_1',NULL,NULL,NULL),(2,'content_2',NULL,NULL,NULL),(3,'content_3',NULL,NULL,NULL);
/*!40000 ALTER TABLE `document_content` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `document_image`
--

DROP TABLE IF EXISTS `document_image`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `document_image` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `image_url` varchar(100) DEFAULT NULL,
  `image_heigh` float DEFAULT NULL,
  `image_width` float DEFAULT NULL,
  `gmt_create` datetime DEFAULT NULL,
  `gmt_modified` datetime DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `document_image`
--

LOCK TABLES `document_image` WRITE;
/*!40000 ALTER TABLE `document_image` DISABLE KEYS */;
INSERT INTO `document_image` VALUES (1,'image_1',NULL,NULL,NULL,NULL,NULL),(2,'image_2',NULL,NULL,NULL,NULL,NULL),(3,'image_3',NULL,NULL,NULL,NULL,NULL),(4,'image_4',NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `document_image` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `document_tab`
--

DROP TABLE IF EXISTS `document_tab`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `document_tab` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `view_name` varchar(45) DEFAULT NULL,
  `url` varchar(45) DEFAULT NULL,
  `id_del` tinyint(1) DEFAULT NULL,
  `icon` varchar(45) DEFAULT NULL,
  `image_url` varchar(45) DEFAULT NULL,
  `image_height` varchar(45) DEFAULT NULL,
  `image_width` varchar(45) DEFAULT NULL,
  `level` int(11) DEFAULT NULL,
  `pid` int(11) DEFAULT NULL,
  `gmt_create` datetime DEFAULT NULL,
  `gmt_modified` datetime DEFAULT NULL,
  `dbid` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `tab_base` (`dbid`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `document_tab`
--

LOCK TABLES `document_tab` WRITE;
/*!40000 ALTER TABLE `document_tab` DISABLE KEYS */;
INSERT INTO `document_tab` VALUES (1,'测试',NULL,NULL,NULL,NULL,NULL,NULL,NULL,1,NULL,'2019-10-14 14:54:26','2019-10-14 14:54:26',NULL),(2,'tab_1',NULL,NULL,NULL,NULL,NULL,NULL,NULL,1,NULL,'2019-10-18 15:24:12','2019-10-18 15:24:14',NULL),(3,'tab_1_1',NULL,NULL,NULL,NULL,NULL,NULL,NULL,2,2,'2019-10-18 15:24:44','2019-10-18 15:24:46',NULL),(4,'tab_1_2',NULL,NULL,NULL,NULL,NULL,NULL,NULL,2,2,NULL,NULL,NULL),(5,'tab_2',NULL,NULL,NULL,NULL,NULL,NULL,NULL,1,NULL,NULL,NULL,NULL),(6,'tab_2_1',NULL,NULL,NULL,NULL,NULL,NULL,NULL,2,2,NULL,NULL,NULL);
/*!40000 ALTER TABLE `document_tab` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `document_title`
--

DROP TABLE IF EXISTS `document_title`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `document_title` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `is_del` tinyint(1) DEFAULT NULL,
  `title_content` varchar(45) DEFAULT NULL,
  `gmt_create` datetime DEFAULT NULL,
  `gmt_modified` datetime DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `document_title`
--

LOCK TABLES `document_title` WRITE;
/*!40000 ALTER TABLE `document_title` DISABLE KEYS */;
/*!40000 ALTER TABLE `document_title` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `image_base_association`
--

DROP TABLE IF EXISTS `image_base_association`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `image_base_association` (
  `bid` int(11) NOT NULL,
  `imageid` int(11) NOT NULL,
  PRIMARY KEY (`bid`,`imageid`) USING BTREE,
  KEY `fk_base_image_imageid` (`imageid`) USING BTREE,
  KEY `fk_base_image_bid` (`bid`) USING BTREE,
  CONSTRAINT `fk_base_image_bid` FOREIGN KEY (`bid`) REFERENCES `document_base` (`id`),
  CONSTRAINT `fk_base_image_imageid` FOREIGN KEY (`imageid`) REFERENCES `document_image` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `image_base_association`
--

LOCK TABLES `image_base_association` WRITE;
/*!40000 ALTER TABLE `image_base_association` DISABLE KEYS */;
INSERT INTO `image_base_association` VALUES (1,1),(1,2),(2,3),(3,3),(3,4);
/*!40000 ALTER TABLE `image_base_association` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `management_action`
--

DROP TABLE IF EXISTS `management_action`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `management_action` (
  `name` varchar(20) NOT NULL,
  `sort` int(11) NOT NULL DEFAULT '999',
  `remark` varchar(100) DEFAULT NULL,
  `gmt_create` datetime DEFAULT NULL,
  `gmt_modified` datetime DEFAULT NULL,
  `parent_id` int(11) NOT NULL DEFAULT '0',
  `url` varchar(255) NOT NULL,
  `area_name` varchar(32) DEFAULT NULL,
  `method_name` varchar(32) DEFAULT NULL,
  `controller_name` varchar(32) DEFAULT NULL,
  `js_function_name` varchar(32) DEFAULT NULL,
  `type_enum` int(11) NOT NULL,
  `menu_icon` varchar(32) NOT NULL,
  `icon_width` int(11) NOT NULL,
  `icon_height` int(11) NOT NULL,
  `icon_cls` varchar(32) DEFAULT NULL,
  `icon_class_name` varchar(32) DEFAULT NULL,
  `is_show` tinyint(1) NOT NULL DEFAULT '1',
  `method_type_enum` int(11) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `url` (`url`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `management_action`
--

LOCK TABLES `management_action` WRITE;
/*!40000 ALTER TABLE `management_action` DISABLE KEYS */;
INSERT INTO `management_action` VALUES ('测试权限',999,NULL,'2019-02-28 19:00:23','2019-02-28 19:00:23',0,'safasg',NULL,NULL,NULL,NULL,2,'hh',2,3,NULL,NULL,1,5,1),('测试新增',999,NULL,'2019-03-10 00:31:32','2019-03-10 00:31:34',0,'user/add',NULL,NULL,NULL,NULL,2,'add',2,2,NULL,NULL,1,2,2),('测试删除',999,NULL,'2019-03-10 00:38:15','2019-03-10 00:38:17',0,'user/del',NULL,NULL,NULL,NULL,2,'del',2,2,NULL,NULL,1,3,3),('测试查看权限',999,NULL,'2019-03-10 00:40:06','2019-03-10 00:40:09',0,'user/view',NULL,NULL,NULL,NULL,3,'view',3,3,NULL,NULL,1,3,4),('权限',999,NULL,'2019-08-23 10:27:45','2019-08-23 10:27:45',0,'sad','asd','asd',NULL,NULL,123,'adf',123,123,NULL,NULL,1,123,5),('新测试屈远',999,NULL,'2019-09-25 20:29:46','2019-09-25 20:29:46',0,'sdsdasd','aa','dd',NULL,NULL,35,'aa',4,5,NULL,NULL,1,5555,6);
/*!40000 ALTER TABLE `management_action` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `management_role`
--

DROP TABLE IF EXISTS `management_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `management_role` (
  `name` varchar(20) NOT NULL,
  `remark` varchar(100) DEFAULT NULL,
  `sort` int(11) NOT NULL DEFAULT '999',
  `gmt_create` datetime DEFAULT NULL,
  `gmt_modified` datetime DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `management_role`
--

LOCK TABLES `management_role` WRITE;
/*!40000 ALTER TABLE `management_role` DISABLE KEYS */;
INSERT INTO `management_role` VALUES ('系统管理员',NULL,999,'2019-02-25 16:09:47','2019-02-25 16:09:47',1),('部门领导',NULL,999,'2019-02-25 16:10:27','2019-02-25 16:10:27',2),('组长',NULL,999,'2019-02-26 15:28:14','2019-02-26 15:28:14',3),('组员',NULL,999,'2019-02-26 18:37:39','2019-02-26 18:37:39',4);
/*!40000 ALTER TABLE `management_role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `management_user`
--

DROP TABLE IF EXISTS `management_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `management_user` (
  `account` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `is_delete` tinyint(1) NOT NULL DEFAULT '0',
  `sort` int(11) NOT NULL DEFAULT '999',
  `remark` varchar(100) DEFAULT NULL,
  `gmt_create` datetime DEFAULT NULL,
  `gmt_modified` datetime DEFAULT NULL,
  `name` varchar(20) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `is_locked` tinyint(1) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `account` (`account`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `management_user`
--

LOCK TABLES `management_user` WRITE;
/*!40000 ALTER TABLE `management_user` DISABLE KEYS */;
INSERT INTO `management_user` VALUES ('aabbcc','2312421',1,44,NULL,'2019-02-23 23:23:35','2019-02-24 15:31:13','测试',7,0),('aabcc12','2312421',0,44,NULL,'2019-02-24 15:00:17','2019-02-24 15:00:17','屈远测试',8,0),('aabbcc222','2312421',0,44,NULL,'2019-02-24 21:53:53','2019-02-24 21:53:53','测试',9,0),('aabbcc22255','2312421',0,44,NULL,'2019-02-25 12:29:49','2019-02-25 12:29:49','测试测试测试',10,0),('wangdong','38964',0,999,NULL,'2019-02-27 00:04:18','2019-02-27 00:04:18','大为',11,0),('wangdouu8ng','38964',0,999,NULL,'2019-02-27 00:13:24','2019-02-27 00:13:24','大为',12,0),('hhhhh8ng','38964',0,999,NULL,'2019-02-27 00:21:53','2019-02-27 00:21:53','我是为',13,0),('hhhhttth8ng','38964',0,999,NULL,'2019-02-27 00:42:07','2019-02-27 00:42:07','我是屈远',14,0),('quyuan','111111',0,999,NULL,'2019-02-27 01:37:26','2019-02-27 13:28:48','希罗测试金卡会员',15,0),('hahaha','889211',0,999,NULL,'2019-02-27 13:30:11','2019-02-27 13:35:58','希罗测试管理员',16,0);
/*!40000 ALTER TABLE `management_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `type` int(11) DEFAULT NULL,
  `area` int(11) DEFAULT NULL,
  `interval` int(255) DEFAULT NULL,
  `image_url` varchar(255) DEFAULT NULL,
  `target_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,'current',0,1,24,'xxx.jpg','2019-10-05 16:00:00'),(2,'ice',1,2,24,'xxx1.jpg','2019-10-05 16:00:00');
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_info`
--

DROP TABLE IF EXISTS `product_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product_info` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `area` int(11) DEFAULT NULL,
  `interval` int(11) DEFAULT NULL,
  `image_url` varchar(45) DEFAULT NULL,
  `target_date` timestamp NULL DEFAULT NULL,
  `gmt_create` timestamp NULL DEFAULT NULL,
  `gmt_modified` timestamp NULL DEFAULT NULL,
  `type` int(11) DEFAULT NULL,
  `relative_path` varchar(255) DEFAULT NULL,
  `root_path` varchar(255) DEFAULT NULL,
  `file_name` varchar(255) DEFAULT NULL,
  `ext` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=145 DEFAULT CHARSET=latin1 ROW_FORMAT=COMPACT;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_info`
--

LOCK TABLES `product_info` WRITE;
/*!40000 ALTER TABLE `product_info` DISABLE KEYS */;
INSERT INTO `product_info` VALUES (73,'coast04.png',1,4,'D:\\03data\\neargoos\\wave\\2019\\12\\13','2019-12-12 18:25:01','2019-12-12 18:25:00','2019-12-12 18:25:00',1,'2019\\12\\13','D:\\03data\\neargoos\\wave','coast04.png',NULL),(74,'coast08.png',1,8,'D:\\03data\\neargoos\\wave\\2019\\12\\13','2019-12-12 18:25:01','2019-12-12 18:25:00','2019-12-12 18:25:00',1,'2019\\12\\13','D:\\03data\\neargoos\\wave','coast08.png',NULL),(75,'coast12.png',1,12,'D:\\03data\\neargoos\\wave\\2019\\12\\13','2019-12-12 18:25:01','2019-12-12 18:25:00','2019-12-12 18:25:00',1,'2019\\12\\13','D:\\03data\\neargoos\\wave','coast12.png',NULL),(76,'coast16.png',1,16,'D:\\03data\\neargoos\\wave\\2019\\12\\13','2019-12-12 18:25:01','2019-12-12 18:25:00','2019-12-12 18:25:00',1,'2019\\12\\13','D:\\03data\\neargoos\\wave','coast16.png',NULL),(77,'coast20.png',1,20,'D:\\03data\\neargoos\\wave\\2019\\12\\13','2019-12-12 18:25:01','2019-12-12 18:25:00','2019-12-12 18:25:00',1,'2019\\12\\13','D:\\03data\\neargoos\\wave','coast20.png',NULL),(78,'xb04.png',2,4,'D:\\03data\\neargoos\\wave\\2019\\12\\13','2019-12-12 18:25:01','2019-12-12 18:25:00','2019-12-12 18:25:00',1,'2019\\12\\13','D:\\03data\\neargoos\\wave','xb04.png',NULL),(79,'xb08.png',2,8,'D:\\03data\\neargoos\\wave\\2019\\12\\13','2019-12-12 18:25:01','2019-12-12 18:25:00','2019-12-12 18:25:00',1,'2019\\12\\13','D:\\03data\\neargoos\\wave','xb08.png',NULL),(80,'xb12.png',2,12,'D:\\03data\\neargoos\\wave\\2019\\12\\13','2019-12-12 18:25:02','2019-12-12 18:25:00','2019-12-12 18:25:00',1,'2019\\12\\13','D:\\03data\\neargoos\\wave','xb12.png',NULL),(81,'xb16.png',2,16,'D:\\03data\\neargoos\\wave\\2019\\12\\13','2019-12-12 18:25:02','2019-12-12 18:25:00','2019-12-12 18:25:00',1,'2019\\12\\13','D:\\03data\\neargoos\\wave','xb16.png',NULL),(82,'xb20.png',2,20,'D:\\03data\\neargoos\\wave\\2019\\12\\13','2019-12-12 18:25:02','2019-12-12 18:25:00','2019-12-12 18:25:00',1,'2019\\12\\13','D:\\03data\\neargoos\\wave','xb20.png',NULL),(83,'sped-top-024.jpg',3,24,'D:\\03data\\neargoos\\current\\2019\\12\\13','2019-12-12 18:25:02','2019-12-12 18:25:00','2019-12-12 18:25:00',2,'2019\\12\\13','D:\\03data\\neargoos\\current','sped-top-024.jpg',NULL),(84,'sped-top-048.jpg',3,48,'D:\\03data\\neargoos\\current\\2019\\12\\13','2019-12-12 18:25:02','2019-12-12 18:25:00','2019-12-12 18:25:00',2,'2019\\12\\13','D:\\03data\\neargoos\\current','sped-top-048.jpg',NULL),(85,'sped-top-072.jpg',3,72,'D:\\03data\\neargoos\\current\\2019\\12\\13','2019-12-12 18:25:02','2019-12-12 18:25:00','2019-12-12 18:25:00',2,'2019\\12\\13','D:\\03data\\neargoos\\current','sped-top-072.jpg',NULL),(86,'sped-top-096.jpg',3,96,'D:\\03data\\neargoos\\current\\2019\\12\\13','2019-12-12 18:25:02','2019-12-12 18:25:00','2019-12-12 18:25:00',2,'2019\\12\\13','D:\\03data\\neargoos\\current','sped-top-096.jpg',NULL),(87,'sped-top-120.jpg',3,120,'D:\\03data\\neargoos\\current\\2019\\12\\13','2019-12-12 18:25:02','2019-12-12 18:25:00','2019-12-12 18:25:00',2,'2019\\12\\13','D:\\03data\\neargoos\\current','sped-top-120.jpg',NULL),(88,'048_UV_0000.png',2,48,'D:\\03data\\neargoos\\current\\2019\\12\\13','2019-12-12 18:25:02','2019-12-12 18:25:00','2019-12-12 18:25:00',2,'2019\\12\\13','D:\\03data\\neargoos\\current','048_UV_0000.png',NULL),(89,'cur_NMEFC_near_goos_00Hr.png',4,0,'D:\\03data\\neargoos\\current\\2019\\12\\13','2019-12-12 18:25:03','2019-12-12 18:25:00','2019-12-12 18:25:00',2,'2019\\12\\13','D:\\03data\\neargoos\\current','cur_NMEFC_near_goos_00Hr.png',NULL),(90,'cur_NMEFC_near_goos_03Hr.png',4,3,'D:\\03data\\neargoos\\current\\2019\\12\\13','2019-12-12 18:25:03','2019-12-12 18:25:00','2019-12-12 18:25:00',2,'2019\\12\\13','D:\\03data\\neargoos\\current','cur_NMEFC_near_goos_03Hr.png',NULL),(91,'cur_NMEFC_near_goos_06Hr.png',4,6,'D:\\03data\\neargoos\\current\\2019\\12\\13','2019-12-12 18:25:03','2019-12-12 18:25:00','2019-12-12 18:25:00',2,'2019\\12\\13','D:\\03data\\neargoos\\current','cur_NMEFC_near_goos_06Hr.png',NULL),(92,'cur_NMEFC_near_goos_09Hr.png',4,9,'D:\\03data\\neargoos\\current\\2019\\12\\13','2019-12-12 18:25:03','2019-12-12 18:25:00','2019-12-12 18:25:00',2,'2019\\12\\13','D:\\03data\\neargoos\\current','cur_NMEFC_near_goos_09Hr.png',NULL),(93,'cur_NMEFC_near_goos_12Hr.png',4,12,'D:\\03data\\neargoos\\current\\2019\\12\\13','2019-12-12 18:25:03','2019-12-12 18:25:00','2019-12-12 18:25:00',2,'2019\\12\\13','D:\\03data\\neargoos\\current','cur_NMEFC_near_goos_12Hr.png',NULL),(94,'cur_NMEFC_near_goos_15Hr.png',4,15,'D:\\03data\\neargoos\\current\\2019\\12\\13','2019-12-12 18:25:03','2019-12-12 18:25:00','2019-12-12 18:25:00',2,'2019\\12\\13','D:\\03data\\neargoos\\current','cur_NMEFC_near_goos_15Hr.png',NULL),(95,'cur_NMEFC_near_goos_18Hr.png',4,18,'D:\\03data\\neargoos\\current\\2019\\12\\13','2019-12-12 18:25:03','2019-12-12 18:25:00','2019-12-12 18:25:00',2,'2019\\12\\13','D:\\03data\\neargoos\\current','cur_NMEFC_near_goos_18Hr.png',NULL),(96,'cur_NMEFC_near_goos_21Hr.png',4,21,'D:\\03data\\neargoos\\current\\2019\\12\\13','2019-12-12 18:25:03','2019-12-12 18:25:00','2019-12-12 18:25:00',2,'2019\\12\\13','D:\\03data\\neargoos\\current','cur_NMEFC_near_goos_21Hr.png',NULL),(97,'cur_NMEFC_near_goos_24Hr.png',4,24,'D:\\03data\\neargoos\\current\\2019\\12\\13','2019-12-12 18:25:03','2019-12-12 18:25:00','2019-12-12 18:25:00',2,'2019\\12\\13','D:\\03data\\neargoos\\current','cur_NMEFC_near_goos_24Hr.png',NULL),(98,'cur_NMEFC_near_goos_27Hr.png',4,27,'D:\\03data\\neargoos\\current\\2019\\12\\13','2019-12-12 18:25:03','2019-12-12 18:25:00','2019-12-12 18:25:00',2,'2019\\12\\13','D:\\03data\\neargoos\\current','cur_NMEFC_near_goos_27Hr.png',NULL),(99,'cur_NMEFC_near_goos_30Hr.png',4,30,'D:\\03data\\neargoos\\current\\2019\\12\\13','2019-12-12 18:25:03','2019-12-12 18:25:00','2019-12-12 18:25:00',2,'2019\\12\\13','D:\\03data\\neargoos\\current','cur_NMEFC_near_goos_30Hr.png',NULL),(100,'cur_NMEFC_near_goos_33Hr.png',4,33,'D:\\03data\\neargoos\\current\\2019\\12\\13','2019-12-12 18:25:03','2019-12-12 18:25:00','2019-12-12 18:25:00',2,'2019\\12\\13','D:\\03data\\neargoos\\current','cur_NMEFC_near_goos_33Hr.png',NULL),(101,'cur_NMEFC_near_goos_36Hr.png',4,36,'D:\\03data\\neargoos\\current\\2019\\12\\13','2019-12-12 18:25:03','2019-12-12 18:25:00','2019-12-12 18:25:00',2,'2019\\12\\13','D:\\03data\\neargoos\\current','cur_NMEFC_near_goos_36Hr.png',NULL),(102,'cur_NMEFC_near_goos_39Hr.png',4,39,'D:\\03data\\neargoos\\current\\2019\\12\\13','2019-12-12 18:25:03','2019-12-12 18:25:00','2019-12-12 18:25:00',2,'2019\\12\\13','D:\\03data\\neargoos\\current','cur_NMEFC_near_goos_39Hr.png',NULL),(103,'cur_NMEFC_near_goos_42Hr.png',4,42,'D:\\03data\\neargoos\\current\\2019\\12\\13','2019-12-12 18:25:03','2019-12-12 18:25:00','2019-12-12 18:25:00',2,'2019\\12\\13','D:\\03data\\neargoos\\current','cur_NMEFC_near_goos_42Hr.png',NULL),(104,'cur_NMEFC_near_goos_45Hr.png',4,45,'D:\\03data\\neargoos\\current\\2019\\12\\13','2019-12-12 18:25:03','2019-12-12 18:25:00','2019-12-12 18:25:00',2,'2019\\12\\13','D:\\03data\\neargoos\\current','cur_NMEFC_near_goos_45Hr.png',NULL),(105,'cur_NMEFC_near_goos_48Hr.png',4,48,'D:\\03data\\neargoos\\current\\2019\\12\\13','2019-12-12 18:25:03','2019-12-12 18:25:00','2019-12-12 18:25:00',2,'2019\\12\\13','D:\\03data\\neargoos\\current','cur_NMEFC_near_goos_48Hr.png',NULL),(106,'cur_NMEFC_near_goos_51Hr.png',4,51,'D:\\03data\\neargoos\\current\\2019\\12\\13','2019-12-12 18:25:03','2019-12-12 18:25:00','2019-12-12 18:25:00',2,'2019\\12\\13','D:\\03data\\neargoos\\current','cur_NMEFC_near_goos_51Hr.png',NULL),(107,'cur_NMEFC_near_goos_54Hr.png',4,54,'D:\\03data\\neargoos\\current\\2019\\12\\13','2019-12-12 18:25:03','2019-12-12 18:25:00','2019-12-12 18:25:00',2,'2019\\12\\13','D:\\03data\\neargoos\\current','cur_NMEFC_near_goos_54Hr.png',NULL),(108,'cur_NMEFC_near_goos_57Hr.png',4,57,'D:\\03data\\neargoos\\current\\2019\\12\\13','2019-12-12 18:25:04','2019-12-12 18:25:00','2019-12-12 18:25:00',2,'2019\\12\\13','D:\\03data\\neargoos\\current','cur_NMEFC_near_goos_57Hr.png',NULL),(109,'cur_NMEFC_near_goos_60Hr.png',4,60,'D:\\03data\\neargoos\\current\\2019\\12\\13','2019-12-12 18:25:04','2019-12-12 18:25:00','2019-12-12 18:25:00',2,'2019\\12\\13','D:\\03data\\neargoos\\current','cur_NMEFC_near_goos_60Hr.png',NULL),(110,'cur_NMEFC_near_goos_63Hr.png',4,63,'D:\\03data\\neargoos\\current\\2019\\12\\13','2019-12-12 18:25:04','2019-12-12 18:25:00','2019-12-12 18:25:00',2,'2019\\12\\13','D:\\03data\\neargoos\\current','cur_NMEFC_near_goos_63Hr.png',NULL),(111,'cur_NMEFC_near_goos_66Hr.png',4,66,'D:\\03data\\neargoos\\current\\2019\\12\\13','2019-12-12 18:25:04','2019-12-12 18:25:00','2019-12-12 18:25:00',2,'2019\\12\\13','D:\\03data\\neargoos\\current','cur_NMEFC_near_goos_66Hr.png',NULL),(112,'cur_NMEFC_near_goos_69Hr.png',4,69,'D:\\03data\\neargoos\\current\\2019\\12\\13','2019-12-12 18:25:04','2019-12-12 18:25:00','2019-12-12 18:25:00',2,'2019\\12\\13','D:\\03data\\neargoos\\current','cur_NMEFC_near_goos_69Hr.png',NULL),(113,'cur_NMEFC_near_goos_72Hr.png',4,72,'D:\\03data\\neargoos\\current\\2019\\12\\13','2019-12-12 18:25:04','2019-12-12 18:25:00','2019-12-12 18:25:00',2,'2019\\12\\13','D:\\03data\\neargoos\\current','cur_NMEFC_near_goos_72Hr.png',NULL),(114,'temp-top-024.jpg',3,24,'D:\\03data\\neargoos\\SST\\2019\\12\\13','2019-12-12 18:25:04','2019-12-12 18:25:00','2019-12-12 18:25:00',4,'2019\\12\\13','D:\\03data\\neargoos\\SST','temp-top-024.jpg',NULL),(115,'temp-top-048.jpg',3,48,'D:\\03data\\neargoos\\SST\\2019\\12\\13','2019-12-12 18:25:04','2019-12-12 18:25:00','2019-12-12 18:25:00',4,'2019\\12\\13','D:\\03data\\neargoos\\SST','temp-top-048.jpg',NULL),(116,'temp-top-072.jpg',3,72,'D:\\03data\\neargoos\\SST\\2019\\12\\13','2019-12-12 18:25:04','2019-12-12 18:25:00','2019-12-12 18:25:00',4,'2019\\12\\13','D:\\03data\\neargoos\\SST','temp-top-072.jpg',NULL),(117,'temp-top-096.jpg',3,96,'D:\\03data\\neargoos\\SST\\2019\\12\\13','2019-12-12 18:25:04','2019-12-12 18:25:00','2019-12-12 18:25:00',4,'2019\\12\\13','D:\\03data\\neargoos\\SST','temp-top-096.jpg',NULL),(118,'temp-top-120.jpg',3,120,'D:\\03data\\neargoos\\SST\\2019\\12\\13','2019-12-12 18:25:04','2019-12-12 18:25:00','2019-12-12 18:25:00',4,'2019\\12\\13','D:\\03data\\neargoos\\SST','temp-top-120.jpg',NULL),(119,'024_T_0000.png',2,24,'D:\\03data\\neargoos\\SST\\2019\\12\\13','2019-12-12 18:25:04','2019-12-12 18:25:00','2019-12-12 18:25:00',4,'2019\\12\\13','D:\\03data\\neargoos\\SST','024_T_0000.png',NULL),(120,'ssh_NMEFC_near_goos_00Hr.png',4,0,'D:\\03data\\neargoos\\SSH\\2019\\12\\13','2019-12-12 18:25:04','2019-12-12 18:25:00','2019-12-12 18:25:00',5,'2019\\12\\13','D:\\03data\\neargoos\\SSH','ssh_NMEFC_near_goos_00Hr.png',NULL),(121,'ssh_NMEFC_near_goos_03Hr.png',4,3,'D:\\03data\\neargoos\\SSH\\2019\\12\\13','2019-12-12 18:25:04','2019-12-12 18:25:00','2019-12-12 18:25:00',5,'2019\\12\\13','D:\\03data\\neargoos\\SSH','ssh_NMEFC_near_goos_03Hr.png',NULL),(122,'ssh_NMEFC_near_goos_06Hr.png',4,6,'D:\\03data\\neargoos\\SSH\\2019\\12\\13','2019-12-12 18:25:05','2019-12-12 18:25:00','2019-12-12 18:25:00',5,'2019\\12\\13','D:\\03data\\neargoos\\SSH','ssh_NMEFC_near_goos_06Hr.png',NULL),(123,'ssh_NMEFC_near_goos_09Hr.png',4,9,'D:\\03data\\neargoos\\SSH\\2019\\12\\13','2019-12-12 18:25:05','2019-12-12 18:25:00','2019-12-12 18:25:00',5,'2019\\12\\13','D:\\03data\\neargoos\\SSH','ssh_NMEFC_near_goos_09Hr.png',NULL),(124,'ssh_NMEFC_near_goos_12Hr.png',4,12,'D:\\03data\\neargoos\\SSH\\2019\\12\\13','2019-12-12 18:25:05','2019-12-12 18:25:00','2019-12-12 18:25:00',5,'2019\\12\\13','D:\\03data\\neargoos\\SSH','ssh_NMEFC_near_goos_12Hr.png',NULL),(125,'ssh_NMEFC_near_goos_15Hr.png',4,15,'D:\\03data\\neargoos\\SSH\\2019\\12\\13','2019-12-12 18:25:05','2019-12-12 18:25:00','2019-12-12 18:25:00',5,'2019\\12\\13','D:\\03data\\neargoos\\SSH','ssh_NMEFC_near_goos_15Hr.png',NULL),(126,'ssh_NMEFC_near_goos_18Hr.png',4,18,'D:\\03data\\neargoos\\SSH\\2019\\12\\13','2019-12-12 18:25:05','2019-12-12 18:25:00','2019-12-12 18:25:00',5,'2019\\12\\13','D:\\03data\\neargoos\\SSH','ssh_NMEFC_near_goos_18Hr.png',NULL),(127,'ssh_NMEFC_near_goos_21Hr.png',4,21,'D:\\03data\\neargoos\\SSH\\2019\\12\\13','2019-12-12 18:25:05','2019-12-12 18:25:00','2019-12-12 18:25:00',5,'2019\\12\\13','D:\\03data\\neargoos\\SSH','ssh_NMEFC_near_goos_21Hr.png',NULL),(128,'ssh_NMEFC_near_goos_24Hr.png',4,24,'D:\\03data\\neargoos\\SSH\\2019\\12\\13','2019-12-12 18:25:05','2019-12-12 18:25:00','2019-12-12 18:25:00',5,'2019\\12\\13','D:\\03data\\neargoos\\SSH','ssh_NMEFC_near_goos_24Hr.png',NULL),(129,'ssh_NMEFC_near_goos_27Hr.png',4,27,'D:\\03data\\neargoos\\SSH\\2019\\12\\13','2019-12-12 18:25:05','2019-12-12 18:25:00','2019-12-12 18:25:00',5,'2019\\12\\13','D:\\03data\\neargoos\\SSH','ssh_NMEFC_near_goos_27Hr.png',NULL),(130,'ssh_NMEFC_near_goos_30Hr.png',4,30,'D:\\03data\\neargoos\\SSH\\2019\\12\\13','2019-12-12 18:25:05','2019-12-12 18:25:00','2019-12-12 18:25:00',5,'2019\\12\\13','D:\\03data\\neargoos\\SSH','ssh_NMEFC_near_goos_30Hr.png',NULL),(131,'ssh_NMEFC_near_goos_33Hr.png',4,33,'D:\\03data\\neargoos\\SSH\\2019\\12\\13','2019-12-12 18:25:05','2019-12-12 18:25:00','2019-12-12 18:25:00',5,'2019\\12\\13','D:\\03data\\neargoos\\SSH','ssh_NMEFC_near_goos_33Hr.png',NULL),(132,'ssh_NMEFC_near_goos_36Hr.png',4,36,'D:\\03data\\neargoos\\SSH\\2019\\12\\13','2019-12-12 18:25:05','2019-12-12 18:25:00','2019-12-12 18:25:00',5,'2019\\12\\13','D:\\03data\\neargoos\\SSH','ssh_NMEFC_near_goos_36Hr.png',NULL),(133,'ssh_NMEFC_near_goos_39Hr.png',4,39,'D:\\03data\\neargoos\\SSH\\2019\\12\\13','2019-12-12 18:25:05','2019-12-12 18:25:00','2019-12-12 18:25:00',5,'2019\\12\\13','D:\\03data\\neargoos\\SSH','ssh_NMEFC_near_goos_39Hr.png',NULL),(134,'ssh_NMEFC_near_goos_42Hr.png',4,42,'D:\\03data\\neargoos\\SSH\\2019\\12\\13','2019-12-12 18:25:05','2019-12-12 18:25:00','2019-12-12 18:25:00',5,'2019\\12\\13','D:\\03data\\neargoos\\SSH','ssh_NMEFC_near_goos_42Hr.png',NULL),(135,'ssh_NMEFC_near_goos_45Hr.png',4,45,'D:\\03data\\neargoos\\SSH\\2019\\12\\13','2019-12-12 18:25:05','2019-12-12 18:25:00','2019-12-12 18:25:00',5,'2019\\12\\13','D:\\03data\\neargoos\\SSH','ssh_NMEFC_near_goos_45Hr.png',NULL),(136,'ssh_NMEFC_near_goos_48Hr.png',4,48,'D:\\03data\\neargoos\\SSH\\2019\\12\\13','2019-12-12 18:25:05','2019-12-12 18:25:00','2019-12-12 18:25:00',5,'2019\\12\\13','D:\\03data\\neargoos\\SSH','ssh_NMEFC_near_goos_48Hr.png',NULL),(137,'ssh_NMEFC_near_goos_51Hr.png',4,51,'D:\\03data\\neargoos\\SSH\\2019\\12\\13','2019-12-12 18:25:05','2019-12-12 18:25:00','2019-12-12 18:25:00',5,'2019\\12\\13','D:\\03data\\neargoos\\SSH','ssh_NMEFC_near_goos_51Hr.png',NULL),(138,'ssh_NMEFC_near_goos_54Hr.png',4,54,'D:\\03data\\neargoos\\SSH\\2019\\12\\13','2019-12-12 18:25:05','2019-12-12 18:25:00','2019-12-12 18:25:00',5,'2019\\12\\13','D:\\03data\\neargoos\\SSH','ssh_NMEFC_near_goos_54Hr.png',NULL),(139,'ssh_NMEFC_near_goos_57Hr.png',4,57,'D:\\03data\\neargoos\\SSH\\2019\\12\\13','2019-12-12 18:25:05','2019-12-12 18:25:00','2019-12-12 18:25:00',5,'2019\\12\\13','D:\\03data\\neargoos\\SSH','ssh_NMEFC_near_goos_57Hr.png',NULL),(140,'ssh_NMEFC_near_goos_60Hr.png',4,60,'D:\\03data\\neargoos\\SSH\\2019\\12\\13','2019-12-12 18:25:05','2019-12-12 18:25:00','2019-12-12 18:25:00',5,'2019\\12\\13','D:\\03data\\neargoos\\SSH','ssh_NMEFC_near_goos_60Hr.png',NULL),(141,'ssh_NMEFC_near_goos_63Hr.png',4,63,'D:\\03data\\neargoos\\SSH\\2019\\12\\13','2019-12-12 18:25:05','2019-12-12 18:25:00','2019-12-12 18:25:00',5,'2019\\12\\13','D:\\03data\\neargoos\\SSH','ssh_NMEFC_near_goos_63Hr.png',NULL),(142,'ssh_NMEFC_near_goos_66Hr.png',4,66,'D:\\03data\\neargoos\\SSH\\2019\\12\\13','2019-12-12 18:25:05','2019-12-12 18:25:00','2019-12-12 18:25:00',5,'2019\\12\\13','D:\\03data\\neargoos\\SSH','ssh_NMEFC_near_goos_66Hr.png',NULL),(143,'ssh_NMEFC_near_goos_69Hr.png',4,69,'D:\\03data\\neargoos\\SSH\\2019\\12\\13','2019-12-12 18:25:05','2019-12-12 18:25:00','2019-12-12 18:25:00',5,'2019\\12\\13','D:\\03data\\neargoos\\SSH','ssh_NMEFC_near_goos_69Hr.png',NULL),(144,'ssh_NMEFC_near_goos_72Hr.png',4,72,'D:\\03data\\neargoos\\SSH\\2019\\12\\13','2019-12-12 18:25:05','2019-12-12 18:25:00','2019-12-12 18:25:00',5,'2019\\12\\13','D:\\03data\\neargoos\\SSH','ssh_NMEFC_near_goos_72Hr.png',NULL);
/*!40000 ALTER TABLE `product_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_period`
--

DROP TABLE IF EXISTS `product_period`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product_period` (
  `aid` int(11) NOT NULL,
  `tid` int(11) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `periods` varchar(255) DEFAULT NULL,
  `periodsindex` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `FK_PERIOD_TYPE` (`tid`) USING BTREE,
  KEY `FK_PERIOD_AREA` (`aid`) USING BTREE,
  CONSTRAINT `FK_PERIOD_AREA` FOREIGN KEY (`aid`) REFERENCES `common_area` (`id`),
  CONSTRAINT `FK_PERIOD_TYPE` FOREIGN KEY (`tid`) REFERENCES `product_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1 ROW_FORMAT=COMPACT;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_period`
--

LOCK TABLES `product_period` WRITE;
/*!40000 ALTER TABLE `product_period` DISABLE KEYS */;
INSERT INTO `product_period` VALUES (1,1,1,'24,48,72,96,120','04,08,12,16,18'),(2,1,2,'24,48,72,96,120','04,08,12,16,18'),(3,2,3,'24,48,72,96,120','24,48,72,96,120'),(4,2,5,'0,3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57,60,63,66,69,72','0,3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57,60,63,66,69,72'),(2,4,6,'24,48,72,96,120','24,48,72,96,120'),(3,4,7,'24,48,72,96,120','24,48,72,96,120'),(4,5,8,'0,3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57,60,63,66,69,72','0,3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57,60,63,66,69,72');
/*!40000 ALTER TABLE `product_period` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_type`
--

DROP TABLE IF EXISTS `product_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `remark` varchar(300) CHARACTER SET utf8 DEFAULT NULL,
  `aid` int(5) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `FK_type_area` (`aid`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPACT;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_type`
--

LOCK TABLES `product_type` WRITE;
/*!40000 ALTER TABLE `product_type` DISABLE KEYS */;
INSERT INTO `product_type` VALUES (1,'wave','海浪',NULL),(2,'current','海流',NULL),(3,'ice','海冰',NULL),(4,'template','海表面温度',NULL),(5,'heigh','海表面高度',NULL);
/*!40000 ALTER TABLE `product_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role_action_association`
--

DROP TABLE IF EXISTS `role_action_association`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `role_action_association` (
  `role_id` int(11) NOT NULL,
  `action_id` int(11) NOT NULL,
  PRIMARY KEY (`role_id`,`action_id`) USING BTREE,
  KEY `FK_role_action_association2` (`action_id`) USING BTREE,
  CONSTRAINT `FK_role_action_association` FOREIGN KEY (`role_id`) REFERENCES `management_role` (`id`),
  CONSTRAINT `FK_role_action_association2` FOREIGN KEY (`action_id`) REFERENCES `management_action` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role_action_association`
--

LOCK TABLES `role_action_association` WRITE;
/*!40000 ALTER TABLE `role_action_association` DISABLE KEYS */;
/*!40000 ALTER TABLE `role_action_association` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tab_base_association`
--

DROP TABLE IF EXISTS `tab_base_association`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tab_base_association` (
  `bid` int(11) NOT NULL,
  `tabid` int(11) NOT NULL,
  PRIMARY KEY (`bid`,`tabid`) USING BTREE,
  KEY `fk_tabid_tab` (`tabid`) USING BTREE,
  CONSTRAINT `fk_base_tab` FOREIGN KEY (`bid`) REFERENCES `document_base` (`id`),
  CONSTRAINT `fk_tabid_tab` FOREIGN KEY (`tabid`) REFERENCES `document_tab` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tab_base_association`
--

LOCK TABLES `tab_base_association` WRITE;
/*!40000 ALTER TABLE `tab_base_association` DISABLE KEYS */;
INSERT INTO `tab_base_association` VALUES (1,1),(2,2),(2,4),(3,4);
/*!40000 ALTER TABLE `tab_base_association` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tab_content_association`
--

DROP TABLE IF EXISTS `tab_content_association`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tab_content_association` (
  `titleid` int(11) NOT NULL,
  `contentid` int(11) NOT NULL,
  PRIMARY KEY (`titleid`,`contentid`) USING BTREE,
  KEY `fk_title_content_cid` (`contentid`) USING BTREE,
  CONSTRAINT `fk_title_content_cid` FOREIGN KEY (`contentid`) REFERENCES `document_content` (`id`) ON UPDATE CASCADE,
  CONSTRAINT `fk_title_content_tid` FOREIGN KEY (`titleid`) REFERENCES `document_tab` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1 ROW_FORMAT=COMPACT;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tab_content_association`
--

LOCK TABLES `tab_content_association` WRITE;
/*!40000 ALTER TABLE `tab_content_association` DISABLE KEYS */;
/*!40000 ALTER TABLE `tab_content_association` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `title_base_association`
--

DROP TABLE IF EXISTS `title_base_association`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `title_base_association` (
  `tid` int(11) NOT NULL,
  `bid` int(11) NOT NULL,
  PRIMARY KEY (`tid`,`bid`) USING BTREE,
  KEY `fk_title` (`tid`) USING BTREE,
  KEY `fk_base` (`bid`) USING BTREE,
  CONSTRAINT `fk_base` FOREIGN KEY (`bid`) REFERENCES `document_base` (`id`),
  CONSTRAINT `fk_title` FOREIGN KEY (`tid`) REFERENCES `document_title` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `title_base_association`
--

LOCK TABLES `title_base_association` WRITE;
/*!40000 ALTER TABLE `title_base_association` DISABLE KEYS */;
/*!40000 ALTER TABLE `title_base_association` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_role_association`
--

DROP TABLE IF EXISTS `user_role_association`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_role_association` (
  `use_id` int(11) NOT NULL,
  `rol_id` int(11) NOT NULL,
  PRIMARY KEY (`use_id`,`rol_id`) USING BTREE,
  KEY `FK_user_role_association2` (`rol_id`) USING BTREE,
  CONSTRAINT `FK_user_role_association` FOREIGN KEY (`use_id`) REFERENCES `management_user` (`id`),
  CONSTRAINT `FK_user_role_association2` FOREIGN KEY (`rol_id`) REFERENCES `management_role` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_role_association`
--

LOCK TABLES `user_role_association` WRITE;
/*!40000 ALTER TABLE `user_role_association` DISABLE KEYS */;
INSERT INTO `user_role_association` VALUES (13,1),(14,1),(16,1),(13,2),(14,2);
/*!40000 ALTER TABLE `user_role_association` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-01-01 19:28:23
