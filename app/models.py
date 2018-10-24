# This is an auto-generated Django model module.
# You"ll have to do the following manually to clean this up:
#   * Rearrange models" order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don"t rename db_table values or field names.
from django.db import models
import uuid
import django.utils.timezone as timezone

"""
  系统配置
"""
class SystemConfig(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(u"code",max_length=20)
    code_value = models.IntegerField(u"code值")
    code_desc = models.CharField(u"描述",max_length=100)
    create_time = models.DateTimeField(u"用户创建时间", auto_now_add=True)
    update_time = models.DateTimeField(u"更新时间", auto_now=True)

    class Meta:
        db_table = "t_system_config"

"""
  黑名单IP
"""
class BlacklistIp(models.Model):
    id = models.AutoField(primary_key=True)
    black_uid = models.UUIDField(default=uuid.uuid4, editable=False)
    ip = models.CharField(max_length=30)
    remark = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField(db_column="create_time",auto_now_add=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "t_blacklist_ip"

"""
  keyword filter
"""
class KeywordFilter(models.Model):
    id = models.AutoField(primary_key=True)
    keyword = models.CharField(u"关键字",max_length=30)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "t_keyword_filter"

"""
  用户组
"""
class Group(models.Model):
    id = models.AutoField(primary_key=True)
    group = models.CharField(u"group", unique=True, max_length=20)
    name = models.CharField(u"名称",max_length=50)
    create_time = models.DateTimeField(u"用户创建时间", auto_now_add=True)
    update_time = models.DateTimeField(u"更新时间", auto_now=True)

    class Meta:
        db_table = "t_group"

"""
  用户信息
"""
class User(models.Model):
    user_status = (
        ("1",u"正常"),
        ("2",u"封禁"),
    )
    id = models.AutoField(primary_key=True)
    user_id = models.UUIDField(unique=True,default=uuid.uuid4, editable=False)
    username = models.CharField(u"用户名",max_length=30,blank=True,null=True,default=None)
    email = models.CharField(u"Email",max_length=30,blank=True,null=True,default=None)
    password = models.CharField(u"Password",max_length=200,blank=True,null=True,default=None)
    mobile = models.CharField(u"手机号", max_length=11, null=True, blank=True, default=None)
    user_status = models.IntegerField(u"用户状态",choices=user_status)
    group = models.ForeignKey(Group,to_field="group",on_delete=models.CASCADE,db_column="group")
    realname = models.CharField(u"昵称",max_length=50,null=True,blank=True,default=None)
    position = models.CharField(u"职位",max_length=50,null=True,blank=True,default=None)
    gender = models.IntegerField(u"性别",help_text="性别 0：未知、1：男、2：女",default="0")
    avatarUrl = models.CharField(u"头像",max_length=300,null=True,blank=True,default=None)
    province = models.CharField(u"省份",max_length=20,null=True,blank=True,default=None)
    city = models.CharField(u"城市",max_length=20,null=True,blank=True,default=None)
    source = models.CharField(u"来源",max_length=20,null=True,blank=True,default=None)
    create_time = models.DateTimeField(u"用户创建时间", auto_now_add=True)
    update_time = models.DateTimeField(u"更新时间", auto_now=True)

    class Meta:
        unique_together = ("email", "realname")
        db_table = "t_user"

"""
 token
"""
class Authentication(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="uid")
    token = models.CharField(u"token", max_length=200,default=None)

    class Meta:
        db_table = "t_authentication"

"""
  产品表
"""
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(u"产品名称",max_length=50)
    product_code = models.CharField(u"产品编号",unique=True,max_length=20)
    creator_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="creator_id")
    status = models.IntegerField(u"状态", default=0)
    principal = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="principal",related_name="principal")
    remark = models.CharField(u"备忘",max_length=100,null=True,blank=True,default=None)
    start_time = models.DateTimeField(u"开始日期",null=True,blank=True,default=None)
    end_time = models.DateTimeField(u"结束日期",null=True,blank=True,default=None)
    create_time = models.DateTimeField(u"创建时间",auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "t_product"

"""
  产品组成员
"""
class ProductMembers(models.Model):
    status = (
        ("0", u"启用"),
        ("1", u"禁用"),
    )
    id = models.AutoField(primary_key=True)
    product_code = models.ForeignKey(Product,to_field="product_code",on_delete=models.CASCADE,db_column="product_code")
    member_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="member_id")
    status = models.IntegerField(u"状态",choices=status,default=0)
    join_time = models.DateTimeField(u"创建时间",auto_now_add=True)
    banned_time = models.DateTimeField(u"禁止时间",null=True,blank=True,default=None)
    
    class Meta:
        db_table = "t_product_members"

