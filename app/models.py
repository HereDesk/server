# This is an auto-generated Django model module.
# You"ll have to do the following manually to clean this up:
#   * Rearrange models" order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don"t rename db_table values or field names.
from django.db import models
from jsonfield import JSONField
import uuid
import django.utils.timezone as timezone

"""
  系统配置
"""
class SystemConfig(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(u"code",max_length=20)
    code_value = models.CharField(u"code值",max_length=100)
    code_desc = models.CharField(u"描述",max_length=100)
    create_time = models.DateTimeField(u"用户创建时间", auto_now_add=True)
    update_time = models.DateTimeField(u"更新时间", auto_now=True)

    class Meta:
        db_table = "system_config"

"""
  黑名单IP
"""
class SystemBlacklistIp(models.Model):
    id = models.AutoField(primary_key=True)
    black_uid = models.UUIDField(default=uuid.uuid4, editable=False)
    ip = models.CharField(max_length=30)
    remark = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField(db_column="create_time",auto_now_add=True)
    update_time = models.DateTimeField(u"更新时间", auto_now=True)

    class Meta:
        managed = False
        db_table = "system_blacklist_ip"

"""
  keyword filter
"""
class SystemKeywordFilter(models.Model):
    id = models.AutoField(primary_key=True)
    keyword = models.CharField(u"关键字",max_length=30)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(u"更新时间", auto_now=True)

    class Meta:
        db_table = "system_keyword_filter"

"""
  keyword filter
"""
class UserPosition(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.CharField(u"职业",max_length=30)
    name = models.CharField(u"职业",max_length=30)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(u"更新时间", auto_now=True)

    class Meta:
        db_table = "user_position"

"""
  用户组
"""
class UserRole(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.CharField(u"role", unique=True, max_length=20)
    name = models.CharField(u"名称",max_length=50)
    create_time = models.DateTimeField(u"用户创建时间", auto_now_add=True)
    update_time = models.DateTimeField(u"更新时间", auto_now=True)

    class Meta:
        db_table = "user_role"

"""
  用户信息
"""
class User(models.Model):
    user_status = (
        ("1",u"正常"),
        ("2",u"封禁"),
    )
    identity = (
        ("0",u"超级管理员"),
        ("1",u"普通用户"),
    )
    id = models.AutoField(primary_key=True)
    user_id = models.UUIDField(unique=True,default=uuid.uuid4, editable=False)
    username = models.CharField(u"用户名",max_length=30,blank=True,null=True,default=None)
    email = models.CharField(u"Email",max_length=30,blank=True,null=True,default=None)
    password = models.CharField(u"Password",max_length=200,blank=True,null=True,default=None)
    mobile = models.CharField(u"手机号", max_length=11, null=True, blank=True, default=None)
    user_status = models.IntegerField(u"用户状态",choices=user_status)
    realname = models.CharField(u"昵称",max_length=50,null=True,blank=True,default=None)
    position = models.CharField(u"职位",max_length=50,null=True,blank=True,default=None)
    gender = models.IntegerField(u"性别",help_text="性别 0：未知、1：男、2：女",default="0")
    avatarUrl = models.CharField(u"头像",max_length=300,null=True,blank=True,default=None)
    province = models.CharField(u"省份",max_length=20,null=True,blank=True,default=None)
    city = models.CharField(u"城市",max_length=20,null=True,blank=True,default=None)
    source = models.CharField(u"来源",max_length=20,null=True,blank=True,default=None)
    identity = models.IntegerField(u"用户身份",choices=identity)
    create_time = models.DateTimeField(u"用户创建时间", auto_now_add=True)
    update_time = models.DateTimeField(u"更新时间", auto_now=True)

    class Meta:
        unique_together = ("email", "realname")
        db_table = "user"

"""
  team
"""
class Team(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, unique=True,editable=False)
    team_name = models.CharField(u"团队名称",max_length=100)
    creator_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="creator_id")
    create_time = models.DateTimeField(u"用户创建时间", auto_now_add=True)
    update_time = models.DateTimeField(u"更新时间", auto_now=True)

    class Meta:
        db_table = "team"

"""
  team成员
"""
class TeamMembers(models.Model):
    status = (
        ("0", u"启用"),
        ("1", u"禁用"),
    )
    id = models.AutoField(primary_key=True)
    team_id = models.ForeignKey(Team,to_field="id",on_delete=models.CASCADE,null=True,default=None,db_column="team_id")
    user_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="user_id")
    status = models.IntegerField(u"状态",choices=status,default=0)
    join_time = models.DateTimeField(u"创建时间",auto_now_add=True)
    banned_time = models.DateTimeField(u"禁止时间",null=True,blank=True,default=None)
    update_time = models.DateTimeField(u"更新时间", auto_now=True)

    class Meta:
        db_table = "team_members"

"""
 token
"""
class Authentication(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="uid")
    token = models.CharField(u"token", max_length=200,default=None)
    create_time = models.DateTimeField(u"用户创建时间", auto_now_add=True)
    update_time = models.DateTimeField(u"更新时间", auto_now=True)

    class Meta:
        db_table = "user_authentication"

"""
  user config
"""
class UserConfig(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(u"code",max_length=20)
    code_value = models.CharField(u"code值",max_length=100)
    code_desc = models.CharField(u"描述",max_length=100)
    user_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="user_id")
    create_time = models.DateTimeField(u"用户创建时间", auto_now_add=True)
    update_time = models.DateTimeField(u"更新时间", auto_now=True)

    class Meta:
        db_table = "user_config"

"""
  产品表
"""
class Product(models.Model):
    is_change = (
        ("0", u"否"),
        ("1", u"是"),
    )
    id = models.AutoField(primary_key=True)
    product_id = models.UUIDField(default=uuid.uuid4, unique=True,editable=False)
    product_name = models.CharField(u"产品名称",max_length=50)
    product_code = models.CharField(u"产品编号或简称",unique=True,max_length=20)
    creator_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="creator_id")
    status = models.IntegerField(u"状态", default=0)
    principal = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="principal",related_name="principal")
    remark = models.CharField(u"备忘",max_length=100,null=True,blank=True,default=None)
    is_change = models.IntegerField(u"是否变更",choices=is_change,default=0)
    start_time = models.DateTimeField(u"开始日期",null=True,blank=True,default=None)
    end_time = models.DateTimeField(u"结束日期",null=True,blank=True,default=None)
    create_time = models.DateTimeField(u"创建时间",auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "product"

"""
  产品组成员
"""
class ProductMembers(models.Model):
    status = (
        ("0", u"启用"),
        ("1", u"禁用"),
    )
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product,to_field="product_id",on_delete=models.CASCADE,db_column="product_id")
    member_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="member_id")
    user_role = models.ForeignKey(UserRole,to_field="role",on_delete=models.CASCADE,db_column="user_role")
    status = models.IntegerField(u"状态",choices=status,default=0)
    join_time = models.DateTimeField(u"创建时间",auto_now_add=True)
    banned_time = models.DateTimeField(u"禁止时间",null=True,blank=True,default=None)

    class Meta:
        db_table = "product_members"

