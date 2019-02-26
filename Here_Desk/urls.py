"""zhelitech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path("", views.home, name="home")
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path("", Home.as_view(), name="home")
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path("blog/", include("blog.urls"))
"""

from django.conf import settings
from django.conf.urls.static import static

from Here_Desk.settings import MEDIA_ROOT
from django.views.static import serve

from django.contrib import admin
from django.conf.urls import include,url
from django.conf.urls import handler404
from django.urls import path

from app.api.user import login
from app.api.user import passwd
from app.api.user import user
from app.api.user import pages

from app.api.user import config

from app.api.pm import product
from app.api.pm import version
from app.api.pm import members
from app.api.pm import module

from app.api.qa import config as qa_config

from app.api.qa.bug import datalist as bug_list
from app.api.qa.bug import create as bug_create
from app.api.qa.bug import edit as bug_edit
from app.api.qa.bug import delete as bug_delete
from app.api.qa.bug import details as bug_details
from app.api.qa.bug import report as bug_report
from app.api.qa.bug import search as bug_search
from app.api.qa.bug import export as bug_export
from app.api.qa.bug import action as bug_action
from app.api.qa.bug import annex as bug_annex
from app.api.qa.bug import support as bug_support


from app.api.qa.testcase import datalist as case_list
from app.api.qa.testcase import search as case_search
from app.api.qa.testcase import delete as case_delete
from app.api.qa.testcase import details as case_details
from app.api.qa.testcase import edit as case_edit
from app.api.qa.testcase import export as case_export
from app.api.qa.testcase import fall as case_fall
from app.api.qa.testcase import review as case_review


from app.api.qa.testsuite import create as testsuite_create
from app.api.qa.testsuite import datalist as testsuite_list

from app.api.qa.testsuite.cell import add as cell_add
from app.api.qa.testsuite.cell import loader as cell_loader_list
from app.api.qa.testsuite.cell import run as cell_run
from app.api.qa.testsuite.cell import run_list as cell_run_list

from app.api.dashboard import dashboard
from app.api.analyze import bug_analyze
from app.api.analyze import testcase_analyze

from app.api.system import api
from app.api.system import page
from app.api.system import log
from app.api.support import upload