"""
  产品版本
"""
class Release(models.Model):
    id = models.AutoField(primary_key=True)
    product_code = models.ForeignKey(Product,to_field="product_code",on_delete=models.CASCADE,db_column="product_code")
    version = models.CharField(u"版本记录",max_length=20)
    creator_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="creator_id",related_name="release_creator")
    changer_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="changer_id",null=True,related_name="release_changer")
    deleter_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="deleter_id",null=True,related_name="release_deleter")
    start_time = models.DateTimeField(u"开始日期", null=True, blank=True, default=None)
    online_time = models.DateTimeField(u"预计上线时间", null=True, blank=True, default=None)
    practicalnline_time = models.DateTimeField(u"实际上线时间", null=True, blank=True, default=None)
    create_time = models.DateTimeField(u"创建时间", auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "t_release"

"""
  模块维护
"""
class ModuleA(models.Model):
    isChange = (
        ("0", u"否"),
        ("1", u"是"),
    )
    isDelete = (
        ("0", u"否"),
        ("1", u"是")
    )
    id = models.AutoField(primary_key=True)
    product_code = models.ForeignKey(Product,to_field="product_code",on_delete=models.CASCADE,db_column="product_code")
    m1 = models.CharField(u"模块名称",max_length=200)
    creator_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="creator_id",related_name="module_creator")
    changer_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="changer_id",null=True,related_name="module_changer")
    deleter_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="deleter_id",null=True,related_name="module_deleter")
    isChange = models.IntegerField(u"是否有修改",choices=isChange,default=0)
    isDelete = models.IntegerField(u"是否删除",choices=isDelete,default=0)
    create_time = models.DateTimeField(u"创建时间", auto_now_add=True)
    change_time = models.DateTimeField("修改时间",null=True,blank=True,default=None)
    delete_time = models.DateTimeField("删除时间",null=True,blank=True,default=None)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "t_module_1"

# 二级模块
class ModuleB(models.Model):
    isChange = (
        ("0", u"否"),
        ("1", u"是"),
    )
    isDelete = (
        ("0", u"否"),
        ("1", u"是")
    )
    id = models.AutoField(primary_key=True)
    m1_id = models.ForeignKey(ModuleA,to_field="id",on_delete=models.CASCADE,db_column="ModuleA_ID")
    m2 = models.CharField(u"模块名称",max_length=200)
    creator_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="creator_id",related_name="module_b_creator")
    changer_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="changer_id",null=True,related_name="module_b_changer")
    deleter_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="deleter_id",null=True,related_name="module_b_deleter")
    isChange = models.IntegerField(u"是否有修改",choices=isChange,default=0)
    isDelete = models.IntegerField(u"是否删除",choices=isDelete,default=0)
    create_time = models.DateTimeField(u"创建时间", auto_now_add=True)
    change_time = models.DateTimeField("修改时间",null=True,blank=True,default=None)
    delete_time = models.DateTimeField("删除时间",null=True,blank=True,default=None)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "t_module_2"