"""
  产品版本
"""
class Release(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product,to_field="product_id",on_delete=models.CASCADE,db_column="product_id")
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
        db_table = "product_release"

"""
  模块维护
"""
class ModuleA(models.Model):
    is_change = (
        ("0", u"否"),
        ("1", u"是"),
    )
    is_delete = (
        ("0", u"否"),
        ("1", u"是")
    )
    id = models.AutoField(primary_key=True)
    m1_id = models.UUIDField(unique=True,default=uuid.uuid4, editable=False)
    product_id = models.ForeignKey(Product,to_field="product_id",on_delete=models.CASCADE,db_column="product_id")
    m1_name = models.CharField(u"模块名称",max_length=200)
    creator_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="creator_id",related_name="module_creator")
    changer_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="changer_id",null=True,related_name="module_changer")
    deleter_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="deleter_id",null=True,related_name="module_deleter")
    is_change = models.IntegerField(u"是否有修改",choices=is_change,default=0)
    is_delete = models.IntegerField(u"是否删除",choices=is_delete,default=0)
    create_time = models.DateTimeField(u"创建时间", auto_now_add=True)
    change_time = models.DateTimeField("修改时间",null=True,blank=True,default=None)
    delete_time = models.DateTimeField("删除时间",null=True,blank=True,default=None)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "product_module_1"

