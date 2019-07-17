

-- bug优先级
insert into `bug_priority` ( `key`, `name`,`create_time`, `update_time`) values ( 'P1', 'P1', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `bug_priority` ( `key`, `name`,`create_time`, `update_time`) values ( 'P2', 'P2', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `bug_priority` ( `key`, `name`,`create_time`, `update_time`) values ( 'P3', 'P3', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `bug_priority` ( `key`, `name`,`create_time`, `update_time`) values ( 'P4', 'P4', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `bug_priority` ( `key`, `name`,`create_time`, `update_time`) values ( 'P5', 'P5', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');

-- bug严重程度
insert into `bug_severity` ( `key`, `name`,`create_time`, `update_time`) values ( 'Fatal', '致命', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `bug_severity` ( `key`, `name`,`create_time`, `update_time`) values ( 'Critical', '严重', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `bug_severity` ( `key`, `name`,`create_time`, `update_time`) values ( 'Normal', '一般', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `bug_severity` ( `key`, `name`,`create_time`, `update_time`) values ( 'Minor', '轻微', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `bug_severity` ( `key`, `name`,`create_time`, `update_time`) values ( 'Suggestion', '建议', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');

-- bug解决方案
insert into `bug_solution` ( `key`, `name`,`create_time`, `update_time`) values ( 'Fixed', '已修复', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `bug_solution` ( `key`, `name`,`create_time`, `update_time`) values ( 'Can\'t reproduce', '无法复现', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `bug_solution` ( `key`, `name`,`create_time`, `update_time`) values ( 'Repeat', '重复Bug', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `bug_solution` ( `key`, `name`,`create_time`, `update_time`) values ( 'Not a bug', '不是缺陷', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `bug_solution` ( `key`, `name`,`create_time`, `update_time`) values ( 'Designed so', '设计如此', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `bug_solution` ( `key`, `name`,`create_time`, `update_time`) values ( 'Requirements so', '需求如此', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `bug_solution` ( `key`, `name`,`create_time`, `update_time`) values ( 'other', '其它', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');

-- bug状态
insert into `bug_status` ( `key`, `name`,`create_time`, `update_time`) values ( 'New', '新建未分配', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `bug_status` ( `key`, `name`,`create_time`, `update_time`) values ( 'Open', '待解决', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `bug_status` ( `key`, `name`,`create_time`, `update_time`) values ( 'Closed', '已关闭', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `bug_status` ( `key`, `name`,`create_time`, `update_time`) values ( 'Fixed', '已解决', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `bug_status` ( `key`, `name`,`create_time`, `update_time`) values ( 'Reopen', '重新打开', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `bug_status` ( `key`, `name`,`create_time`, `update_time`) values ( 'Hang-up', '挂起延期', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');

-- bug类型
insert into `bug_type` ( `key`, `name`,`create_time`, `update_time`) values ( 'Function', '功能', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `bug_type` ( `key`, `name`,`create_time`, `update_time`) values ( 'UI', 'UI', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `bug_type` ( `key`, `name`,`create_time`, `update_time`) values ( 'compatible', '兼容适配', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `bug_type` ( `key`, `name`,`create_time`, `update_time`) values ( 'Perfor', '性能', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `bug_type` ( `key`, `name`,`create_time`, `update_time`) values ( 'interface', '接口', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `bug_type` ( `key`, `name`,`create_time`, `update_time`) values ( 'PM', '需求', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `bug_type` ( `key`, `name`,`create_time`, `update_time`) values ( 'Design', '设计', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `bug_type` ( `key`, `name`,`create_time`, `update_time`) values ( 'Code', '代码', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');
insert into `bug_type` ( `key`, `name`,`create_time`, `update_time`) values ( 'other', '其它', '2018-08-20 17:46:48.000000', '2018-08-20 17:46:50.000000');

-- bug来源
insert into `bug_source` ( `key`, `name`, `create_time`, `update_time`) values ( 'tester', '测试发现', '2019-02-16 15:26:52.000000', '2019-02-16 15:26:55.000000');
insert into `bug_source` ( `key`, `name`, `create_time`, `update_time`) values ( 'dev-self-test', '开发自测', '2019-02-16 15:27:35.000000', '2019-02-16 15:27:37.000000');
insert into `bug_source` ( `key`, `name`, `create_time`, `update_time`) values ( 'pm-feedback', '产品人员反馈', '2019-02-16 15:27:59.000000', '2019-02-16 15:28:01.000000');
insert into `bug_source` ( `key`, `name`, `create_time`, `update_time`) values ( 'designer', '设计师反馈', '2019-02-16 15:28:12.000000', '2019-02-16 15:28:14.000000');
insert into `bug_source` ( `key`, `name`, `create_time`, `update_time`) values ( 'online-feedback', '线上用户反馈', '2019-02-16 15:28:29.000000', '2019-02-16 15:28:31.000000');
insert into `bug_source` ( `key`, `name`, `create_time`, `update_time`) values ( 'leader-feedback', '领导反馈', '2019-02-16 15:28:44.000000', '2019-02-16 15:28:46.000000');