"""
  TEST: test case
"""
class TestCase(models.Model):
    isChange = (
        ("0", u"否"),
        ("1", u"是"),
    )
    isDelete = (
        ("0", u"否"),
        ("1", u"是")
    )
    isReview = (
        ("0", u"未评审"),
        ("1", u"评审不通过"),
        ("2", u"评审通过")
    )
    isStatus = (
        ("0", u"有效"),
        ("1", u"无效")
    )
    id = models.AutoField(primary_key=True)
    case_id = models.UUIDField(default=uuid.uuid4,unique=True, editable=False)
    product_code = models.ForeignKey(Product,to_field="product_code",on_delete=models.CASCADE,db_column="product_code")
    m1_id = models.ForeignKey(ModuleA,to_field="id",on_delete=models.CASCADE,null=True,db_column="m1_id")
    m2_id = models.ForeignKey(ModuleB,to_field="id",on_delete=models.CASCADE,null=True,db_column="m2_id")
    category = models.CharField(u"用例分类",max_length=20)
    title = models.TextField(u"用例名称",max_length=500)
    precondition = models.CharField(u"前置条件",max_length=500,null=True,blank=True,default=None)
    DataInput = models.TextField(u"数据输入",max_length=500,null=True,blank=True,default=None)
    steps = models.TextField(u"操作步骤",max_length=5000)
    expected_result = models.TextField(u"预期结果",max_length=500)
    priority = models.CharField(u"优先级:P1,P2,P3",max_length=10,null=True,blank=True,default=None)
    remark = models.TextField(u"备注",max_length=1000)
    creator_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="creator_id",related_name="case_creator")
    changer_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="changer_id",null=True,related_name="case_changer")
    deleter_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="deleter_id",null=True,related_name="case_deleter")
    faller_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="faller_id",null=True,related_name="case_faller")
    isChange = models.IntegerField(u"是否变更",choices=isChange,default=0)
    isDelete = models.IntegerField(u"是否删除",choices=isDelete,default=0)
    isReview = models.IntegerField(u"是否评审",choices=isReview,default=0)
    status = models.IntegerField(u"状态",choices=isStatus,default=0)
    fall_time = models.DateTimeField("失效时间",null=True,blank=True,default=None)
    change_time = models.DateTimeField("变更时间",null=True,blank=True,default=None)
    delete_time = models.DateTimeField("删除时间",null=True,blank=True,default=None)
    create_time = models.DateTimeField(u"创建时间", auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "t_testcase"

"""
  测试用例文件
"""
class TestCaseFiles(models.Model):
    isDelete = (
        ("0", u"否"),
        ("1", u"是")
    )
    id = models.AutoField(primary_key=True)
    case_id = models.ForeignKey(TestCase,to_field="case_id",on_delete=models.CASCADE,db_column="case_id")
    file_path = models.CharField(u"路径",max_length=200)
    isDelete = models.IntegerField(u"是否删除",choices=isDelete,default=0)
    create_time = models.DateTimeField(u"创建时间", auto_now_add=True)

    class Meta:
        db_table = "t_testcase_files"
        
"""
  TEST: test case suite version
"""
class TestSuite(models.Model):
    id = models.AutoField(primary_key=True)
    suite_id = models.UUIDField(default=uuid.uuid4,unique=True, editable=False)
    product_code = models.ForeignKey(Product,to_field="product_code",on_delete=models.CASCADE,db_column="product_code")
    suite_name = models.CharField(u"名称",max_length=30)
    creator_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="creator_id")
    create_time = models.DateTimeField(u"创建时间", auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "t_testsuite"

"""
  Test: Test case suite cell
"""
class TestSuiteCell(models.Model):
    result = (
        ("0", u"未执行"),
        ("1", u"成功"),
        ("-1", u"失败"),
    )
    id = models.AutoField(primary_key=True)
    cell_id = models.UUIDField(default=uuid.uuid4,unique=True, editable=False)
    result = models.IntegerField(u"结果",choices=result,default=0)
    suite_id = models.ForeignKey(TestSuite, to_field="suite_id", on_delete=models.CASCADE,db_column="suite_id")
    case_id = models.ForeignKey(TestCase, to_field="case_id", on_delete=models.CASCADE,db_column="case_id")
    run_time = models.DateTimeField(u"运行时间",null=True,blank=True,default=None)
    runner_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="runner_id",null=True,related_name="cell_runner_id")
    creator_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="creator_id",related_name="cell_creator_id")
    create_time = models.DateTimeField(u"创建时间", auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "t_testsuite_cell"


"""
 testcase review
"""
class TestCaseReview(models.Model):
    isReview = (
        ("0", u"评审未通过"),
        ("1", u"评审通过"),
    )
    id = models.AutoField(primary_key=True)
    case_id = models.ForeignKey(TestCase,to_field="case_id",on_delete=models.CASCADE,db_column="case_id")
    result = models.IntegerField(u"是否评审",choices=isReview,default=0)
    remark = models.CharField(u"评审意见",max_length=2000,null=True,blank=True,default=None)
    user_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="user_id")
    create_time = models.DateTimeField(u"创建时间", auto_now_add=True)

    class Meta:
        db_table = "t_testcase_review"