# 二级模块
class ModuleB(models.Model):
    is_change = (
        ("0", u"否"),
        ("1", u"是"),
    )
    is_delete = (
        ("0", u"否"),
        ("1", u"是")
    )
    id = models.AutoField(primary_key=True)
    m2_id = models.UUIDField(unique=True,default=uuid.uuid4, editable=False)
    m1_id = models.ForeignKey(ModuleA,to_field="m1_id",on_delete=models.CASCADE,db_column="m1_id")
    m2_name = models.CharField(u"模块名称",max_length=200)
    creator_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="creator_id",related_name="module_b_creator")
    changer_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="changer_id",null=True,related_name="module_b_changer")
    deleter_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="deleter_id",null=True,related_name="module_b_deleter")
    is_change = models.IntegerField(u"是否有修改",choices=is_change,default=0)
    is_delete = models.IntegerField(u"是否删除",choices=is_delete,default=0)
    create_time = models.DateTimeField(u"创建时间", auto_now_add=True)
    change_time = models.DateTimeField("修改时间",null=True,blank=True,default=None)
    delete_time = models.DateTimeField("删除时间",null=True,blank=True,default=None)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "product_module_2"

"""
  TEST: test case
"""
class TestCase(models.Model):
    is_change = (
        ("0", u"否"),
        ("1", u"是"),
    )
    is_delete = (
        ("0", u"否"),
        ("1", u"是")
    )
    is_review = (
        ("0", u"未评审"),
        ("1", u"评审不通过"),
        ("2", u"评审通过")
    )
    is_status = (
        ("0", u"有效"),
        ("1", u"无效")
    )
    case_id = models.UUIDField(default=uuid.uuid4,unique=True, editable=False,primary_key=True)
    id = models.IntegerField(u"测试用例辅助id",default=None)
    case_sn = models.CharField(u"用户自定义用例编号",max_length=20,null=True,blank=True,default=None)
    product_id = models.ForeignKey(Product,to_field="product_id",on_delete=models.CASCADE,db_column="product_id")
    m1_id = models.ForeignKey(ModuleA,to_field="m1_id",on_delete=models.CASCADE,null=True,db_column="m1_id")
    m2_id = models.ForeignKey(ModuleB,to_field="m2_id",on_delete=models.CASCADE,null=True,db_column="m2_id")
    category = models.CharField(u"用例分类",max_length=20)
    title = models.TextField(u"用例名称",max_length=500)
    precondition = models.CharField(u"前置条件",max_length=10000,null=True,blank=True,default=None)
    DataInput = models.TextField(u"数据输入",max_length=10000,null=True,blank=True,default=None)
    steps = models.TextField(u"操作步骤",max_length=100000)
    expected_result = models.TextField(u"预期结果",max_length=100000)
    priority = models.CharField(u"优先级:P1,P2,P3",max_length=10,null=True,blank=True,default=None)
    remark = models.TextField(u"备注",max_length=100000)
    creator_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="creator_id",related_name="case_creator")
    changer_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="changer_id",null=True,related_name="case_changer")
    deleter_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="deleter_id",null=True,related_name="case_deleter")
    faller_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="faller_id",null=True,related_name="case_faller")
    is_change = models.IntegerField(u"是否变更",choices=is_change,default=0)
    is_delete = models.IntegerField(u"是否删除",choices=is_delete,default=0)
    is_review = models.IntegerField(u"是否评审",choices=is_review,default=0)
    status = models.IntegerField(u"状态",choices=is_status,default=0)
    fall_time = models.DateTimeField("失效时间",null=True,blank=True,default=None)
    change_time = models.DateTimeField("变更时间",null=True,blank=True,default=None)
    delete_time = models.DateTimeField("删除时间",null=True,blank=True,default=None)
    create_time = models.DateTimeField(u"创建时间", auto_now_add=True)
    last_operation = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="last_operation",null=True,related_name="case_last_operation")
    last_time = models.DateTimeField(u"最后一次操作时间",auto_now=True)

    class Meta:
        db_table = "testcase"

"""
  测试用例文件
"""
class TestCaseFiles(models.Model):
    is_delete = (
        ("0", u"否"),
        ("1", u"是")
    )
    id = models.AutoField(primary_key=True)
    case_id = models.ForeignKey(TestCase,to_field="case_id",on_delete=models.CASCADE,db_column="case_id")
    url = models.CharField(u"路径",max_length=200)
    is_delete = models.IntegerField(u"是否删除",choices=is_delete,default=0)
    create_time = models.DateTimeField(u"创建时间", auto_now_add=True)

    class Meta:
        db_table = "testcase_files"

