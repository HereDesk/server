/*
 Navicat Premium Data Transfer

 Source Server         : 127.0.0.1
 Source Server Type    : MySQL
 Source Server Version : 80012
 Source Host           : localhost
 Source Database       : here_desk

 Target Server Type    : MySQL
 Target Server Version : 80012
 File Encoding         : utf-8

 Date: 11/04/2018 13:55:36 PM
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `auth_group`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
--  Table structure for `auth_permission`
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=153 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
--  Records of `auth_permission`
-- ----------------------------
BEGIN;
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry'), ('2', 'Can change log entry', '1', 'change_logentry'), ('3', 'Can delete log entry', '1', 'delete_logentry'), ('4', 'Can view log entry', '1', 'view_logentry'), ('5', 'Can add permission', '2', 'add_permission'), ('6', 'Can change permission', '2', 'change_permission'), ('7', 'Can delete permission', '2', 'delete_permission'), ('8', 'Can view permission', '2', 'view_permission'), ('9', 'Can add group', '3', 'add_group'), ('10', 'Can change group', '3', 'change_group'), ('11', 'Can delete group', '3', 'delete_group'), ('12', 'Can view group', '3', 'view_group'), ('13', 'Can add user', '4', 'add_user'), ('14', 'Can change user', '4', 'change_user'), ('15', 'Can delete user', '4', 'delete_user'), ('16', 'Can view user', '4', 'view_user'), ('17', 'Can add content type', '5', 'add_contenttype'), ('18', 'Can change content type', '5', 'change_contenttype'), ('19', 'Can delete content type', '5', 'delete_contenttype'), ('20', 'Can view content type', '5', 'view_contenttype'), ('21', 'Can add session', '6', 'add_session'), ('22', 'Can change session', '6', 'change_session'), ('23', 'Can delete session', '6', 'delete_session'), ('24', 'Can view session', '6', 'view_session'), ('25', 'Can add blacklist ip', '7', 'add_blacklistip'), ('26', 'Can change blacklist ip', '7', 'change_blacklistip'), ('27', 'Can delete blacklist ip', '7', 'delete_blacklistip'), ('28', 'Can view blacklist ip', '7', 'view_blacklistip'), ('29', 'Can add api', '8', 'add_api'), ('30', 'Can change api', '8', 'change_api'), ('31', 'Can delete api', '8', 'delete_api'), ('32', 'Can view api', '8', 'view_api'), ('33', 'Can add api permissions', '9', 'add_apipermissions'), ('34', 'Can change api permissions', '9', 'change_apipermissions'), ('35', 'Can delete api permissions', '9', 'delete_apipermissions'), ('36', 'Can view api permissions', '9', 'view_apipermissions'), ('37', 'Can add authentication', '10', 'add_authentication'), ('38', 'Can change authentication', '10', 'change_authentication'), ('39', 'Can delete authentication', '10', 'delete_authentication'), ('40', 'Can view authentication', '10', 'view_authentication'), ('41', 'Can add bug', '11', 'add_bug'), ('42', 'Can change bug', '11', 'change_bug'), ('43', 'Can delete bug', '11', 'delete_bug'), ('44', 'Can view bug', '11', 'view_bug'), ('45', 'Can add bug annex', '12', 'add_bugannex'), ('46', 'Can change bug annex', '12', 'change_bugannex'), ('47', 'Can delete bug annex', '12', 'delete_bugannex'), ('48', 'Can view bug annex', '12', 'view_bugannex'), ('49', 'Can add bug history', '13', 'add_bughistory'), ('50', 'Can change bug history', '13', 'change_bughistory'), ('51', 'Can delete bug history', '13', 'delete_bughistory'), ('52', 'Can view bug history', '13', 'view_bughistory'), ('53', 'Can add bug priority', '14', 'add_bugpriority'), ('54', 'Can change bug priority', '14', 'change_bugpriority'), ('55', 'Can delete bug priority', '14', 'delete_bugpriority'), ('56', 'Can view bug priority', '14', 'view_bugpriority'), ('57', 'Can add bug report', '15', 'add_bugreport'), ('58', 'Can change bug report', '15', 'change_bugreport'), ('59', 'Can delete bug report', '15', 'delete_bugreport'), ('60', 'Can view bug report', '15', 'view_bugreport'), ('61', 'Can add bug severity', '16', 'add_bugseverity'), ('62', 'Can change bug severity', '16', 'change_bugseverity'), ('63', 'Can delete bug severity', '16', 'delete_bugseverity'), ('64', 'Can view bug severity', '16', 'view_bugseverity'), ('65', 'Can add bug solution', '17', 'add_bugsolution'), ('66', 'Can change bug solution', '17', 'change_bugsolution'), ('67', 'Can delete bug solution', '17', 'delete_bugsolution'), ('68', 'Can view bug solution', '17', 'view_bugsolution'), ('69', 'Can add bug status', '18', 'add_bugstatus'), ('70', 'Can change bug status', '18', 'change_bugstatus'), ('71', 'Can delete bug status', '18', 'delete_bugstatus'), ('72', 'Can view bug status', '18', 'view_bugstatus'), ('73', 'Can add bug type', '19', 'add_bugtype'), ('74', 'Can change bug type', '19', 'change_bugtype'), ('75', 'Can delete bug type', '19', 'delete_bugtype'), ('76', 'Can view bug type', '19', 'view_bugtype'), ('77', 'Can add group', '20', 'add_group'), ('78', 'Can change group', '20', 'change_group'), ('79', 'Can delete group', '20', 'delete_group'), ('80', 'Can view group', '20', 'view_group'), ('81', 'Can add keyword filter', '21', 'add_keywordfilter'), ('82', 'Can change keyword filter', '21', 'change_keywordfilter'), ('83', 'Can delete keyword filter', '21', 'delete_keywordfilter'), ('84', 'Can view keyword filter', '21', 'view_keywordfilter'), ('85', 'Can add logged log', '22', 'add_loggedlog'), ('86', 'Can change logged log', '22', 'change_loggedlog'), ('87', 'Can delete logged log', '22', 'delete_loggedlog'), ('88', 'Can view logged log', '22', 'view_loggedlog'), ('89', 'Can add module a', '23', 'add_modulea'), ('90', 'Can change module a', '23', 'change_modulea'), ('91', 'Can delete module a', '23', 'delete_modulea'), ('92', 'Can view module a', '23', 'view_modulea'), ('93', 'Can add module b', '24', 'add_moduleb'), ('94', 'Can change module b', '24', 'change_moduleb'), ('95', 'Can delete module b', '24', 'delete_moduleb'), ('96', 'Can view module b', '24', 'view_moduleb'), ('97', 'Can add pages', '25', 'add_pages'), ('98', 'Can change pages', '25', 'change_pages'), ('99', 'Can delete pages', '25', 'delete_pages'), ('100', 'Can view pages', '25', 'view_pages'), ('101', 'Can add pages permissions', '26', 'add_pagespermissions'), ('102', 'Can change pages permissions', '26', 'change_pagespermissions'), ('103', 'Can delete pages permissions', '26', 'delete_pagespermissions'), ('104', 'Can view pages permissions', '26', 'view_pagespermissions'), ('105', 'Can add product', '27', 'add_product'), ('106', 'Can change product', '27', 'change_product'), ('107', 'Can delete product', '27', 'delete_product'), ('108', 'Can view product', '27', 'view_product'), ('109', 'Can add product members', '28', 'add_productmembers'), ('110', 'Can change product members', '28', 'change_productmembers'), ('111', 'Can delete product members', '28', 'delete_productmembers'), ('112', 'Can view product members', '28', 'view_productmembers'), ('113', 'Can add release', '29', 'add_release'), ('114', 'Can change release', '29', 'change_release'), ('115', 'Can delete release', '29', 'delete_release'), ('116', 'Can view release', '29', 'view_release'), ('117', 'Can add system config', '30', 'add_systemconfig'), ('118', 'Can change system config', '30', 'change_systemconfig'), ('119', 'Can delete system config', '30', 'delete_systemconfig'), ('120', 'Can view system config', '30', 'view_systemconfig'), ('121', 'Can add team', '31', 'add_team'), ('122', 'Can change team', '31', 'change_team'), ('123', 'Can delete team', '31', 'delete_team'), ('124', 'Can view team', '31', 'view_team'), ('125', 'Can add test case', '32', 'add_testcase'), ('126', 'Can change test case', '32', 'change_testcase'), ('127', 'Can delete test case', '32', 'delete_testcase'), ('128', 'Can view test case', '32', 'view_testcase'), ('129', 'Can add test case files', '33', 'add_testcasefiles'), ('130', 'Can change test case files', '33', 'change_testcasefiles'), ('131', 'Can delete test case files', '33', 'delete_testcasefiles'), ('132', 'Can view test case files', '33', 'view_testcasefiles'), ('133', 'Can add test case review', '34', 'add_testcasereview'), ('134', 'Can change test case review', '34', 'change_testcasereview'), ('135', 'Can delete test case review', '34', 'delete_testcasereview'), ('136', 'Can view test case review', '34', 'view_testcasereview'), ('137', 'Can add test suite', '35', 'add_testsuite'), ('138', 'Can change test suite', '35', 'change_testsuite'), ('139', 'Can delete test suite', '35', 'delete_testsuite'), ('140', 'Can view test suite', '35', 'view_testsuite'), ('141', 'Can add test suite cell', '36', 'add_testsuitecell'), ('142', 'Can change test suite cell', '36', 'change_testsuitecell'), ('143', 'Can delete test suite cell', '36', 'delete_testsuitecell'), ('144', 'Can view test suite cell', '36', 'view_testsuitecell'), ('145', 'Can add user', '37', 'add_user'), ('146', 'Can change user', '37', 'change_user'), ('147', 'Can delete user', '37', 'delete_user'), ('148', 'Can view user', '37', 'view_user'), ('149', 'Can add user log', '38', 'add_userlog'), ('150', 'Can change user log', '38', 'change_userlog'), ('151', 'Can delete user log', '38', 'delete_userlog'), ('152', 'Can view user log', '38', 'view_userlog');
COMMIT;

-- ----------------------------
--  Table structure for `auth_user`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_general_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_general_ci NOT NULL,
  `first_name` varchar(30) COLLATE utf8mb4_general_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
--  Table structure for `django_admin_log`
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_general_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
--  Table structure for `django_content_type`
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
--  Records of `django_content_type`
-- ----------------------------
BEGIN;
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry'), ('8', 'app', 'api'), ('9', 'app', 'apipermissions'), ('10', 'app', 'authentication'), ('7', 'app', 'blacklistip'), ('11', 'app', 'bug'), ('12', 'app', 'bugannex'), ('13', 'app', 'bughistory'), ('14', 'app', 'bugpriority'), ('15', 'app', 'bugreport'), ('16', 'app', 'bugseverity'), ('17', 'app', 'bugsolution'), ('18', 'app', 'bugstatus'), ('19', 'app', 'bugtype'), ('20', 'app', 'group'), ('21', 'app', 'keywordfilter'), ('22', 'app', 'loggedlog'), ('23', 'app', 'modulea'), ('24', 'app', 'moduleb'), ('25', 'app', 'pages'), ('26', 'app', 'pagespermissions'), ('27', 'app', 'product'), ('28', 'app', 'productmembers'), ('29', 'app', 'release'), ('30', 'app', 'systemconfig'), ('31', 'app', 'team'), ('32', 'app', 'testcase'), ('33', 'app', 'testcasefiles'), ('34', 'app', 'testcasereview'), ('35', 'app', 'testsuite'), ('36', 'app', 'testsuitecell'), ('37', 'app', 'user'), ('38', 'app', 'userlog'), ('3', 'auth', 'group'), ('2', 'auth', 'permission'), ('4', 'auth', 'user'), ('5', 'contenttypes', 'contenttype'), ('6', 'sessions', 'session');
COMMIT;

-- ----------------------------
--  Table structure for `django_migrations`
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
--  Records of `django_migrations`
-- ----------------------------
BEGIN;
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2018-11-04 13:45:16.976031'), ('2', 'auth', '0001_initial', '2018-11-04 13:45:17.396176'), ('3', 'admin', '0001_initial', '2018-11-04 13:45:17.517001'), ('4', 'admin', '0002_logentry_remove_auto_add', '2018-11-04 13:45:17.531777'), ('5', 'admin', '0003_logentry_add_action_flag_choices', '2018-11-04 13:45:17.546899'), ('6', 'app', '0001_initial', '2018-11-04 13:45:25.057602'), ('7', 'contenttypes', '0002_remove_content_type_name', '2018-11-04 13:45:25.222822'), ('8', 'auth', '0002_alter_permission_name_max_length', '2018-11-04 13:45:25.283433'), ('9', 'auth', '0003_alter_user_email_max_length', '2018-11-04 13:45:25.331014'), ('10', 'auth', '0004_alter_user_username_opts', '2018-11-04 13:45:25.356259'), ('11', 'auth', '0005_alter_user_last_login_null', '2018-11-04 13:45:25.417337'), ('12', 'auth', '0006_require_contenttypes_0002', '2018-11-04 13:45:25.425416'), ('13', 'auth', '0007_alter_validators_add_error_messages', '2018-11-04 13:45:25.445822'), ('14', 'auth', '0008_alter_user_username_max_length', '2018-11-04 13:45:25.521509'), ('15', 'auth', '0009_alter_user_last_name_max_length', '2018-11-04 13:45:25.583676'), ('16', 'sessions', '0001_initial', '2018-11-04 13:45:25.623909');
COMMIT;

-- ----------------------------
--  Table structure for `django_session`
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_general_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
--  Table structure for `t_api`
-- ----------------------------
DROP TABLE IF EXISTS `t_api`;
CREATE TABLE `t_api` (
  `id` char(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `api_name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `api_code` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `url` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `flag` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `create_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `api_name` (`api_name`),
  UNIQUE KEY `api_code` (`api_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
--  Records of `t_api`
-- ----------------------------
BEGIN;
INSERT INTO `t_api` VALUES ('045210cf30a94f23951c7e68b9dcf5bb', '封禁用户', 'user_banned', '/api/user/banned', '用户管理', '2018-09-09 21:54:41.013389'), ('04bdf9e393e3418b9f941a8a6d493065', '重新打开缺陷', 'bug_reopen', '/api/qa/bug/reopen', '缺陷', '2018-09-09 21:46:22.508814'), ('0725da1a6ae74c1b90446584dd234e39', '缺陷属性信息（优先级、严重程度、类型）', 'bug_property', '/api/qa/bug/bug_property', '缺陷', '2018-09-09 21:41:51.484677'), ('0c8ec92ab1964d1dba198e65eb61f23e', '一级模块增加', 'module_1_add', '/api/pm/module/1/add', '模块管理', '2018-09-09 22:11:08.630362'), ('0e14a50d3984432fb7b99ff7227b5795', '上传图片附件', 'public_upload', '/api/support/upload', '公共部分', '2018-09-09 22:07:46.057965'), ('0f61062a5aca4e7299a4fde489b9d83e', '测试用例执行集列表', 'testsuite_list', '/api/qa/testsuite/list', '测试用例', '2018-09-09 22:26:04.354928'), ('15ed7c9856984c079c6ec1da800297b8', '产品人员列表', 'product_member_list', '/api/pm/member/list', '产品管理', '2018-09-09 22:15:43.763976'), ('19a01e70033c411dabf2f734e15fa49d', '测试执行集：测试用例列表', 'testsuite_cell_detailsed_list', '/api/qa/testsuite/cell/detailed_list', '测试用例', '2018-09-09 22:32:12.875040'), ('19f266cd29a14e0fa7d6c61ef5b41490', '删除缺陷', 'bug_delete', '/api/qa/bug/delete', '缺陷', '2018-09-09 21:42:21.084483'), ('27b600b5bdc34bc48a3c1bebd6ef830a', '测试用例附件删除', 'testcase_annex_delete', '/api/qa/testcase/annex_delete', '测试用例', '2018-10-22 07:35:13.028507'), ('2c8b2faf5934494cbed2692a71a57e96', '创建缺陷', 'bug_create', '/api/qa/bug/create', '缺陷', '2018-09-09 18:04:23.513690'), ('30e7db997a2f4a3d85ce54ae5dc21e06', '编辑缺陷', 'bug_edit', '/api/qa/bug/edit', '缺陷', '2018-09-09 21:39:12.997472'), ('316cd908ddab4ac280bf7c0c299b78e5', '产品人员重新加入', 'product_member_rejoin', '/api/pm/member/rejoin', '产品管理', '2018-09-09 22:16:47.586931'), ('32e4fbba7762472484d0a66bbe64808d', '缺陷趋势分析', 'bug_analyze_create', '/api/analyze/bug/date/create', '缺陷', '2018-09-09 22:20:53.529293'), ('3ce348164a0f4e5d9dd77eee89942042', '关闭缺陷', 'bug_close', '/api/qa/bug/close', '缺陷', '2018-09-09 21:45:51.769239'), ('49aad34abecb4939863812c2c3f5659c', '所有产品列表', 'product_all_list', '/api/pm/product/all_list', '产品管理', '2018-10-25 12:32:21.086476'), ('4d346aaedd75430aaa8be6390c6595f1', '二级模块列表', 'module_2_list', '/api/pm/module/2/list', '模块管理', '2018-09-09 22:11:42.795975'), ('54c452206228426096d41dff943ad90f', '产品人员移除', 'product_member_ban', '/api/pm/member/ban', '产品管理', '2018-09-09 22:16:28.030676'), ('565c01742ab34ed18d037e791a586099', '评审测试用例', 'testcase_review', '/api/qa/testcase/review', '测试用例', '2018-09-09 21:36:31.865626'), ('5d9189aa7973426ebe1417d8ddcc122f', '二级模块删除', 'module_2_del', '/api/pm/module/2/del', '模块管理', '2018-09-09 22:12:39.213172'), ('6067b35290e9426e96c146dcb149c0ae', '解决修复缺陷', 'bug_resolve', '/api/qa/bug/resolve', '缺陷', '2018-09-09 21:44:02.679900'), ('64e6b09e09374b079afdc0e1c44a5545', '修改密码', 'user_setpasswd', '/api/user/setpasswd', '用户管理', '2018-09-09 21:57:33.754000'), ('68043153e40143dd97a9acbbc3f94ac5', '缺陷解决方案列表', 'bug_solution', '/api/qa/bug/solution', '缺陷', '2018-09-09 21:40:49.325408'), ('6913ad4a9a1a401eaf2ef3ee26a4a465', 'dashboard', 'public_dashboard', '/api/dashboard/data_statistics', '公共部分', '2018-09-09 22:45:58.361916'), ('6cc1755a2ca1477c87a398d8dafaf1fc', '缺陷分析（优先级、严重程度、类型等）', 'bug_analyze_query', '/api/analyze/bug/query', '缺陷', '2018-09-09 22:19:39.090896'), ('6d27df660a414a3fb6d73156f0cb7d3d', '测试用例列表', 'testcase_list', '/api/qa/testcase/list', '测试用例', '2018-09-09 21:18:58.554355'), ('6ece36af9b1848bf810ee108f0b1c55c', '二级模块编辑', 'module_2_edit', '/api/pm/module/2/edit', '模块管理', '2018-09-09 22:12:19.798866'), ('708e501b81e0428ea0f0427c4e97964a', '测试用例详情', 'testcase_details', '/api/qa/testcase/details', '测试用例', '2018-09-09 21:34:08.351895'), ('71037db9d038487593da113a6b1f65be', '测试执行集：增加测试用例', 'testsuite_cell_add', '/api/qa/testsuite/cell/add', '测试用例', '2018-09-09 22:29:01.149785'), ('72ab70daaf7b4f7d8a9335554ed01094', '用户列表', 'user_list', '/api/user/user_list', '用户管理', '2018-09-09 21:54:07.966925'), ('782e404322e24caa9846b04207414bbb', '给用户重置密码', 'user_reset_passwd', '/api/user/reset_passwd', '用户管理', '2018-09-09 21:59:20.951504'), ('7999649a6f794f2ea8b1b64ba0f52cfc', '二级模块增加', 'module_2_add', '/api/pm/module/2/add', '模块管理', '2018-09-09 22:12:02.257355'), ('7c7293a59b154467b59fe87309fa72e2', '搜索测试用例', 'testcase_search', '/api/qa/testcase/search', '测试用例', '2018-09-09 21:35:41.048930'), ('820b5a9cde714cd18ba0c3f2cb9fed3c', '创建测试用例', 'testcase_create', '/api/qa/testcase/add', '测试用例', '2018-09-09 21:33:16.610486'), ('83ce6de7a3034c7da03c793051639243', '测试用例导出', 'testcase_export', '/api/qa/testcase/export', '测试用例', '2018-11-02 20:16:06.593155'), ('84ad0a19ace047cba13112107136183b', '缺陷历史记录', 'bug_history', '/api/qa/bug/history', '缺陷', '2018-10-26 11:43:00.544375'), ('863cf952242545f2bf5bcca5aa8a3515', '缺陷列表', 'bug_list', '/api/qa/bug/list', '缺陷', '2018-09-09 17:29:12.118311'), ('868db45b920a4bf28990bdf47cb28673', '产品列表', 'product_my_list', '/api/pm/product/my_list', '产品管理', '2018-09-09 22:03:00.733424'), ('8dd468711f41404fab71530951d2340c', '版本创建', 'version_create', '/api/pm/release/create', '版本管理', '2018-09-09 22:08:45.494056'), ('8f79ba2c30394f4fa6dc9f8b027724c3', '产品人员加入', 'product_member_join', '/api/pm/member/join', '产品管理', '2018-09-09 22:16:07.602744'), ('94374b45faf04df28755f039bd883d70', '挂起缺陷', 'bug_hangup', '/api/qa/bug/hangup', '缺陷', '2018-09-09 21:47:21.551919'), ('9569acd658b04880a23a21febd3c29ce', '测试用例运行', 'testsuite_run', '/api/qa/testsuite/cell/run', '测试用例', '2018-09-09 22:26:39.679360'), ('994e168db4c74c588503a1174da999bc', '生成缺陷报告', 'bug_report_generate', '/api/qa/bug/report/generate', '缺陷', '2018-09-09 21:48:28.784626'), ('9ab3b78b43a94ea9ad42c063a24e7f53', '创建产品', 'product_create', '/api/pm/product/create', '产品管理', '2018-09-09 22:00:45.104629'), ('9b3f96f30978401681edd38ea41d75bf', '给缺陷增加备注', 'bug_notes', '/api/qa/bug/add_notes', '缺陷', '2018-09-09 21:47:43.882246'), ('9c4e5773b642454180ede04e7bd6f793', '缺陷详情', 'bug_details', '/api/qa/bug/details', '缺陷', '2018-09-09 21:39:38.688695'), ('9f08d915207b41adbe626a00774a9a61', '产品版本列表', 'product_release', '/api/pm/product_release', '产品管理', '2018-09-09 22:04:33.630679'), ('a14c6fdd1fd74cb6b9db2a25c6475941', '按开发人员统计缺陷', 'bug_analyze_developer', '/api/analyze/bug/developer', '缺陷', '2018-09-09 22:21:47.301458'), ('a1dece243b0142ff81f75c5b5d3f89f3', '版本列表', 'version_list', '/api/pm/release/list', '版本管理', '2018-09-09 22:09:11.877218'), ('a7afbd5edb4845869687bc43aacb4a01', '创建测试用例执行集', 'testsuite_create', '/api/qa/testsuite/create', '测试用例', '2018-09-09 22:25:40.039569'), ('aa830da9b76d44d2a1305631704f254d', '删除缺陷附件', 'bug_annex_delete', '/api/qa/bug/annex/delete', '缺陷', '2018-09-09 21:49:28.677009'), ('b6ba4637ec5849618f78e7cc5c9d7a58', '删除测试用例', 'testcase_delete', '/api/qa/testcase/del', '测试用例', '2018-09-09 21:33:43.303670'), ('bcfb5ff72d8d403d858058f2444efca1', '搜索缺陷', 'bug_search', '/api/qa/bug/search', '缺陷', '2018-09-09 21:40:16.858626'), ('bdf1edf832fe42ec93917473f9208250', '统计今日测试用例工作量', 'testcase_analyze_my_today', '/api/analyze/testcase/my_today', '测试用例', '2018-09-09 22:22:42.221809'), ('c2f61fb98e2747ee8068536327731340', '按测试人员统计缺陷', 'bug_analyze_tester', '/api/analyze/bug/tester', '缺陷', '2018-09-09 22:21:24.632336'), ('c5ee2c3945284305aa199d57ff24a8c9', '缺陷版本列表（统计部分）', 'product_release_list', '/api/pm/new_product_release', '产品管理', '2018-10-25 13:03:00.470212'), ('c7f6188a109543bfa3d953e2a00dacca', '失效测试用例', 'testcase_fail', '/api/qa/testcase/fall', '测试用例', '2018-09-09 21:37:23.027153'), ('d43210b4c9234f9a88e7a78beb24f36f', '测试执行集：已选的测试用例列表', 'testsuite_cell_brief_list', '/api/qa/testsuite/cell/brief_list', '测试用例', '2018-09-09 22:34:02.758692'), ('d86f172da2d44497aaa0474b791c4f6d', '获取用户信息', 'user_userinfo', '/api/user/userinfo', '用户管理', '2018-09-09 21:56:35.787525'), ('e4e118f015b941e0ad039971d1d6658e', '创建用户', 'user_add', '/api/user/add', '用户管理', '2018-09-09 21:55:21.658182'), ('e64a095d843041f3bc17eb6fa992032f', '有效的测试用例列表', 'testcase_valid_list', '/api/qa/testcase/valid_list', '测试用例', '2018-09-09 22:34:40.804703'), ('e9e8f559390c46ff8f15ed870ee3594e', '模块列表树', 'module_all_list', '/api/pm/get_module', '模块管理', '2018-09-09 22:10:10.690063'), ('e9eb50e0646f4198aa4cbefbdd01403f', '缺陷报告详情', 'bug_report_details', '/api/qa/bug/report/details', '缺陷', '2018-09-09 21:48:52.653870'), ('ec23739ecfe742b89e0854cf487b5c54', '编辑测试用例', 'testcase_edit', '/api/qa/testcase/edit', '测试用例', '2018-09-09 21:34:40.653532'), ('ec4d17bae1584c2db469d38a0693ae09', '一级模块列表', 'module_1_list', '/api/pm/module/1/list', '模块管理', '2018-09-09 22:10:44.835845'), ('f4fdd5cc44d049ccbcb86da50ffeca51', '缺陷分析_我的今天', 'bug_analyze_my_today', '/api/analyze/bug/my_today', '缺陷', '2018-09-09 22:20:21.709562'), ('f702d500989048b4801d0a538bb73027', '获取用户组列表', 'user_group', '/api/user/group', '用户管理', '2018-09-09 21:56:04.568396'), ('f8f590873fbd4808b82d4e8186b6f4cf', '分配缺陷', 'bug_assign', '/api/qa/bug/assign', '缺陷', '2018-09-09 21:44:29.029846');
COMMIT;

-- ----------------------------
--  Table structure for `t_api_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `t_api_permissions`;
CREATE TABLE `t_api_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `is_allow` int(11) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `api_id` char(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `group` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `t_api_permissions_api_id_c5d7fa19_fk_t_api_id` (`api_id`),
  KEY `t_api_permissions_group_ee6c9fc7_fk_t_group_group` (`group`),
  CONSTRAINT `t_api_permissions_api_id_c5d7fa19_fk_t_api_id` FOREIGN KEY (`api_id`) REFERENCES `t_api` (`id`),
  CONSTRAINT `t_api_permissions_group_ee6c9fc7_fk_t_group_group` FOREIGN KEY (`group`) REFERENCES `t_group` (`group`)
) ENGINE=InnoDB AUTO_INCREMENT=336 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
--  Records of `t_api_permissions`
-- ----------------------------
BEGIN;
INSERT INTO `t_api_permissions` VALUES ('1', '1', '2018-09-10 06:48:00.000000', '6913ad4a9a1a401eaf2ef3ee26a4a465', 'test'), ('2', '1', '2018-09-10 06:48:00.000000', 'ec4d17bae1584c2db469d38a0693ae09', 'test'), ('3', '1', '2018-09-10 06:48:00.000000', '0c8ec92ab1964d1dba198e65eb61f23e', 'test'), ('4', '1', '2018-09-10 06:48:00.000000', '0e14a50d3984432fb7b99ff7227b5795', 'test'), ('5', '1', '2018-09-10 06:48:00.000000', '4d346aaedd75430aaa8be6390c6595f1', 'test'), ('6', '1', '2018-09-10 06:48:00.000000', '5d9189aa7973426ebe1417d8ddcc122f', 'test'), ('7', '1', '2018-09-10 06:48:00.000000', '7999649a6f794f2ea8b1b64ba0f52cfc', 'test'), ('8', '1', '2018-09-10 06:48:00.000000', '6ece36af9b1848bf810ee108f0b1c55c', 'test'), ('9', '1', '2018-09-10 06:48:00.000000', '15ed7c9856984c079c6ec1da800297b8', 'test'), ('10', '-1', '2018-09-10 06:48:00.000000', '8f79ba2c30394f4fa6dc9f8b027724c3', 'test'), ('11', '-1', '2018-09-10 06:48:00.000000', '54c452206228426096d41dff943ad90f', 'test'), ('12', '-1', '2018-09-10 06:48:00.000000', '316cd908ddab4ac280bf7c0c299b78e5', 'test'), ('13', '1', '2018-09-10 06:48:00.000000', '868db45b920a4bf28990bdf47cb28673', 'test'), ('14', '1', '2018-09-10 06:48:00.000000', '9f08d915207b41adbe626a00774a9a61', 'test'), ('15', '1', '2018-09-10 06:48:00.000000', '64e6b09e09374b079afdc0e1c44a5545', 'test'), ('16', '1', '2018-09-10 06:48:00.000000', '3ce348164a0f4e5d9dd77eee89942042', 'test'), ('17', '1', '2018-09-10 06:48:00.000000', 'f8f590873fbd4808b82d4e8186b6f4cf', 'test'), ('18', '-1', '2018-09-10 06:48:00.000000', '9ab3b78b43a94ea9ad42c063a24e7f53', 'test'), ('19', '1', '2018-09-10 06:48:00.000000', '820b5a9cde714cd18ba0c3f2cb9fed3c', 'test'), ('20', '1', '2018-09-10 06:48:00.000000', 'a7afbd5edb4845869687bc43aacb4a01', 'test'), ('21', '-1', '2018-09-10 06:48:00.000000', 'e4e118f015b941e0ad039971d1d6658e', 'test'), ('22', '1', '2018-09-10 06:48:00.000000', '2c8b2faf5934494cbed2692a71a57e96', 'test'), ('23', '1', '2018-09-10 06:48:00.000000', 'b6ba4637ec5849618f78e7cc5c9d7a58', 'test'), ('24', '1', '2018-09-10 06:48:00.000000', '19f266cd29a14e0fa7d6c61ef5b41490', 'test'), ('25', '1', '2018-09-10 06:48:00.000000', 'aa830da9b76d44d2a1305631704f254d', 'test'), ('26', '1', '2018-09-10 06:48:00.000000', 'c7f6188a109543bfa3d953e2a00dacca', 'test'), ('27', '-1', '2018-09-10 06:48:00.000000', '045210cf30a94f23951c7e68b9dcf5bb', 'test'), ('28', '1', '2018-09-10 06:48:00.000000', '94374b45faf04df28755f039bd883d70', 'test'), ('29', '1', '2018-09-10 06:48:00.000000', 'a14c6fdd1fd74cb6b9db2a25c6475941', 'test'), ('30', '1', '2018-09-10 06:48:00.000000', 'c2f61fb98e2747ee8068536327731340', 'test'), ('31', '1', '2018-09-10 06:48:00.000000', '7c7293a59b154467b59fe87309fa72e2', 'test'), ('32', '1', '2018-09-10 06:48:00.000000', 'bcfb5ff72d8d403d858058f2444efca1', 'test'), ('33', '1', '2018-09-10 06:48:00.000000', 'e64a095d843041f3bc17eb6fa992032f', 'test'), ('34', '1', '2018-09-10 06:48:00.000000', 'e9e8f559390c46ff8f15ed870ee3594e', 'test'), ('35', '1', '2018-09-10 06:48:00.000000', '71037db9d038487593da113a6b1f65be', 'test'), ('36', '1', '2018-09-10 06:48:00.000000', 'd43210b4c9234f9a88e7a78beb24f36f', 'test'), ('37', '1', '2018-09-10 06:48:00.000000', '19a01e70033c411dabf2f734e15fa49d', 'test'), ('38', '1', '2018-09-10 06:48:00.000000', '6d27df660a414a3fb6d73156f0cb7d3d', 'test'), ('39', '1', '2018-09-10 06:48:00.000000', '0f61062a5aca4e7299a4fde489b9d83e', 'test'), ('40', '1', '2018-09-10 06:48:00.000000', '708e501b81e0428ea0f0427c4e97964a', 'test'), ('41', '1', '2018-09-10 06:48:00.000000', '9569acd658b04880a23a21febd3c29ce', 'test'), ('42', '1', '2018-09-10 06:48:00.000000', 'a1dece243b0142ff81f75c5b5d3f89f3', 'test'), ('43', '-1', '2018-09-10 06:48:00.000000', '8dd468711f41404fab71530951d2340c', 'test'), ('44', '1', '2018-09-10 06:48:00.000000', '994e168db4c74c588503a1174da999bc', 'test'), ('45', '1', '2018-09-10 06:48:00.000000', '72ab70daaf7b4f7d8a9335554ed01094', 'test'), ('46', '-1', '2018-09-10 06:48:00.000000', '782e404322e24caa9846b04207414bbb', 'test'), ('47', '1', '2018-09-10 06:48:00.000000', '9b3f96f30978401681edd38ea41d75bf', 'test'), ('48', '1', '2018-09-10 06:48:00.000000', 'bdf1edf832fe42ec93917473f9208250', 'test'), ('49', '1', '2018-09-10 06:48:00.000000', 'ec23739ecfe742b89e0854cf487b5c54', 'test'), ('50', '1', '2018-09-10 06:48:00.000000', '30e7db997a2f4a3d85ce54ae5dc21e06', 'test'), ('51', '1', '2018-09-10 06:48:00.000000', 'f4fdd5cc44d049ccbcb86da50ffeca51', 'test'), ('52', '1', '2018-09-10 06:48:00.000000', '6cc1755a2ca1477c87a398d8dafaf1fc', 'test'), ('53', '1', '2018-09-10 06:48:00.000000', '863cf952242545f2bf5bcca5aa8a3515', 'test'), ('54', '1', '2018-09-10 06:48:00.000000', '0725da1a6ae74c1b90446584dd234e39', 'test'), ('55', '1', '2018-09-10 06:48:00.000000', 'e9eb50e0646f4198aa4cbefbdd01403f', 'test'), ('56', '1', '2018-09-10 06:48:00.000000', '68043153e40143dd97a9acbbc3f94ac5', 'test'), ('57', '1', '2018-09-10 06:48:00.000000', '9c4e5773b642454180ede04e7bd6f793', 'test'), ('58', '1', '2018-09-10 06:48:00.000000', '32e4fbba7762472484d0a66bbe64808d', 'test'), ('59', '1', '2018-09-10 06:48:00.000000', 'd86f172da2d44497aaa0474b791c4f6d', 'test'), ('60', '1', '2018-09-10 06:48:00.000000', 'f702d500989048b4801d0a538bb73027', 'test'), ('61', '1', '2018-09-10 06:48:00.000000', '6067b35290e9426e96c146dcb149c0ae', 'test'), ('62', '1', '2018-09-10 06:48:00.000000', '565c01742ab34ed18d037e791a586099', 'test'), ('63', '1', '2018-09-10 06:48:00.000000', '04bdf9e393e3418b9f941a8a6d493065', 'test'), ('64', '1', '2018-09-10 06:48:00.000000', '6913ad4a9a1a401eaf2ef3ee26a4a465', 'developer'), ('65', '1', '2018-09-10 06:48:00.000000', 'ec4d17bae1584c2db469d38a0693ae09', 'developer'), ('66', '1', '2018-09-10 06:48:00.000000', '0c8ec92ab1964d1dba198e65eb61f23e', 'developer'), ('67', '1', '2018-09-10 06:48:00.000000', '0e14a50d3984432fb7b99ff7227b5795', 'developer'), ('68', '1', '2018-09-10 06:48:00.000000', '4d346aaedd75430aaa8be6390c6595f1', 'developer'), ('69', '1', '2018-09-10 06:48:00.000000', '5d9189aa7973426ebe1417d8ddcc122f', 'developer'), ('70', '1', '2018-09-10 06:48:00.000000', '7999649a6f794f2ea8b1b64ba0f52cfc', 'developer'), ('71', '1', '2018-09-10 06:48:00.000000', '6ece36af9b1848bf810ee108f0b1c55c', 'developer'), ('72', '1', '2018-09-10 06:48:00.000000', '15ed7c9856984c079c6ec1da800297b8', 'developer'), ('73', '-1', '2018-09-10 06:48:00.000000', '8f79ba2c30394f4fa6dc9f8b027724c3', 'developer'), ('74', '-1', '2018-09-10 06:48:00.000000', '54c452206228426096d41dff943ad90f', 'developer'), ('75', '-1', '2018-09-10 06:48:00.000000', '316cd908ddab4ac280bf7c0c299b78e5', 'developer'), ('76', '1', '2018-09-10 06:48:00.000000', '868db45b920a4bf28990bdf47cb28673', 'developer'), ('77', '1', '2018-09-10 06:48:00.000000', '9f08d915207b41adbe626a00774a9a61', 'developer'), ('78', '1', '2018-09-10 06:48:00.000000', '64e6b09e09374b079afdc0e1c44a5545', 'developer'), ('79', '-1', '2018-09-10 06:48:00.000000', '3ce348164a0f4e5d9dd77eee89942042', 'developer'), ('80', '1', '2018-09-10 06:48:00.000000', 'f8f590873fbd4808b82d4e8186b6f4cf', 'developer'), ('81', '-1', '2018-09-10 06:48:00.000000', '9ab3b78b43a94ea9ad42c063a24e7f53', 'developer'), ('82', '1', '2018-09-10 06:48:00.000000', '820b5a9cde714cd18ba0c3f2cb9fed3c', 'developer'), ('83', '1', '2018-09-10 06:48:00.000000', 'a7afbd5edb4845869687bc43aacb4a01', 'developer'), ('84', '-1', '2018-09-10 06:48:00.000000', 'e4e118f015b941e0ad039971d1d6658e', 'developer'), ('85', '1', '2018-09-10 06:48:00.000000', '2c8b2faf5934494cbed2692a71a57e96', 'developer'), ('86', '1', '2018-09-10 06:48:00.000000', 'b6ba4637ec5849618f78e7cc5c9d7a58', 'developer'), ('87', '-1', '2018-09-10 06:48:00.000000', '19f266cd29a14e0fa7d6c61ef5b41490', 'developer'), ('88', '1', '2018-09-10 06:48:00.000000', 'aa830da9b76d44d2a1305631704f254d', 'developer'), ('89', '1', '2018-09-10 06:48:00.000000', 'c7f6188a109543bfa3d953e2a00dacca', 'developer'), ('90', '-1', '2018-09-10 06:48:00.000000', '045210cf30a94f23951c7e68b9dcf5bb', 'developer'), ('91', '1', '2018-09-10 06:48:00.000000', '94374b45faf04df28755f039bd883d70', 'developer'), ('92', '1', '2018-09-10 06:48:00.000000', 'a14c6fdd1fd74cb6b9db2a25c6475941', 'developer'), ('93', '1', '2018-09-10 06:48:00.000000', 'c2f61fb98e2747ee8068536327731340', 'developer'), ('94', '1', '2018-09-10 06:48:00.000000', '7c7293a59b154467b59fe87309fa72e2', 'developer'), ('95', '1', '2018-09-10 06:48:00.000000', 'bcfb5ff72d8d403d858058f2444efca1', 'developer'), ('96', '1', '2018-09-10 06:48:00.000000', 'e64a095d843041f3bc17eb6fa992032f', 'developer'), ('97', '1', '2018-09-10 06:48:00.000000', 'e9e8f559390c46ff8f15ed870ee3594e', 'developer'), ('98', '1', '2018-09-10 06:48:00.000000', '71037db9d038487593da113a6b1f65be', 'developer'), ('99', '1', '2018-09-10 06:48:00.000000', 'd43210b4c9234f9a88e7a78beb24f36f', 'developer'), ('100', '1', '2018-09-10 06:48:00.000000', '19a01e70033c411dabf2f734e15fa49d', 'developer'), ('101', '1', '2018-09-10 06:48:00.000000', '6d27df660a414a3fb6d73156f0cb7d3d', 'developer'), ('102', '1', '2018-09-10 06:48:00.000000', '0f61062a5aca4e7299a4fde489b9d83e', 'developer'), ('103', '1', '2018-09-10 06:48:00.000000', '708e501b81e0428ea0f0427c4e97964a', 'developer'), ('104', '1', '2018-09-10 06:48:00.000000', '9569acd658b04880a23a21febd3c29ce', 'developer'), ('105', '1', '2018-09-10 06:48:00.000000', 'a1dece243b0142ff81f75c5b5d3f89f3', 'developer'), ('106', '-1', '2018-09-10 06:48:00.000000', '8dd468711f41404fab71530951d2340c', 'developer'), ('107', '1', '2018-09-10 06:48:00.000000', '994e168db4c74c588503a1174da999bc', 'developer'), ('108', '1', '2018-09-10 06:48:00.000000', '72ab70daaf7b4f7d8a9335554ed01094', 'developer'), ('109', '-1', '2018-09-10 06:48:00.000000', '782e404322e24caa9846b04207414bbb', 'developer'), ('110', '1', '2018-09-10 06:48:00.000000', '9b3f96f30978401681edd38ea41d75bf', 'developer'), ('111', '1', '2018-09-10 06:48:00.000000', 'bdf1edf832fe42ec93917473f9208250', 'developer'), ('112', '1', '2018-09-10 06:48:00.000000', 'ec23739ecfe742b89e0854cf487b5c54', 'developer'), ('113', '1', '2018-09-10 06:48:00.000000', '30e7db997a2f4a3d85ce54ae5dc21e06', 'developer'), ('114', '1', '2018-09-10 06:48:00.000000', 'f4fdd5cc44d049ccbcb86da50ffeca51', 'developer'), ('115', '1', '2018-09-10 06:48:00.000000', '6cc1755a2ca1477c87a398d8dafaf1fc', 'developer'), ('116', '1', '2018-09-10 06:48:00.000000', '863cf952242545f2bf5bcca5aa8a3515', 'developer'), ('117', '1', '2018-09-10 06:48:00.000000', '0725da1a6ae74c1b90446584dd234e39', 'developer'), ('118', '1', '2018-09-10 06:48:00.000000', 'e9eb50e0646f4198aa4cbefbdd01403f', 'developer'), ('119', '1', '2018-09-10 06:48:00.000000', '68043153e40143dd97a9acbbc3f94ac5', 'developer'), ('120', '1', '2018-09-10 06:48:00.000000', '9c4e5773b642454180ede04e7bd6f793', 'developer'), ('121', '1', '2018-09-10 06:48:00.000000', '32e4fbba7762472484d0a66bbe64808d', 'developer'), ('122', '1', '2018-09-10 06:48:00.000000', 'd86f172da2d44497aaa0474b791c4f6d', 'developer'), ('123', '1', '2018-09-10 06:48:00.000000', 'f702d500989048b4801d0a538bb73027', 'developer'), ('124', '1', '2018-09-10 06:48:00.000000', '6067b35290e9426e96c146dcb149c0ae', 'developer'), ('125', '1', '2018-09-10 06:48:00.000000', '565c01742ab34ed18d037e791a586099', 'developer'), ('126', '1', '2018-09-10 06:48:00.000000', '04bdf9e393e3418b9f941a8a6d493065', 'developer'), ('127', '1', '2018-09-10 06:48:00.000000', '6913ad4a9a1a401eaf2ef3ee26a4a465', 'design'), ('128', '1', '2018-09-10 06:48:00.000000', 'ec4d17bae1584c2db469d38a0693ae09', 'design'), ('129', '1', '2018-09-10 06:48:00.000000', '0c8ec92ab1964d1dba198e65eb61f23e', 'design'), ('130', '1', '2018-09-10 06:48:00.000000', '0e14a50d3984432fb7b99ff7227b5795', 'design'), ('131', '1', '2018-09-10 06:48:00.000000', '4d346aaedd75430aaa8be6390c6595f1', 'design'), ('132', '1', '2018-09-10 06:48:00.000000', '5d9189aa7973426ebe1417d8ddcc122f', 'design'), ('133', '1', '2018-09-10 06:48:00.000000', '7999649a6f794f2ea8b1b64ba0f52cfc', 'design'), ('134', '1', '2018-09-10 06:48:00.000000', '6ece36af9b1848bf810ee108f0b1c55c', 'design'), ('135', '1', '2018-09-10 06:48:00.000000', '15ed7c9856984c079c6ec1da800297b8', 'design'), ('136', '-1', '2018-09-10 06:48:00.000000', '8f79ba2c30394f4fa6dc9f8b027724c3', 'design'), ('137', '-1', '2018-09-10 06:48:00.000000', '54c452206228426096d41dff943ad90f', 'design'), ('138', '-1', '2018-09-10 06:48:00.000000', '316cd908ddab4ac280bf7c0c299b78e5', 'design'), ('139', '1', '2018-09-10 06:48:00.000000', '868db45b920a4bf28990bdf47cb28673', 'design'), ('140', '1', '2018-09-10 06:48:00.000000', '9f08d915207b41adbe626a00774a9a61', 'design'), ('141', '1', '2018-09-10 06:48:00.000000', '64e6b09e09374b079afdc0e1c44a5545', 'design'), ('142', '-1', '2018-09-10 06:48:00.000000', '3ce348164a0f4e5d9dd77eee89942042', 'design'), ('143', '1', '2018-09-10 06:48:00.000000', 'f8f590873fbd4808b82d4e8186b6f4cf', 'design'), ('144', '-1', '2018-09-10 06:48:00.000000', '9ab3b78b43a94ea9ad42c063a24e7f53', 'design'), ('145', '1', '2018-09-10 06:48:00.000000', '820b5a9cde714cd18ba0c3f2cb9fed3c', 'design'), ('146', '1', '2018-09-10 06:48:00.000000', 'a7afbd5edb4845869687bc43aacb4a01', 'design'), ('147', '-1', '2018-09-10 06:48:00.000000', 'e4e118f015b941e0ad039971d1d6658e', 'design'), ('148', '1', '2018-09-10 06:48:00.000000', '2c8b2faf5934494cbed2692a71a57e96', 'design'), ('149', '1', '2018-09-10 06:48:00.000000', 'b6ba4637ec5849618f78e7cc5c9d7a58', 'design'), ('150', '-1', '2018-09-10 06:48:00.000000', '19f266cd29a14e0fa7d6c61ef5b41490', 'design'), ('151', '1', '2018-09-10 06:48:00.000000', 'aa830da9b76d44d2a1305631704f254d', 'design'), ('152', '1', '2018-09-10 06:48:00.000000', 'c7f6188a109543bfa3d953e2a00dacca', 'design'), ('153', '-1', '2018-09-10 06:48:00.000000', '045210cf30a94f23951c7e68b9dcf5bb', 'design'), ('154', '1', '2018-09-10 06:48:00.000000', '94374b45faf04df28755f039bd883d70', 'design'), ('155', '1', '2018-09-10 06:48:00.000000', 'a14c6fdd1fd74cb6b9db2a25c6475941', 'design'), ('156', '1', '2018-09-10 06:48:00.000000', 'c2f61fb98e2747ee8068536327731340', 'design'), ('157', '1', '2018-09-10 06:48:00.000000', '7c7293a59b154467b59fe87309fa72e2', 'design'), ('158', '1', '2018-09-10 06:48:00.000000', 'bcfb5ff72d8d403d858058f2444efca1', 'design'), ('159', '1', '2018-09-10 06:48:00.000000', 'e64a095d843041f3bc17eb6fa992032f', 'design'), ('160', '1', '2018-09-10 06:48:00.000000', 'e9e8f559390c46ff8f15ed870ee3594e', 'design'), ('161', '1', '2018-09-10 06:48:00.000000', '71037db9d038487593da113a6b1f65be', 'design'), ('162', '1', '2018-09-10 06:48:00.000000', 'd43210b4c9234f9a88e7a78beb24f36f', 'design'), ('163', '1', '2018-09-10 06:48:00.000000', '19a01e70033c411dabf2f734e15fa49d', 'design'), ('164', '1', '2018-09-10 06:48:00.000000', '6d27df660a414a3fb6d73156f0cb7d3d', 'design'), ('165', '1', '2018-09-10 06:48:00.000000', '0f61062a5aca4e7299a4fde489b9d83e', 'design'), ('166', '1', '2018-09-10 06:48:00.000000', '708e501b81e0428ea0f0427c4e97964a', 'design'), ('167', '1', '2018-09-10 06:48:00.000000', '9569acd658b04880a23a21febd3c29ce', 'design'), ('168', '1', '2018-09-10 06:48:00.000000', 'a1dece243b0142ff81f75c5b5d3f89f3', 'design'), ('169', '-1', '2018-09-10 06:48:00.000000', '8dd468711f41404fab71530951d2340c', 'design'), ('170', '1', '2018-09-10 06:48:00.000000', '994e168db4c74c588503a1174da999bc', 'design'), ('171', '1', '2018-09-10 06:48:00.000000', '72ab70daaf7b4f7d8a9335554ed01094', 'design'), ('172', '-1', '2018-09-10 06:48:00.000000', '782e404322e24caa9846b04207414bbb', 'design'), ('173', '1', '2018-09-10 06:48:00.000000', '9b3f96f30978401681edd38ea41d75bf', 'design'), ('174', '1', '2018-09-10 06:48:00.000000', 'bdf1edf832fe42ec93917473f9208250', 'design'), ('175', '1', '2018-09-10 06:48:00.000000', 'ec23739ecfe742b89e0854cf487b5c54', 'design'), ('176', '-1', '2018-09-10 06:48:00.000000', '30e7db997a2f4a3d85ce54ae5dc21e06', 'design'), ('177', '1', '2018-09-10 06:48:00.000000', 'f4fdd5cc44d049ccbcb86da50ffeca51', 'design'), ('178', '1', '2018-09-10 06:48:00.000000', '6cc1755a2ca1477c87a398d8dafaf1fc', 'design'), ('179', '1', '2018-09-10 06:48:00.000000', '863cf952242545f2bf5bcca5aa8a3515', 'design'), ('180', '1', '2018-09-10 06:48:00.000000', '0725da1a6ae74c1b90446584dd234e39', 'design'), ('181', '1', '2018-09-10 06:48:00.000000', 'e9eb50e0646f4198aa4cbefbdd01403f', 'design'), ('182', '1', '2018-09-10 06:48:00.000000', '68043153e40143dd97a9acbbc3f94ac5', 'design'), ('183', '1', '2018-09-10 06:48:00.000000', '9c4e5773b642454180ede04e7bd6f793', 'design'), ('184', '1', '2018-09-10 06:48:00.000000', '32e4fbba7762472484d0a66bbe64808d', 'design'), ('185', '1', '2018-09-10 06:48:00.000000', 'd86f172da2d44497aaa0474b791c4f6d', 'design'), ('186', '1', '2018-09-10 06:48:00.000000', 'f702d500989048b4801d0a538bb73027', 'design'), ('187', '1', '2018-09-10 06:48:00.000000', '6067b35290e9426e96c146dcb149c0ae', 'design'), ('188', '1', '2018-09-10 06:48:00.000000', '565c01742ab34ed18d037e791a586099', 'design'), ('189', '-1', '2018-09-10 06:48:00.000000', '04bdf9e393e3418b9f941a8a6d493065', 'design'), ('190', '1', '2018-09-10 06:48:00.000000', '6913ad4a9a1a401eaf2ef3ee26a4a465', 'pm'), ('191', '1', '2018-09-10 06:48:00.000000', 'ec4d17bae1584c2db469d38a0693ae09', 'pm'), ('192', '1', '2018-09-10 06:48:00.000000', '0c8ec92ab1964d1dba198e65eb61f23e', 'pm'), ('193', '1', '2018-09-10 06:48:00.000000', '0e14a50d3984432fb7b99ff7227b5795', 'pm'), ('194', '1', '2018-09-10 06:48:00.000000', '4d346aaedd75430aaa8be6390c6595f1', 'pm'), ('195', '1', '2018-09-10 06:48:00.000000', '5d9189aa7973426ebe1417d8ddcc122f', 'pm'), ('196', '1', '2018-09-10 06:48:00.000000', '7999649a6f794f2ea8b1b64ba0f52cfc', 'pm'), ('197', '1', '2018-09-10 06:48:00.000000', '6ece36af9b1848bf810ee108f0b1c55c', 'pm'), ('198', '1', '2018-09-10 06:48:00.000000', '15ed7c9856984c079c6ec1da800297b8', 'pm'), ('199', '-1', '2018-09-10 06:48:00.000000', '8f79ba2c30394f4fa6dc9f8b027724c3', 'pm'), ('200', '-1', '2018-09-10 06:48:00.000000', '54c452206228426096d41dff943ad90f', 'pm'), ('201', '-1', '2018-09-10 06:48:00.000000', '316cd908ddab4ac280bf7c0c299b78e5', 'pm'), ('202', '1', '2018-09-10 06:48:00.000000', '868db45b920a4bf28990bdf47cb28673', 'pm'), ('203', '1', '2018-09-10 06:48:00.000000', '9f08d915207b41adbe626a00774a9a61', 'pm'), ('204', '1', '2018-09-10 06:48:00.000000', '64e6b09e09374b079afdc0e1c44a5545', 'pm'), ('205', '-1', '2018-09-10 06:48:00.000000', '3ce348164a0f4e5d9dd77eee89942042', 'pm'), ('206', '1', '2018-09-10 06:48:00.000000', 'f8f590873fbd4808b82d4e8186b6f4cf', 'pm'), ('207', '-1', '2018-09-10 06:48:00.000000', '9ab3b78b43a94ea9ad42c063a24e7f53', 'pm'), ('208', '1', '2018-09-10 06:48:00.000000', '820b5a9cde714cd18ba0c3f2cb9fed3c', 'pm'), ('209', '1', '2018-09-10 06:48:00.000000', 'a7afbd5edb4845869687bc43aacb4a01', 'pm'), ('210', '-1', '2018-09-10 06:48:00.000000', 'e4e118f015b941e0ad039971d1d6658e', 'pm'), ('211', '1', '2018-09-10 06:48:00.000000', '2c8b2faf5934494cbed2692a71a57e96', 'pm'), ('212', '1', '2018-09-10 06:48:00.000000', 'b6ba4637ec5849618f78e7cc5c9d7a58', 'pm'), ('213', '-1', '2018-09-10 06:48:00.000000', '19f266cd29a14e0fa7d6c61ef5b41490', 'pm'), ('214', '1', '2018-09-10 06:48:00.000000', 'aa830da9b76d44d2a1305631704f254d', 'pm'), ('215', '1', '2018-09-10 06:48:00.000000', 'c7f6188a109543bfa3d953e2a00dacca', 'pm'), ('216', '-1', '2018-09-10 06:48:00.000000', '045210cf30a94f23951c7e68b9dcf5bb', 'pm'), ('217', '1', '2018-09-10 06:48:00.000000', '94374b45faf04df28755f039bd883d70', 'pm'), ('218', '1', '2018-09-10 06:48:00.000000', 'a14c6fdd1fd74cb6b9db2a25c6475941', 'pm'), ('219', '1', '2018-09-10 06:48:00.000000', 'c2f61fb98e2747ee8068536327731340', 'pm'), ('220', '1', '2018-09-10 06:48:00.000000', '7c7293a59b154467b59fe87309fa72e2', 'pm'), ('221', '1', '2018-09-10 06:48:00.000000', 'bcfb5ff72d8d403d858058f2444efca1', 'pm'), ('222', '1', '2018-09-10 06:48:00.000000', 'e64a095d843041f3bc17eb6fa992032f', 'pm'), ('223', '1', '2018-09-10 06:48:00.000000', 'e9e8f559390c46ff8f15ed870ee3594e', 'pm'), ('224', '1', '2018-09-10 06:48:00.000000', '71037db9d038487593da113a6b1f65be', 'pm'), ('225', '1', '2018-09-10 06:48:00.000000', 'd43210b4c9234f9a88e7a78beb24f36f', 'pm'), ('226', '1', '2018-09-10 06:48:00.000000', '19a01e70033c411dabf2f734e15fa49d', 'pm'), ('227', '1', '2018-09-10 06:48:00.000000', '6d27df660a414a3fb6d73156f0cb7d3d', 'pm'), ('228', '1', '2018-09-10 06:48:00.000000', '0f61062a5aca4e7299a4fde489b9d83e', 'pm'), ('229', '1', '2018-09-10 06:48:00.000000', '708e501b81e0428ea0f0427c4e97964a', 'pm'), ('230', '1', '2018-09-10 06:48:00.000000', '9569acd658b04880a23a21febd3c29ce', 'pm'), ('231', '1', '2018-09-10 06:48:00.000000', 'a1dece243b0142ff81f75c5b5d3f89f3', 'pm'), ('232', '-1', '2018-09-10 06:48:00.000000', '8dd468711f41404fab71530951d2340c', 'pm'), ('233', '1', '2018-09-10 06:48:00.000000', '994e168db4c74c588503a1174da999bc', 'pm'), ('234', '1', '2018-09-10 06:48:00.000000', '72ab70daaf7b4f7d8a9335554ed01094', 'pm'), ('235', '-1', '2018-09-10 06:48:00.000000', '782e404322e24caa9846b04207414bbb', 'pm'), ('236', '1', '2018-09-10 06:48:00.000000', '9b3f96f30978401681edd38ea41d75bf', 'pm'), ('237', '1', '2018-09-10 06:48:00.000000', 'bdf1edf832fe42ec93917473f9208250', 'pm'), ('238', '1', '2018-09-10 06:48:00.000000', 'ec23739ecfe742b89e0854cf487b5c54', 'pm'), ('239', '-1', '2018-09-10 06:48:00.000000', '30e7db997a2f4a3d85ce54ae5dc21e06', 'pm'), ('240', '1', '2018-09-10 06:48:00.000000', 'f4fdd5cc44d049ccbcb86da50ffeca51', 'pm'), ('241', '1', '2018-09-10 06:48:00.000000', '6cc1755a2ca1477c87a398d8dafaf1fc', 'pm'), ('242', '1', '2018-09-10 06:48:00.000000', '863cf952242545f2bf5bcca5aa8a3515', 'pm'), ('243', '1', '2018-09-10 06:48:00.000000', '0725da1a6ae74c1b90446584dd234e39', 'pm'), ('244', '1', '2018-09-10 06:48:00.000000', 'e9eb50e0646f4198aa4cbefbdd01403f', 'pm'), ('245', '1', '2018-09-10 06:48:00.000000', '68043153e40143dd97a9acbbc3f94ac5', 'pm'), ('246', '1', '2018-09-10 06:48:00.000000', '9c4e5773b642454180ede04e7bd6f793', 'pm'), ('247', '1', '2018-09-10 06:48:00.000000', '32e4fbba7762472484d0a66bbe64808d', 'pm'), ('248', '1', '2018-09-10 06:48:00.000000', 'd86f172da2d44497aaa0474b791c4f6d', 'pm'), ('249', '1', '2018-09-10 06:48:00.000000', 'f702d500989048b4801d0a538bb73027', 'pm'), ('250', '1', '2018-09-10 06:48:00.000000', '6067b35290e9426e96c146dcb149c0ae', 'pm'), ('251', '1', '2018-09-10 06:48:00.000000', '565c01742ab34ed18d037e791a586099', 'pm'), ('252', '-1', '2018-09-10 06:48:00.000000', '04bdf9e393e3418b9f941a8a6d493065', 'pm'), ('253', '1', '2018-09-10 06:48:00.000000', '6913ad4a9a1a401eaf2ef3ee26a4a465', 'manager'), ('254', '1', '2018-09-10 06:48:00.000000', 'ec4d17bae1584c2db469d38a0693ae09', 'manager'), ('255', '1', '2018-09-10 06:48:00.000000', '0c8ec92ab1964d1dba198e65eb61f23e', 'manager'), ('256', '1', '2018-09-10 06:48:00.000000', '0e14a50d3984432fb7b99ff7227b5795', 'manager'), ('257', '1', '2018-09-10 06:48:00.000000', '4d346aaedd75430aaa8be6390c6595f1', 'manager'), ('258', '1', '2018-09-10 06:48:00.000000', '5d9189aa7973426ebe1417d8ddcc122f', 'manager'), ('259', '1', '2018-09-10 06:48:00.000000', '7999649a6f794f2ea8b1b64ba0f52cfc', 'manager'), ('260', '1', '2018-09-10 06:48:00.000000', '6ece36af9b1848bf810ee108f0b1c55c', 'manager'), ('261', '1', '2018-09-10 06:48:00.000000', '15ed7c9856984c079c6ec1da800297b8', 'manager'), ('262', '1', '2018-09-10 06:48:00.000000', '8f79ba2c30394f4fa6dc9f8b027724c3', 'manager'), ('263', '1', '2018-09-10 06:48:00.000000', '54c452206228426096d41dff943ad90f', 'manager'), ('264', '1', '2018-09-10 06:48:00.000000', '316cd908ddab4ac280bf7c0c299b78e5', 'manager'), ('265', '1', '2018-09-10 06:48:00.000000', '868db45b920a4bf28990bdf47cb28673', 'manager'), ('266', '1', '2018-09-10 06:48:00.000000', '9f08d915207b41adbe626a00774a9a61', 'manager'), ('267', '1', '2018-09-10 06:48:00.000000', '64e6b09e09374b079afdc0e1c44a5545', 'manager'), ('268', '1', '2018-09-10 06:48:00.000000', '3ce348164a0f4e5d9dd77eee89942042', 'manager'), ('269', '1', '2018-09-10 06:48:00.000000', 'f8f590873fbd4808b82d4e8186b6f4cf', 'manager'), ('270', '1', '2018-09-10 06:48:00.000000', '9ab3b78b43a94ea9ad42c063a24e7f53', 'manager'), ('271', '1', '2018-09-10 06:48:00.000000', '820b5a9cde714cd18ba0c3f2cb9fed3c', 'manager'), ('272', '1', '2018-09-10 06:48:00.000000', 'a7afbd5edb4845869687bc43aacb4a01', 'manager'), ('273', '1', '2018-09-10 06:48:00.000000', 'e4e118f015b941e0ad039971d1d6658e', 'manager'), ('274', '1', '2018-09-10 06:48:00.000000', '2c8b2faf5934494cbed2692a71a57e96', 'manager'), ('275', '1', '2018-09-10 06:48:00.000000', 'b6ba4637ec5849618f78e7cc5c9d7a58', 'manager'), ('276', '1', '2018-09-10 06:48:00.000000', '19f266cd29a14e0fa7d6c61ef5b41490', 'manager'), ('277', '1', '2018-09-10 06:48:00.000000', 'aa830da9b76d44d2a1305631704f254d', 'manager'), ('278', '1', '2018-09-10 06:48:00.000000', 'c7f6188a109543bfa3d953e2a00dacca', 'manager'), ('279', '1', '2018-09-10 06:48:00.000000', '045210cf30a94f23951c7e68b9dcf5bb', 'manager'), ('280', '1', '2018-09-10 06:48:00.000000', '94374b45faf04df28755f039bd883d70', 'manager'), ('281', '1', '2018-09-10 06:48:00.000000', 'a14c6fdd1fd74cb6b9db2a25c6475941', 'manager'), ('282', '1', '2018-09-10 06:48:00.000000', 'c2f61fb98e2747ee8068536327731340', 'manager'), ('283', '1', '2018-09-10 06:48:00.000000', '7c7293a59b154467b59fe87309fa72e2', 'manager'), ('284', '1', '2018-09-10 06:48:00.000000', 'bcfb5ff72d8d403d858058f2444efca1', 'manager'), ('285', '1', '2018-09-10 06:48:00.000000', 'e64a095d843041f3bc17eb6fa992032f', 'manager'), ('286', '1', '2018-09-10 06:48:00.000000', 'e9e8f559390c46ff8f15ed870ee3594e', 'manager'), ('287', '1', '2018-09-10 06:48:00.000000', '71037db9d038487593da113a6b1f65be', 'manager'), ('288', '1', '2018-09-10 06:48:00.000000', 'd43210b4c9234f9a88e7a78beb24f36f', 'manager'), ('289', '1', '2018-09-10 06:48:00.000000', '19a01e70033c411dabf2f734e15fa49d', 'manager'), ('290', '1', '2018-09-10 06:48:00.000000', '6d27df660a414a3fb6d73156f0cb7d3d', 'manager'), ('291', '1', '2018-09-10 06:48:00.000000', '0f61062a5aca4e7299a4fde489b9d83e', 'manager'), ('292', '1', '2018-09-10 06:48:00.000000', '708e501b81e0428ea0f0427c4e97964a', 'manager'), ('293', '1', '2018-09-10 06:48:00.000000', '9569acd658b04880a23a21febd3c29ce', 'manager'), ('294', '1', '2018-09-10 06:48:00.000000', 'a1dece243b0142ff81f75c5b5d3f89f3', 'manager'), ('295', '1', '2018-09-10 06:48:00.000000', '8dd468711f41404fab71530951d2340c', 'manager'), ('296', '1', '2018-09-10 06:48:00.000000', '994e168db4c74c588503a1174da999bc', 'manager'), ('297', '1', '2018-09-10 06:48:00.000000', '72ab70daaf7b4f7d8a9335554ed01094', 'manager'), ('298', '1', '2018-09-10 06:48:00.000000', '782e404322e24caa9846b04207414bbb', 'manager'), ('299', '1', '2018-09-10 06:48:00.000000', '9b3f96f30978401681edd38ea41d75bf', 'manager'), ('300', '1', '2018-09-10 06:48:00.000000', 'bdf1edf832fe42ec93917473f9208250', 'manager'), ('301', '1', '2018-09-10 06:48:00.000000', 'ec23739ecfe742b89e0854cf487b5c54', 'manager'), ('302', '1', '2018-09-10 06:48:00.000000', '30e7db997a2f4a3d85ce54ae5dc21e06', 'manager'), ('303', '1', '2018-09-10 06:48:00.000000', 'f4fdd5cc44d049ccbcb86da50ffeca51', 'manager'), ('304', '1', '2018-09-10 06:48:00.000000', '6cc1755a2ca1477c87a398d8dafaf1fc', 'manager'), ('305', '1', '2018-09-10 06:48:00.000000', '863cf952242545f2bf5bcca5aa8a3515', 'manager'), ('306', '1', '2018-09-10 06:48:00.000000', '0725da1a6ae74c1b90446584dd234e39', 'manager'), ('307', '1', '2018-09-10 06:48:00.000000', 'e9eb50e0646f4198aa4cbefbdd01403f', 'manager'), ('308', '1', '2018-09-10 06:48:00.000000', '68043153e40143dd97a9acbbc3f94ac5', 'manager'), ('309', '1', '2018-09-10 06:48:00.000000', '9c4e5773b642454180ede04e7bd6f793', 'manager'), ('310', '1', '2018-09-10 06:48:00.000000', '32e4fbba7762472484d0a66bbe64808d', 'manager'), ('311', '1', '2018-09-10 06:48:00.000000', 'd86f172da2d44497aaa0474b791c4f6d', 'manager'), ('312', '1', '2018-09-10 06:48:00.000000', 'f702d500989048b4801d0a538bb73027', 'manager'), ('313', '1', '2018-09-10 06:48:00.000000', '6067b35290e9426e96c146dcb149c0ae', 'manager'), ('314', '1', '2018-09-10 06:48:00.000000', '565c01742ab34ed18d037e791a586099', 'manager'), ('315', '1', '2018-09-10 06:48:00.000000', '04bdf9e393e3418b9f941a8a6d493065', 'manager'), ('316', '1', '2018-10-22 07:43:39.472258', '27b600b5bdc34bc48a3c1bebd6ef830a', 'test'), ('317', '1', '2018-10-22 07:43:44.232894', '27b600b5bdc34bc48a3c1bebd6ef830a', 'developer'), ('318', '1', '2018-10-22 07:43:47.737383', '27b600b5bdc34bc48a3c1bebd6ef830a', 'pm'), ('319', '1', '2018-10-22 07:43:50.956803', '27b600b5bdc34bc48a3c1bebd6ef830a', 'design'), ('320', '1', '2018-10-22 07:43:54.246047', '27b600b5bdc34bc48a3c1bebd6ef830a', 'manager'), ('321', '1', '2018-10-25 12:32:30.158901', '49aad34abecb4939863812c2c3f5659c', 'test'), ('322', '1', '2018-10-25 12:32:35.795969', '49aad34abecb4939863812c2c3f5659c', 'developer'), ('323', '1', '2018-10-25 12:32:39.073645', '49aad34abecb4939863812c2c3f5659c', 'pm'), ('324', '1', '2018-10-25 12:32:41.392732', '49aad34abecb4939863812c2c3f5659c', 'design'), ('325', '1', '2018-10-25 12:32:43.682455', '49aad34abecb4939863812c2c3f5659c', 'manager'), ('326', '1', '2018-10-25 13:03:05.643807', 'c5ee2c3945284305aa199d57ff24a8c9', 'test'), ('327', '1', '2018-10-25 13:03:07.896895', 'c5ee2c3945284305aa199d57ff24a8c9', 'manager'), ('328', '1', '2018-10-25 13:03:10.817730', 'c5ee2c3945284305aa199d57ff24a8c9', 'design'), ('329', '1', '2018-10-25 13:03:14.063519', 'c5ee2c3945284305aa199d57ff24a8c9', 'pm'), ('330', '1', '2018-10-25 13:03:18.132693', 'c5ee2c3945284305aa199d57ff24a8c9', 'developer'), ('331', '1', '2018-11-02 20:16:13.584076', '83ce6de7a3034c7da03c793051639243', 'test'), ('332', '1', '2018-11-02 20:16:23.953687', '83ce6de7a3034c7da03c793051639243', 'developer'), ('333', '1', '2018-11-02 20:16:35.287411', '83ce6de7a3034c7da03c793051639243', 'pm'), ('334', '1', '2018-11-02 20:16:39.859221', '83ce6de7a3034c7da03c793051639243', 'design'), ('335', '1', '2018-11-02 20:16:45.154741', '83ce6de7a3034c7da03c793051639243', 'manager');
COMMIT;

-- ----------------------------
--  Table structure for `t_authentication`
-- ----------------------------
DROP TABLE IF EXISTS `t_authentication`;
CREATE TABLE `t_authentication` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `token` varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  `uid` char(32) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `t_authentication_uid_200d4eab_fk_t_user_user_id` (`uid`),
  CONSTRAINT `t_authentication_uid_200d4eab_fk_t_user_user_id` FOREIGN KEY (`uid`) REFERENCES `t_user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
--  Records of `t_authentication`
-- ----------------------------
BEGIN;
INSERT INTO `t_authentication` VALUES ('1', 'ZQSz4yvMmfVg2chSmFwFPeuzmP0oM8PU2eg51G1js1G+HKjhElIsuYKREJRGnUMPcOQ+Dse0UYHPpCnJ/F8J/SFHwyX1oGHN0g8yNdQssXu8nwOhynCeXuo6zfHHF8kbiqa+acH1LBNqRzhLCuQHwhTJjz1p8g5Dvy6N53GoLCL3mWyzvN6neJOIPLv8+uCko/cSqKsX', '990a339b2ae24e09b25e08eb38c24a3f');
COMMIT;

-- ----------------------------
--  Table structure for `t_bug`
-- ----------------------------
DROP TABLE IF EXISTS `t_bug`;
CREATE TABLE `t_bug` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bug_id` char(32) COLLATE utf8mb4_general_ci NOT NULL,
  `title` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `steps` varchar(1000) COLLATE utf8mb4_general_ci NOT NULL,
  `reality_result` varchar(500) COLLATE utf8mb4_general_ci NOT NULL,
  `expected_result` varchar(500) COLLATE utf8mb4_general_ci NOT NULL,
  `remark` varchar(1000) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `create_time` datetime(6) NOT NULL,
  `assignedTo_time` datetime(6) NOT NULL,
  `fixed_time` datetime(6) DEFAULT NULL,
  `closed_time` datetime(6) DEFAULT NULL,
  `hangUp_time` datetime(6) DEFAULT NULL,
  `isDelete` int(11) NOT NULL,
  `delete_time` datetime(6) DEFAULT NULL,
  `last_Time` datetime(6) NOT NULL,
  `assignedTo_id` char(32) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `bug_type` varchar(10) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `case_id` char(32) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `cell_id` char(32) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `closed_id` char(32) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `creator_id` char(32) COLLATE utf8mb4_general_ci NOT NULL,
  `delete_id` char(32) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `fixed_id` char(32) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `hangUp_id` char(32) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `m1_id` int(11) DEFAULT NULL,
  `m2_id` int(11) DEFAULT NULL,
  `priority` varchar(15) COLLATE utf8mb4_general_ci NOT NULL,
  `product_code` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `severity` varchar(15) COLLATE utf8mb4_general_ci NOT NULL,
  `solution` varchar(15) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `status` varchar(15) COLLATE utf8mb4_general_ci NOT NULL,
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
--  Table structure for `t_bug_annex`
-- ----------------------------
DROP TABLE IF EXISTS `t_bug_annex`;
CREATE TABLE `t_bug_annex` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `isDelete` int(11) NOT NULL,
  `bug_id` char(32) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `t_bug_annex_bug_id_c6e889e1_fk_t_bug_bug_id` (`bug_id`),
  CONSTRAINT `t_bug_annex_bug_id_c6e889e1_fk_t_bug_bug_id` FOREIGN KEY (`bug_id`) REFERENCES `t_bug` (`bug_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
--  Table structure for `t_bug_history`
-- ----------------------------
DROP TABLE IF EXISTS `t_bug_history`;
CREATE TABLE `t_bug_history` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `desc` varchar(1000) COLLATE utf8mb4_general_ci NOT NULL,
  `remark` varchar(2000) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `create_time` datetime(6) NOT NULL,
  `bug_id` char(32) COLLATE utf8mb4_general_ci NOT NULL,
  `user_id` char(32) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `t_bug_history_bug_id_f83d43ea_fk_t_bug_bug_id` (`bug_id`),
  KEY `t_bug_history_user_id_979407d0_fk_t_user_user_id` (`user_id`),
  CONSTRAINT `t_bug_history_bug_id_f83d43ea_fk_t_bug_bug_id` FOREIGN KEY (`bug_id`) REFERENCES `t_bug` (`bug_id`),
  CONSTRAINT `t_bug_history_user_id_979407d0_fk_t_user_user_id` FOREIGN KEY (`user_id`) REFERENCES `t_user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
--  Table structure for `t_bug_priority`
-- ----------------------------
DROP TABLE IF EXISTS `t_bug_priority`;
CREATE TABLE `t_bug_priority` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `key` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `key` (`key`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ROW_FORMAT=DYNAMIC;

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
  `report_id` char(32) COLLATE utf8mb4_general_ci NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `content` longtext COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `report_id` (`report_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
--  Table structure for `t_bug_severity`
-- ----------------------------
DROP TABLE IF EXISTS `t_bug_severity`;
CREATE TABLE `t_bug_severity` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `key` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `key` (`key`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ROW_FORMAT=DYNAMIC;

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
  `key` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `key` (`key`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ROW_FORMAT=DYNAMIC;

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
  `key` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `key` (`key`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ROW_FORMAT=DYNAMIC;

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
  `key` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `key` (`key`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ROW_FORMAT=DYNAMIC;

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
  `group` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group` (`group`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
--  Records of `t_group`
-- ----------------------------
BEGIN;
INSERT INTO `t_group` VALUES ('1', 'admin', '超级管理员', '2018-08-20 15:24:26.000000', '2018-08-20 15:24:29.000000'), ('2', 'test', '测试', '2018-08-20 16:57:54.000000', '2018-08-20 16:57:59.000000'), ('3', 'developer', '开发', '2018-08-20 17:04:50.000000', '2018-08-20 17:04:52.000000'), ('4', 'pm', '产品', '2018-08-20 17:05:05.000000', '2018-08-20 17:05:07.000000'), ('5', 'design', '设计', '2018-08-20 17:05:21.000000', '2018-08-20 17:05:23.000000'), ('6', 'manager', '管理层', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
COMMIT;

-- ----------------------------
--  Table structure for `t_keyword_filter`
-- ----------------------------
DROP TABLE IF EXISTS `t_keyword_filter`;
CREATE TABLE `t_keyword_filter` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `keyword` varchar(30) COLLATE utf8mb4_general_ci NOT NULL,
  `create_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
--  Table structure for `t_logged_log`
-- ----------------------------
DROP TABLE IF EXISTS `t_logged_log`;
CREATE TABLE `t_logged_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(20) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `path` varchar(200) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `method` varchar(20) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `request` varchar(10000) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `platform` varchar(200) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `browser` varchar(200) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `user_id` char(32) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `t_logged_log_user_id_2bfe0aa9_fk_t_user_user_id` (`user_id`),
  CONSTRAINT `t_logged_log_user_id_2bfe0aa9_fk_t_user_user_id` FOREIGN KEY (`user_id`) REFERENCES `t_user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
--  Table structure for `t_module_1`
-- ----------------------------
DROP TABLE IF EXISTS `t_module_1`;
CREATE TABLE `t_module_1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `m1` varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  `isChange` int(11) NOT NULL,
  `isDelete` int(11) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `change_time` datetime(6) DEFAULT NULL,
  `delete_time` datetime(6) DEFAULT NULL,
  `update_time` datetime(6) NOT NULL,
  `changer_id` char(32) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `creator_id` char(32) COLLATE utf8mb4_general_ci NOT NULL,
  `deleter_id` char(32) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `product_code` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `t_module_1_changer_id_fe604c32_fk_t_user_user_id` (`changer_id`),
  KEY `t_module_1_creator_id_080bbfa1_fk_t_user_user_id` (`creator_id`),
  KEY `t_module_1_deleter_id_cd56e807_fk_t_user_user_id` (`deleter_id`),
  KEY `t_module_1_product_code_16b2e778_fk_t_product_product_code` (`product_code`),
  CONSTRAINT `t_module_1_changer_id_fe604c32_fk_t_user_user_id` FOREIGN KEY (`changer_id`) REFERENCES `t_user` (`user_id`),
  CONSTRAINT `t_module_1_creator_id_080bbfa1_fk_t_user_user_id` FOREIGN KEY (`creator_id`) REFERENCES `t_user` (`user_id`),
  CONSTRAINT `t_module_1_deleter_id_cd56e807_fk_t_user_user_id` FOREIGN KEY (`deleter_id`) REFERENCES `t_user` (`user_id`),
  CONSTRAINT `t_module_1_product_code_16b2e778_fk_t_product_product_code` FOREIGN KEY (`product_code`) REFERENCES `t_product` (`product_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
--  Table structure for `t_module_2`
-- ----------------------------
DROP TABLE IF EXISTS `t_module_2`;
CREATE TABLE `t_module_2` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `m2` varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  `isChange` int(11) NOT NULL,
  `isDelete` int(11) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `change_time` datetime(6) DEFAULT NULL,
  `delete_time` datetime(6) DEFAULT NULL,
  `update_time` datetime(6) NOT NULL,
  `changer_id` char(32) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `creator_id` char(32) COLLATE utf8mb4_general_ci NOT NULL,
  `deleter_id` char(32) COLLATE utf8mb4_general_ci DEFAULT NULL,
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
--  Table structure for `t_pages`
-- ----------------------------
DROP TABLE IF EXISTS `t_pages`;
CREATE TABLE `t_pages` (
  `id` char(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `page_name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `page_url` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `flag` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `create_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `page_name` (`page_name`),
  UNIQUE KEY `page_url` (`page_url`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
--  Records of `t_pages`
-- ----------------------------
BEGIN;
INSERT INTO `t_pages` VALUES ('0a3a0c4311134eb198dff5933ac2b2dd', '测试用例（列表）', '/app/qa/testcase', '测试用例', '2018-10-15 14:10:26.000000'), ('1452b489e06d4c5386724ba321312b47', '缺陷（详情）', '/app/qa/bug/deatils', '缺陷', '2018-10-15 14:10:26.000000'), ('1b3953f13759455b964347b170779944', '缺陷（统计）', '/app/qa/bug/count', '缺陷', '2018-10-15 14:10:26.000000'), ('2a16016b00fa4c39a80ae4140a92d5f0', 'Dashboard', '/app/dashboard', '首页', '2018-10-15 14:10:26.000000'), ('33eeef208a444ef18b528b5f5890b8b9', '缺陷（增加）', '/app/qa/bug/add', '缺陷', '2018-10-15 14:10:26.000000'), ('3c9370c5351d4711bd23937dc288639b', '系统设置（权限）', '/app/system/permissions', '系统设置', '2018-10-15 14:10:26.000000'), ('45993fc8a6b947be9c5cdf719089db13', '系统设置（缺陷）', '/app/system/bug', '系统设置', '2018-10-15 14:10:26.000000'), ('52f23beb1faf40b5bf8eda4d57fb07c4', '缺陷（编辑）', '/app/qa/bug/edit', '缺陷', '2018-10-15 14:10:26.000000'), ('606040ce942048748c6c9ae47c64927d', '系统设置', '/app/system', '系统设置', '2018-10-15 14:10:26.000000'), ('6779c9a09b004018b95273e5b71e2ce7', '产品（列表）', '/app/products', '产品管理', '2018-10-15 14:10:26.000000'), ('6addbb93a2974551ac6f39afb2cffe52', '缺陷（列表）', '/app/qa/bug', '缺陷', '2018-10-15 14:10:26.000000'), ('6feeacc00d644a0ba1df38d461d0dfbd', '测试用例执行', '/app/qa/testsuite/loader', '测试用例', '2018-10-15 14:10:26.000000'), ('846bbc4cfbe24de0b36cdf59bcfd635a', 'testsuite', '/app/qa/testsuite', '测试用例', '2018-10-15 14:10:26.000000'), ('85602f019cdb49fda5ce5d61e8ced662', '产品版本', '/app/products/release', '产品管理', '2018-10-15 14:10:26.000000'), ('88fe84b661bd40c0b37ffcdf580861e4', '测试用例（详情）', '/app/qa/testcase/deatils', '测试用例', '2018-10-15 14:10:26.000000'), ('9b3ca9dfb15f4b7fa6aa6b3f1e8619f1', '缺陷（报告详情）', '/app/qa/bug/report_details', '缺陷', '2018-10-15 14:10:26.000000'), ('a7dfefb886bb4c3bbf6b250c2bed1ecf', '缺陷（生成报告）', '/app/qa/bug/report', '缺陷', '2018-10-15 14:10:26.000000'), ('b3be361d61614184bc87d2b273a03b96', 'API', '/app/auto/api', '系统设置', '2018-10-15 14:10:26.000000'), ('b911770ecf2f49ce8493910653cf7422', '产品（模块）', '/app/products/modules', '产品管理', '2018-10-15 14:10:26.000000'), ('beced0b00904435d932ea2671d050dc3', '测试用例（编辑）', '/app/qa/testcase/edit', '测试用例', '2018-10-15 14:10:26.000000'), ('c064bce1da0f48729523c7ebedcd8f13', '用户管理（用户列表）', '/app/user-management/user', '用户管理', '2018-10-15 14:10:26.000000'), ('c880ec50a8bc480e9803a03dcfbed80d', '用户管理（创建用户）', '/app/user-management/user/adduser', '用户管理', '2018-10-15 14:10:26.000000'), ('e15c910a5428419a960e23b170712bab', '测试用例（运行）', '/app/qa/testsuite/run', '测试用例', '2018-10-15 14:10:26.000000'), ('e1ffdf5b1e48411ea914878617a0d1b4', '产品（人员）', '/app/products/members', '产品管理', '2018-10-15 14:10:26.000000'), ('ebf8d4aeb37a476aa2d351457d34fee6', '测试用例（创建）', '/app/qa/testcase/add', '测试用例', '2018-10-15 14:10:26.000000'), ('f536711bc69b404285261f710f36a13b', '设置密码', '/app/set/passwd', '用户设置', '2018-10-15 14:10:26.000000');
COMMIT;

-- ----------------------------
--  Table structure for `t_pages_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `t_pages_permissions`;
CREATE TABLE `t_pages_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `is_allow` int(11) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `group` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `page_id` char(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `t_pages_permissions_group_011956a4_fk_t_group_group` (`group`),
  KEY `t_pages_permissions_page_id_9a2df006_fk_t_pages_id` (`page_id`),
  CONSTRAINT `t_pages_permissions_group_011956a4_fk_t_group_group` FOREIGN KEY (`group`) REFERENCES `t_group` (`group`),
  CONSTRAINT `t_pages_permissions_page_id_9a2df006_fk_t_pages_id` FOREIGN KEY (`page_id`) REFERENCES `t_pages` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=130 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
--  Records of `t_pages_permissions`
-- ----------------------------
BEGIN;
INSERT INTO `t_pages_permissions` VALUES ('1', '1', '2018-10-20 22:05:07.630835', 'test', '0a3a0c4311134eb198dff5933ac2b2dd'), ('2', '1', '2018-10-20 22:05:34.480644', 'test', '6feeacc00d644a0ba1df38d461d0dfbd'), ('3', '1', '2018-10-20 22:05:35.214975', 'test', '846bbc4cfbe24de0b36cdf59bcfd635a'), ('4', '1', '2018-10-20 22:05:35.890295', 'test', '88fe84b661bd40c0b37ffcdf580861e4'), ('5', '1', '2018-10-20 22:05:36.549002', 'test', 'beced0b00904435d932ea2671d050dc3'), ('6', '1', '2018-10-20 22:05:37.317528', 'test', 'e15c910a5428419a960e23b170712bab'), ('7', '1', '2018-10-20 22:05:37.935269', 'test', 'ebf8d4aeb37a476aa2d351457d34fee6'), ('8', '1', '2018-10-20 22:05:39.423720', 'test', '1452b489e06d4c5386724ba321312b47'), ('9', '1', '2018-10-20 22:05:40.012667', 'test', '1b3953f13759455b964347b170779944'), ('10', '1', '2018-10-20 22:05:40.785948', 'test', '33eeef208a444ef18b528b5f5890b8b9'), ('11', '1', '2018-10-20 22:05:41.403420', 'test', '52f23beb1faf40b5bf8eda4d57fb07c4'), ('12', '1', '2018-10-20 22:05:42.078644', 'test', '6addbb93a2974551ac6f39afb2cffe52'), ('13', '1', '2018-10-20 22:05:42.772667', 'test', '9b3ca9dfb15f4b7fa6aa6b3f1e8619f1'), ('14', '1', '2018-10-20 22:05:43.475107', 'test', 'a7dfefb886bb4c3bbf6b250c2bed1ecf'), ('15', '1', '2018-10-20 22:05:44.738989', 'test', '2a16016b00fa4c39a80ae4140a92d5f0'), ('16', '-1', '2018-10-20 22:05:46.120163', 'test', '3c9370c5351d4711bd23937dc288639b'), ('17', '-1', '2018-10-20 22:05:46.943933', 'test', '45993fc8a6b947be9c5cdf719089db13'), ('18', '-1', '2018-10-20 22:05:47.633986', 'test', '606040ce942048748c6c9ae47c64927d'), ('19', '-1', '2018-10-20 22:05:48.255765', 'test', 'b3be361d61614184bc87d2b273a03b96'), ('20', '-1', '2018-10-20 22:05:49.499146', 'test', '6779c9a09b004018b95273e5b71e2ce7'), ('21', '-1', '2018-10-20 22:05:50.068582', 'test', '85602f019cdb49fda5ce5d61e8ced662'), ('22', '-1', '2018-10-20 22:05:50.683537', 'test', 'b911770ecf2f49ce8493910653cf7422'), ('23', '-1', '2018-10-20 22:05:51.442302', 'test', 'e1ffdf5b1e48411ea914878617a0d1b4'), ('24', '-1', '2018-10-20 22:05:52.676685', 'test', 'c064bce1da0f48729523c7ebedcd8f13'), ('25', '-1', '2018-10-20 22:05:53.320833', 'test', 'c880ec50a8bc480e9803a03dcfbed80d'), ('26', '1', '2018-10-20 22:06:11.767455', 'developer', '0a3a0c4311134eb198dff5933ac2b2dd'), ('27', '1', '2018-10-20 22:06:12.488268', 'developer', '6feeacc00d644a0ba1df38d461d0dfbd'), ('28', '1', '2018-10-20 22:06:14.223104', 'developer', '846bbc4cfbe24de0b36cdf59bcfd635a'), ('29', '1', '2018-10-20 22:06:14.911681', 'developer', '88fe84b661bd40c0b37ffcdf580861e4'), ('30', '1', '2018-10-20 22:06:15.661059', 'developer', 'beced0b00904435d932ea2671d050dc3'), ('31', '1', '2018-10-20 22:06:16.593536', 'developer', 'e15c910a5428419a960e23b170712bab'), ('32', '1', '2018-10-20 22:06:17.385582', 'developer', 'ebf8d4aeb37a476aa2d351457d34fee6'), ('33', '1', '2018-10-20 22:06:18.674061', 'developer', '1452b489e06d4c5386724ba321312b47'), ('34', '1', '2018-10-20 22:06:19.317345', 'developer', '1b3953f13759455b964347b170779944'), ('35', '1', '2018-10-20 22:06:19.991645', 'developer', '33eeef208a444ef18b528b5f5890b8b9'), ('36', '1', '2018-10-20 22:06:20.732892', 'developer', '52f23beb1faf40b5bf8eda4d57fb07c4'), ('37', '1', '2018-10-20 22:06:22.221639', 'developer', '6addbb93a2974551ac6f39afb2cffe52'), ('38', '1', '2018-10-20 22:06:22.810417', 'developer', '9b3ca9dfb15f4b7fa6aa6b3f1e8619f1'), ('39', '1', '2018-10-20 22:06:23.586181', 'developer', 'a7dfefb886bb4c3bbf6b250c2bed1ecf'), ('40', '1', '2018-10-20 22:06:27.399962', 'developer', 'f536711bc69b404285261f710f36a13b'), ('41', '-1', '2018-10-20 22:06:28.406993', 'developer', 'c880ec50a8bc480e9803a03dcfbed80d'), ('42', '-1', '2018-10-20 22:06:29.238254', 'developer', 'c064bce1da0f48729523c7ebedcd8f13'), ('43', '-1', '2018-10-20 22:06:30.067673', 'developer', 'e1ffdf5b1e48411ea914878617a0d1b4'), ('44', '-1', '2018-10-20 22:06:30.772935', 'developer', 'b911770ecf2f49ce8493910653cf7422'), ('45', '-1', '2018-10-20 22:06:31.544004', 'developer', '85602f019cdb49fda5ce5d61e8ced662'), ('46', '-1', '2018-10-20 22:06:32.291091', 'developer', '6779c9a09b004018b95273e5b71e2ce7'), ('47', '-1', '2018-10-20 22:06:34.107075', 'developer', 'b3be361d61614184bc87d2b273a03b96'), ('48', '-1', '2018-10-20 22:06:34.888898', 'developer', '606040ce942048748c6c9ae47c64927d'), ('49', '-1', '2018-10-20 22:06:35.517540', 'developer', '45993fc8a6b947be9c5cdf719089db13'), ('50', '-1', '2018-10-20 22:06:36.953128', 'developer', '3c9370c5351d4711bd23937dc288639b'), ('51', '1', '2018-10-20 22:06:38.165718', 'developer', '2a16016b00fa4c39a80ae4140a92d5f0'), ('52', '1', '2018-10-20 22:06:47.297157', 'pm', '0a3a0c4311134eb198dff5933ac2b2dd'), ('53', '1', '2018-10-20 22:06:47.888223', 'pm', '6feeacc00d644a0ba1df38d461d0dfbd'), ('54', '1', '2018-10-20 22:06:48.599069', 'pm', '846bbc4cfbe24de0b36cdf59bcfd635a'), ('55', '1', '2018-10-20 22:06:49.395304', 'pm', '88fe84b661bd40c0b37ffcdf580861e4'), ('56', '1', '2018-10-20 22:06:50.070667', 'pm', 'beced0b00904435d932ea2671d050dc3'), ('57', '1', '2018-10-20 22:06:50.740600', 'pm', 'e15c910a5428419a960e23b170712bab'), ('58', '1', '2018-10-20 22:06:53.051390', 'pm', 'ebf8d4aeb37a476aa2d351457d34fee6'), ('59', '1', '2018-10-20 22:06:54.855151', 'pm', '1452b489e06d4c5386724ba321312b47'), ('60', '1', '2018-10-20 22:06:56.233950', 'pm', '1b3953f13759455b964347b170779944'), ('61', '1', '2018-10-20 22:06:56.860701', 'pm', '33eeef208a444ef18b528b5f5890b8b9'), ('62', '1', '2018-10-20 22:06:57.487179', 'pm', '52f23beb1faf40b5bf8eda4d57fb07c4'), ('63', '1', '2018-10-20 22:06:58.464566', 'pm', '6addbb93a2974551ac6f39afb2cffe52'), ('64', '1', '2018-10-20 22:06:59.287387', 'pm', '9b3ca9dfb15f4b7fa6aa6b3f1e8619f1'), ('65', '1', '2018-10-20 22:07:00.578677', 'pm', 'a7dfefb886bb4c3bbf6b250c2bed1ecf'), ('66', '1', '2018-10-20 22:07:01.798051', 'pm', '2a16016b00fa4c39a80ae4140a92d5f0'), ('67', '-1', '2018-10-20 22:07:03.139220', 'pm', '3c9370c5351d4711bd23937dc288639b'), ('68', '-1', '2018-10-20 22:07:03.896444', 'pm', '45993fc8a6b947be9c5cdf719089db13'), ('69', '-1', '2018-10-20 22:07:04.533505', 'pm', '606040ce942048748c6c9ae47c64927d'), ('70', '-1', '2018-10-20 22:07:05.189746', 'pm', 'b3be361d61614184bc87d2b273a03b96'), ('71', '1', '2018-10-20 22:07:06.449587', 'pm', '6779c9a09b004018b95273e5b71e2ce7'), ('72', '1', '2018-10-20 22:07:07.749436', 'pm', '85602f019cdb49fda5ce5d61e8ced662'), ('73', '1', '2018-10-20 22:07:08.445953', 'pm', 'b911770ecf2f49ce8493910653cf7422'), ('74', '1', '2018-10-20 22:07:09.065274', 'pm', 'e1ffdf5b1e48411ea914878617a0d1b4'), ('75', '-1', '2018-10-20 22:07:10.446038', 'pm', 'c064bce1da0f48729523c7ebedcd8f13'), ('76', '-1', '2018-10-20 22:07:11.845938', 'pm', 'c880ec50a8bc480e9803a03dcfbed80d'), ('77', '1', '2018-10-20 22:07:13.191961', 'pm', 'f536711bc69b404285261f710f36a13b'), ('78', '1', '2018-10-20 22:07:16.478769', 'design', '0a3a0c4311134eb198dff5933ac2b2dd'), ('79', '1', '2018-10-20 22:07:17.074930', 'design', '6feeacc00d644a0ba1df38d461d0dfbd'), ('80', '1', '2018-10-20 22:07:17.950101', 'design', '846bbc4cfbe24de0b36cdf59bcfd635a'), ('81', '1', '2018-10-20 22:07:18.643334', 'design', '88fe84b661bd40c0b37ffcdf580861e4'), ('82', '1', '2018-10-20 22:07:19.266142', 'design', 'beced0b00904435d932ea2671d050dc3'), ('83', '1', '2018-10-20 22:07:19.845319', 'design', 'e15c910a5428419a960e23b170712bab'), ('84', '1', '2018-10-20 22:07:20.489282', 'design', 'ebf8d4aeb37a476aa2d351457d34fee6'), ('85', '1', '2018-10-20 22:07:21.847381', 'design', '1452b489e06d4c5386724ba321312b47'), ('86', '1', '2018-10-20 22:07:25.067545', 'design', '1b3953f13759455b964347b170779944'), ('87', '1', '2018-10-20 22:07:25.696145', 'design', '33eeef208a444ef18b528b5f5890b8b9'), ('88', '1', '2018-10-20 22:07:26.471451', 'design', '52f23beb1faf40b5bf8eda4d57fb07c4'), ('89', '1', '2018-10-20 22:07:27.950463', 'design', '6addbb93a2974551ac6f39afb2cffe52'), ('90', '1', '2018-10-20 22:07:29.431501', 'design', '9b3ca9dfb15f4b7fa6aa6b3f1e8619f1'), ('91', '1', '2018-10-20 22:07:30.131792', 'design', 'a7dfefb886bb4c3bbf6b250c2bed1ecf'), ('92', '1', '2018-10-20 22:07:31.507224', 'design', '2a16016b00fa4c39a80ae4140a92d5f0'), ('93', '-1', '2018-10-20 22:07:34.396826', 'design', '3c9370c5351d4711bd23937dc288639b'), ('94', '-1', '2018-10-20 22:07:35.994407', 'design', '45993fc8a6b947be9c5cdf719089db13'), ('95', '-1', '2018-10-20 22:07:36.642521', 'design', '606040ce942048748c6c9ae47c64927d'), ('96', '-1', '2018-10-20 22:07:37.325990', 'design', 'b3be361d61614184bc87d2b273a03b96'), ('97', '1', '2018-10-20 22:07:38.370184', 'design', '6779c9a09b004018b95273e5b71e2ce7'), ('98', '1', '2018-10-20 22:07:39.680422', 'design', '85602f019cdb49fda5ce5d61e8ced662'), ('99', '1', '2018-10-20 22:07:40.557148', 'design', 'b911770ecf2f49ce8493910653cf7422'), ('100', '1', '2018-10-20 22:07:41.325290', 'design', 'e1ffdf5b1e48411ea914878617a0d1b4'), ('101', '-1', '2018-10-20 22:07:42.813458', 'design', 'c064bce1da0f48729523c7ebedcd8f13'), ('102', '-1', '2018-10-20 22:07:43.530813', 'design', 'c880ec50a8bc480e9803a03dcfbed80d'), ('103', '1', '2018-10-20 22:07:44.517492', 'design', 'f536711bc69b404285261f710f36a13b'), ('104', '1', '2018-10-20 22:07:48.373738', 'manager', '0a3a0c4311134eb198dff5933ac2b2dd'), ('105', '1', '2018-10-20 22:07:49.031539', 'manager', '6feeacc00d644a0ba1df38d461d0dfbd'), ('106', '1', '2018-10-20 22:07:49.650431', 'manager', '846bbc4cfbe24de0b36cdf59bcfd635a'), ('107', '1', '2018-10-20 22:07:51.477354', 'manager', '88fe84b661bd40c0b37ffcdf580861e4'), ('108', '1', '2018-10-20 22:07:53.120992', 'manager', 'beced0b00904435d932ea2671d050dc3'), ('109', '1', '2018-10-20 22:07:53.986331', 'manager', 'e15c910a5428419a960e23b170712bab'), ('110', '1', '2018-10-20 22:07:54.711433', 'manager', 'ebf8d4aeb37a476aa2d351457d34fee6'), ('111', '1', '2018-10-20 22:07:56.184469', 'manager', '1452b489e06d4c5386724ba321312b47'), ('112', '1', '2018-10-20 22:07:56.978029', 'manager', '1b3953f13759455b964347b170779944'), ('113', '1', '2018-10-20 22:07:57.854049', 'manager', '33eeef208a444ef18b528b5f5890b8b9'), ('114', '1', '2018-10-20 22:07:59.710964', 'manager', '52f23beb1faf40b5bf8eda4d57fb07c4'), ('115', '1', '2018-10-20 22:08:00.869524', 'manager', '6addbb93a2974551ac6f39afb2cffe52'), ('116', '1', '2018-10-20 22:08:02.318616', 'manager', '9b3ca9dfb15f4b7fa6aa6b3f1e8619f1'), ('117', '1', '2018-10-20 22:08:03.729159', 'manager', 'a7dfefb886bb4c3bbf6b250c2bed1ecf'), ('118', '1', '2018-10-20 22:08:05.269825', 'manager', '2a16016b00fa4c39a80ae4140a92d5f0'), ('119', '1', '2018-10-20 22:08:06.394937', 'manager', '3c9370c5351d4711bd23937dc288639b'), ('120', '1', '2018-10-20 22:08:07.307500', 'manager', '45993fc8a6b947be9c5cdf719089db13'), ('121', '1', '2018-10-20 22:08:09.173532', 'manager', '606040ce942048748c6c9ae47c64927d'), ('122', '1', '2018-10-20 22:08:09.822062', 'manager', 'b3be361d61614184bc87d2b273a03b96'), ('123', '1', '2018-10-20 22:08:11.201881', 'manager', '6779c9a09b004018b95273e5b71e2ce7'), ('124', '1', '2018-10-20 22:08:12.173255', 'manager', '85602f019cdb49fda5ce5d61e8ced662'), ('125', '1', '2018-10-20 22:08:12.837789', 'manager', 'b911770ecf2f49ce8493910653cf7422'), ('126', '1', '2018-10-20 22:08:13.547009', 'manager', 'e1ffdf5b1e48411ea914878617a0d1b4'), ('127', '1', '2018-10-20 22:08:14.999589', 'manager', 'c064bce1da0f48729523c7ebedcd8f13'), ('128', '1', '2018-10-20 22:08:15.728062', 'manager', 'c880ec50a8bc480e9803a03dcfbed80d'), ('129', '1', '2018-10-20 22:08:17.342738', 'manager', 'f536711bc69b404285261f710f36a13b');
COMMIT;

-- ----------------------------
--  Table structure for `t_product`
-- ----------------------------
DROP TABLE IF EXISTS `t_product`;
CREATE TABLE `t_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_name` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `product_code` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `status` int(11) NOT NULL,
  `remark` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `start_time` datetime(6) DEFAULT NULL,
  `end_time` datetime(6) DEFAULT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `creator_id` char(32) COLLATE utf8mb4_general_ci NOT NULL,
  `principal` char(32) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `product_code` (`product_code`),
  KEY `t_product_creator_id_b47a31d9_fk_t_user_user_id` (`creator_id`),
  KEY `t_product_principal_caf02773_fk_t_user_user_id` (`principal`),
  CONSTRAINT `t_product_creator_id_b47a31d9_fk_t_user_user_id` FOREIGN KEY (`creator_id`) REFERENCES `t_user` (`user_id`),
  CONSTRAINT `t_product_principal_caf02773_fk_t_user_user_id` FOREIGN KEY (`principal`) REFERENCES `t_user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
--  Table structure for `t_product_members`
-- ----------------------------
DROP TABLE IF EXISTS `t_product_members`;
CREATE TABLE `t_product_members` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status` int(11) NOT NULL,
  `join_time` datetime(6) NOT NULL,
  `banned_time` datetime(6) DEFAULT NULL,
  `member_id` char(32) COLLATE utf8mb4_general_ci NOT NULL,
  `product_code` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `t_product_members_member_id_fbad669f_fk_t_user_user_id` (`member_id`),
  KEY `t_product_members_product_code_5dfbe5b6_fk_t_product` (`product_code`),
  CONSTRAINT `t_product_members_member_id_fbad669f_fk_t_user_user_id` FOREIGN KEY (`member_id`) REFERENCES `t_user` (`user_id`),
  CONSTRAINT `t_product_members_product_code_5dfbe5b6_fk_t_product` FOREIGN KEY (`product_code`) REFERENCES `t_product` (`product_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
--  Table structure for `t_release`
-- ----------------------------
DROP TABLE IF EXISTS `t_release`;
CREATE TABLE `t_release` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `version` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `start_time` datetime(6) DEFAULT NULL,
  `online_time` datetime(6) DEFAULT NULL,
  `practicalnline_time` datetime(6) DEFAULT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `changer_id` char(32) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `creator_id` char(32) COLLATE utf8mb4_general_ci NOT NULL,
  `deleter_id` char(32) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `product_code` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `t_release_changer_id_156ce7f1_fk_t_user_user_id` (`changer_id`),
  KEY `t_release_creator_id_ac9c41ba_fk_t_user_user_id` (`creator_id`),
  KEY `t_release_deleter_id_edb34e97_fk_t_user_user_id` (`deleter_id`),
  KEY `t_release_product_code_2020d330_fk_t_product_product_code` (`product_code`),
  CONSTRAINT `t_release_changer_id_156ce7f1_fk_t_user_user_id` FOREIGN KEY (`changer_id`) REFERENCES `t_user` (`user_id`),
  CONSTRAINT `t_release_creator_id_ac9c41ba_fk_t_user_user_id` FOREIGN KEY (`creator_id`) REFERENCES `t_user` (`user_id`),
  CONSTRAINT `t_release_deleter_id_edb34e97_fk_t_user_user_id` FOREIGN KEY (`deleter_id`) REFERENCES `t_user` (`user_id`),
  CONSTRAINT `t_release_product_code_2020d330_fk_t_product_product_code` FOREIGN KEY (`product_code`) REFERENCES `t_product` (`product_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
--  Table structure for `t_system_config`
-- ----------------------------
DROP TABLE IF EXISTS `t_system_config`;
CREATE TABLE `t_system_config` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `code_value` int(11) NOT NULL,
  `code_desc` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
--  Table structure for `t_team`
-- ----------------------------
DROP TABLE IF EXISTS `t_team`;
CREATE TABLE `t_team` (
  `id` char(32) COLLATE utf8mb4_general_ci NOT NULL,
  `team_name` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
--  Records of `t_team`
-- ----------------------------
BEGIN;
INSERT INTO `t_team` VALUES ('25bdb281e1da431bbcd50dd75cd59946', 'DCloud', '2018-11-04 13:54:52.000000', '2018-11-04 13:54:52.000000'), ('7f0e6afb97a746fbb8ef51b9cc604b04', 'DCloud', '2018-11-04 13:48:42.000000', '2018-11-04 13:48:42.000000'), ('98508707845e4b559cba52a5678802c1', 'DCloud1234', '2018-11-04 13:50:26.000000', '2018-11-04 13:50:26.000000'), ('b7d3085df9da4b87a6560990f27d08c6', 'DCloud', '2018-11-04 13:52:35.000000', '2018-11-04 13:52:35.000000');
COMMIT;

-- ----------------------------
--  Table structure for `t_testcase`
-- ----------------------------
DROP TABLE IF EXISTS `t_testcase`;
CREATE TABLE `t_testcase` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `case_id` char(32) COLLATE utf8mb4_general_ci NOT NULL,
  `category` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `title` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `precondition` varchar(500) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `DataInput` longtext COLLATE utf8mb4_general_ci,
  `steps` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `expected_result` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `priority` varchar(10) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `remark` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `isChange` int(11) NOT NULL,
  `isDelete` int(11) NOT NULL,
  `isReview` int(11) NOT NULL,
  `status` int(11) NOT NULL,
  `fall_time` datetime(6) DEFAULT NULL,
  `change_time` datetime(6) DEFAULT NULL,
  `delete_time` datetime(6) DEFAULT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `changer_id` char(32) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `creator_id` char(32) COLLATE utf8mb4_general_ci NOT NULL,
  `deleter_id` char(32) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `faller_id` char(32) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `m1_id` int(11) DEFAULT NULL,
  `m2_id` int(11) DEFAULT NULL,
  `product_code` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
--  Table structure for `t_testcase_files`
-- ----------------------------
DROP TABLE IF EXISTS `t_testcase_files`;
CREATE TABLE `t_testcase_files` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `file_path` varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  `isDelete` int(11) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `case_id` char(32) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `t_testcase_files_case_id_15d690b6_fk_t_testcase_case_id` (`case_id`),
  CONSTRAINT `t_testcase_files_case_id_15d690b6_fk_t_testcase_case_id` FOREIGN KEY (`case_id`) REFERENCES `t_testcase` (`case_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
--  Table structure for `t_testcase_review`
-- ----------------------------
DROP TABLE IF EXISTS `t_testcase_review`;
CREATE TABLE `t_testcase_review` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `result` int(11) NOT NULL,
  `remark` varchar(2000) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `create_time` datetime(6) NOT NULL,
  `case_id` char(32) COLLATE utf8mb4_general_ci NOT NULL,
  `user_id` char(32) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `t_testcase_review_case_id_8b4cfa88_fk_t_testcase_case_id` (`case_id`),
  KEY `t_testcase_review_user_id_973a5df0_fk_t_user_user_id` (`user_id`),
  CONSTRAINT `t_testcase_review_case_id_8b4cfa88_fk_t_testcase_case_id` FOREIGN KEY (`case_id`) REFERENCES `t_testcase` (`case_id`),
  CONSTRAINT `t_testcase_review_user_id_973a5df0_fk_t_user_user_id` FOREIGN KEY (`user_id`) REFERENCES `t_user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
--  Table structure for `t_testsuite`
-- ----------------------------
DROP TABLE IF EXISTS `t_testsuite`;
CREATE TABLE `t_testsuite` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `suite_id` char(32) COLLATE utf8mb4_general_ci NOT NULL,
  `suite_name` varchar(30) COLLATE utf8mb4_general_ci NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `creator_id` char(32) COLLATE utf8mb4_general_ci NOT NULL,
  `product_code` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `suite_id` (`suite_id`),
  KEY `t_testsuite_creator_id_9499e1b4_fk_t_user_user_id` (`creator_id`),
  KEY `t_testsuite_product_code_7b806ee3_fk_t_product_product_code` (`product_code`),
  CONSTRAINT `t_testsuite_creator_id_9499e1b4_fk_t_user_user_id` FOREIGN KEY (`creator_id`) REFERENCES `t_user` (`user_id`),
  CONSTRAINT `t_testsuite_product_code_7b806ee3_fk_t_product_product_code` FOREIGN KEY (`product_code`) REFERENCES `t_product` (`product_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
--  Table structure for `t_testsuite_cell`
-- ----------------------------
DROP TABLE IF EXISTS `t_testsuite_cell`;
CREATE TABLE `t_testsuite_cell` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cell_id` char(32) COLLATE utf8mb4_general_ci NOT NULL,
  `result` int(11) NOT NULL,
  `run_time` datetime(6) DEFAULT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `case_id` char(32) COLLATE utf8mb4_general_ci NOT NULL,
  `creator_id` char(32) COLLATE utf8mb4_general_ci NOT NULL,
  `runner_id` char(32) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `suite_id` char(32) COLLATE utf8mb4_general_ci NOT NULL,
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
--  Table structure for `t_user`
-- ----------------------------
DROP TABLE IF EXISTS `t_user`;
CREATE TABLE `t_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` char(32) COLLATE utf8mb4_general_ci NOT NULL,
  `username` varchar(30) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `email` varchar(30) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `password` varchar(200) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `mobile` varchar(11) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `user_status` int(11) NOT NULL,
  `realname` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `position` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `gender` int(11) NOT NULL,
  `avatarUrl` varchar(300) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `province` varchar(20) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `city` varchar(20) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `source` varchar(20) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `identity` int(11) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `group` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `team_id` char(32) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  UNIQUE KEY `t_user_email_realname_eb131b7b_uniq` (`email`,`realname`),
  KEY `t_user_group_e5ccc203_fk_t_group_group` (`group`),
  KEY `t_user_team_id_6c48bc20_fk_t_team_id` (`team_id`),
  CONSTRAINT `t_user_group_e5ccc203_fk_t_group_group` FOREIGN KEY (`group`) REFERENCES `t_group` (`group`),
  CONSTRAINT `t_user_team_id_6c48bc20_fk_t_team_id` FOREIGN KEY (`team_id`) REFERENCES `t_team` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
--  Records of `t_user`
-- ----------------------------
BEGIN;
INSERT INTO `t_user` VALUES ('3', '990a339b2ae24e09b25e08eb38c24a3f', null, 'admin@1.com', '206492adca4f8ea4d638b21ceda168e52e0c32e9', null, '1', '超级管理员', null, '1', null, null, null, null, '0', '2018-11-04 13:54:52.000000', '2018-11-04 13:54:52.000000', 'admin', '25bdb281e1da431bbcd50dd75cd59946');
COMMIT;

-- ----------------------------
--  Table structure for `t_user_log`
-- ----------------------------
DROP TABLE IF EXISTS `t_user_log`;
CREATE TABLE `t_user_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(20) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `flag` varchar(200) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `user_id` char(32) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `t_user_log_user_id_9b05c49e_fk_t_user_user_id` (`user_id`),
  CONSTRAINT `t_user_log_user_id_9b05c49e_fk_t_user_user_id` FOREIGN KEY (`user_id`) REFERENCES `t_user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

SET FOREIGN_KEY_CHECKS = 1;