"""
  bug 类型
"""
class BugType(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.CharField(u"bug类型",unique=True,max_length=10)
    name = models.CharField(u"bug状态说明",max_length=20,null=True,blank=True,default=None)

    class Meta:
        db_table = "t_bug_type"

"""
  bug 状态
"""
class BugStatus(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.CharField(u"bug状态",unique=True,max_length=15)
    name = models.CharField(u"bug状态说明",max_length=20,null=True,blank=True,default=None)

    class Meta:
        db_table = "t_bug_status"

"""
  bug 优先级
"""
class BugPriority(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.CharField(u"bug优先级",unique=True,max_length=15)
    name = models.CharField(u"bug优先级说明",max_length=20)

    class Meta:
        db_table = "t_bug_priority"

"""
  bug 严重程度
"""
class BugSeverity(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.CharField(u"bug严重程度",unique=True,max_length=15)
    name = models.CharField(u"bug严重程度说明",max_length=20,null=True,blank=True,default=None)

    class Meta:
        db_table = "t_bug_severity"

"""
  bug 解决方案
"""
class BugSolution(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.CharField(u"bug修复方案",unique=True,max_length=15)
    name = models.CharField(u"bug严重程度说明",max_length=20,null=True,blank=True,default=None)

    class Meta:
        db_table = "t_bug_solution"

"""
  bug
"""
class Bug(models.Model):
    isDelete = (
        ("0", u"否"),
        ("1", u"是")
    )
    id = models.AutoField(primary_key=True)
    bug_id = models.UUIDField(default=uuid.uuid4, unique=True,editable=False)
    product_code = models.ForeignKey(Product,to_field="product_code",on_delete=models.CASCADE,db_column="product_code",related_name="bug_product_code")
    version_id = models.ForeignKey(Release,to_field="id",on_delete=models.CASCADE,db_column="versionId")
    title = models.CharField(u"Bug标题",max_length=100)
    steps = models.CharField(u"步骤",max_length=1000)
    reality_result = models.CharField(u"实际结果",max_length=500)
    expected_result = models.CharField(u"预期",max_length=500)
    remark = models.CharField(u"备注",null=True,blank=True,default=None,max_length=1000)
    bug_type = models.ForeignKey(BugType,to_field="key",on_delete=models.CASCADE,null=True,db_column="bug_type",related_name="bug_type_key")
    status = models.ForeignKey(BugStatus,to_field="key",on_delete=models.CASCADE,db_column="status",default="Open")
    priority = models.ForeignKey(BugPriority,to_field="key",on_delete=models.CASCADE,db_column="priority")
    severity = models.ForeignKey(BugSeverity,to_field="key",on_delete=models.CASCADE,db_column="severity")
    creator_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="creator_id",related_name="openedBy")
    create_time = models.DateTimeField(u"创建时间", auto_now_add=True)
    assignedTo_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="assignedTo_id",related_name="assignedTo",null=True)
    assignedTo_time = models.DateTimeField(u"分配时间", auto_now_add=True)
    fixed_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="fixed_id",null=True,related_name="resolvedBy")
    fixed_time = models.DateTimeField(u"解决时间",null=True,blank=True,default=None)
    solution = models.ForeignKey(BugSolution,to_field="key",null=True,on_delete=models.CASCADE,db_column="solution")
    closed_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="closed_id",null=True,related_name="closedBy")
    closed_time = models.DateTimeField(u"关闭时间",null=True,blank=True,default=None)
    hangUp_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="hangUp_id",null=True,related_name="hangUpBy")
    hangUp_time = models.DateTimeField(u"挂起时间",null=True,blank=True,default=None)
    isDelete = models.IntegerField(u"是否删除",choices=isDelete,default=0)
    delete_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="delete_id",null=True,related_name="DeleteBy")
    delete_time = models.DateTimeField("删除时间",null=True,blank=True,default=None)
    last_Time = models.DateTimeField(u"最后一次操作时间",auto_now=True)
    case_id = models.ForeignKey(TestCase,to_field="case_id",on_delete=models.CASCADE,db_column="case_id",null=True)
    cell_id = models.ForeignKey(TestSuiteCell,to_field="cell_id",on_delete=models.CASCADE,db_column="cell_id",null=True,related_name="suite_cell_id")
    m1_id = models.ForeignKey(ModuleA,to_field="id",on_delete=models.CASCADE,null=True,db_column="m1_id")
    m2_id = models.ForeignKey(ModuleB,to_field="id",on_delete=models.CASCADE,null=True,db_column="m2_id")

    class Meta:
        db_table = "t_bug"

