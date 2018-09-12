alter table t_bug comment '缺陷表';
alter table t_bug_history comment '缺陷操作历史表';
alter table t_bug_annex comment '缺陷附件表';
alter table t_bug_type comment '缺陷类型数据';
alter table t_bug_status comment '缺陷状态数据';
alter table t_bug_solution comment '缺陷解决方案数据';
alter table t_bug_severity comment '缺陷严重程度数据';
alter table t_bug_priority comment '缺陷优先级数据';
alter table t_bug_report comment '缺陷报告表';

alter table t_group comment '用户群组表';
alter table t_user comment '用户表';

alter table t_testcase comment '测试用例表';
alter table t_testcase_review comment '测试用例评审表';
alter table t_testsuite_cell comment '测试用例执行表';
alter table t_testsuite comment '测试用例执行集';

alter table t_product comment '产品/项目表';
alter table t_product_members comment '产品/项目成员表';
alter table t_release comment '产品/项目版本表';
alter table t_module_1 comment '一级模块';
alter table t_module_2 comment '二级模块';

alter table t_permissions comment '权限表';
alter table t_permissions_group comment '用户组权限';