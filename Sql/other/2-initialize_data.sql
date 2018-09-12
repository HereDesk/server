
-- 缺陷状态
insert into `t_bug_status` ( `key`, `name`) values ( 'New', '新建未分配');
insert into `t_bug_status` ( `key`, `name`) values ( 'Open', '待解决');
insert into `t_bug_status` ( `key`, `name`) values ( 'Closed', '已关闭');
insert into `t_bug_status` ( `key`, `name`) values ( 'Fixed', '已解决');
insert into `t_bug_status` ( `key`, `name`) values ( 'Reopen', '重新打开');
insert into `t_bug_status` ( `key`, `name`) values ( 'Hang-up', '挂起延期');

-- 缺陷解决方案
insert into `t_bug_solution` ( `key`, `name`) values ( 'Fixed', '已修复');
insert into `t_bug_solution` ( `key`, `name`) values ( 'Can\'t reproduce', '无法复现');
insert into `t_bug_solution` ( `key`, `name`) values ( 'Repeat', '重复Bug');
insert into `t_bug_solution` ( `key`, `name`) values ( 'Not a bug', '不是缺陷');
insert into `t_bug_solution` ( `key`, `name`) values ( 'Designed so', '设计如此');
insert into `t_bug_solution` ( `key`, `name`) values ( 'Requirements so', '需求如此');
insert into `t_bug_solution` ( `key`, `name`) values ( 'other', '其它');

-- 缺陷严重程度
insert into `t_bug_severity` ( `key`, `name`) values ( 'Fatal', '致命');
insert into `t_bug_severity` ( `key`, `name`) values ( 'Critical', '严重');
insert into `t_bug_severity` ( `key`, `name`) values ( 'Normal', '一般');
insert into `t_bug_severity` ( `key`, `name`) values ( 'Minor', '轻微');
insert into `t_bug_severity` ( `key`, `name`) values ( 'Suggestion', '建议');

-- 缺陷优先级
insert into `t_bug_priority` ( `key`, `name`) values ( 'P1', 'P1');
insert into `t_bug_priority` ( `key`, `name`) values ( 'P2', 'P2');
insert into `t_bug_priority` ( `key`, `name`) values ( 'P3', 'P3');
insert into `t_bug_priority` ( `key`, `name`) values ( 'P4', 'P4');
insert into `t_bug_priority` ( `key`, `name`) values ( 'P5', 'P5');

-- 缺陷类型
insert into `t_bug_type` ( `key`, `name`) values ( 'Function', '功能');
insert into `t_bug_type` ( `key`, `name`) values ( 'UI', 'UI');
insert into `t_bug_type` ( `key`, `name`) values ( 'compatible', '兼容适配');
insert into `t_bug_type` ( `key`, `name`) values ( 'Perfor', '性能');
insert into `t_bug_type` ( `key`, `name`) values ( 'interface', '接口');
insert into `t_bug_type` ( `key`, `name`) values ( 'PM', '需求');
insert into `t_bug_type` ( `key`, `name`) values ( 'Design', '设计');
insert into `t_bug_type` ( `key`, `name`) values ( 'Code', '代码');
insert into `t_bug_type` ( `key`, `name`) values ( 'other', '其它');

-- 用户群组
insert into `t_group` ( `group`, `name`, `create_time`, `update_time`) values ( 'admin', '超级管理员', '2018-08-20 15:24:26.000000', '2018-08-20 15:24:29.000000');
insert into `t_group` ( `group`, `name`, `create_time`, `update_time`) values ( 'test', '测试', '2018-08-20 16:57:54.000000', '2018-08-20 16:57:59.000000');
insert into `t_group` ( `group`, `name`, `create_time`, `update_time`) values ( 'developer', '开发', '2018-08-20 17:04:50.000000', '2018-08-20 17:04:52.000000');
insert into `t_group` ( `group`, `name`, `create_time`, `update_time`) values ( 'pm', '产品', '2018-08-20 17:05:05.000000', '2018-08-20 17:05:07.000000');
insert into `t_group` ( `group`, `name`, `create_time`, `update_time`) values ( 'design', '设计', '2018-08-20 17:05:21.000000', '2018-08-20 17:05:23.000000');
insert into `t_group` ( `group`, `name`, `create_time`, `update_time`) values ( 'manager', '领导层', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');