"""
  bug 附件
"""
class BugAnnex(models.Model):
    isDelete = (
        ("0", u"否"),
        ("1", u"是")
    )
    id = models.AutoField(primary_key=True)
    bug_id = models.ForeignKey(Bug,to_field="bug_id",on_delete=models.CASCADE,db_column="bug_id")
    url = models.CharField(u"路径",max_length=100)
    create_time = models.DateTimeField(u"创建时间", auto_now_add=True)
    isDelete = models.IntegerField(u"是否删除",choices=isDelete,default=0)

    class Meta:
        db_table = "t_bug_annex"

"""
 bug report
"""
class BugReport(models.Model):
    id = models.AutoField(primary_key=True)
    report_id = models.UUIDField(default=uuid.uuid4, unique=True,editable=False)
    create_time = models.DateTimeField(u"创建时间", auto_now_add=True)
    content = models.TextField(max_length=100000)

    class Meta:
        db_table = "t_bug_report"

"""
  bug history
"""
class BugHistory(models.Model):
    id = models.AutoField(primary_key=True)
    bug_id = models.ForeignKey(Bug,to_field="bug_id",on_delete=models.CASCADE,db_column="bug_id")
    user_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="user_id",null=True)
    desc = models.CharField(u"说明",max_length=1000)
    remark = models.CharField(u"备注",null=True,blank=True,default=None,max_length=2000)
    create_time = models.DateTimeField(u"创建时间", auto_now_add=True)

    class Meta:
        db_table = "t_bug_history"

"""
  用户的log
"""
class LoggedLog(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,null=True,db_column="user_id")
    ip = models.CharField(u"ip",blank=True,null=True,default=None,max_length=20)
    path = models.CharField(u"path",blank=True,null=True,default=None,max_length=200)
    method = models.CharField(u"method",blank=True,null=True,default=None,max_length=20)
    request = models.CharField(u"请求内容",blank=True,null=True,default=None,max_length=10000)
    platform = models.CharField(u"平台",max_length=200,blank=True,null=True,default=None)
    browser = models.CharField(u"浏览器", max_length=200, blank=True, null=True, default=None)
    create_time = models.DateTimeField(u"创建时间", auto_now_add=True)
    update_time = models.DateTimeField(u"更新时间", auto_now=True)

    class Meta:
        db_table = "t_logged_log"

"""
  权限
"""
class Api(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, unique=True,editable=False)
    api_name = models.CharField(u"权限名称",unique=True,max_length=100)
    api_code = models.CharField(u"权限code",unique=True,max_length=200)
    url = models.CharField(max_length=200)
    flag = models.CharField(u"标记",max_length=200)
    create_time = models.DateTimeField(u"创建时间", auto_now_add=True)

    class Meta:
        db_table = "t_api"

"""
  权限
"""
class ApiPermissions(models.Model):
    is_allow = (
        ("-1", u"不允许"),
        ("1", u"允许")
    )
    id = models.AutoField(primary_key=True)
    api_id = models.ForeignKey(Api,to_field="id",on_delete=models.CASCADE,db_column="api_id")
    group = models.ForeignKey(Group,to_field="group",on_delete=models.CASCADE,db_column="group")
    is_allow = models.IntegerField(choices=is_allow,default=1)
    create_time = models.DateTimeField(u"创建时间", auto_now_add=True)

    class Meta:
        db_table = "t_api_permissions"


"""
  权限
"""
class Pages(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, unique=True,editable=False)
    page_name = models.CharField(u"页面名称",unique=True,max_length=100)
    page_url = models.CharField(u"页面url",max_length=200,unique=True)
    flag = models.CharField(u"标记",max_length=200)
    create_time = models.DateTimeField(u"创建时间", auto_now_add=True)

    class Meta:
        db_table = "t_pages"

"""
  权限
"""
class PagesPermissions(models.Model):
    is_allow = (
        ("-1", u"不允许"),
        ("1", u"允许")
    )
    id = models.AutoField(primary_key=True)
    page_id = models.ForeignKey(Pages,to_field="id",on_delete=models.CASCADE,db_column="page_id")
    group = models.ForeignKey(Group,to_field="group",on_delete=models.CASCADE,db_column="group")
    is_allow = models.IntegerField(choices=is_allow,default=1)
    create_time = models.DateTimeField(u"创建时间", auto_now_add=True)

    class Meta:
        db_table = "t_pages_permissions"