urlpatterns = [
    url(r"^api/support/upload", upload.upload, name="upload"),
    url(r"^media/(?P<path>.*)", serve, {"document_root": MEDIA_ROOT}),

    url(r"^api/user/login", login.login, name="login"),
    url(r"^api/user/setpasswd", passwd.set_passwd, name="set_passwd"),
    url(r"^api/user/user_list", user.user_list, name="user_list"),
    url(r"^api/user/userinfo", user.userinfo, name="userinfo"),
    url(r"^api/user/banned", user.banned, name="banned"),
    url(r"^api/user/group", user.group, name="group"),
    url(r"^api/user/add", user.add, name="user_add"),

    url(r"^api/userconfig", config.user, name="userconfig"),

    # 管理员重置密码
    url(r"^api/user/reset_passwd", passwd.reset_passwd, name="reset_passwd"),

    # dashboard 
    url(r"^api/dashboard/data_statistics", dashboard.data_statistics, name="data_statistics"),

    # 统计
    url(r"^api/analyze/bug/query", bug_analyze.query, name="analyze_bug_query"),
    url(r"^api/analyze/bug/my_today", bug_analyze.my_today, name="analyze_my_today"),
    url(r"^api/analyze/bug/date/create", bug_analyze.date_create, name="analyze_date_create"),

    url(r"^api/analyze/bug/tester", bug_analyze.tester, name="bug_analyze_tester"),
    url(r"^api/analyze/bug/developer", bug_analyze.developer, name="bug_analyze_developer"),

    url(r"api/analyze/testcase/my_today", testcase_analyze.my_today, name="testcase_analyze_my_today"),
    
    
    # 项目或产品
    url(r"^api/pm/product/cascader/my", product.product_release_cascader, name="product_release_cascader"),
    url(r"^api/pm/product/my", product.my_product_list, name="my_product_info"),
    url(r"^api/pm/product/all_list", product.all_product_list, name="all_product_info"),
    url(r"^api/pm/product/create", product.create_product, name="create_product"),

    # module
    url(r"^api/pm/module/all/list", module.module_list_all, name="module_list_all"),
    url(r"^api/pm/module/1/list", module.module_list_a, name="module_list_a"),
    url(r"^api/pm/module/1/add", module.module_add_a, name="add_module_a"),
    url(r"^api/pm/module/2/list", module.module_list_b, name="module_list_b"),
    url(r"^api/pm/module/2/add", module.module_add_b, name="add_module_b"),
    url(r"^api/pm/module/2/edit", module.module_edit_b, name="module_edit_b"),
    url(r"^api/pm/module/2/del", module.module_del_b, name="module_del_b"),

    # 版本
    url(r"^api/pm/release/create", version.create_release, name="create_release"),
    url(r"^api/pm/release/list",version.get_release, name="get_release"),

    # 人员product_members
    url(r"^api/pm/member/list",members.members_list, name="members_list"),
    url(r"^api/pm/member/join",members.product_members_join, name="product_members_join"),
    url(r"^api/pm/member/ban",members.product_members_ban, name="product_members_ban"),
    url(r"^api/pm/member/rejoin",members.product_members_rejoin, name="product_members_rejoin"),


    # qa config
    url(r"^api/qa/get_config", qa_config.get_qa_config, name="get_qa_config"),
    url(r"^api/qa/create_config", qa_config.create_qa_config, name="create_qa_config"),

    # 测试用例相关
    url(r"^api/qa/testcase/list", case_list.data_list, name="case_all_list"),
    url(r"^api/qa/testcase/valid_list", case_list.valid_list, name="case_valid_list"),

    url(r"^api/qa/testcase/search", case_search.search, name="case_search"),
    url(r"^api/qa/testcase/details", case_details.details, name="case_details"),
    url(r"^api/qa/testcase/add", case_edit.add, name="case_add"),
    url(r"^api/qa/testcase/edit", case_edit.edit, name="case_edit"),
    url(r"^api/qa/testcase/fall",case_fall.fall,name="case_fall"),

    url(r"^api/qa/testcase/del", case_delete.delete, name="case_delete"),
    url(r"^api/qa/testcase/annex/delete",case_delete.annex_delete,name="case_annex_delete"),

    url(r"^api/qa/testcase/review", case_review.review, name="case_review"),
    url(r"^api/qa/testcase/export",case_export.export,name="case_export"),

    # test case sutie and cell
    url(r"^api/qa/testsuite/create",testsuite_create.create,name="testsuite_create"),
    url(r"^api/qa/testsuite/list",testsuite_list.data_list,name="testsuite_list"),
    url(r"^api/qa/testsuite/cell/run_list",cell_run_list.run_list,name="cell_run_list"),
    url(r"^api/qa/testsuite/cell/run",cell_run.run,name="cell_run"),
    url(r"^api/qa/testsuite/cell/loader_list",cell_loader_list.loader_list,name="cell_loader_list"),
    url(r"^api/qa/testsuite/cell/add",cell_add.add,name="cell_add"), 

    # bug
    url(r"^api/qa/bug/bug_property",bug_support.property, name="bug_property"),
    
    url(r"^api/qa/bug/list",bug_list.list, name="bug_list"),
    url(r"^api/qa/bug/search",bug_search.search, name="bug_search"),
    url(r"^api/qa/bug/create",bug_create.create, name="bug_create"),
    url(r"^api/qa/bug/edit",bug_edit.edit, name="bug_edit"),
    url(r"^api/qa/bug/details",bug_details.details, name="bug_details"),
    url(r"^api/qa/bug/history",bug_details.history,name="bug_history"),
    url(r"^api/qa/bug/export",bug_export.export,name="export"),

    url(r"^api/qa/bug/delete",bug_delete.delete, name="bug_delete"),
    url(r"^api/qa/bug/resolve",bug_action.resolve,name="bug_resolve"),
    url(r"^api/qa/bug/assign",bug_action.assign,name="bug_assign"),
    url(r"^api/qa/bug/close",bug_action.close,name="bug_close"),
    url(r"^api/qa/bug/reopen",bug_action.reopen,name="bug_reopen"),
    url(r"^api/qa/bug/hangup",bug_action.hangup,name="bug_hangup"),

    url(r"^api/qa/bug/report/generate",bug_report.report,name="bug_report"),
    url(r"^api/qa/bug/report/details",bug_report.report_details,name="bug_report_details"),

    url(r"^api/qa/bug/remarks",bug_action.remarks,name="bug_remarks"),
    url(r"^api/qa/bug/annex/delete",bug_annex.delete,name="annex_delete"),


    # 权限控制
    url(r"^api/system/api/create",api.api_create,name="api_create"),
    url(r"^api/system/api/list",api.api_list,name="api_list"),
    url(r"^api/system/api/manage",api.api_manage,name="api_manage"),

    url(r"^api/system/page/create",page.create,name="page_create"),
    url(r"^api/system/page/list",page.pages_list,name="page_list"),
    url(r"^api/system/page/manage",page.manage,name="page_manage"),

    url(r"^api/system/user_log",log.userlog,name="userlog"),

    # page
    url(r"^api/user/pages",pages.pages,name="user_pages"),
]