"""
  TEST: test case suite version
"""
class TestSuite(models.Model):
    id = models.AutoField(primary_key=True)
    suite_id = models.UUIDField(default=uuid.uuid4,unique=True, editable=False)
    product_id = models.ForeignKey(Product,to_field="product_id",on_delete=models.CASCADE,db_column="product_id")
    suite_name = models.CharField(u"名称",max_length=30)
    creator_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="creator_id")
    create_time = models.DateTimeField(u"创建时间", auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "testsuite"

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
        db_table = "testsuite_cell"


"""
 testcase review
"""
class TestCaseReview(models.Model):
    is_review = (
        ("0", u"评审未通过"),
        ("1", u"评审通过"),
    )
    id = models.AutoField(primary_key=True)
    case_id = models.ForeignKey(TestCase,to_field="case_id",on_delete=models.CASCADE,db_column="case_id")
    result = models.IntegerField(u"是否评审",choices=is_review,default=0)
    remark = models.CharField(u"评审意见",max_length=2000,null=True,blank=True,default=None)
    user_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="user_id")
    create_time = models.DateTimeField(u"创建时间", auto_now_add=True)
    update_time = models.DateTimeField(u"更新时间", auto_now=True)

    class Meta:
        db_table = "testcase_review"


"""
  testcase history
"""
class TestCaseHistory(models.Model):
    id = models.AutoField(primary_key=True)
    case_id = models.ForeignKey(TestCase,to_field="case_id",on_delete=models.CASCADE,db_column="case_id")
    user_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="user_id",null=True)
    desc = models.TextField(u"说明",max_length=10000)
    remark = models.CharField(u"备注",null=True,blank=True,default=None,max_length=2000)
    create_time = models.DateTimeField(u"创建时间", auto_now_add=True)
    update_time = models.DateTimeField(u"更新时间", auto_now=True)

    class Meta:
        db_table = "testcase_history"

