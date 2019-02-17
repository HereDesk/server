insert into `t_group` ( `group`, `name`, `create_time`, `update_time`) values ( 'admin', '超级管理员', '2018-08-20 15:24:26.000000', '2018-08-20 15:24:29.000000');
insert into `t_group` ( `group`, `name`, `create_time`, `update_time`) values ( 'test', '测试', '2018-08-20 16:57:54.000000', '2018-08-20 16:57:59.000000');
insert into `t_group` ( `group`, `name`, `create_time`, `update_time`) values ( 'developer', '开发', '2018-08-20 17:04:50.000000', '2018-08-20 17:04:52.000000');
insert into `t_group` ( `group`, `name`, `create_time`, `update_time`) values ( 'pm', '产品', '2018-08-20 17:05:05.000000', '2018-08-20 17:05:07.000000');
insert into `t_group` ( `group`, `name`, `create_time`, `update_time`) values ( 'design', '设计', '2018-08-20 17:05:21.000000', '2018-08-20 17:05:23.000000');
insert into `t_group` ( `group`, `name`, `create_time`, `update_time`) values ( 'manager', '管理层', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `t_group` ( `group`, `name`, `create_time`, `update_time`) values ( 'originator', '产品创建者', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');

# bug优先级
insert into `t_bug_priority` ( `key`, `name`,`create_time`, `update_time`) values ( 'P1', 'P1', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `t_bug_priority` ( `key`, `name`,`create_time`, `update_time`) values ( 'P2', 'P2', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `t_bug_priority` ( `key`, `name`,`create_time`, `update_time`) values ( 'P3', 'P3', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `t_bug_priority` ( `key`, `name`,`create_time`, `update_time`) values ( 'P4', 'P4', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `t_bug_priority` ( `key`, `name`,`create_time`, `update_time`) values ( 'P5', 'P5', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');

# bug严重程度
insert into `t_bug_severity` ( `key`, `name`,`create_time`, `update_time`) values ( 'Fatal', '致命', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `t_bug_severity` ( `key`, `name`,`create_time`, `update_time`) values ( 'Critical', '严重', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `t_bug_severity` ( `key`, `name`,`create_time`, `update_time`) values ( 'Normal', '一般', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `t_bug_severity` ( `key`, `name`,`create_time`, `update_time`) values ( 'Minor', '轻微', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `t_bug_severity` ( `key`, `name`,`create_time`, `update_time`) values ( 'Suggestion', '建议', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');

# bug解决方案
insert into `t_bug_solution` ( `key`, `name`,`create_time`, `update_time`) values ( 'Fixed', '已修复', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `t_bug_solution` ( `key`, `name`,`create_time`, `update_time`) values ( 'Can\'t reproduce', '无法复现', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `t_bug_solution` ( `key`, `name`,`create_time`, `update_time`) values ( 'Repeat', '重复Bug', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `t_bug_solution` ( `key`, `name`,`create_time`, `update_time`) values ( 'Not a bug', '不是缺陷', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `t_bug_solution` ( `key`, `name`,`create_time`, `update_time`) values ( 'Designed so', '设计如此', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `t_bug_solution` ( `key`, `name`,`create_time`, `update_time`) values ( 'Requirements so', '需求如此', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `t_bug_solution` ( `key`, `name`,`create_time`, `update_time`) values ( 'other', '其它', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');

# bug状态
insert into `t_bug_status` ( `key`, `name`,`create_time`, `update_time`) values ( 'New', '新建未分配', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `t_bug_status` ( `key`, `name`,`create_time`, `update_time`) values ( 'Open', '待解决', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `t_bug_status` ( `key`, `name`,`create_time`, `update_time`) values ( 'Closed', '已关闭', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `t_bug_status` ( `key`, `name`,`create_time`, `update_time`) values ( 'Fixed', '已解决', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `t_bug_status` ( `key`, `name`,`create_time`, `update_time`) values ( 'Reopen', '重新打开', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `t_bug_status` ( `key`, `name`,`create_time`, `update_time`) values ( 'Hang-up', '挂起延期', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');

# bug类型
insert into `t_bug_type` ( `key`, `name`,`create_time`, `update_time`) values ( 'Function', '功能', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `t_bug_type` ( `key`, `name`,`create_time`, `update_time`) values ( 'UI', 'UI', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `t_bug_type` ( `key`, `name`,`create_time`, `update_time`) values ( 'compatible', '兼容适配', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `t_bug_type` ( `key`, `name`,`create_time`, `update_time`) values ( 'Perfor', '性能', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `t_bug_type` ( `key`, `name`,`create_time`, `update_time`) values ( 'interface', '接口', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `t_bug_type` ( `key`, `name`,`create_time`, `update_time`) values ( 'PM', '需求', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `t_bug_type` ( `key`, `name`,`create_time`, `update_time`) values ( 'Design', '设计', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `t_bug_type` ( `key`, `name`,`create_time`, `update_time`) values ( 'Code', '代码', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `t_bug_type` ( `key`, `name`,`create_time`, `update_time`) values ( 'other', '其它', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');

# bug来源
insert into `t_bug_source` ( `key`, `name`, `create_time`, `update_time`) values ( 'tester', '测试发现', '2019-02-16 15:26:52.000000', '2019-02-16 15:26:55.000000');
insert into `t_bug_source` ( `key`, `name`, `create_time`, `update_time`) values ( 'dev-self-test', '开发自测', '2019-02-16 15:27:35.000000', '2019-02-16 15:27:37.000000');
insert into `t_bug_source` ( `key`, `name`, `create_time`, `update_time`) values ( 'pm-feedback', '产品人员反馈', '2019-02-16 15:27:59.000000', '2019-02-16 15:28:01.000000');
insert into `t_bug_source` ( `key`, `name`, `create_time`, `update_time`) values ( 'designer', '设计师反馈', '2019-02-16 15:28:12.000000', '2019-02-16 15:28:14.000000');
insert into `t_bug_source` ( `key`, `name`, `create_time`, `update_time`) values ( 'online-feedback', '线上用户反馈', '2019-02-16 15:28:29.000000', '2019-02-16 15:28:31.000000');
insert into `t_bug_source` ( `key`, `name`, `create_time`, `update_time`) values ( 'leader-feedback', '领导反馈', '2019-02-16 15:28:44.000000', '2019-02-16 15:28:46.000000');