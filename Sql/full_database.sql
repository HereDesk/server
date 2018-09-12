/*
 Navicat Premium Data Transfer

 Source Server         : 127.0.0.1
 Source Server Type    : MySQL
 Source Server Version : 50717
 Source Host           : localhost
 Source Database       : hdesk

 Target Server Type    : MySQL
 Target Server Version : 50717
 File Encoding         : utf-8

 Date: 09/12/2018 07:45:29 AM
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `auth_group`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
--  Table structure for `auth_group_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
--  Table structure for `auth_permission`
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=103 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
--  Records of `auth_permission`
-- ----------------------------
BEGIN;
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry'), ('2', 'Can change log entry', '1', 'change_logentry'), ('3', 'Can delete log entry', '1', 'delete_logentry'), ('4', 'Can add permission', '2', 'add_permission'), ('5', 'Can change permission', '2', 'change_permission'), ('6', 'Can delete permission', '2', 'delete_permission'), ('7', 'Can add group', '3', 'add_group'), ('8', 'Can change group', '3', 'change_group'), ('9', 'Can delete group', '3', 'delete_group'), ('10', 'Can add user', '4', 'add_user'), ('11', 'Can change user', '4', 'change_user'), ('12', 'Can delete user', '4', 'delete_user'), ('13', 'Can add content type', '5', 'add_contenttype'), ('14', 'Can change content type', '5', 'change_contenttype'), ('15', 'Can delete content type', '5', 'delete_contenttype'), ('16', 'Can add session', '6', 'add_session'), ('17', 'Can change session', '6', 'change_session'), ('18', 'Can delete session', '6', 'delete_session'), ('19', 'Can add blacklist ip', '7', 'add_blacklistip'), ('20', 'Can change blacklist ip', '7', 'change_blacklistip'), ('21', 'Can delete blacklist ip', '7', 'delete_blacklistip'), ('22', 'Can add authentication', '8', 'add_authentication'), ('23', 'Can change authentication', '8', 'change_authentication'), ('24', 'Can delete authentication', '8', 'delete_authentication'), ('25', 'Can add bug', '9', 'add_bug'), ('26', 'Can change bug', '9', 'change_bug'), ('27', 'Can delete bug', '9', 'delete_bug'), ('28', 'Can add bug annex', '10', 'add_bugannex'), ('29', 'Can change bug annex', '10', 'change_bugannex'), ('30', 'Can delete bug annex', '10', 'delete_bugannex'), ('31', 'Can add bug history', '11', 'add_bughistory'), ('32', 'Can change bug history', '11', 'change_bughistory'), ('33', 'Can delete bug history', '11', 'delete_bughistory'), ('34', 'Can add bug priority', '12', 'add_bugpriority'), ('35', 'Can change bug priority', '12', 'change_bugpriority'), ('36', 'Can delete bug priority', '12', 'delete_bugpriority'), ('37', 'Can add bug report', '13', 'add_bugreport'), ('38', 'Can change bug report', '13', 'change_bugreport'), ('39', 'Can delete bug report', '13', 'delete_bugreport'), ('40', 'Can add bug severity', '14', 'add_bugseverity'), ('41', 'Can change bug severity', '14', 'change_bugseverity'), ('42', 'Can delete bug severity', '14', 'delete_bugseverity'), ('43', 'Can add bug solution', '15', 'add_bugsolution'), ('44', 'Can change bug solution', '15', 'change_bugsolution'), ('45', 'Can delete bug solution', '15', 'delete_bugsolution'), ('46', 'Can add bug status', '16', 'add_bugstatus'), ('47', 'Can change bug status', '16', 'change_bugstatus'), ('48', 'Can delete bug status', '16', 'delete_bugstatus'), ('49', 'Can add bug type', '17', 'add_bugtype'), ('50', 'Can change bug type', '17', 'change_bugtype'), ('51', 'Can delete bug type', '17', 'delete_bugtype'), ('52', 'Can add group', '18', 'add_group'), ('53', 'Can change group', '18', 'change_group'), ('54', 'Can delete group', '18', 'delete_group'), ('55', 'Can add keyword filter', '19', 'add_keywordfilter'), ('56', 'Can change keyword filter', '19', 'change_keywordfilter'), ('57', 'Can delete keyword filter', '19', 'delete_keywordfilter'), ('58', 'Can add logged log', '20', 'add_loggedlog'), ('59', 'Can change logged log', '20', 'change_loggedlog'), ('60', 'Can delete logged log', '20', 'delete_loggedlog'), ('61', 'Can add module a', '21', 'add_modulea'), ('62', 'Can change module a', '21', 'change_modulea'), ('63', 'Can delete module a', '21', 'delete_modulea'), ('64', 'Can add module b', '22', 'add_moduleb'), ('65', 'Can change module b', '22', 'change_moduleb'), ('66', 'Can delete module b', '22', 'delete_moduleb'), ('67', 'Can add permissions', '23', 'add_permissions'), ('68', 'Can change permissions', '23', 'change_permissions'), ('69', 'Can delete permissions', '23', 'delete_permissions'), ('70', 'Can add permissions group', '24', 'add_permissionsgroup'), ('71', 'Can change permissions group', '24', 'change_permissionsgroup'), ('72', 'Can delete permissions group', '24', 'delete_permissionsgroup'), ('73', 'Can add product', '25', 'add_product'), ('74', 'Can change product', '25', 'change_product'), ('75', 'Can delete product', '25', 'delete_product'), ('76', 'Can add product members', '26', 'add_productmembers'), ('77', 'Can change product members', '26', 'change_productmembers'), ('78', 'Can delete product members', '26', 'delete_productmembers'), ('79', 'Can add release', '27', 'add_release'), ('80', 'Can change release', '27', 'change_release'), ('81', 'Can delete release', '27', 'delete_release'), ('82', 'Can add system config', '28', 'add_systemconfig'), ('83', 'Can change system config', '28', 'change_systemconfig'), ('84', 'Can delete system config', '28', 'delete_systemconfig'), ('85', 'Can add test case', '29', 'add_testcase'), ('86', 'Can change test case', '29', 'change_testcase'), ('87', 'Can delete test case', '29', 'delete_testcase'), ('88', 'Can add test case review', '30', 'add_testcasereview'), ('89', 'Can change test case review', '30', 'change_testcasereview'), ('90', 'Can delete test case review', '30', 'delete_testcasereview'), ('91', 'Can add test suite', '31', 'add_testsuite'), ('92', 'Can change test suite', '31', 'change_testsuite'), ('93', 'Can delete test suite', '31', 'delete_testsuite'), ('94', 'Can add test suite cell', '32', 'add_testsuitecell'), ('95', 'Can change test suite cell', '32', 'change_testsuitecell'), ('96', 'Can delete test suite cell', '32', 'delete_testsuitecell'), ('97', 'Can add upload image', '33', 'add_uploadimage'), ('98', 'Can change upload image', '33', 'change_uploadimage'), ('99', 'Can delete upload image', '33', 'delete_uploadimage'), ('100', 'Can add user', '34', 'add_user'), ('101', 'Can change user', '34', 'change_user'), ('102', 'Can delete user', '34', 'delete_user');
COMMIT;

-- ----------------------------
--  Table structure for `auth_user`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
--  Table structure for `auth_user_groups`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
--  Table structure for `auth_user_user_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
--  Table structure for `django_admin_log`
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
--  Table structure for `django_content_type`
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
--  Records of `django_content_type`
-- ----------------------------
BEGIN;
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry'), ('8', 'app', 'authentication'), ('7', 'app', 'blacklistip'), ('9', 'app', 'bug'), ('10', 'app', 'bugannex'), ('11', 'app', 'bughistory'), ('12', 'app', 'bugpriority'), ('13', 'app', 'bugreport'), ('14', 'app', 'bugseverity'), ('15', 'app', 'bugsolution'), ('16', 'app', 'bugstatus'), ('17', 'app', 'bugtype'), ('18', 'app', 'group'), ('19', 'app', 'keywordfilter'), ('20', 'app', 'loggedlog'), ('21', 'app', 'modulea'), ('22', 'app', 'moduleb'), ('23', 'app', 'permissions'), ('24', 'app', 'permissionsgroup'), ('25', 'app', 'product'), ('26', 'app', 'productmembers'), ('27', 'app', 'release'), ('28', 'app', 'systemconfig'), ('29', 'app', 'testcase'), ('30', 'app', 'testcasereview'), ('31', 'app', 'testsuite'), ('32', 'app', 'testsuitecell'), ('33', 'app', 'uploadimage'), ('34', 'app', 'user'), ('3', 'auth', 'group'), ('2', 'auth', 'permission'), ('4', 'auth', 'user'), ('5', 'contenttypes', 'contenttype'), ('6', 'sessions', 'session');
COMMIT;

-- ----------------------------
--  Table structure for `django_migrations`
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
--  Records of `django_migrations`
-- ----------------------------
BEGIN;
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2018-09-12 07:41:29.442783'), ('2', 'auth', '0001_initial', '2018-09-12 07:41:30.162452'), ('3', 'admin', '0001_initial', '2018-09-12 07:41:30.336652'), ('4', 'admin', '0002_logentry_remove_auto_add', '2018-09-12 07:41:30.352684'), ('5', 'app', '0001_initial', '2018-09-12 07:41:38.923147'), ('6', 'contenttypes', '0002_remove_content_type_name', '2018-09-12 07:41:39.148280'), ('7', 'auth', '0002_alter_permission_name_max_length', '2018-09-12 07:41:39.245250'), ('8', 'auth', '0003_alter_user_email_max_length', '2018-09-12 07:41:39.298528'), ('9', 'auth', '0004_alter_user_username_opts', '2018-09-12 07:41:39.403978'), ('10', 'auth', '0005_alter_user_last_login_null', '2018-09-12 07:41:39.482991'), ('11', 'auth', '0006_require_contenttypes_0002', '2018-09-12 07:41:39.492274'), ('12', 'auth', '0007_alter_validators_add_error_messages', '2018-09-12 07:41:39.512783'), ('13', 'auth', '0008_alter_user_username_max_length', '2018-09-12 07:41:39.672336'), ('14', 'auth', '0009_alter_user_last_name_max_length', '2018-09-12 07:41:39.748479'), ('15', 'sessions', '0001_initial', '2018-09-12 07:41:39.805206');
COMMIT;

-- ----------------------------
--  Table structure for `django_session`
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
--  Table structure for `t_authentication`
-- ----------------------------
DROP TABLE IF EXISTS `t_authentication`;
CREATE TABLE `t_authentication` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `token` varchar(200) NOT NULL,
  `uid` char(32) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `t_authentication_uid_200d4eab_fk_t_user_user_id` (`uid`),
  CONSTRAINT `t_authentication_uid_200d4eab_fk_t_user_user_id` FOREIGN KEY (`uid`) REFERENCES `t_user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
--  Table structure for `t_bug`
-- ----------------------------
DROP TABLE IF EXISTS `t_bug`;
CREATE TABLE `t_bug` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bug_id` char(32) NOT NULL,
  `title` varchar(100) NOT NULL,
  `steps` varchar(1000) NOT NULL,
  `reality_result` varchar(500) NOT NULL,
  `expected_result` varchar(500) NOT NULL,
  `remark` varchar(1000) DEFAULT NULL,
  `create_time` datetime(6) NOT NULL,
  `assignedTo_time` datetime(6) NOT NULL,
  `fixed_time` datetime(6) DEFAULT NULL,
  `closed_time` datetime(6) DEFAULT NULL,
  `hangUp_time` datetime(6) DEFAULT NULL,
  `isDelete` int(11) NOT NULL,
  `delete_time` datetime(6) DEFAULT NULL,
  `last_Time` datetime(6) NOT NULL,
  `assignedTo_id` char(32) DEFAULT NULL,
  `bug_type` varchar(10) DEFAULT NULL,
  `case_id` char(32) DEFAULT NULL,
  `cell_id` char(32) DEFAULT NULL,
  `closed_id` char(32) DEFAULT NULL,
  `creator_id` char(32) NOT NULL,
  `delete_id` char(32) DEFAULT NULL,
  `fixed_id` char(32) DEFAULT NULL,
  `hangUp_id` char(32) DEFAULT NULL,
  `m1_id` int(11) DEFAULT NULL,
  `m2_id` int(11) DEFAULT NULL,
  `priority` varchar(15) NOT NULL,
  `product_code` varchar(20) NOT NULL,
  `severity` varchar(15) NOT NULL,
  `solution` varchar(15) DEFAULT NULL,
  `status` varchar(15) NOT NULL,
  `versionId` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `bug_id` (`bug_id`),
  KEY `t_bug_assignedTo_id_23edc9cc_fk_t_user_user_id` (`assignedTo_id`),
  KEY `t_bug_bug_type_f8a03306_fk_t_bug_type_key` (`bug_type`),
  KEY `t_bug_case_id_4d63e76b_fk_t_testcase_case_id` (`case_id`),
  KEY `t_bug_cell_id_c750a5d3_fk_t_testsuite_cell_cell_id` (`cell_id`),
  KEY `t_bug_closed_id_966534bb_fk_t_user_user_id` (`closed_id`),
  KEY `t_bug_creator_id_5b253ef0_fk_t_user_user_id` (`creator_id`),
  KEY `t_bug_delete_id_340cc31b_fk_t_user_user_id` (`delete_id`),
  KEY `t_bug_fixed_id_8a0fad75_fk_t_user_user_id` (`fixed_id`),
  KEY `t_bug_hangUp_id_e195a0e6_fk_t_user_user_id` (`hangUp_id`),
  KEY `t_bug_m1_id_5a3a4f9f_fk_t_module_1_id` (`m1_id`),
  KEY `t_bug_m2_id_456beed9_fk_t_module_2_id` (`m2_id`),
  KEY `t_bug_priority_7c945266_fk_t_bug_priority_key` (`priority`),
  KEY `t_bug_product_code_84492df3_fk_t_product_product_code` (`product_code`),
  KEY `t_bug_severity_5a5c69df_fk_t_bug_severity_key` (`severity`),
  KEY `t_bug_solution_18497e33_fk_t_bug_solution_key` (`solution`),
  KEY `t_bug_status_e35371f6_fk_t_bug_status_key` (`status`),
  KEY `t_bug_versionId_e1ab02de_fk_t_release_id` (`versionId`),
  CONSTRAINT `t_bug_assignedTo_id_23edc9cc_fk_t_user_user_id` FOREIGN KEY (`assignedTo_id`) REFERENCES `t_user` (`user_id`),
  CONSTRAINT `t_bug_bug_type_f8a03306_fk_t_bug_type_key` FOREIGN KEY (`bug_type`) REFERENCES `t_bug_type` (`key`),
  CONSTRAINT `t_bug_case_id_4d63e76b_fk_t_testcase_case_id` FOREIGN KEY (`case_id`) REFERENCES `t_testcase` (`case_id`),
  CONSTRAINT `t_bug_cell_id_c750a5d3_fk_t_testsuite_cell_cell_id` FOREIGN KEY (`cell_id`) REFERENCES `t_testsuite_cell` (`cell_id`),
  CONSTRAINT `t_bug_closed_id_966534bb_fk_t_user_user_id` FOREIGN KEY (`closed_id`) REFERENCES `t_user` (`user_id`),
  CONSTRAINT `t_bug_creator_id_5b253ef0_fk_t_user_user_id` FOREIGN KEY (`creator_id`) REFERENCES `t_user` (`user_id`),
  CONSTRAINT `t_bug_delete_id_340cc31b_fk_t_user_user_id` FOREIGN KEY (`delete_id`) REFERENCES `t_user` (`user_id`),
  CONSTRAINT `t_bug_fixed_id_8a0fad75_fk_t_user_user_id` FOREIGN KEY (`fixed_id`) REFERENCES `t_user` (`user_id`),
  CONSTRAINT `t_bug_hangUp_id_e195a0e6_fk_t_user_user_id` FOREIGN KEY (`hangUp_id`) REFERENCES `t_user` (`user_id`),
  CONSTRAINT `t_bug_m1_id_5a3a4f9f_fk_t_module_1_id` FOREIGN KEY (`m1_id`) REFERENCES `t_module_1` (`id`),
  CONSTRAINT `t_bug_m2_id_456beed9_fk_t_module_2_id` FOREIGN KEY (`m2_id`) REFERENCES `t_module_2` (`id`),
  CONSTRAINT `t_bug_priority_7c945266_fk_t_bug_priority_key` FOREIGN KEY (`priority`) REFERENCES `t_bug_priority` (`key`),
  CONSTRAINT `t_bug_product_code_84492df3_fk_t_product_product_code` FOREIGN KEY (`product_code`) REFERENCES `t_product` (`product_code`),
  CONSTRAINT `t_bug_severity_5a5c69df_fk_t_bug_severity_key` FOREIGN KEY (`severity`) REFERENCES `t_bug_severity` (`key`),
  CONSTRAINT `t_bug_solution_18497e33_fk_t_bug_solution_key` FOREIGN KEY (`solution`) REFERENCES `t_bug_solution` (`key`),
  CONSTRAINT `t_bug_status_e35371f6_fk_t_bug_status_key` FOREIGN KEY (`status`) REFERENCES `t_bug_status` (`key`),
  CONSTRAINT `t_bug_versionId_e1ab02de_fk_t_release_id` FOREIGN KEY (`versionId`) REFERENCES `t_release` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='缺陷表';

-- ----------------------------
--  Table structure for `t_bug_annex`
-- ----------------------------
DROP TABLE IF EXISTS `t_bug_annex`;
CREATE TABLE `t_bug_annex` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(100) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `isDelete` int(11) NOT NULL,
  `bug_id` char(32) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `t_bug_annex_bug_id_c6e889e1_fk_t_bug_bug_id` (`bug_id`),
  CONSTRAINT `t_bug_annex_bug_id_c6e889e1_fk_t_bug_bug_id` FOREIGN KEY (`bug_id`) REFERENCES `t_bug` (`bug_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='缺陷附件表';

-- ----------------------------
--  Table structure for `t_bug_history`
-- ----------------------------
DROP TABLE IF EXISTS `t_bug_history`;
CREATE TABLE `t_bug_history` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `desc` varchar(1000) NOT NULL,
  `remark` varchar(2000) DEFAULT NULL,
  `create_time` datetime(6) NOT NULL,
  `bug_id` char(32) NOT NULL,
  `user_id` char(32) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `t_bug_history_bug_id_f83d43ea_fk_t_bug_bug_id` (`bug_id`),
  KEY `t_bug_history_user_id_979407d0_fk_t_user_user_id` (`user_id`),
  CONSTRAINT `t_bug_history_bug_id_f83d43ea_fk_t_bug_bug_id` FOREIGN KEY (`bug_id`) REFERENCES `t_bug` (`bug_id`),
  CONSTRAINT `t_bug_history_user_id_979407d0_fk_t_user_user_id` FOREIGN KEY (`user_id`) REFERENCES `t_user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='缺陷操作历史表';

-- ----------------------------
--  Table structure for `t_bug_priority`
-- ----------------------------
DROP TABLE IF EXISTS `t_bug_priority`;
CREATE TABLE `t_bug_priority` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `key` varchar(15) NOT NULL,
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `key` (`key`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COMMENT='缺陷优先级数据';

-- ----------------------------
--  Records of `t_bug_priority`
-- ----------------------------
BEGIN;
INSERT INTO `t_bug_priority` VALUES ('1', 'P1', 'P1'), ('2', 'P2', 'P2'), ('3', 'P3', 'P3'), ('4', 'P4', 'P4'), ('5', 'P5', 'P5');
COMMIT;

-- ----------------------------
--  Table structure for `t_bug_report`
-- ----------------------------
DROP TABLE IF EXISTS `t_bug_report`;
CREATE TABLE `t_bug_report` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `report_id` char(32) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `content` longtext NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `report_id` (`report_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='缺陷报告表';

-- ----------------------------
--  Table structure for `t_bug_severity`
-- ----------------------------
DROP TABLE IF EXISTS `t_bug_severity`;
CREATE TABLE `t_bug_severity` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `key` varchar(15) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `key` (`key`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COMMENT='缺陷严重程度数据';

-- ----------------------------
--  Records of `t_bug_severity`
-- ----------------------------
BEGIN;
INSERT INTO `t_bug_severity` VALUES ('1', 'Fatal', '致命'), ('2', 'Critical', '严重'), ('3', 'Normal', '一般'), ('4', 'Minor', '轻微'), ('5', 'Suggestion', '建议');
COMMIT;

-- ----------------------------
--  Table structure for `t_bug_solution`
-- ----------------------------
DROP TABLE IF EXISTS `t_bug_solution`;
CREATE TABLE `t_bug_solution` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `key` varchar(15) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `key` (`key`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COMMENT='缺陷解决方案数据';

-- ----------------------------
--  Records of `t_bug_solution`
-- ----------------------------
BEGIN;
INSERT INTO `t_bug_solution` VALUES ('1', 'Fixed', '已修复'), ('2', 'Can\'t reproduce', '无法复现'), ('3', 'Repeat', '重复Bug'), ('4', 'Not a bug', '不是缺陷'), ('5', 'Designed so', '设计如此'), ('6', 'Requirements so', '需求如此'), ('7', 'other', '其它');
COMMIT;

-- ----------------------------
--  Table structure for `t_bug_status`
-- ----------------------------
DROP TABLE IF EXISTS `t_bug_status`;
CREATE TABLE `t_bug_status` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `key` varchar(15) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `key` (`key`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COMMENT='缺陷状态数据';

-- ----------------------------
--  Records of `t_bug_status`
-- ----------------------------
BEGIN;
INSERT INTO `t_bug_status` VALUES ('1', 'New', '新建未分配'), ('2', 'Open', '待解决'), ('3', 'Closed', '已关闭'), ('4', 'Fixed', '已解决'), ('5', 'Reopen', '重新打开'), ('6', 'Hang-up', '挂起延期');
COMMIT;

-- ----------------------------
--  Table structure for `t_bug_type`
-- ----------------------------
DROP TABLE IF EXISTS `t_bug_type`;
CREATE TABLE `t_bug_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `key` varchar(10) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `key` (`key`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COMMENT='缺陷类型数据';

-- ----------------------------
--  Records of `t_bug_type`
-- ----------------------------
BEGIN;
INSERT INTO `t_bug_type` VALUES ('1', 'Function', '功能'), ('2', 'UI', 'UI'), ('3', 'compatible', '兼容适配'), ('4', 'Perfor', '性能'), ('5', 'interface', '接口'), ('6', 'PM', '需求'), ('7', 'Design', '设计'), ('8', 'Code', '代码'), ('9', 'other', '其它');
COMMIT;

-- ----------------------------
--  Table structure for `t_group`
-- ----------------------------
DROP TABLE IF EXISTS `t_group`;
CREATE TABLE `t_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group` varchar(20) NOT NULL,
  `name` varchar(50) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group` (`group`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COMMENT='用户群组表';

-- ----------------------------
--  Records of `t_group`
-- ----------------------------
BEGIN;
INSERT INTO `t_group` VALUES ('1', 'admin', '超级管理员', '2018-08-20 15:24:26.000000', '2018-08-20 15:24:29.000000'), ('2', 'test', '测试', '2018-08-20 16:57:54.000000', '2018-08-20 16:57:59.000000'), ('3', 'developer', '开发', '2018-08-20 17:04:50.000000', '2018-08-20 17:04:52.000000'), ('4', 'pm', '产品', '2018-08-20 17:05:05.000000', '2018-08-20 17:05:07.000000'), ('5', 'design', '设计', '2018-08-20 17:05:21.000000', '2018-08-20 17:05:23.000000'), ('6', 'manager', '领导层', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
COMMIT;

-- ----------------------------
--  Table structure for `t_keyword_filter`
-- ----------------------------
DROP TABLE IF EXISTS `t_keyword_filter`;
CREATE TABLE `t_keyword_filter` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `keyword` varchar(30) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
--  Table structure for `t_logged_log`
-- ----------------------------
DROP TABLE IF EXISTS `t_logged_log`;
CREATE TABLE `t_logged_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(20) DEFAULT NULL,
  `path` varchar(200) DEFAULT NULL,
  `method` varchar(20) DEFAULT NULL,
  `request` varchar(10000) DEFAULT NULL,
  `platform` varchar(200) DEFAULT NULL,
  `browser` varchar(200) DEFAULT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `user_id` char(32) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `t_logged_log_user_id_2bfe0aa9_fk_t_user_user_id` (`user_id`),
  CONSTRAINT `t_logged_log_user_id_2bfe0aa9_fk_t_user_user_id` FOREIGN KEY (`user_id`) REFERENCES `t_user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
--  Table structure for `t_module_1`
-- ----------------------------
DROP TABLE IF EXISTS `t_module_1`;
CREATE TABLE `t_module_1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `m1` varchar(200) NOT NULL,
  `isChange` int(11) NOT NULL,
  `isDelete` int(11) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `change_time` datetime(6) DEFAULT NULL,
  `delete_time` datetime(6) DEFAULT NULL,
  `update_time` datetime(6) NOT NULL,
  `changer_id` char(32) DEFAULT NULL,
  `creator_id` char(32) NOT NULL,
  `deleter_id` char(32) DEFAULT NULL,
  `product_code` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `t_module_1_changer_id_fe604c32_fk_t_user_user_id` (`changer_id`),
  KEY `t_module_1_creator_id_080bbfa1_fk_t_user_user_id` (`creator_id`),
  KEY `t_module_1_deleter_id_cd56e807_fk_t_user_user_id` (`deleter_id`),
  KEY `t_module_1_product_code_16b2e778_fk_t_product_product_code` (`product_code`),
  CONSTRAINT `t_module_1_changer_id_fe604c32_fk_t_user_user_id` FOREIGN KEY (`changer_id`) REFERENCES `t_user` (`user_id`),
  CONSTRAINT `t_module_1_creator_id_080bbfa1_fk_t_user_user_id` FOREIGN KEY (`creator_id`) REFERENCES `t_user` (`user_id`),
  CONSTRAINT `t_module_1_deleter_id_cd56e807_fk_t_user_user_id` FOREIGN KEY (`deleter_id`) REFERENCES `t_user` (`user_id`),
  CONSTRAINT `t_module_1_product_code_16b2e778_fk_t_product_product_code` FOREIGN KEY (`product_code`) REFERENCES `t_product` (`product_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='一级模块';

-- ----------------------------
--  Table structure for `t_module_2`
-- ----------------------------
DROP TABLE IF EXISTS `t_module_2`;
CREATE TABLE `t_module_2` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `m2` varchar(200) NOT NULL,
  `isChange` int(11) NOT NULL,
  `isDelete` int(11) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `change_time` datetime(6) DEFAULT NULL,
  `delete_time` datetime(6) DEFAULT NULL,
  `update_time` datetime(6) NOT NULL,
  `changer_id` char(32) DEFAULT NULL,
  `creator_id` char(32) NOT NULL,
  `deleter_id` char(32) DEFAULT NULL,
  `ModuleA_ID` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `t_module_2_changer_id_b4d186a8_fk_t_user_user_id` (`changer_id`),
  KEY `t_module_2_creator_id_2a15a5e9_fk_t_user_user_id` (`creator_id`),
  KEY `t_module_2_deleter_id_96c82135_fk_t_user_user_id` (`deleter_id`),
  KEY `t_module_2_ModuleA_ID_dfcaf900_fk_t_module_1_id` (`ModuleA_ID`),
  CONSTRAINT `t_module_2_ModuleA_ID_dfcaf900_fk_t_module_1_id` FOREIGN KEY (`ModuleA_ID`) REFERENCES `t_module_1` (`id`),
  CONSTRAINT `t_module_2_changer_id_b4d186a8_fk_t_user_user_id` FOREIGN KEY (`changer_id`) REFERENCES `t_user` (`user_id`),
  CONSTRAINT `t_module_2_creator_id_2a15a5e9_fk_t_user_user_id` FOREIGN KEY (`creator_id`) REFERENCES `t_user` (`user_id`),
  CONSTRAINT `t_module_2_deleter_id_96c82135_fk_t_user_user_id` FOREIGN KEY (`deleter_id`) REFERENCES `t_user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='二级模块';

-- ----------------------------
--  Table structure for `t_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `t_permissions`;
CREATE TABLE `t_permissions` (
  `id` char(32) NOT NULL,
  `name` varchar(100) NOT NULL,
  `code` varchar(200) NOT NULL,
  `url` varchar(200) NOT NULL,
  `flag` varchar(200) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='权限表';

-- ----------------------------
--  Records of `t_permissions`
-- ----------------------------
BEGIN;
INSERT INTO `t_permissions` VALUES ('045210cf30a94f23951c7e68b9dcf5bb', '封禁用户', 'user_banned', '/api/user/banned', '用户管理', '2018-09-09 21:54:41.013389'), ('04bdf9e393e3418b9f941a8a6d493065', '重新打开缺陷', 'bug_reopen', '/api/qa/bug/reopen', '缺陷', '2018-09-09 21:46:22.508814'), ('0725da1a6ae74c1b90446584dd234e39', '缺陷属性信息（优先级、严重程度、类型）', 'bug_property', '/api/qa/bug/bug_property', '缺陷', '2018-09-09 21:41:51.484677'), ('0c8ec92ab1964d1dba198e65eb61f23e', '一级模块增加', 'module_1_add', '/api/pm/module/1/add', '模块管理', '2018-09-09 22:11:08.630362'), ('0e14a50d3984432fb7b99ff7227b5795', '上传图片附件', 'public_upload', '/api/support/upload', '公共部分', '2018-09-09 22:07:46.057965'), ('0f61062a5aca4e7299a4fde489b9d83e', '测试用例执行集列表', 'testsuite_list', '/api/qa/testsuite/list', '测试用例', '2018-09-09 22:26:04.354928'), ('15ed7c9856984c079c6ec1da800297b8', '产品人员列表', 'product_member_list', '/api/pm/member/list', '产品管理', '2018-09-09 22:15:43.763976'), ('19a01e70033c411dabf2f734e15fa49d', '测试执行集：测试用例列表', 'testsuite_cell_detailsed_list', '/api/qa/testsuite/cell/detailed_list', '测试用例', '2018-09-09 22:32:12.875040'), ('19f266cd29a14e0fa7d6c61ef5b41490', '删除缺陷', 'bug_delete', '/api/qa/bug/delete', '缺陷', '2018-09-09 21:42:21.084483'), ('2c8b2faf5934494cbed2692a71a57e96', '创建缺陷', 'bug_create', '/api/qa/bug/create', '缺陷', '2018-09-09 18:04:23.513690'), ('30e7db997a2f4a3d85ce54ae5dc21e06', '编辑缺陷', 'bug_edit', '/api/qa/bug/edit', '缺陷', '2018-09-09 21:39:12.997472'), ('316cd908ddab4ac280bf7c0c299b78e5', '产品人员重新加入', 'product_member_rejoin', '/api/pm/member/rejoin', '产品管理', '2018-09-09 22:16:47.586931'), ('32e4fbba7762472484d0a66bbe64808d', '缺陷趋势分析', 'bug_analyze_create', '/api/analyze/bug/date/create', '缺陷', '2018-09-09 22:20:53.529293'), ('3ce348164a0f4e5d9dd77eee89942042', '关闭缺陷', 'bug_close', '/api/qa/bug/close', '缺陷', '2018-09-09 21:45:51.769239'), ('4d346aaedd75430aaa8be6390c6595f1', '二级模块列表', 'module_2_list', '/api/pm/module/2/list', '模块管理', '2018-09-09 22:11:42.795975'), ('54c452206228426096d41dff943ad90f', '产品人员移除', 'product_member_ban', '/api/pm/member/ban', '产品管理', '2018-09-09 22:16:28.030676'), ('565c01742ab34ed18d037e791a586099', '评审测试用例', 'testcase_review', '/api/qa/testcase/review', '测试用例', '2018-09-09 21:36:31.865626'), ('5d9189aa7973426ebe1417d8ddcc122f', '二级模块删除', 'module_2_del', '/api/pm/module/2/del', '模块管理', '2018-09-09 22:12:39.213172'), ('6067b35290e9426e96c146dcb149c0ae', '解决修复缺陷', 'bug_resolve', '/api/qa/bug/resolve', '缺陷', '2018-09-09 21:44:02.679900'), ('64e6b09e09374b079afdc0e1c44a5545', '修改密码', 'user_setpasswd', '/api/user/setpasswd', '用户管理', '2018-09-09 21:57:33.754000'), ('68043153e40143dd97a9acbbc3f94ac5', '缺陷解决方案列表', 'bug_solution', '/api/qa/bug/solution', '缺陷', '2018-09-09 21:40:49.325408'), ('6913ad4a9a1a401eaf2ef3ee26a4a465', 'dashboard', 'public_dashboard', '/api/dashboard/data_statistics', '公共部分', '2018-09-09 22:45:58.361916'), ('6cc1755a2ca1477c87a398d8dafaf1fc', '缺陷分析（优先级、严重程度、类型等）', 'bug_analyze_query', '/api/analyze/bug/query', '缺陷', '2018-09-09 22:19:39.090896'), ('6d27df660a414a3fb6d73156f0cb7d3d', '测试用例列表', 'testcase_list', '/api/qa/testcase/list', '测试用例', '2018-09-09 21:18:58.554355'), ('6ece36af9b1848bf810ee108f0b1c55c', '二级模块编辑', 'module_2_edit', '/api/pm/module/2/edit', '模块管理', '2018-09-09 22:12:19.798866'), ('708e501b81e0428ea0f0427c4e97964a', '测试用例详情', 'testcase_details', '/api/qa/testcase/details', '测试用例', '2018-09-09 21:34:08.351895'), ('71037db9d038487593da113a6b1f65be', '测试执行集：增加测试用例', 'testsuite_cell_add', '/api/qa/testsuite/cell/add', '测试用例', '2018-09-09 22:29:01.149785'), ('72ab70daaf7b4f7d8a9335554ed01094', '用户列表', 'user_list', '/api/user/user_list', '用户管理', '2018-09-09 21:54:07.966925'), ('782e404322e24caa9846b04207414bbb', '给用户重置密码', 'user_reset_passwd', '/api/user/reset_passwd', '用户管理', '2018-09-09 21:59:20.951504'), ('7999649a6f794f2ea8b1b64ba0f52cfc', '二级模块增加', 'module_2_add', '/api/pm/module/2/add', '模块管理', '2018-09-09 22:12:02.257355'), ('7c7293a59b154467b59fe87309fa72e2', '搜索测试用例', 'testcase_search', '/api/qa/testcase/search', '测试用例', '2018-09-09 21:35:41.048930'), ('820b5a9cde714cd18ba0c3f2cb9fed3c', '创建测试用例', 'testcase_create', '/api/qa/testcase/add', '测试用例', '2018-09-09 21:33:16.610486'), ('863cf952242545f2bf5bcca5aa8a3515', '缺陷列表', 'bug_list', '/api/qa/bug/list', '缺陷', '2018-09-09 17:29:12.118311'), ('868db45b920a4bf28990bdf47cb28673', '产品列表', 'product_all_list', '/api/pm/get_product_name', '产品管理', '2018-09-09 22:03:00.733424'), ('8dd468711f41404fab71530951d2340c', '版本创建', 'version_create', '/api/pm/release/create', '版本管理', '2018-09-09 22:08:45.494056'), ('8f79ba2c30394f4fa6dc9f8b027724c3', '产品人员加入', 'product_member_join', '/api/pm/member/join', '产品管理', '2018-09-09 22:16:07.602744'), ('94374b45faf04df28755f039bd883d70', '挂起缺陷', 'bug_hangup', '/api/qa/bug/hangup', '缺陷', '2018-09-09 21:47:21.551919'), ('9569acd658b04880a23a21febd3c29ce', '测试用例运行', 'testsuite_run', '/api/qa/testsuite/cell/run', '测试用例', '2018-09-09 22:26:39.679360'), ('994e168db4c74c588503a1174da999bc', '生成缺陷报告', 'bug_report_generate', '/api/qa/bug/report/generate', '缺陷', '2018-09-09 21:48:28.784626'), ('9ab3b78b43a94ea9ad42c063a24e7f53', '创建产品', 'product_create', '/api/pm/product/create', '产品管理', '2018-09-09 22:00:45.104629'), ('9b3f96f30978401681edd38ea41d75bf', '给缺陷增加备注', 'bug_notes', '/api/qa/bug/add_notes', '缺陷', '2018-09-09 21:47:43.882246'), ('9c4e5773b642454180ede04e7bd6f793', '缺陷详情', 'bug_details', '/api/qa/bug/details', '缺陷', '2018-09-09 21:39:38.688695'), ('9f08d915207b41adbe626a00774a9a61', '产品版本列表', 'product_release', '/api/pm/product_release', '产品管理', '2018-09-09 22:04:33.630679'), ('a14c6fdd1fd74cb6b9db2a25c6475941', '按开发人员统计缺陷', 'bug_analyze_developer', '/api/analyze/bug/developer', '缺陷', '2018-09-09 22:21:47.301458'), ('a1dece243b0142ff81f75c5b5d3f89f3', '版本列表', 'version_list', '/api/pm/release/list', '版本管理', '2018-09-09 22:09:11.877218'), ('a7afbd5edb4845869687bc43aacb4a01', '创建测试用例执行集', 'testsuite_create', '/api/qa/testsuite/create', '测试用例', '2018-09-09 22:25:40.039569'), ('aa830da9b76d44d2a1305631704f254d', '删除缺陷附件', 'bug_annex_delete', '/api/qa/bug/annex/delete', '缺陷', '2018-09-09 21:49:28.677009'), ('b6ba4637ec5849618f78e7cc5c9d7a58', '删除测试用例', 'testcase_delete', '/api/qa/testcase/del', '测试用例', '2018-09-09 21:33:43.303670'), ('bcfb5ff72d8d403d858058f2444efca1', '搜索缺陷', 'bug_search', '/api/qa/bug/search', '缺陷', '2018-09-09 21:40:16.858626'), ('bdf1edf832fe42ec93917473f9208250', '统计今日测试用例工作量', 'testcase_analyze_my_today', '/api/analyze/testcase/my_today', '测试用例', '2018-09-09 22:22:42.221809'), ('c2f61fb98e2747ee8068536327731340', '按测试人员统计缺陷', 'bug_analyze_tester', '/api/analyze/bug/tester', '缺陷', '2018-09-09 22:21:24.632336'), ('c7f6188a109543bfa3d953e2a00dacca', '失效测试用例', 'testcase_fail', '/api/qa/testcase/fall', '测试用例', '2018-09-09 21:37:23.027153'), ('d43210b4c9234f9a88e7a78beb24f36f', '测试执行集：已选的测试用例列表', 'testsuite_cell_brief_list', '/api/qa/testsuite/cell/brief_list', '测试用例', '2018-09-09 22:34:02.758692'), ('d86f172da2d44497aaa0474b791c4f6d', '获取用户信息', 'user_userinfo', '/api/user/userinfo', '用户管理', '2018-09-09 21:56:35.787525'), ('e4e118f015b941e0ad039971d1d6658e', '创建用户', 'user_add', '/api/user/add', '用户管理', '2018-09-09 21:55:21.658182'), ('e64a095d843041f3bc17eb6fa992032f', '有效的测试用例列表', 'testcase_valid_list', '/api/qa/testcase/valid_list', '测试用例', '2018-09-09 22:34:40.804703'), ('e9e8f559390c46ff8f15ed870ee3594e', '模块列表树', 'module_all_list', '/api/pm/get_module', '模块管理', '2018-09-09 22:10:10.690063'), ('e9eb50e0646f4198aa4cbefbdd01403f', '缺陷报告详情', 'bug_report_details', '/api/qa/bug/report/details', '缺陷', '2018-09-09 21:48:52.653870'), ('ec23739ecfe742b89e0854cf487b5c54', '编辑测试用例', 'testcase_edit', '/api/qa/testcase/edit', '测试用例', '2018-09-09 21:34:40.653532'), ('ec4d17bae1584c2db469d38a0693ae09', '一级模块列表', 'module_1_list', '/api/pm/module/1/list', '模块管理', '2018-09-09 22:10:44.835845'), ('f4fdd5cc44d049ccbcb86da50ffeca51', '缺陷分析_我的今天', 'bug_analyze_my_today', '/api/analyze/bug/my_today', '缺陷', '2018-09-09 22:20:21.709562'), ('f702d500989048b4801d0a538bb73027', '获取用户组列表', 'user_group', '/api/user/group', '用户管理', '2018-09-09 21:56:04.568396'), ('f8f590873fbd4808b82d4e8186b6f4cf', '分配缺陷', 'bug_assign', '/api/qa/bug/assign', '缺陷', '2018-09-09 21:44:29.029846');
COMMIT;

-- ----------------------------
--  Table structure for `t_permissions_group`
-- ----------------------------
DROP TABLE IF EXISTS `t_permissions_group`;
CREATE TABLE `t_permissions_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `is_allow` int(11) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `group` varchar(20) NOT NULL,
  `permissions_id` char(32) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `t_permissions_group_group_b3e300fa_fk_t_group_group` (`group`),
  KEY `t_permissions_group_permissions_id_543b7169_fk_t_permissions_id` (`permissions_id`),
  CONSTRAINT `t_permissions_group_group_b3e300fa_fk_t_group_group` FOREIGN KEY (`group`) REFERENCES `t_group` (`group`),
  CONSTRAINT `t_permissions_group_permissions_id_543b7169_fk_t_permissions_id` FOREIGN KEY (`permissions_id`) REFERENCES `t_permissions` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=316 DEFAULT CHARSET=utf8mb4 COMMENT='用户组权限';

-- ----------------------------
--  Records of `t_permissions_group`
-- ----------------------------
BEGIN;
INSERT INTO `t_permissions_group` VALUES ('1', '1', '2018-09-10 06:48:00.000000', 'test', '6913ad4a9a1a401eaf2ef3ee26a4a465'), ('2', '1', '2018-09-10 06:48:00.000000', 'test', 'ec4d17bae1584c2db469d38a0693ae09'), ('3', '1', '2018-09-10 06:48:00.000000', 'test', '0c8ec92ab1964d1dba198e65eb61f23e'), ('4', '1', '2018-09-10 06:48:00.000000', 'test', '0e14a50d3984432fb7b99ff7227b5795'), ('5', '1', '2018-09-10 06:48:00.000000', 'test', '4d346aaedd75430aaa8be6390c6595f1'), ('6', '1', '2018-09-10 06:48:00.000000', 'test', '5d9189aa7973426ebe1417d8ddcc122f'), ('7', '1', '2018-09-10 06:48:00.000000', 'test', '7999649a6f794f2ea8b1b64ba0f52cfc'), ('8', '1', '2018-09-10 06:48:00.000000', 'test', '6ece36af9b1848bf810ee108f0b1c55c'), ('9', '1', '2018-09-10 06:48:00.000000', 'test', '15ed7c9856984c079c6ec1da800297b8'), ('10', '-1', '2018-09-10 06:48:00.000000', 'test', '8f79ba2c30394f4fa6dc9f8b027724c3'), ('11', '-1', '2018-09-10 06:48:00.000000', 'test', '54c452206228426096d41dff943ad90f'), ('12', '-1', '2018-09-10 06:48:00.000000', 'test', '316cd908ddab4ac280bf7c0c299b78e5'), ('13', '1', '2018-09-10 06:48:00.000000', 'test', '868db45b920a4bf28990bdf47cb28673'), ('14', '1', '2018-09-10 06:48:00.000000', 'test', '9f08d915207b41adbe626a00774a9a61'), ('15', '1', '2018-09-10 06:48:00.000000', 'test', '64e6b09e09374b079afdc0e1c44a5545'), ('16', '1', '2018-09-10 06:48:00.000000', 'test', '3ce348164a0f4e5d9dd77eee89942042'), ('17', '1', '2018-09-10 06:48:00.000000', 'test', 'f8f590873fbd4808b82d4e8186b6f4cf'), ('18', '-1', '2018-09-10 06:48:00.000000', 'test', '9ab3b78b43a94ea9ad42c063a24e7f53'), ('19', '1', '2018-09-10 06:48:00.000000', 'test', '820b5a9cde714cd18ba0c3f2cb9fed3c'), ('20', '1', '2018-09-10 06:48:00.000000', 'test', 'a7afbd5edb4845869687bc43aacb4a01'), ('21', '-1', '2018-09-10 06:48:00.000000', 'test', 'e4e118f015b941e0ad039971d1d6658e'), ('22', '1', '2018-09-10 06:48:00.000000', 'test', '2c8b2faf5934494cbed2692a71a57e96'), ('23', '1', '2018-09-10 06:48:00.000000', 'test', 'b6ba4637ec5849618f78e7cc5c9d7a58'), ('24', '1', '2018-09-10 06:48:00.000000', 'test', '19f266cd29a14e0fa7d6c61ef5b41490'), ('25', '1', '2018-09-10 06:48:00.000000', 'test', 'aa830da9b76d44d2a1305631704f254d'), ('26', '1', '2018-09-10 06:48:00.000000', 'test', 'c7f6188a109543bfa3d953e2a00dacca'), ('27', '-1', '2018-09-10 06:48:00.000000', 'test', '045210cf30a94f23951c7e68b9dcf5bb'), ('28', '1', '2018-09-10 06:48:00.000000', 'test', '94374b45faf04df28755f039bd883d70'), ('29', '1', '2018-09-10 06:48:00.000000', 'test', 'a14c6fdd1fd74cb6b9db2a25c6475941'), ('30', '1', '2018-09-10 06:48:00.000000', 'test', 'c2f61fb98e2747ee8068536327731340'), ('31', '1', '2018-09-10 06:48:00.000000', 'test', '7c7293a59b154467b59fe87309fa72e2'), ('32', '1', '2018-09-10 06:48:00.000000', 'test', 'bcfb5ff72d8d403d858058f2444efca1'), ('33', '1', '2018-09-10 06:48:00.000000', 'test', 'e64a095d843041f3bc17eb6fa992032f'), ('34', '1', '2018-09-10 06:48:00.000000', 'test', 'e9e8f559390c46ff8f15ed870ee3594e'), ('35', '1', '2018-09-10 06:48:00.000000', 'test', '71037db9d038487593da113a6b1f65be'), ('36', '1', '2018-09-10 06:48:00.000000', 'test', 'd43210b4c9234f9a88e7a78beb24f36f'), ('37', '1', '2018-09-10 06:48:00.000000', 'test', '19a01e70033c411dabf2f734e15fa49d'), ('38', '1', '2018-09-10 06:48:00.000000', 'test', '6d27df660a414a3fb6d73156f0cb7d3d'), ('39', '1', '2018-09-10 06:48:00.000000', 'test', '0f61062a5aca4e7299a4fde489b9d83e'), ('40', '1', '2018-09-10 06:48:00.000000', 'test', '708e501b81e0428ea0f0427c4e97964a'), ('41', '1', '2018-09-10 06:48:00.000000', 'test', '9569acd658b04880a23a21febd3c29ce'), ('42', '1', '2018-09-10 06:48:00.000000', 'test', 'a1dece243b0142ff81f75c5b5d3f89f3'), ('43', '-1', '2018-09-10 06:48:00.000000', 'test', '8dd468711f41404fab71530951d2340c'), ('44', '1', '2018-09-10 06:48:00.000000', 'test', '994e168db4c74c588503a1174da999bc'), ('45', '1', '2018-09-10 06:48:00.000000', 'test', '72ab70daaf7b4f7d8a9335554ed01094'), ('46', '-1', '2018-09-10 06:48:00.000000', 'test', '782e404322e24caa9846b04207414bbb'), ('47', '1', '2018-09-10 06:48:00.000000', 'test', '9b3f96f30978401681edd38ea41d75bf'), ('48', '1', '2018-09-10 06:48:00.000000', 'test', 'bdf1edf832fe42ec93917473f9208250'), ('49', '1', '2018-09-10 06:48:00.000000', 'test', 'ec23739ecfe742b89e0854cf487b5c54'), ('50', '1', '2018-09-10 06:48:00.000000', 'test', '30e7db997a2f4a3d85ce54ae5dc21e06'), ('51', '1', '2018-09-10 06:48:00.000000', 'test', 'f4fdd5cc44d049ccbcb86da50ffeca51'), ('52', '1', '2018-09-10 06:48:00.000000', 'test', '6cc1755a2ca1477c87a398d8dafaf1fc'), ('53', '1', '2018-09-10 06:48:00.000000', 'test', '863cf952242545f2bf5bcca5aa8a3515'), ('54', '1', '2018-09-10 06:48:00.000000', 'test', '0725da1a6ae74c1b90446584dd234e39'), ('55', '1', '2018-09-10 06:48:00.000000', 'test', 'e9eb50e0646f4198aa4cbefbdd01403f'), ('56', '1', '2018-09-10 06:48:00.000000', 'test', '68043153e40143dd97a9acbbc3f94ac5'), ('57', '1', '2018-09-10 06:48:00.000000', 'test', '9c4e5773b642454180ede04e7bd6f793'), ('58', '1', '2018-09-10 06:48:00.000000', 'test', '32e4fbba7762472484d0a66bbe64808d'), ('59', '1', '2018-09-10 06:48:00.000000', 'test', 'd86f172da2d44497aaa0474b791c4f6d'), ('60', '1', '2018-09-10 06:48:00.000000', 'test', 'f702d500989048b4801d0a538bb73027'), ('61', '1', '2018-09-10 06:48:00.000000', 'test', '6067b35290e9426e96c146dcb149c0ae'), ('62', '1', '2018-09-10 06:48:00.000000', 'test', '565c01742ab34ed18d037e791a586099'), ('63', '1', '2018-09-10 06:48:00.000000', 'test', '04bdf9e393e3418b9f941a8a6d493065'), ('64', '1', '2018-09-10 06:48:00.000000', 'developer', '6913ad4a9a1a401eaf2ef3ee26a4a465'), ('65', '1', '2018-09-10 06:48:00.000000', 'developer', 'ec4d17bae1584c2db469d38a0693ae09'), ('66', '1', '2018-09-10 06:48:00.000000', 'developer', '0c8ec92ab1964d1dba198e65eb61f23e'), ('67', '1', '2018-09-10 06:48:00.000000', 'developer', '0e14a50d3984432fb7b99ff7227b5795'), ('68', '1', '2018-09-10 06:48:00.000000', 'developer', '4d346aaedd75430aaa8be6390c6595f1'), ('69', '1', '2018-09-10 06:48:00.000000', 'developer', '5d9189aa7973426ebe1417d8ddcc122f'), ('70', '1', '2018-09-10 06:48:00.000000', 'developer', '7999649a6f794f2ea8b1b64ba0f52cfc'), ('71', '1', '2018-09-10 06:48:00.000000', 'developer', '6ece36af9b1848bf810ee108f0b1c55c'), ('72', '1', '2018-09-10 06:48:00.000000', 'developer', '15ed7c9856984c079c6ec1da800297b8'), ('73', '-1', '2018-09-10 06:48:00.000000', 'developer', '8f79ba2c30394f4fa6dc9f8b027724c3'), ('74', '-1', '2018-09-10 06:48:00.000000', 'developer', '54c452206228426096d41dff943ad90f'), ('75', '-1', '2018-09-10 06:48:00.000000', 'developer', '316cd908ddab4ac280bf7c0c299b78e5'), ('76', '1', '2018-09-10 06:48:00.000000', 'developer', '868db45b920a4bf28990bdf47cb28673'), ('77', '1', '2018-09-10 06:48:00.000000', 'developer', '9f08d915207b41adbe626a00774a9a61'), ('78', '1', '2018-09-10 06:48:00.000000', 'developer', '64e6b09e09374b079afdc0e1c44a5545'), ('79', '1', '2018-09-10 06:48:00.000000', 'developer', '3ce348164a0f4e5d9dd77eee89942042'), ('80', '1', '2018-09-10 06:48:00.000000', 'developer', 'f8f590873fbd4808b82d4e8186b6f4cf'), ('81', '-1', '2018-09-10 06:48:00.000000', 'developer', '9ab3b78b43a94ea9ad42c063a24e7f53'), ('82', '1', '2018-09-10 06:48:00.000000', 'developer', '820b5a9cde714cd18ba0c3f2cb9fed3c'), ('83', '1', '2018-09-10 06:48:00.000000', 'developer', 'a7afbd5edb4845869687bc43aacb4a01'), ('84', '-1', '2018-09-10 06:48:00.000000', 'developer', 'e4e118f015b941e0ad039971d1d6658e'), ('85', '1', '2018-09-10 06:48:00.000000', 'developer', '2c8b2faf5934494cbed2692a71a57e96'), ('86', '1', '2018-09-10 06:48:00.000000', 'developer', 'b6ba4637ec5849618f78e7cc5c9d7a58'), ('87', '-1', '2018-09-10 06:48:00.000000', 'developer', '19f266cd29a14e0fa7d6c61ef5b41490'), ('88', '1', '2018-09-10 06:48:00.000000', 'developer', 'aa830da9b76d44d2a1305631704f254d'), ('89', '1', '2018-09-10 06:48:00.000000', 'developer', 'c7f6188a109543bfa3d953e2a00dacca'), ('90', '-1', '2018-09-10 06:48:00.000000', 'developer', '045210cf30a94f23951c7e68b9dcf5bb'), ('91', '1', '2018-09-10 06:48:00.000000', 'developer', '94374b45faf04df28755f039bd883d70'), ('92', '1', '2018-09-10 06:48:00.000000', 'developer', 'a14c6fdd1fd74cb6b9db2a25c6475941'), ('93', '1', '2018-09-10 06:48:00.000000', 'developer', 'c2f61fb98e2747ee8068536327731340'), ('94', '1', '2018-09-10 06:48:00.000000', 'developer', '7c7293a59b154467b59fe87309fa72e2'), ('95', '1', '2018-09-10 06:48:00.000000', 'developer', 'bcfb5ff72d8d403d858058f2444efca1'), ('96', '1', '2018-09-10 06:48:00.000000', 'developer', 'e64a095d843041f3bc17eb6fa992032f'), ('97', '1', '2018-09-10 06:48:00.000000', 'developer', 'e9e8f559390c46ff8f15ed870ee3594e'), ('98', '1', '2018-09-10 06:48:00.000000', 'developer', '71037db9d038487593da113a6b1f65be'), ('99', '1', '2018-09-10 06:48:00.000000', 'developer', 'd43210b4c9234f9a88e7a78beb24f36f'), ('100', '1', '2018-09-10 06:48:00.000000', 'developer', '19a01e70033c411dabf2f734e15fa49d'), ('101', '1', '2018-09-10 06:48:00.000000', 'developer', '6d27df660a414a3fb6d73156f0cb7d3d'), ('102', '1', '2018-09-10 06:48:00.000000', 'developer', '0f61062a5aca4e7299a4fde489b9d83e'), ('103', '1', '2018-09-10 06:48:00.000000', 'developer', '708e501b81e0428ea0f0427c4e97964a'), ('104', '1', '2018-09-10 06:48:00.000000', 'developer', '9569acd658b04880a23a21febd3c29ce'), ('105', '1', '2018-09-10 06:48:00.000000', 'developer', 'a1dece243b0142ff81f75c5b5d3f89f3'), ('106', '-1', '2018-09-10 06:48:00.000000', 'developer', '8dd468711f41404fab71530951d2340c'), ('107', '1', '2018-09-10 06:48:00.000000', 'developer', '994e168db4c74c588503a1174da999bc'), ('108', '1', '2018-09-10 06:48:00.000000', 'developer', '72ab70daaf7b4f7d8a9335554ed01094'), ('109', '-1', '2018-09-10 06:48:00.000000', 'developer', '782e404322e24caa9846b04207414bbb'), ('110', '1', '2018-09-10 06:48:00.000000', 'developer', '9b3f96f30978401681edd38ea41d75bf'), ('111', '1', '2018-09-10 06:48:00.000000', 'developer', 'bdf1edf832fe42ec93917473f9208250'), ('112', '1', '2018-09-10 06:48:00.000000', 'developer', 'ec23739ecfe742b89e0854cf487b5c54'), ('113', '-1', '2018-09-10 06:48:00.000000', 'developer', '30e7db997a2f4a3d85ce54ae5dc21e06'), ('114', '1', '2018-09-10 06:48:00.000000', 'developer', 'f4fdd5cc44d049ccbcb86da50ffeca51'), ('115', '1', '2018-09-10 06:48:00.000000', 'developer', '6cc1755a2ca1477c87a398d8dafaf1fc'), ('116', '1', '2018-09-10 06:48:00.000000', 'developer', '863cf952242545f2bf5bcca5aa8a3515'), ('117', '1', '2018-09-10 06:48:00.000000', 'developer', '0725da1a6ae74c1b90446584dd234e39'), ('118', '1', '2018-09-10 06:48:00.000000', 'developer', 'e9eb50e0646f4198aa4cbefbdd01403f'), ('119', '1', '2018-09-10 06:48:00.000000', 'developer', '68043153e40143dd97a9acbbc3f94ac5'), ('120', '1', '2018-09-10 06:48:00.000000', 'developer', '9c4e5773b642454180ede04e7bd6f793'), ('121', '1', '2018-09-10 06:48:00.000000', 'developer', '32e4fbba7762472484d0a66bbe64808d'), ('122', '1', '2018-09-10 06:48:00.000000', 'developer', 'd86f172da2d44497aaa0474b791c4f6d'), ('123', '1', '2018-09-10 06:48:00.000000', 'developer', 'f702d500989048b4801d0a538bb73027'), ('124', '1', '2018-09-10 06:48:00.000000', 'developer', '6067b35290e9426e96c146dcb149c0ae'), ('125', '1', '2018-09-10 06:48:00.000000', 'developer', '565c01742ab34ed18d037e791a586099'), ('126', '-1', '2018-09-10 06:48:00.000000', 'developer', '04bdf9e393e3418b9f941a8a6d493065'), ('127', '1', '2018-09-10 06:48:00.000000', 'design', '6913ad4a9a1a401eaf2ef3ee26a4a465'), ('128', '1', '2018-09-10 06:48:00.000000', 'design', 'ec4d17bae1584c2db469d38a0693ae09'), ('129', '1', '2018-09-10 06:48:00.000000', 'design', '0c8ec92ab1964d1dba198e65eb61f23e'), ('130', '1', '2018-09-10 06:48:00.000000', 'design', '0e14a50d3984432fb7b99ff7227b5795'), ('131', '1', '2018-09-10 06:48:00.000000', 'design', '4d346aaedd75430aaa8be6390c6595f1'), ('132', '1', '2018-09-10 06:48:00.000000', 'design', '5d9189aa7973426ebe1417d8ddcc122f'), ('133', '1', '2018-09-10 06:48:00.000000', 'design', '7999649a6f794f2ea8b1b64ba0f52cfc'), ('134', '1', '2018-09-10 06:48:00.000000', 'design', '6ece36af9b1848bf810ee108f0b1c55c'), ('135', '1', '2018-09-10 06:48:00.000000', 'design', '15ed7c9856984c079c6ec1da800297b8'), ('136', '-1', '2018-09-10 06:48:00.000000', 'design', '8f79ba2c30394f4fa6dc9f8b027724c3'), ('137', '-1', '2018-09-10 06:48:00.000000', 'design', '54c452206228426096d41dff943ad90f'), ('138', '-1', '2018-09-10 06:48:00.000000', 'design', '316cd908ddab4ac280bf7c0c299b78e5'), ('139', '1', '2018-09-10 06:48:00.000000', 'design', '868db45b920a4bf28990bdf47cb28673'), ('140', '1', '2018-09-10 06:48:00.000000', 'design', '9f08d915207b41adbe626a00774a9a61'), ('141', '1', '2018-09-10 06:48:00.000000', 'design', '64e6b09e09374b079afdc0e1c44a5545'), ('142', '1', '2018-09-10 06:48:00.000000', 'design', '3ce348164a0f4e5d9dd77eee89942042'), ('143', '1', '2018-09-10 06:48:00.000000', 'design', 'f8f590873fbd4808b82d4e8186b6f4cf'), ('144', '-1', '2018-09-10 06:48:00.000000', 'design', '9ab3b78b43a94ea9ad42c063a24e7f53'), ('145', '1', '2018-09-10 06:48:00.000000', 'design', '820b5a9cde714cd18ba0c3f2cb9fed3c'), ('146', '1', '2018-09-10 06:48:00.000000', 'design', 'a7afbd5edb4845869687bc43aacb4a01'), ('147', '-1', '2018-09-10 06:48:00.000000', 'design', 'e4e118f015b941e0ad039971d1d6658e'), ('148', '1', '2018-09-10 06:48:00.000000', 'design', '2c8b2faf5934494cbed2692a71a57e96'), ('149', '1', '2018-09-10 06:48:00.000000', 'design', 'b6ba4637ec5849618f78e7cc5c9d7a58'), ('150', '-1', '2018-09-10 06:48:00.000000', 'design', '19f266cd29a14e0fa7d6c61ef5b41490'), ('151', '1', '2018-09-10 06:48:00.000000', 'design', 'aa830da9b76d44d2a1305631704f254d'), ('152', '1', '2018-09-10 06:48:00.000000', 'design', 'c7f6188a109543bfa3d953e2a00dacca'), ('153', '-1', '2018-09-10 06:48:00.000000', 'design', '045210cf30a94f23951c7e68b9dcf5bb'), ('154', '1', '2018-09-10 06:48:00.000000', 'design', '94374b45faf04df28755f039bd883d70'), ('155', '1', '2018-09-10 06:48:00.000000', 'design', 'a14c6fdd1fd74cb6b9db2a25c6475941'), ('156', '1', '2018-09-10 06:48:00.000000', 'design', 'c2f61fb98e2747ee8068536327731340'), ('157', '1', '2018-09-10 06:48:00.000000', 'design', '7c7293a59b154467b59fe87309fa72e2'), ('158', '1', '2018-09-10 06:48:00.000000', 'design', 'bcfb5ff72d8d403d858058f2444efca1'), ('159', '1', '2018-09-10 06:48:00.000000', 'design', 'e64a095d843041f3bc17eb6fa992032f'), ('160', '1', '2018-09-10 06:48:00.000000', 'design', 'e9e8f559390c46ff8f15ed870ee3594e'), ('161', '1', '2018-09-10 06:48:00.000000', 'design', '71037db9d038487593da113a6b1f65be'), ('162', '1', '2018-09-10 06:48:00.000000', 'design', 'd43210b4c9234f9a88e7a78beb24f36f'), ('163', '1', '2018-09-10 06:48:00.000000', 'design', '19a01e70033c411dabf2f734e15fa49d'), ('164', '1', '2018-09-10 06:48:00.000000', 'design', '6d27df660a414a3fb6d73156f0cb7d3d'), ('165', '1', '2018-09-10 06:48:00.000000', 'design', '0f61062a5aca4e7299a4fde489b9d83e'), ('166', '1', '2018-09-10 06:48:00.000000', 'design', '708e501b81e0428ea0f0427c4e97964a'), ('167', '1', '2018-09-10 06:48:00.000000', 'design', '9569acd658b04880a23a21febd3c29ce'), ('168', '1', '2018-09-10 06:48:00.000000', 'design', 'a1dece243b0142ff81f75c5b5d3f89f3'), ('169', '-1', '2018-09-10 06:48:00.000000', 'design', '8dd468711f41404fab71530951d2340c'), ('170', '1', '2018-09-10 06:48:00.000000', 'design', '994e168db4c74c588503a1174da999bc'), ('171', '1', '2018-09-10 06:48:00.000000', 'design', '72ab70daaf7b4f7d8a9335554ed01094'), ('172', '-1', '2018-09-10 06:48:00.000000', 'design', '782e404322e24caa9846b04207414bbb'), ('173', '1', '2018-09-10 06:48:00.000000', 'design', '9b3f96f30978401681edd38ea41d75bf'), ('174', '1', '2018-09-10 06:48:00.000000', 'design', 'bdf1edf832fe42ec93917473f9208250'), ('175', '1', '2018-09-10 06:48:00.000000', 'design', 'ec23739ecfe742b89e0854cf487b5c54'), ('176', '-1', '2018-09-10 06:48:00.000000', 'design', '30e7db997a2f4a3d85ce54ae5dc21e06'), ('177', '1', '2018-09-10 06:48:00.000000', 'design', 'f4fdd5cc44d049ccbcb86da50ffeca51'), ('178', '1', '2018-09-10 06:48:00.000000', 'design', '6cc1755a2ca1477c87a398d8dafaf1fc'), ('179', '1', '2018-09-10 06:48:00.000000', 'design', '863cf952242545f2bf5bcca5aa8a3515'), ('180', '1', '2018-09-10 06:48:00.000000', 'design', '0725da1a6ae74c1b90446584dd234e39'), ('181', '1', '2018-09-10 06:48:00.000000', 'design', 'e9eb50e0646f4198aa4cbefbdd01403f'), ('182', '1', '2018-09-10 06:48:00.000000', 'design', '68043153e40143dd97a9acbbc3f94ac5'), ('183', '1', '2018-09-10 06:48:00.000000', 'design', '9c4e5773b642454180ede04e7bd6f793'), ('184', '1', '2018-09-10 06:48:00.000000', 'design', '32e4fbba7762472484d0a66bbe64808d'), ('185', '1', '2018-09-10 06:48:00.000000', 'design', 'd86f172da2d44497aaa0474b791c4f6d'), ('186', '1', '2018-09-10 06:48:00.000000', 'design', 'f702d500989048b4801d0a538bb73027'), ('187', '1', '2018-09-10 06:48:00.000000', 'design', '6067b35290e9426e96c146dcb149c0ae'), ('188', '1', '2018-09-10 06:48:00.000000', 'design', '565c01742ab34ed18d037e791a586099'), ('189', '-1', '2018-09-10 06:48:00.000000', 'design', '04bdf9e393e3418b9f941a8a6d493065'), ('190', '1', '2018-09-10 06:48:00.000000', 'pm', '6913ad4a9a1a401eaf2ef3ee26a4a465'), ('191', '1', '2018-09-10 06:48:00.000000', 'pm', 'ec4d17bae1584c2db469d38a0693ae09'), ('192', '1', '2018-09-10 06:48:00.000000', 'pm', '0c8ec92ab1964d1dba198e65eb61f23e'), ('193', '1', '2018-09-10 06:48:00.000000', 'pm', '0e14a50d3984432fb7b99ff7227b5795'), ('194', '1', '2018-09-10 06:48:00.000000', 'pm', '4d346aaedd75430aaa8be6390c6595f1'), ('195', '1', '2018-09-10 06:48:00.000000', 'pm', '5d9189aa7973426ebe1417d8ddcc122f'), ('196', '1', '2018-09-10 06:48:00.000000', 'pm', '7999649a6f794f2ea8b1b64ba0f52cfc'), ('197', '1', '2018-09-10 06:48:00.000000', 'pm', '6ece36af9b1848bf810ee108f0b1c55c'), ('198', '1', '2018-09-10 06:48:00.000000', 'pm', '15ed7c9856984c079c6ec1da800297b8'), ('199', '-1', '2018-09-10 06:48:00.000000', 'pm', '8f79ba2c30394f4fa6dc9f8b027724c3'), ('200', '-1', '2018-09-10 06:48:00.000000', 'pm', '54c452206228426096d41dff943ad90f'), ('201', '-1', '2018-09-10 06:48:00.000000', 'pm', '316cd908ddab4ac280bf7c0c299b78e5'), ('202', '1', '2018-09-10 06:48:00.000000', 'pm', '868db45b920a4bf28990bdf47cb28673'), ('203', '1', '2018-09-10 06:48:00.000000', 'pm', '9f08d915207b41adbe626a00774a9a61'), ('204', '1', '2018-09-10 06:48:00.000000', 'pm', '64e6b09e09374b079afdc0e1c44a5545'), ('205', '1', '2018-09-10 06:48:00.000000', 'pm', '3ce348164a0f4e5d9dd77eee89942042'), ('206', '1', '2018-09-10 06:48:00.000000', 'pm', 'f8f590873fbd4808b82d4e8186b6f4cf'), ('207', '-1', '2018-09-10 06:48:00.000000', 'pm', '9ab3b78b43a94ea9ad42c063a24e7f53'), ('208', '1', '2018-09-10 06:48:00.000000', 'pm', '820b5a9cde714cd18ba0c3f2cb9fed3c'), ('209', '1', '2018-09-10 06:48:00.000000', 'pm', 'a7afbd5edb4845869687bc43aacb4a01'), ('210', '-1', '2018-09-10 06:48:00.000000', 'pm', 'e4e118f015b941e0ad039971d1d6658e'), ('211', '1', '2018-09-10 06:48:00.000000', 'pm', '2c8b2faf5934494cbed2692a71a57e96'), ('212', '1', '2018-09-10 06:48:00.000000', 'pm', 'b6ba4637ec5849618f78e7cc5c9d7a58'), ('213', '-1', '2018-09-10 06:48:00.000000', 'pm', '19f266cd29a14e0fa7d6c61ef5b41490'), ('214', '1', '2018-09-10 06:48:00.000000', 'pm', 'aa830da9b76d44d2a1305631704f254d'), ('215', '1', '2018-09-10 06:48:00.000000', 'pm', 'c7f6188a109543bfa3d953e2a00dacca'), ('216', '-1', '2018-09-10 06:48:00.000000', 'pm', '045210cf30a94f23951c7e68b9dcf5bb'), ('217', '1', '2018-09-10 06:48:00.000000', 'pm', '94374b45faf04df28755f039bd883d70'), ('218', '1', '2018-09-10 06:48:00.000000', 'pm', 'a14c6fdd1fd74cb6b9db2a25c6475941'), ('219', '1', '2018-09-10 06:48:00.000000', 'pm', 'c2f61fb98e2747ee8068536327731340'), ('220', '1', '2018-09-10 06:48:00.000000', 'pm', '7c7293a59b154467b59fe87309fa72e2'), ('221', '1', '2018-09-10 06:48:00.000000', 'pm', 'bcfb5ff72d8d403d858058f2444efca1'), ('222', '1', '2018-09-10 06:48:00.000000', 'pm', 'e64a095d843041f3bc17eb6fa992032f'), ('223', '1', '2018-09-10 06:48:00.000000', 'pm', 'e9e8f559390c46ff8f15ed870ee3594e'), ('224', '1', '2018-09-10 06:48:00.000000', 'pm', '71037db9d038487593da113a6b1f65be'), ('225', '1', '2018-09-10 06:48:00.000000', 'pm', 'd43210b4c9234f9a88e7a78beb24f36f'), ('226', '1', '2018-09-10 06:48:00.000000', 'pm', '19a01e70033c411dabf2f734e15fa49d'), ('227', '1', '2018-09-10 06:48:00.000000', 'pm', '6d27df660a414a3fb6d73156f0cb7d3d'), ('228', '1', '2018-09-10 06:48:00.000000', 'pm', '0f61062a5aca4e7299a4fde489b9d83e'), ('229', '1', '2018-09-10 06:48:00.000000', 'pm', '708e501b81e0428ea0f0427c4e97964a'), ('230', '1', '2018-09-10 06:48:00.000000', 'pm', '9569acd658b04880a23a21febd3c29ce'), ('231', '1', '2018-09-10 06:48:00.000000', 'pm', 'a1dece243b0142ff81f75c5b5d3f89f3'), ('232', '-1', '2018-09-10 06:48:00.000000', 'pm', '8dd468711f41404fab71530951d2340c'), ('233', '1', '2018-09-10 06:48:00.000000', 'pm', '994e168db4c74c588503a1174da999bc'), ('234', '1', '2018-09-10 06:48:00.000000', 'pm', '72ab70daaf7b4f7d8a9335554ed01094'), ('235', '-1', '2018-09-10 06:48:00.000000', 'pm', '782e404322e24caa9846b04207414bbb'), ('236', '1', '2018-09-10 06:48:00.000000', 'pm', '9b3f96f30978401681edd38ea41d75bf'), ('237', '1', '2018-09-10 06:48:00.000000', 'pm', 'bdf1edf832fe42ec93917473f9208250'), ('238', '1', '2018-09-10 06:48:00.000000', 'pm', 'ec23739ecfe742b89e0854cf487b5c54'), ('239', '-1', '2018-09-10 06:48:00.000000', 'pm', '30e7db997a2f4a3d85ce54ae5dc21e06'), ('240', '1', '2018-09-10 06:48:00.000000', 'pm', 'f4fdd5cc44d049ccbcb86da50ffeca51'), ('241', '1', '2018-09-10 06:48:00.000000', 'pm', '6cc1755a2ca1477c87a398d8dafaf1fc'), ('242', '1', '2018-09-10 06:48:00.000000', 'pm', '863cf952242545f2bf5bcca5aa8a3515'), ('243', '1', '2018-09-10 06:48:00.000000', 'pm', '0725da1a6ae74c1b90446584dd234e39'), ('244', '1', '2018-09-10 06:48:00.000000', 'pm', 'e9eb50e0646f4198aa4cbefbdd01403f'), ('245', '1', '2018-09-10 06:48:00.000000', 'pm', '68043153e40143dd97a9acbbc3f94ac5'), ('246', '1', '2018-09-10 06:48:00.000000', 'pm', '9c4e5773b642454180ede04e7bd6f793'), ('247', '1', '2018-09-10 06:48:00.000000', 'pm', '32e4fbba7762472484d0a66bbe64808d'), ('248', '1', '2018-09-10 06:48:00.000000', 'pm', 'd86f172da2d44497aaa0474b791c4f6d'), ('249', '1', '2018-09-10 06:48:00.000000', 'pm', 'f702d500989048b4801d0a538bb73027'), ('250', '1', '2018-09-10 06:48:00.000000', 'pm', '6067b35290e9426e96c146dcb149c0ae'), ('251', '1', '2018-09-10 06:48:00.000000', 'pm', '565c01742ab34ed18d037e791a586099'), ('252', '-1', '2018-09-10 06:48:00.000000', 'pm', '04bdf9e393e3418b9f941a8a6d493065'), ('253', '1', '2018-09-10 06:48:00.000000', 'manager', '6913ad4a9a1a401eaf2ef3ee26a4a465'), ('254', '1', '2018-09-10 06:48:00.000000', 'manager', 'ec4d17bae1584c2db469d38a0693ae09'), ('255', '1', '2018-09-10 06:48:00.000000', 'manager', '0c8ec92ab1964d1dba198e65eb61f23e'), ('256', '1', '2018-09-10 06:48:00.000000', 'manager', '0e14a50d3984432fb7b99ff7227b5795'), ('257', '1', '2018-09-10 06:48:00.000000', 'manager', '4d346aaedd75430aaa8be6390c6595f1'), ('258', '1', '2018-09-10 06:48:00.000000', 'manager', '5d9189aa7973426ebe1417d8ddcc122f'), ('259', '1', '2018-09-10 06:48:00.000000', 'manager', '7999649a6f794f2ea8b1b64ba0f52cfc'), ('260', '1', '2018-09-10 06:48:00.000000', 'manager', '6ece36af9b1848bf810ee108f0b1c55c'), ('261', '1', '2018-09-10 06:48:00.000000', 'manager', '15ed7c9856984c079c6ec1da800297b8'), ('262', '-1', '2018-09-10 06:48:00.000000', 'manager', '8f79ba2c30394f4fa6dc9f8b027724c3'), ('263', '-1', '2018-09-10 06:48:00.000000', 'manager', '54c452206228426096d41dff943ad90f'), ('264', '-1', '2018-09-10 06:48:00.000000', 'manager', '316cd908ddab4ac280bf7c0c299b78e5'), ('265', '1', '2018-09-10 06:48:00.000000', 'manager', '868db45b920a4bf28990bdf47cb28673'), ('266', '1', '2018-09-10 06:48:00.000000', 'manager', '9f08d915207b41adbe626a00774a9a61'), ('267', '1', '2018-09-10 06:48:00.000000', 'manager', '64e6b09e09374b079afdc0e1c44a5545'), ('268', '1', '2018-09-10 06:48:00.000000', 'manager', '3ce348164a0f4e5d9dd77eee89942042'), ('269', '1', '2018-09-10 06:48:00.000000', 'manager', 'f8f590873fbd4808b82d4e8186b6f4cf'), ('270', '-1', '2018-09-10 06:48:00.000000', 'manager', '9ab3b78b43a94ea9ad42c063a24e7f53'), ('271', '1', '2018-09-10 06:48:00.000000', 'manager', '820b5a9cde714cd18ba0c3f2cb9fed3c'), ('272', '1', '2018-09-10 06:48:00.000000', 'manager', 'a7afbd5edb4845869687bc43aacb4a01'), ('273', '-1', '2018-09-10 06:48:00.000000', 'manager', 'e4e118f015b941e0ad039971d1d6658e'), ('274', '1', '2018-09-10 06:48:00.000000', 'manager', '2c8b2faf5934494cbed2692a71a57e96'), ('275', '1', '2018-09-10 06:48:00.000000', 'manager', 'b6ba4637ec5849618f78e7cc5c9d7a58'), ('276', '-1', '2018-09-10 06:48:00.000000', 'manager', '19f266cd29a14e0fa7d6c61ef5b41490'), ('277', '1', '2018-09-10 06:48:00.000000', 'manager', 'aa830da9b76d44d2a1305631704f254d'), ('278', '1', '2018-09-10 06:48:00.000000', 'manager', 'c7f6188a109543bfa3d953e2a00dacca'), ('279', '-1', '2018-09-10 06:48:00.000000', 'manager', '045210cf30a94f23951c7e68b9dcf5bb'), ('280', '1', '2018-09-10 06:48:00.000000', 'manager', '94374b45faf04df28755f039bd883d70'), ('281', '1', '2018-09-10 06:48:00.000000', 'manager', 'a14c6fdd1fd74cb6b9db2a25c6475941'), ('282', '1', '2018-09-10 06:48:00.000000', 'manager', 'c2f61fb98e2747ee8068536327731340'), ('283', '1', '2018-09-10 06:48:00.000000', 'manager', '7c7293a59b154467b59fe87309fa72e2'), ('284', '1', '2018-09-10 06:48:00.000000', 'manager', 'bcfb5ff72d8d403d858058f2444efca1'), ('285', '1', '2018-09-10 06:48:00.000000', 'manager', 'e64a095d843041f3bc17eb6fa992032f'), ('286', '1', '2018-09-10 06:48:00.000000', 'manager', 'e9e8f559390c46ff8f15ed870ee3594e'), ('287', '1', '2018-09-10 06:48:00.000000', 'manager', '71037db9d038487593da113a6b1f65be'), ('288', '1', '2018-09-10 06:48:00.000000', 'manager', 'd43210b4c9234f9a88e7a78beb24f36f'), ('289', '1', '2018-09-10 06:48:00.000000', 'manager', '19a01e70033c411dabf2f734e15fa49d'), ('290', '1', '2018-09-10 06:48:00.000000', 'manager', '6d27df660a414a3fb6d73156f0cb7d3d'), ('291', '1', '2018-09-10 06:48:00.000000', 'manager', '0f61062a5aca4e7299a4fde489b9d83e'), ('292', '1', '2018-09-10 06:48:00.000000', 'manager', '708e501b81e0428ea0f0427c4e97964a'), ('293', '1', '2018-09-10 06:48:00.000000', 'manager', '9569acd658b04880a23a21febd3c29ce'), ('294', '1', '2018-09-10 06:48:00.000000', 'manager', 'a1dece243b0142ff81f75c5b5d3f89f3'), ('295', '-1', '2018-09-10 06:48:00.000000', 'manager', '8dd468711f41404fab71530951d2340c'), ('296', '1', '2018-09-10 06:48:00.000000', 'manager', '994e168db4c74c588503a1174da999bc'), ('297', '1', '2018-09-10 06:48:00.000000', 'manager', '72ab70daaf7b4f7d8a9335554ed01094'), ('298', '-1', '2018-09-10 06:48:00.000000', 'manager', '782e404322e24caa9846b04207414bbb'), ('299', '1', '2018-09-10 06:48:00.000000', 'manager', '9b3f96f30978401681edd38ea41d75bf'), ('300', '1', '2018-09-10 06:48:00.000000', 'manager', 'bdf1edf832fe42ec93917473f9208250'), ('301', '1', '2018-09-10 06:48:00.000000', 'manager', 'ec23739ecfe742b89e0854cf487b5c54'), ('302', '-1', '2018-09-10 06:48:00.000000', 'manager', '30e7db997a2f4a3d85ce54ae5dc21e06'), ('303', '1', '2018-09-10 06:48:00.000000', 'manager', 'f4fdd5cc44d049ccbcb86da50ffeca51'), ('304', '1', '2018-09-10 06:48:00.000000', 'manager', '6cc1755a2ca1477c87a398d8dafaf1fc'), ('305', '1', '2018-09-10 06:48:00.000000', 'manager', '863cf952242545f2bf5bcca5aa8a3515'), ('306', '1', '2018-09-10 06:48:00.000000', 'manager', '0725da1a6ae74c1b90446584dd234e39'), ('307', '1', '2018-09-10 06:48:00.000000', 'manager', 'e9eb50e0646f4198aa4cbefbdd01403f'), ('308', '1', '2018-09-10 06:48:00.000000', 'manager', '68043153e40143dd97a9acbbc3f94ac5'), ('309', '1', '2018-09-10 06:48:00.000000', 'manager', '9c4e5773b642454180ede04e7bd6f793'), ('310', '1', '2018-09-10 06:48:00.000000', 'manager', '32e4fbba7762472484d0a66bbe64808d'), ('311', '1', '2018-09-10 06:48:00.000000', 'manager', 'd86f172da2d44497aaa0474b791c4f6d'), ('312', '1', '2018-09-10 06:48:00.000000', 'manager', 'f702d500989048b4801d0a538bb73027'), ('313', '1', '2018-09-10 06:48:00.000000', 'manager', '6067b35290e9426e96c146dcb149c0ae'), ('314', '1', '2018-09-10 06:48:00.000000', 'manager', '565c01742ab34ed18d037e791a586099'), ('315', '-1', '2018-09-10 06:48:00.000000', 'manager', '04bdf9e393e3418b9f941a8a6d493065');
COMMIT;

-- ----------------------------
--  Table structure for `t_product`
-- ----------------------------
DROP TABLE IF EXISTS `t_product`;
CREATE TABLE `t_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_name` varchar(50) NOT NULL,
  `product_code` varchar(20) NOT NULL,
  `status` int(11) NOT NULL,
  `remark` varchar(100) DEFAULT NULL,
  `start_time` datetime(6) DEFAULT NULL,
  `end_time` datetime(6) DEFAULT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `creator_id` char(32) NOT NULL,
  `principal` char(32) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `product_code` (`product_code`),
  KEY `t_product_creator_id_b47a31d9_fk_t_user_user_id` (`creator_id`),
  KEY `t_product_principal_caf02773_fk_t_user_user_id` (`principal`),
  CONSTRAINT `t_product_creator_id_b47a31d9_fk_t_user_user_id` FOREIGN KEY (`creator_id`) REFERENCES `t_user` (`user_id`),
  CONSTRAINT `t_product_principal_caf02773_fk_t_user_user_id` FOREIGN KEY (`principal`) REFERENCES `t_user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='产品/项目表';

-- ----------------------------
--  Table structure for `t_product_members`
-- ----------------------------
DROP TABLE IF EXISTS `t_product_members`;
CREATE TABLE `t_product_members` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status` int(11) NOT NULL,
  `join_time` datetime(6) NOT NULL,
  `banned_time` datetime(6) DEFAULT NULL,
  `member_id` char(32) NOT NULL,
  `product_code` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `t_product_members_member_id_fbad669f_fk_t_user_user_id` (`member_id`),
  KEY `t_product_members_product_code_5dfbe5b6_fk_t_product` (`product_code`),
  CONSTRAINT `t_product_members_member_id_fbad669f_fk_t_user_user_id` FOREIGN KEY (`member_id`) REFERENCES `t_user` (`user_id`),
  CONSTRAINT `t_product_members_product_code_5dfbe5b6_fk_t_product` FOREIGN KEY (`product_code`) REFERENCES `t_product` (`product_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='产品/项目成员表';

-- ----------------------------
--  Table structure for `t_release`
-- ----------------------------
DROP TABLE IF EXISTS `t_release`;
CREATE TABLE `t_release` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `version` varchar(20) NOT NULL,
  `start_time` datetime(6) DEFAULT NULL,
  `online_time` datetime(6) DEFAULT NULL,
  `practicalnline_time` datetime(6) DEFAULT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `changer_id` char(32) DEFAULT NULL,
  `creator_id` char(32) NOT NULL,
  `deleter_id` char(32) DEFAULT NULL,
  `product_code` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `t_release_changer_id_156ce7f1_fk_t_user_user_id` (`changer_id`),
  KEY `t_release_creator_id_ac9c41ba_fk_t_user_user_id` (`creator_id`),
  KEY `t_release_deleter_id_edb34e97_fk_t_user_user_id` (`deleter_id`),
  KEY `t_release_product_code_2020d330_fk_t_product_product_code` (`product_code`),
  CONSTRAINT `t_release_changer_id_156ce7f1_fk_t_user_user_id` FOREIGN KEY (`changer_id`) REFERENCES `t_user` (`user_id`),
  CONSTRAINT `t_release_creator_id_ac9c41ba_fk_t_user_user_id` FOREIGN KEY (`creator_id`) REFERENCES `t_user` (`user_id`),
  CONSTRAINT `t_release_deleter_id_edb34e97_fk_t_user_user_id` FOREIGN KEY (`deleter_id`) REFERENCES `t_user` (`user_id`),
  CONSTRAINT `t_release_product_code_2020d330_fk_t_product_product_code` FOREIGN KEY (`product_code`) REFERENCES `t_product` (`product_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='产品/项目版本表';

-- ----------------------------
--  Table structure for `t_system_config`
-- ----------------------------
DROP TABLE IF EXISTS `t_system_config`;
CREATE TABLE `t_system_config` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(20) NOT NULL,
  `code_value` int(11) NOT NULL,
  `code_desc` varchar(100) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
--  Table structure for `t_testcase`
-- ----------------------------
DROP TABLE IF EXISTS `t_testcase`;
CREATE TABLE `t_testcase` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `case_id` char(32) NOT NULL,
  `category` varchar(20) NOT NULL,
  `title` longtext NOT NULL,
  `precondition` varchar(500) DEFAULT NULL,
  `DataInput` longtext,
  `steps` longtext NOT NULL,
  `expected_result` longtext NOT NULL,
  `priority` varchar(10) DEFAULT NULL,
  `remark` longtext NOT NULL,
  `isChange` int(11) NOT NULL,
  `isDelete` int(11) NOT NULL,
  `isReview` int(11) NOT NULL,
  `status` int(11) NOT NULL,
  `fall_time` datetime(6) DEFAULT NULL,
  `change_time` datetime(6) DEFAULT NULL,
  `delete_time` datetime(6) DEFAULT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `changer_id` char(32) DEFAULT NULL,
  `creator_id` char(32) NOT NULL,
  `deleter_id` char(32) DEFAULT NULL,
  `faller_id` char(32) DEFAULT NULL,
  `m1_id` int(11) DEFAULT NULL,
  `m2_id` int(11) DEFAULT NULL,
  `product_code` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `case_id` (`case_id`),
  KEY `t_testcase_changer_id_2e16b5c8_fk_t_user_user_id` (`changer_id`),
  KEY `t_testcase_creator_id_3410804e_fk_t_user_user_id` (`creator_id`),
  KEY `t_testcase_deleter_id_10cba4fd_fk_t_user_user_id` (`deleter_id`),
  KEY `t_testcase_faller_id_608011bf_fk_t_user_user_id` (`faller_id`),
  KEY `t_testcase_m1_id_b98ddcb8_fk_t_module_1_id` (`m1_id`),
  KEY `t_testcase_m2_id_1c19276c_fk_t_module_2_id` (`m2_id`),
  KEY `t_testcase_product_code_3dd1fed5_fk_t_product_product_code` (`product_code`),
  CONSTRAINT `t_testcase_changer_id_2e16b5c8_fk_t_user_user_id` FOREIGN KEY (`changer_id`) REFERENCES `t_user` (`user_id`),
  CONSTRAINT `t_testcase_creator_id_3410804e_fk_t_user_user_id` FOREIGN KEY (`creator_id`) REFERENCES `t_user` (`user_id`),
  CONSTRAINT `t_testcase_deleter_id_10cba4fd_fk_t_user_user_id` FOREIGN KEY (`deleter_id`) REFERENCES `t_user` (`user_id`),
  CONSTRAINT `t_testcase_faller_id_608011bf_fk_t_user_user_id` FOREIGN KEY (`faller_id`) REFERENCES `t_user` (`user_id`),
  CONSTRAINT `t_testcase_m1_id_b98ddcb8_fk_t_module_1_id` FOREIGN KEY (`m1_id`) REFERENCES `t_module_1` (`id`),
  CONSTRAINT `t_testcase_m2_id_1c19276c_fk_t_module_2_id` FOREIGN KEY (`m2_id`) REFERENCES `t_module_2` (`id`),
  CONSTRAINT `t_testcase_product_code_3dd1fed5_fk_t_product_product_code` FOREIGN KEY (`product_code`) REFERENCES `t_product` (`product_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='测试用例表';

-- ----------------------------
--  Table structure for `t_testcase_review`
-- ----------------------------
DROP TABLE IF EXISTS `t_testcase_review`;
CREATE TABLE `t_testcase_review` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `result` int(11) NOT NULL,
  `remark` varchar(2000) DEFAULT NULL,
  `create_time` datetime(6) NOT NULL,
  `case_id` char(32) NOT NULL,
  `user_id` char(32) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `t_testcase_review_case_id_8b4cfa88_fk_t_testcase_case_id` (`case_id`),
  KEY `t_testcase_review_user_id_973a5df0_fk_t_user_user_id` (`user_id`),
  CONSTRAINT `t_testcase_review_case_id_8b4cfa88_fk_t_testcase_case_id` FOREIGN KEY (`case_id`) REFERENCES `t_testcase` (`case_id`),
  CONSTRAINT `t_testcase_review_user_id_973a5df0_fk_t_user_user_id` FOREIGN KEY (`user_id`) REFERENCES `t_user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='测试用例评审表';

-- ----------------------------
--  Table structure for `t_testsuite`
-- ----------------------------
DROP TABLE IF EXISTS `t_testsuite`;
CREATE TABLE `t_testsuite` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `suite_id` char(32) NOT NULL,
  `suite_name` varchar(30) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `creator_id` char(32) NOT NULL,
  `product_code` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `suite_id` (`suite_id`),
  KEY `t_testsuite_creator_id_9499e1b4_fk_t_user_user_id` (`creator_id`),
  KEY `t_testsuite_product_code_7b806ee3_fk_t_product_product_code` (`product_code`),
  CONSTRAINT `t_testsuite_creator_id_9499e1b4_fk_t_user_user_id` FOREIGN KEY (`creator_id`) REFERENCES `t_user` (`user_id`),
  CONSTRAINT `t_testsuite_product_code_7b806ee3_fk_t_product_product_code` FOREIGN KEY (`product_code`) REFERENCES `t_product` (`product_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='测试用例执行集';

-- ----------------------------
--  Table structure for `t_testsuite_cell`
-- ----------------------------
DROP TABLE IF EXISTS `t_testsuite_cell`;
CREATE TABLE `t_testsuite_cell` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cell_id` char(32) NOT NULL,
  `result` int(11) NOT NULL,
  `run_time` datetime(6) DEFAULT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `case_id` char(32) NOT NULL,
  `creator_id` char(32) NOT NULL,
  `runner_id` char(32) DEFAULT NULL,
  `suite_id` char(32) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cell_id` (`cell_id`),
  KEY `t_testsuite_cell_case_id_d05db246_fk_t_testcase_case_id` (`case_id`),
  KEY `t_testsuite_cell_creator_id_234a56e8_fk_t_user_user_id` (`creator_id`),
  KEY `t_testsuite_cell_runner_id_11de2317_fk_t_user_user_id` (`runner_id`),
  KEY `t_testsuite_cell_suite_id_e27ca394_fk_t_testsuite_suite_id` (`suite_id`),
  CONSTRAINT `t_testsuite_cell_case_id_d05db246_fk_t_testcase_case_id` FOREIGN KEY (`case_id`) REFERENCES `t_testcase` (`case_id`),
  CONSTRAINT `t_testsuite_cell_creator_id_234a56e8_fk_t_user_user_id` FOREIGN KEY (`creator_id`) REFERENCES `t_user` (`user_id`),
  CONSTRAINT `t_testsuite_cell_runner_id_11de2317_fk_t_user_user_id` FOREIGN KEY (`runner_id`) REFERENCES `t_user` (`user_id`),
  CONSTRAINT `t_testsuite_cell_suite_id_e27ca394_fk_t_testsuite_suite_id` FOREIGN KEY (`suite_id`) REFERENCES `t_testsuite` (`suite_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='测试用例执行表';

-- ----------------------------
--  Table structure for `t_upload_image`
-- ----------------------------
DROP TABLE IF EXISTS `t_upload_image`;
CREATE TABLE `t_upload_image` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `annex` varchar(255) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
--  Table structure for `t_user`
-- ----------------------------
DROP TABLE IF EXISTS `t_user`;
CREATE TABLE `t_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` char(32) NOT NULL,
  `email` varchar(30) DEFAULT NULL,
  `password` varchar(200) DEFAULT NULL,
  `mobile` varchar(11) DEFAULT NULL,
  `user_status` int(11) NOT NULL,
  `realname` varchar(50) DEFAULT NULL,
  `position` varchar(50) DEFAULT NULL,
  `gender` int(11) NOT NULL,
  `avatarUrl` varchar(300) DEFAULT NULL,
  `province` varchar(20) DEFAULT NULL,
  `city` varchar(20) DEFAULT NULL,
  `source` varchar(20) DEFAULT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `group` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  UNIQUE KEY `t_user_email_realname_eb131b7b_uniq` (`email`,`realname`),
  KEY `t_user_group_e5ccc203_fk_t_group_group` (`group`),
  CONSTRAINT `t_user_group_e5ccc203_fk_t_group_group` FOREIGN KEY (`group`) REFERENCES `t_group` (`group`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户表';

SET FOREIGN_KEY_CHECKS = 1;