"""
  bug 类型
"""
class BugType(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.CharField(u"bug类型",unique=True,max_length=10)
    name = models.CharField(u"bug状态说明",max_length=20,null=True,blank=True,default=None)
    create_time = models.DateTimeField(u"用户创建时间", auto_now_add=True)
    update_time = models.DateTimeField(u"更新时间", auto_now=True)

    class Meta:
        db_table = "bug_type"

"""
  bug 状态
"""
class BugStatus(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.CharField(u"bug状态",unique=True,max_length=15)
    name = models.CharField(u"bug状态说明",max_length=20,null=True,blank=True,default=None)
    create_time = models.DateTimeField(u"用户创建时间", auto_now_add=True)
    update_time = models.DateTimeField(u"更新时间", auto_now=True)

    class Meta:
        db_table = "bug_status"

"""
  bug 优先级
"""
class BugPriority(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.CharField(u"bug优先级",unique=True,max_length=15)
    name = models.CharField(u"bug优先级说明",max_length=20,null=True,blank=True,default=None)
    create_time = models.DateTimeField(u"用户创建时间", auto_now_add=True)
    update_time = models.DateTimeField(u"更新时间", auto_now=True)

    class Meta:
        db_table = "bug_priority"

"""
  bug 来源
"""
class BugSource(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.CharField(u"bug来源",unique=True,max_length=15)
    name = models.CharField(u"bug来源说明",max_length=20,null=True,blank=True,default=None)
    create_time = models.DateTimeField(u"用户创建时间", auto_now_add=True)
    update_time = models.DateTimeField(u"更新时间", auto_now=True)

    class Meta:
        db_table = "bug_source"

"""
  bug 严重程度
"""
class BugSeverity(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.CharField(u"bug严重程度",unique=True,max_length=15)
    name = models.CharField(u"bug严重程度说明",max_length=20,null=True,blank=True,default=None)
    create_time = models.DateTimeField(u"用户创建时间", auto_now_add=True)
    update_time = models.DateTimeField(u"更新时间", auto_now=True)

    class Meta:
        db_table = "bug_severity"

"""
  bug 解决方案
"""
class BugSolution(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.CharField(u"bug修复方案",unique=True,max_length=15)
    name = models.CharField(u"bug严重程度说明",max_length=20,null=True,blank=True,default=None)
    create_time = models.DateTimeField(u"用户创建时间", auto_now_add=True)
    update_time = models.DateTimeField(u"更新时间", auto_now=True)

    class Meta:
        db_table = "bug_solution"

"""
  bug
"""
class Bug(models.Model):
    is_delete = (
        ("0", u"否"),
        ("1", u"是")
    )
    bug_id = models.UUIDField(default=uuid.uuid4, unique=True,editable=False,primary_key=True)
    id = models.IntegerField(u"辅助id",default=None)
    product_id = models.ForeignKey(Product,to_field="product_id",on_delete=models.CASCADE,db_column="product_id",related_name="bug_product_id")
    m1_id = models.ForeignKey(ModuleA,to_field="m1_id",on_delete=models.CASCADE,null=True,db_column="m1_id")
    m2_id = models.ForeignKey(ModuleB,to_field="m2_id",on_delete=models.CASCADE,null=True,db_column="m2_id")
    version_id = models.ForeignKey(Release,to_field="id",on_delete=models.CASCADE,db_column="versionId")
    case_id = models.ForeignKey(TestCase,to_field="case_id",on_delete=models.CASCADE,db_column="case_id",null=True)
    cell_id = models.ForeignKey(TestSuiteCell,to_field="cell_id",on_delete=models.CASCADE,db_column="cell_id",null=True,related_name="suite_cell_id")
    bug_label = models.CharField(u"自定义标签",null=True,blank=True,default=None,max_length=1000)
    environment = models.CharField(u"环境",null=True,blank=True,default=None,max_length=500)
    title = models.CharField(u"Bug标题",max_length=100)
    steps = models.TextField(u"步骤",max_length=100000)
    reality_result = models.TextField(u"实际结果",max_length=100000)
    expected_result = models.TextField(u"预期结果",max_length=100000)
    remark = models.CharField(u"备注",null=True,blank=True,default=None,max_length=10000)
    bug_type = models.ForeignKey(BugType,to_field="key",on_delete=models.CASCADE,null=True,db_column="bug_type",related_name="bug_type_key")
    status = models.ForeignKey(BugStatus,to_field="key",on_delete=models.CASCADE,db_column="status",default="Open")
    bug_source = models.ForeignKey(BugSource,to_field="key",null=True,on_delete=models.CASCADE,db_column="bug_source")
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
    is_delete = models.IntegerField(u"是否删除",choices=is_delete,default=0)
    delete_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="delete_id",null=True,related_name="DeleteBy")
    delete_time = models.DateTimeField("删除时间",null=True,blank=True,default=None)
    last_time = models.DateTimeField(u"最后一次操作时间",auto_now=True)
    last_operation = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="last_operation",null=True,related_name="last_operation")

    class Meta:
        db_table = "bug"

"""
  bug 附件
"""
class BugAnnex(models.Model):
    is_delete = (
        ("0", u"否"),
        ("1", u"是")
    )
    id = models.AutoField(primary_key=True)
    bug_id = models.ForeignKey(Bug,to_field="bug_id",on_delete=models.CASCADE,db_column="bug_id")
    url = models.CharField(u"路径",max_length=100)
    is_delete = models.IntegerField(u"是否删除",choices=is_delete,default=0)
    create_time = models.DateTimeField(u"创建时间", auto_now_add=True)
    update_time = models.DateTimeField(u"更新时间", auto_now=True)

    class Meta:
        db_table = "bug_annex"

"""
 bug report
"""
class BugReport(models.Model):
    id = models.AutoField(primary_key=True)
    report_id = models.UUIDField(default=uuid.uuid4, unique=True,editable=False)
    content = models.TextField(max_length=100000)
    create_time = models.DateTimeField(u"创建时间", auto_now_add=True)
    update_time = models.DateTimeField(u"更新时间", auto_now=True)

    class Meta:
        db_table = "bug_report"

"""
  bug history
"""
class BugHistory(models.Model):
    remark_status = (
        ("0", u"删除"),
        ("1", u"新建"),
        ("2", u"修改")
    )
    id = models.AutoField(primary_key=True)
    record_id = models.UUIDField(default=uuid.uuid4, unique=True,editable=False)
    bug_id = models.ForeignKey(Bug,to_field="bug_id",on_delete=models.CASCADE,db_column="bug_id")
    user_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="user_id",null=True)
    desc = models.TextField(u"说明",max_length=10000)
    remark = models.CharField(u"备注",null=True,blank=True,default=None,max_length=2000)
    remark_status = models.IntegerField(u"备注状态",choices=remark_status,default=1)
    create_time = models.DateTimeField(u"创建时间", auto_now_add=True)
    update_time = models.DateTimeField(u"更新时间", auto_now=True)

    class Meta:
        db_table = "bug_history"

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
        db_table = "logged_log"

"""
  用户的log
"""
class UserLog(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,null=True,db_column="user_id")
    ip = models.CharField(u"ip",blank=True,null=True,default=None,max_length=20)
    flag = models.CharField(u"说明",max_length=200,blank=True,null=True,default=None)
    create_time = models.DateTimeField(u"创建时间", auto_now_add=True)
    update_time = models.DateTimeField(u"更新时间", auto_now=True)

    class Meta:
        db_table = "user_log"

"""
  api
"""
class Api(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, unique=True,editable=False)
    api_name = models.CharField(u"权限名称",unique=True,max_length=100)
    api_code = models.CharField(u"权限code",unique=True,max_length=200)
    url = models.CharField(max_length=200)
    flag = models.CharField(u"标记",max_length=200)
    desc = models.CharField(u"介绍说明",max_length=500,null=True,default=None)
    create_time = models.DateTimeField(u"创建时间", auto_now_add=True)
    update_time = models.DateTimeField(u"更新时间", auto_now=True)

    class Meta:
        db_table = "api"

"""
  api权限
"""
class ApiPermissions(models.Model):
    is_allow = (
        ("-1", u"不允许"),
        ("1", u"允许")
    )
    id = models.AutoField(primary_key=True)
    api_id = models.ForeignKey(Api,to_field="id",on_delete=models.CASCADE,db_column="api_id")
    user_role = models.ForeignKey(UserRole,to_field="role",on_delete=models.CASCADE,db_column="user_role")
    is_allow = models.IntegerField(choices=is_allow,default=1)
    create_time = models.DateTimeField(u"创建时间", auto_now_add=True)
    update_time = models.DateTimeField(u"更新时间", auto_now=True)

    class Meta:
        db_table = "api_permissions"


"""
  前端页面
"""
class Pages(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, unique=True,editable=False)
    page_name = models.CharField(u"页面名称",unique=True,max_length=100)
    page_url = models.CharField(u"页面url",max_length=200,unique=True)
    flag = models.CharField(u"标记",max_length=200)
    desc = models.CharField(u"介绍说明",max_length=500,null=True,default=None)
    create_time = models.DateTimeField(u"创建时间", auto_now_add=True)
    update_time = models.DateTimeField(u"更新时间", auto_now=True)

    class Meta:
        db_table = "pages"

"""
  前端页面权限
"""
class PagesPermissions(models.Model):
    is_allow = (
        ("-1", u"不允许"),
        ("1", u"允许")
    )
    id = models.AutoField(primary_key=True)
    page_id = models.ForeignKey(Pages,to_field="id",on_delete=models.CASCADE,db_column="page_id")
    user_role = models.ForeignKey(UserRole,to_field="role",on_delete=models.CASCADE,db_column="user_role")
    is_allow = models.IntegerField(choices=is_allow,default=1)
    create_time = models.DateTimeField(u"创建时间", auto_now_add=True)
    update_time = models.DateTimeField(u"更新时间", auto_now=True)

    class Meta:
        db_table = "pages_permissions"

"""
  文件
"""
class Files(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(u"路径",max_length=100)
    file_format = models.CharField(u"文件格式",max_length=100)
    original_name = models.CharField(u"文件名称",max_length=100)
    user_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,null=True,db_column="user_id")
    create_time = models.DateTimeField(u"创建时间", auto_now_add=True)
    update_time = models.DateTimeField(u"更新时间", auto_now=True)

    class Meta:
        db_table = "files"

"""
  QA config
"""
class QaConfig(models.Model):
    id = models.AutoField(primary_key=True)
    config_name = models.CharField(u"名称",unique=True,max_length=100)
    config_value = JSONField()
    editor_id = models.ForeignKey(User, to_field="user_id", on_delete=models.CASCADE,db_column="editor_id")
    create_time = models.DateTimeField(u"创建时间", auto_now_add=True)
    update_time = models.DateTimeField(u"更新时间", auto_now=True)

    class Meta:
        db_table = "qa_config"
