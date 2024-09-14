from datetime import datetime
import os
import time

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import login_required
from .form import *
from .models import *
from sys_user.func import *

# 词云

from a_simulink_unit.generate_wordcloud import generate_wordcloud_base64

# Create your views here.


def index(request):

    return render(request, "config_visual/index.html", locals())


"""

# 系统中所有数据表名/中英文+字段中英文
用于快速创建查询语句和分析
测试通过后删除此段.
__deprected__ mark_appcenter_views_all_tables_and_fields
__deprected__ mark_appcenter_views_all_tables_and__two_field_fields
# 根据需要按照表结构和csv文件依次导入数据库.
"""


def bi(request):
    if request.method == "GET":
        return HttpResponse(
            loader.get_template("config_visual/bi.html").render({}, request)
        )
    obj = mydict(request.POST)
    res = dict()

    # userinfo(用户信息表)->userid(用户ID唯一标识)

    if obj.get("optype") == "userinfo.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm772_58dd091a279b5392.userinfo group by userid order by x desc",
            "用户ID唯一标识",
        )
    if obj.get("optype") == "userinfo.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm772_58dd091a279b5392.userinfo group by userid",
            "用户ID唯一标识",
        )
    if obj.get("optype") == "userinfo.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm772_58dd091a279b5392.userinfo group by userid",
            "用户ID唯一标识",
        )
    if obj.get("optype") == "userinfo.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm772_58dd091a279b5392.userinfo group by userid",
            "用户ID唯一标识",
        )
    if obj.get("optype") == "userinfo.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm772_58dd091a279b5392.userinfo group by userid",
            "用户ID唯一标识",
        )
    if obj.get("optype") == "userinfo.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm772_58dd091a279b5392.userinfo group by userid",
            "用户ID唯一标识",
        )
    # userinfo(用户信息表)->username(用户名用户登录名或昵称)

    if obj.get("optype") == "userinfo.username_pie":
        res = get_pie(
            "select username x,count(*) y from vm772_58dd091a279b5392.userinfo group by username order by x desc",
            "用户名用户登录名或昵称",
        )
    if obj.get("optype") == "userinfo.username_pie_v1":
        res = get_pie_v1(
            "select username x,count(*) y from vm772_58dd091a279b5392.userinfo group by username",
            "用户名用户登录名或昵称",
        )
    if obj.get("optype") == "userinfo.username_pie_v2":
        res = get_pie_v2(
            "select username x,count(*) y from vm772_58dd091a279b5392.userinfo group by username",
            "用户名用户登录名或昵称",
        )
    if obj.get("optype") == "userinfo.username_line":
        res = get_line(
            "select username x,count(*) y from vm772_58dd091a279b5392.userinfo group by username",
            "用户名用户登录名或昵称",
        )
    if obj.get("optype") == "userinfo.username_bar":
        res = get_bar(
            "select username x,count(*) y from vm772_58dd091a279b5392.userinfo group by username",
            "用户名用户登录名或昵称",
        )
    if obj.get("optype") == "userinfo.username_bar_v1":
        res = get_bar_v1(
            "select username x,count(*) y from vm772_58dd091a279b5392.userinfo group by username",
            "用户名用户登录名或昵称",
        )
    # userinfo(用户信息表)->pkwkwasswkwkwordhkwkwash(密码哈希存储加密后的密码)

    if obj.get("optype") == "userinfo.pkwkwasswkwkwordhkwkwash_pie":
        res = get_pie(
            "select pkwkwasswkwkwordhkwkwash x,count(*) y from vm772_58dd091a279b5392.userinfo group by pkwkwasswkwkwordhkwkwash order by x desc",
            "密码哈希存储加密后的密码",
        )
    if obj.get("optype") == "userinfo.pkwkwasswkwkwordhkwkwash_pie_v1":
        res = get_pie_v1(
            "select pkwkwasswkwkwordhkwkwash x,count(*) y from vm772_58dd091a279b5392.userinfo group by pkwkwasswkwkwordhkwkwash",
            "密码哈希存储加密后的密码",
        )
    if obj.get("optype") == "userinfo.pkwkwasswkwkwordhkwkwash_pie_v2":
        res = get_pie_v2(
            "select pkwkwasswkwkwordhkwkwash x,count(*) y from vm772_58dd091a279b5392.userinfo group by pkwkwasswkwkwordhkwkwash",
            "密码哈希存储加密后的密码",
        )
    if obj.get("optype") == "userinfo.pkwkwasswkwkwordhkwkwash_line":
        res = get_line(
            "select pkwkwasswkwkwordhkwkwash x,count(*) y from vm772_58dd091a279b5392.userinfo group by pkwkwasswkwkwordhkwkwash",
            "密码哈希存储加密后的密码",
        )
    if obj.get("optype") == "userinfo.pkwkwasswkwkwordhkwkwash_bar":
        res = get_bar(
            "select pkwkwasswkwkwordhkwkwash x,count(*) y from vm772_58dd091a279b5392.userinfo group by pkwkwasswkwkwordhkwkwash",
            "密码哈希存储加密后的密码",
        )
    if obj.get("optype") == "userinfo.pkwkwasswkwkwordhkwkwash_bar_v1":
        res = get_bar_v1(
            "select pkwkwasswkwkwordhkwkwash x,count(*) y from vm772_58dd091a279b5392.userinfo group by pkwkwasswkwkwordhkwkwash",
            "密码哈希存储加密后的密码",
        )
    if obj.get("optype") == "userinfo.email_wordcloud":
        textlist = get_data("SELECT email result FROM vm772_58dd091a279b5392.userinfo;")
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # userinfo(用户信息表)->phonenumber(手机号码用户联系电话)

    if obj.get("optype") == "userinfo.phonenumber_pie":
        res = get_pie(
            "select phonenumber x,count(*) y from vm772_58dd091a279b5392.userinfo group by phonenumber order by x desc",
            "手机号码用户联系电话",
        )
    if obj.get("optype") == "userinfo.phonenumber_pie_v1":
        res = get_pie_v1(
            "select phonenumber x,count(*) y from vm772_58dd091a279b5392.userinfo group by phonenumber",
            "手机号码用户联系电话",
        )
    if obj.get("optype") == "userinfo.phonenumber_pie_v2":
        res = get_pie_v2(
            "select phonenumber x,count(*) y from vm772_58dd091a279b5392.userinfo group by phonenumber",
            "手机号码用户联系电话",
        )
    if obj.get("optype") == "userinfo.phonenumber_line":
        res = get_line(
            "select phonenumber x,count(*) y from vm772_58dd091a279b5392.userinfo group by phonenumber",
            "手机号码用户联系电话",
        )
    if obj.get("optype") == "userinfo.phonenumber_bar":
        res = get_bar(
            "select phonenumber x,count(*) y from vm772_58dd091a279b5392.userinfo group by phonenumber",
            "手机号码用户联系电话",
        )
    if obj.get("optype") == "userinfo.phonenumber_bar_v1":
        res = get_bar_v1(
            "select phonenumber x,count(*) y from vm772_58dd091a279b5392.userinfo group by phonenumber",
            "手机号码用户联系电话",
        )
    if obj.get("optype") == "userinfo.regkwkwistertime_line":
        res = get_line(
            "select regkwkwistertime x,count(*) y from vm772_58dd091a279b5392.userinfo group by regkwkwistertime order by x",
            "注册时间用户注册时的日期和时间",
        )
    if obj.get("optype") == "userinfo.lkwkwastlogkwkwintime_line":
        res = get_line(
            "select lkwkwastlogkwkwintime x,count(*) y from vm772_58dd091a279b5392.userinfo group by lkwkwastlogkwkwintime order by x",
            "最后登录时间用户最后一次登录的日期和时间",
        )
    # userinfo(用户信息表)->status(用户状态如活跃、禁用等)

    if obj.get("optype") == "userinfo.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm772_58dd091a279b5392.userinfo group by status order by x desc",
            "用户状态如活跃、禁用等",
        )
    if obj.get("optype") == "userinfo.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm772_58dd091a279b5392.userinfo group by status",
            "用户状态如活跃、禁用等",
        )
    if obj.get("optype") == "userinfo.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm772_58dd091a279b5392.userinfo group by status",
            "用户状态如活跃、禁用等",
        )
    if obj.get("optype") == "userinfo.status_line":
        res = get_line(
            "select status x,count(*) y from vm772_58dd091a279b5392.userinfo group by status",
            "用户状态如活跃、禁用等",
        )
    if obj.get("optype") == "userinfo.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm772_58dd091a279b5392.userinfo group by status",
            "用户状态如活跃、禁用等",
        )
    if obj.get("optype") == "userinfo.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm772_58dd091a279b5392.userinfo group by status",
            "用户状态如活跃、禁用等",
        )
    # userinfo(用户信息表)->avatarurl(头像URL用户头像图片的存储地址)

    if obj.get("optype") == "userinfo.avatarurl_pie":
        res = get_pie(
            "select avatarurl x,count(*) y from vm772_58dd091a279b5392.userinfo group by avatarurl order by x desc",
            "头像URL用户头像图片的存储地址",
        )
    if obj.get("optype") == "userinfo.avatarurl_pie_v1":
        res = get_pie_v1(
            "select avatarurl x,count(*) y from vm772_58dd091a279b5392.userinfo group by avatarurl",
            "头像URL用户头像图片的存储地址",
        )
    if obj.get("optype") == "userinfo.avatarurl_pie_v2":
        res = get_pie_v2(
            "select avatarurl x,count(*) y from vm772_58dd091a279b5392.userinfo group by avatarurl",
            "头像URL用户头像图片的存储地址",
        )
    if obj.get("optype") == "userinfo.avatarurl_line":
        res = get_line(
            "select avatarurl x,count(*) y from vm772_58dd091a279b5392.userinfo group by avatarurl",
            "头像URL用户头像图片的存储地址",
        )
    if obj.get("optype") == "userinfo.avatarurl_bar":
        res = get_bar(
            "select avatarurl x,count(*) y from vm772_58dd091a279b5392.userinfo group by avatarurl",
            "头像URL用户头像图片的存储地址",
        )
    if obj.get("optype") == "userinfo.avatarurl_bar_v1":
        res = get_bar_v1(
            "select avatarurl x,count(*) y from vm772_58dd091a279b5392.userinfo group by avatarurl",
            "头像URL用户头像图片的存储地址",
        )
    # userinfo(用户信息表)->roleid(角色ID关联到角色的ID示用户所属的角色)

    if obj.get("optype") == "userinfo.roleid_pie":
        res = get_pie(
            "select roleid x,count(*) y from vm772_58dd091a279b5392.userinfo group by roleid order by x desc",
            "角色ID关联到角色的ID示用户所属的角色",
        )
    if obj.get("optype") == "userinfo.roleid_pie_v1":
        res = get_pie_v1(
            "select roleid x,count(*) y from vm772_58dd091a279b5392.userinfo group by roleid",
            "角色ID关联到角色的ID示用户所属的角色",
        )
    if obj.get("optype") == "userinfo.roleid_pie_v2":
        res = get_pie_v2(
            "select roleid x,count(*) y from vm772_58dd091a279b5392.userinfo group by roleid",
            "角色ID关联到角色的ID示用户所属的角色",
        )
    if obj.get("optype") == "userinfo.roleid_line":
        res = get_line(
            "select roleid x,count(*) y from vm772_58dd091a279b5392.userinfo group by roleid",
            "角色ID关联到角色的ID示用户所属的角色",
        )
    if obj.get("optype") == "userinfo.roleid_bar":
        res = get_bar(
            "select roleid x,count(*) y from vm772_58dd091a279b5392.userinfo group by roleid",
            "角色ID关联到角色的ID示用户所属的角色",
        )
    if obj.get("optype") == "userinfo.roleid_bar_v1":
        res = get_bar_v1(
            "select roleid x,count(*) y from vm772_58dd091a279b5392.userinfo group by roleid",
            "角色ID关联到角色的ID示用户所属的角色",
        )
    # platkwkwfkwkwormaccount(平台账号表)->platkwkwfkwkwormid(平台ID)

    if obj.get("optype") == "platkwkwfkwkwormaccount.platkwkwfkwkwormid_pie":
        res = get_pie(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by platkwkwfkwkwormid order by x desc",
            "平台ID",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.platkwkwfkwkwormid_pie_v1":
        res = get_pie_v1(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by platkwkwfkwkwormid",
            "平台ID",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.platkwkwfkwkwormid_pie_v2":
        res = get_pie_v2(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by platkwkwfkwkwormid",
            "平台ID",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.platkwkwfkwkwormid_line":
        res = get_line(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by platkwkwfkwkwormid",
            "平台ID",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.platkwkwfkwkwormid_bar":
        res = get_bar(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by platkwkwfkwkwormid",
            "平台ID",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.platkwkwfkwkwormid_bar_v1":
        res = get_bar_v1(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by platkwkwfkwkwormid",
            "平台ID",
        )
    # platkwkwfkwkwormaccount(平台账号表)->accountname(账号名称)

    if obj.get("optype") == "platkwkwfkwkwormaccount.accountname_pie":
        res = get_pie(
            "select accountname x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by accountname order by x desc",
            "账号名称",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.accountname_pie_v1":
        res = get_pie_v1(
            "select accountname x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by accountname",
            "账号名称",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.accountname_pie_v2":
        res = get_pie_v2(
            "select accountname x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by accountname",
            "账号名称",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.accountname_line":
        res = get_line(
            "select accountname x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by accountname",
            "账号名称",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.accountname_bar":
        res = get_bar(
            "select accountname x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by accountname",
            "账号名称",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.accountname_bar_v1":
        res = get_bar_v1(
            "select accountname x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by accountname",
            "账号名称",
        )
    # platkwkwfkwkwormaccount(平台账号表)->accounttype(账号类型)

    if obj.get("optype") == "platkwkwfkwkwormaccount.accounttype_pie":
        res = get_pie(
            "select accounttype x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by accounttype order by x desc",
            "账号类型",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.accounttype_pie_v1":
        res = get_pie_v1(
            "select accounttype x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by accounttype",
            "账号类型",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.accounttype_pie_v2":
        res = get_pie_v2(
            "select accounttype x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by accounttype",
            "账号类型",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.accounttype_line":
        res = get_line(
            "select accounttype x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by accounttype",
            "账号类型",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.accounttype_bar":
        res = get_bar(
            "select accounttype x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by accounttype",
            "账号类型",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.accounttype_bar_v1":
        res = get_bar_v1(
            "select accounttype x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by accounttype",
            "账号类型",
        )
    # platkwkwfkwkwormaccount(平台账号表)->platkwkwfkwkwormname(所属平台名称)

    if obj.get("optype") == "platkwkwfkwkwormaccount.platkwkwfkwkwormname_pie":
        res = get_pie(
            "select platkwkwfkwkwormname x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by platkwkwfkwkwormname order by x desc",
            "所属平台名称",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.platkwkwfkwkwormname_pie_v1":
        res = get_pie_v1(
            "select platkwkwfkwkwormname x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by platkwkwfkwkwormname",
            "所属平台名称",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.platkwkwfkwkwormname_pie_v2":
        res = get_pie_v2(
            "select platkwkwfkwkwormname x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by platkwkwfkwkwormname",
            "所属平台名称",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.platkwkwfkwkwormname_line":
        res = get_line(
            "select platkwkwfkwkwormname x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by platkwkwfkwkwormname",
            "所属平台名称",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.platkwkwfkwkwormname_bar":
        res = get_bar(
            "select platkwkwfkwkwormname x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by platkwkwfkwkwormname",
            "所属平台名称",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.platkwkwfkwkwormname_bar_v1":
        res = get_bar_v1(
            "select platkwkwfkwkwormname x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by platkwkwfkwkwormname",
            "所属平台名称",
        )
    # platkwkwfkwkwormaccount(平台账号表)->username(用户名)

    if obj.get("optype") == "platkwkwfkwkwormaccount.username_pie":
        res = get_pie(
            "select username x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by username order by x desc",
            "用户名",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.username_pie_v1":
        res = get_pie_v1(
            "select username x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by username",
            "用户名",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.username_pie_v2":
        res = get_pie_v2(
            "select username x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by username",
            "用户名",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.username_line":
        res = get_line(
            "select username x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by username",
            "用户名",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.username_bar":
        res = get_bar(
            "select username x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by username",
            "用户名",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.username_bar_v1":
        res = get_bar_v1(
            "select username x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by username",
            "用户名",
        )
    # platkwkwfkwkwormaccount(平台账号表)->pkwkwasswkwkword(密码加密存储)

    if obj.get("optype") == "platkwkwfkwkwormaccount.pkwkwasswkwkword_pie":
        res = get_pie(
            "select pkwkwasswkwkword x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by pkwkwasswkwkword order by x desc",
            "密码加密存储",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.pkwkwasswkwkword_pie_v1":
        res = get_pie_v1(
            "select pkwkwasswkwkword x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by pkwkwasswkwkword",
            "密码加密存储",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.pkwkwasswkwkword_pie_v2":
        res = get_pie_v2(
            "select pkwkwasswkwkword x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by pkwkwasswkwkword",
            "密码加密存储",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.pkwkwasswkwkword_line":
        res = get_line(
            "select pkwkwasswkwkword x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by pkwkwasswkwkword",
            "密码加密存储",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.pkwkwasswkwkword_bar":
        res = get_bar(
            "select pkwkwasswkwkword x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by pkwkwasswkwkword",
            "密码加密存储",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.pkwkwasswkwkword_bar_v1":
        res = get_bar_v1(
            "select pkwkwasswkwkword x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by pkwkwasswkwkword",
            "密码加密存储",
        )
    # platkwkwfkwkwormaccount(平台账号表)->accesstoken(访问令牌)

    if obj.get("optype") == "platkwkwfkwkwormaccount.accesstoken_pie":
        res = get_pie(
            "select accesstoken x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by accesstoken order by x desc",
            "访问令牌",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.accesstoken_pie_v1":
        res = get_pie_v1(
            "select accesstoken x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by accesstoken",
            "访问令牌",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.accesstoken_pie_v2":
        res = get_pie_v2(
            "select accesstoken x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by accesstoken",
            "访问令牌",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.accesstoken_line":
        res = get_line(
            "select accesstoken x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by accesstoken",
            "访问令牌",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.accesstoken_bar":
        res = get_bar(
            "select accesstoken x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by accesstoken",
            "访问令牌",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.accesstoken_bar_v1":
        res = get_bar_v1(
            "select accesstoken x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by accesstoken",
            "访问令牌",
        )
    # platkwkwfkwkwormaccount(平台账号表)->status(账号状态如启用、禁用)

    if obj.get("optype") == "platkwkwfkwkwormaccount.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by status order by x desc",
            "账号状态如启用、禁用",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by status",
            "账号状态如启用、禁用",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by status",
            "账号状态如启用、禁用",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.status_line":
        res = get_line(
            "select status x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by status",
            "账号状态如启用、禁用",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by status",
            "账号状态如启用、禁用",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by status",
            "账号状态如启用、禁用",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.lkwkwastlogkwkwintime_line":
        res = get_line(
            "select lkwkwastlogkwkwintime x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by lkwkwastlogkwkwintime order by x",
            "最后登录时间",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.createdat_line":
        res = get_line(
            "select createdat x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by createdat order by x",
            "创建时间",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.updatedat_line":
        res = get_line(
            "select updatedat x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by updatedat order by x",
            "更新时间",
        )
    # platkwkwfkwkwormaccount(平台账号表)->kwkwassociateduserid(关联用户ID如果有用户与账号关联)

    if obj.get("optype") == "platkwkwfkwkwormaccount.kwkwassociateduserid_pie":
        res = get_pie(
            "select kwkwassociateduserid x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by kwkwassociateduserid order by x desc",
            "关联用户ID如果有用户与账号关联",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.kwkwassociateduserid_pie_v1":
        res = get_pie_v1(
            "select kwkwassociateduserid x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by kwkwassociateduserid",
            "关联用户ID如果有用户与账号关联",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.kwkwassociateduserid_pie_v2":
        res = get_pie_v2(
            "select kwkwassociateduserid x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by kwkwassociateduserid",
            "关联用户ID如果有用户与账号关联",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.kwkwassociateduserid_line":
        res = get_line(
            "select kwkwassociateduserid x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by kwkwassociateduserid",
            "关联用户ID如果有用户与账号关联",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.kwkwassociateduserid_bar":
        res = get_bar(
            "select kwkwassociateduserid x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by kwkwassociateduserid",
            "关联用户ID如果有用户与账号关联",
        )
    if obj.get("optype") == "platkwkwfkwkwormaccount.kwkwassociateduserid_bar_v1":
        res = get_bar_v1(
            "select kwkwassociateduserid x,count(*) y from vm772_58dd091a279b5392.platkwkwfkwkwormaccount group by kwkwassociateduserid",
            "关联用户ID如果有用户与账号关联",
        )
    # messagetemplate(私信模板表)->templateid(模板ID)

    if obj.get("optype") == "messagetemplate.templateid_pie":
        res = get_pie(
            "select templateid x,count(*) y from vm772_58dd091a279b5392.messagetemplate group by templateid order by x desc",
            "模板ID",
        )
    if obj.get("optype") == "messagetemplate.templateid_pie_v1":
        res = get_pie_v1(
            "select templateid x,count(*) y from vm772_58dd091a279b5392.messagetemplate group by templateid",
            "模板ID",
        )
    if obj.get("optype") == "messagetemplate.templateid_pie_v2":
        res = get_pie_v2(
            "select templateid x,count(*) y from vm772_58dd091a279b5392.messagetemplate group by templateid",
            "模板ID",
        )
    if obj.get("optype") == "messagetemplate.templateid_line":
        res = get_line(
            "select templateid x,count(*) y from vm772_58dd091a279b5392.messagetemplate group by templateid",
            "模板ID",
        )
    if obj.get("optype") == "messagetemplate.templateid_bar":
        res = get_bar(
            "select templateid x,count(*) y from vm772_58dd091a279b5392.messagetemplate group by templateid",
            "模板ID",
        )
    if obj.get("optype") == "messagetemplate.templateid_bar_v1":
        res = get_bar_v1(
            "select templateid x,count(*) y from vm772_58dd091a279b5392.messagetemplate group by templateid",
            "模板ID",
        )
    # messagetemplate(私信模板表)->templatename(模板名称)

    if obj.get("optype") == "messagetemplate.templatename_pie":
        res = get_pie(
            "select templatename x,count(*) y from vm772_58dd091a279b5392.messagetemplate group by templatename order by x desc",
            "模板名称",
        )
    if obj.get("optype") == "messagetemplate.templatename_pie_v1":
        res = get_pie_v1(
            "select templatename x,count(*) y from vm772_58dd091a279b5392.messagetemplate group by templatename",
            "模板名称",
        )
    if obj.get("optype") == "messagetemplate.templatename_pie_v2":
        res = get_pie_v2(
            "select templatename x,count(*) y from vm772_58dd091a279b5392.messagetemplate group by templatename",
            "模板名称",
        )
    if obj.get("optype") == "messagetemplate.templatename_line":
        res = get_line(
            "select templatename x,count(*) y from vm772_58dd091a279b5392.messagetemplate group by templatename",
            "模板名称",
        )
    if obj.get("optype") == "messagetemplate.templatename_bar":
        res = get_bar(
            "select templatename x,count(*) y from vm772_58dd091a279b5392.messagetemplate group by templatename",
            "模板名称",
        )
    if obj.get("optype") == "messagetemplate.templatename_bar_v1":
        res = get_bar_v1(
            "select templatename x,count(*) y from vm772_58dd091a279b5392.messagetemplate group by templatename",
            "模板名称",
        )
    if obj.get("optype") == "messagetemplate.templatecontent_wordcloud":
        textlist = get_data(
            "SELECT templatecontent result FROM vm772_58dd091a279b5392.messagetemplate;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # messagetemplate(私信模板表)->creatkwkworid(创建者ID)

    if obj.get("optype") == "messagetemplate.creatkwkworid_pie":
        res = get_pie(
            "select creatkwkworid x,count(*) y from vm772_58dd091a279b5392.messagetemplate group by creatkwkworid order by x desc",
            "创建者ID",
        )
    if obj.get("optype") == "messagetemplate.creatkwkworid_pie_v1":
        res = get_pie_v1(
            "select creatkwkworid x,count(*) y from vm772_58dd091a279b5392.messagetemplate group by creatkwkworid",
            "创建者ID",
        )
    if obj.get("optype") == "messagetemplate.creatkwkworid_pie_v2":
        res = get_pie_v2(
            "select creatkwkworid x,count(*) y from vm772_58dd091a279b5392.messagetemplate group by creatkwkworid",
            "创建者ID",
        )
    if obj.get("optype") == "messagetemplate.creatkwkworid_line":
        res = get_line(
            "select creatkwkworid x,count(*) y from vm772_58dd091a279b5392.messagetemplate group by creatkwkworid",
            "创建者ID",
        )
    if obj.get("optype") == "messagetemplate.creatkwkworid_bar":
        res = get_bar(
            "select creatkwkworid x,count(*) y from vm772_58dd091a279b5392.messagetemplate group by creatkwkworid",
            "创建者ID",
        )
    if obj.get("optype") == "messagetemplate.creatkwkworid_bar_v1":
        res = get_bar_v1(
            "select creatkwkworid x,count(*) y from vm772_58dd091a279b5392.messagetemplate group by creatkwkworid",
            "创建者ID",
        )
    if obj.get("optype") == "messagetemplate.createtime_line":
        res = get_line(
            "select createtime x,count(*) y from vm772_58dd091a279b5392.messagetemplate group by createtime order by x",
            "创建时间",
        )
    if obj.get("optype") == "messagetemplate.updatetime_line":
        res = get_line(
            "select updatetime x,count(*) y from vm772_58dd091a279b5392.messagetemplate group by updatetime order by x",
            "更新时间",
        )
    # messagetemplate(私信模板表)->kwkwisactive(是否激活)

    if obj.get("optype") == "messagetemplate.kwkwisactive_pie":
        res = get_pie(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.messagetemplate group by kwkwisactive order by x desc",
            "是否激活",
        )
    if obj.get("optype") == "messagetemplate.kwkwisactive_pie_v1":
        res = get_pie_v1(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.messagetemplate group by kwkwisactive",
            "是否激活",
        )
    if obj.get("optype") == "messagetemplate.kwkwisactive_pie_v2":
        res = get_pie_v2(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.messagetemplate group by kwkwisactive",
            "是否激活",
        )
    if obj.get("optype") == "messagetemplate.kwkwisactive_line":
        res = get_line(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.messagetemplate group by kwkwisactive",
            "是否激活",
        )
    if obj.get("optype") == "messagetemplate.kwkwisactive_bar":
        res = get_bar(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.messagetemplate group by kwkwisactive",
            "是否激活",
        )
    if obj.get("optype") == "messagetemplate.kwkwisactive_bar_v1":
        res = get_bar_v1(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.messagetemplate group by kwkwisactive",
            "是否激活",
        )
    # messagetemplate(私信模板表)->platkwkwfkwkwormtype(平台类型)

    if obj.get("optype") == "messagetemplate.platkwkwfkwkwormtype_pie":
        res = get_pie(
            "select platkwkwfkwkwormtype x,count(*) y from vm772_58dd091a279b5392.messagetemplate group by platkwkwfkwkwormtype order by x desc",
            "平台类型",
        )
    if obj.get("optype") == "messagetemplate.platkwkwfkwkwormtype_pie_v1":
        res = get_pie_v1(
            "select platkwkwfkwkwormtype x,count(*) y from vm772_58dd091a279b5392.messagetemplate group by platkwkwfkwkwormtype",
            "平台类型",
        )
    if obj.get("optype") == "messagetemplate.platkwkwfkwkwormtype_pie_v2":
        res = get_pie_v2(
            "select platkwkwfkwkwormtype x,count(*) y from vm772_58dd091a279b5392.messagetemplate group by platkwkwfkwkwormtype",
            "平台类型",
        )
    if obj.get("optype") == "messagetemplate.platkwkwfkwkwormtype_line":
        res = get_line(
            "select platkwkwfkwkwormtype x,count(*) y from vm772_58dd091a279b5392.messagetemplate group by platkwkwfkwkwormtype",
            "平台类型",
        )
    if obj.get("optype") == "messagetemplate.platkwkwfkwkwormtype_bar":
        res = get_bar(
            "select platkwkwfkwkwormtype x,count(*) y from vm772_58dd091a279b5392.messagetemplate group by platkwkwfkwkwormtype",
            "平台类型",
        )
    if obj.get("optype") == "messagetemplate.platkwkwfkwkwormtype_bar_v1":
        res = get_bar_v1(
            "select platkwkwfkwkwormtype x,count(*) y from vm772_58dd091a279b5392.messagetemplate group by platkwkwfkwkwormtype",
            "平台类型",
        )
    # messagetemplate(私信模板表)->targetuserid(目标用户ID可选用于指定特定用户)

    if obj.get("optype") == "messagetemplate.targetuserid_pie":
        res = get_pie(
            "select targetuserid x,count(*) y from vm772_58dd091a279b5392.messagetemplate group by targetuserid order by x desc",
            "目标用户ID可选用于指定特定用户",
        )
    if obj.get("optype") == "messagetemplate.targetuserid_pie_v1":
        res = get_pie_v1(
            "select targetuserid x,count(*) y from vm772_58dd091a279b5392.messagetemplate group by targetuserid",
            "目标用户ID可选用于指定特定用户",
        )
    if obj.get("optype") == "messagetemplate.targetuserid_pie_v2":
        res = get_pie_v2(
            "select targetuserid x,count(*) y from vm772_58dd091a279b5392.messagetemplate group by targetuserid",
            "目标用户ID可选用于指定特定用户",
        )
    if obj.get("optype") == "messagetemplate.targetuserid_line":
        res = get_line(
            "select targetuserid x,count(*) y from vm772_58dd091a279b5392.messagetemplate group by targetuserid",
            "目标用户ID可选用于指定特定用户",
        )
    if obj.get("optype") == "messagetemplate.targetuserid_bar":
        res = get_bar(
            "select targetuserid x,count(*) y from vm772_58dd091a279b5392.messagetemplate group by targetuserid",
            "目标用户ID可选用于指定特定用户",
        )
    if obj.get("optype") == "messagetemplate.targetuserid_bar_v1":
        res = get_bar_v1(
            "select targetuserid x,count(*) y from vm772_58dd091a279b5392.messagetemplate group by targetuserid",
            "目标用户ID可选用于指定特定用户",
        )
    # tkwkwaskmanagement(任务管理表)->tkwkwaskid(任务ID)

    if obj.get("optype") == "tkwkwaskmanagement.tkwkwaskid_pie":
        res = get_pie(
            "select tkwkwaskid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskmanagement group by tkwkwaskid order by x desc",
            "任务ID",
        )
    if obj.get("optype") == "tkwkwaskmanagement.tkwkwaskid_pie_v1":
        res = get_pie_v1(
            "select tkwkwaskid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskmanagement group by tkwkwaskid",
            "任务ID",
        )
    if obj.get("optype") == "tkwkwaskmanagement.tkwkwaskid_pie_v2":
        res = get_pie_v2(
            "select tkwkwaskid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskmanagement group by tkwkwaskid",
            "任务ID",
        )
    if obj.get("optype") == "tkwkwaskmanagement.tkwkwaskid_line":
        res = get_line(
            "select tkwkwaskid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskmanagement group by tkwkwaskid",
            "任务ID",
        )
    if obj.get("optype") == "tkwkwaskmanagement.tkwkwaskid_bar":
        res = get_bar(
            "select tkwkwaskid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskmanagement group by tkwkwaskid",
            "任务ID",
        )
    if obj.get("optype") == "tkwkwaskmanagement.tkwkwaskid_bar_v1":
        res = get_bar_v1(
            "select tkwkwaskid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskmanagement group by tkwkwaskid",
            "任务ID",
        )
    # tkwkwaskmanagement(任务管理表)->tkwkwaskname(任务名称)

    if obj.get("optype") == "tkwkwaskmanagement.tkwkwaskname_pie":
        res = get_pie(
            "select tkwkwaskname x,count(*) y from vm772_58dd091a279b5392.tkwkwaskmanagement group by tkwkwaskname order by x desc",
            "任务名称",
        )
    if obj.get("optype") == "tkwkwaskmanagement.tkwkwaskname_pie_v1":
        res = get_pie_v1(
            "select tkwkwaskname x,count(*) y from vm772_58dd091a279b5392.tkwkwaskmanagement group by tkwkwaskname",
            "任务名称",
        )
    if obj.get("optype") == "tkwkwaskmanagement.tkwkwaskname_pie_v2":
        res = get_pie_v2(
            "select tkwkwaskname x,count(*) y from vm772_58dd091a279b5392.tkwkwaskmanagement group by tkwkwaskname",
            "任务名称",
        )
    if obj.get("optype") == "tkwkwaskmanagement.tkwkwaskname_line":
        res = get_line(
            "select tkwkwaskname x,count(*) y from vm772_58dd091a279b5392.tkwkwaskmanagement group by tkwkwaskname",
            "任务名称",
        )
    if obj.get("optype") == "tkwkwaskmanagement.tkwkwaskname_bar":
        res = get_bar(
            "select tkwkwaskname x,count(*) y from vm772_58dd091a279b5392.tkwkwaskmanagement group by tkwkwaskname",
            "任务名称",
        )
    if obj.get("optype") == "tkwkwaskmanagement.tkwkwaskname_bar_v1":
        res = get_bar_v1(
            "select tkwkwaskname x,count(*) y from vm772_58dd091a279b5392.tkwkwaskmanagement group by tkwkwaskname",
            "任务名称",
        )
    # tkwkwaskmanagement(任务管理表)->platkwkwfkwkworm(平台)

    if obj.get("optype") == "tkwkwaskmanagement.platkwkwfkwkworm_pie":
        res = get_pie(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.tkwkwaskmanagement group by platkwkwfkwkworm order by x desc",
            "平台",
        )
    if obj.get("optype") == "tkwkwaskmanagement.platkwkwfkwkworm_pie_v1":
        res = get_pie_v1(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.tkwkwaskmanagement group by platkwkwfkwkworm",
            "平台",
        )
    if obj.get("optype") == "tkwkwaskmanagement.platkwkwfkwkworm_pie_v2":
        res = get_pie_v2(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.tkwkwaskmanagement group by platkwkwfkwkworm",
            "平台",
        )
    if obj.get("optype") == "tkwkwaskmanagement.platkwkwfkwkworm_line":
        res = get_line(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.tkwkwaskmanagement group by platkwkwfkwkworm",
            "平台",
        )
    if obj.get("optype") == "tkwkwaskmanagement.platkwkwfkwkworm_bar":
        res = get_bar(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.tkwkwaskmanagement group by platkwkwfkwkworm",
            "平台",
        )
    if obj.get("optype") == "tkwkwaskmanagement.platkwkwfkwkworm_bar_v1":
        res = get_bar_v1(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.tkwkwaskmanagement group by platkwkwfkwkworm",
            "平台",
        )
    # tkwkwaskmanagement(任务管理表)->targetuserid(目标用户ID)

    if obj.get("optype") == "tkwkwaskmanagement.targetuserid_pie":
        res = get_pie(
            "select targetuserid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskmanagement group by targetuserid order by x desc",
            "目标用户ID",
        )
    if obj.get("optype") == "tkwkwaskmanagement.targetuserid_pie_v1":
        res = get_pie_v1(
            "select targetuserid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskmanagement group by targetuserid",
            "目标用户ID",
        )
    if obj.get("optype") == "tkwkwaskmanagement.targetuserid_pie_v2":
        res = get_pie_v2(
            "select targetuserid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskmanagement group by targetuserid",
            "目标用户ID",
        )
    if obj.get("optype") == "tkwkwaskmanagement.targetuserid_line":
        res = get_line(
            "select targetuserid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskmanagement group by targetuserid",
            "目标用户ID",
        )
    if obj.get("optype") == "tkwkwaskmanagement.targetuserid_bar":
        res = get_bar(
            "select targetuserid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskmanagement group by targetuserid",
            "目标用户ID",
        )
    if obj.get("optype") == "tkwkwaskmanagement.targetuserid_bar_v1":
        res = get_bar_v1(
            "select targetuserid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskmanagement group by targetuserid",
            "目标用户ID",
        )
    if obj.get("optype") == "tkwkwaskmanagement.messagecontent_wordcloud":
        textlist = get_data(
            "SELECT messagecontent result FROM vm772_58dd091a279b5392.tkwkwaskmanagement;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "tkwkwaskmanagement.scheduledtime_line":
        res = get_line(
            "select scheduledtime x,count(*) y from vm772_58dd091a279b5392.tkwkwaskmanagement group by scheduledtime order by x",
            "计划执行时间",
        )
    # tkwkwaskmanagement(任务管理表)->status(任务状态)

    if obj.get("optype") == "tkwkwaskmanagement.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm772_58dd091a279b5392.tkwkwaskmanagement group by status order by x desc",
            "任务状态",
        )
    if obj.get("optype") == "tkwkwaskmanagement.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm772_58dd091a279b5392.tkwkwaskmanagement group by status",
            "任务状态",
        )
    if obj.get("optype") == "tkwkwaskmanagement.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm772_58dd091a279b5392.tkwkwaskmanagement group by status",
            "任务状态",
        )
    if obj.get("optype") == "tkwkwaskmanagement.status_line":
        res = get_line(
            "select status x,count(*) y from vm772_58dd091a279b5392.tkwkwaskmanagement group by status",
            "任务状态",
        )
    if obj.get("optype") == "tkwkwaskmanagement.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm772_58dd091a279b5392.tkwkwaskmanagement group by status",
            "任务状态",
        )
    if obj.get("optype") == "tkwkwaskmanagement.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm772_58dd091a279b5392.tkwkwaskmanagement group by status",
            "任务状态",
        )
    if obj.get("optype") == "tkwkwaskmanagement.createdtime_line":
        res = get_line(
            "select createdtime x,count(*) y from vm772_58dd091a279b5392.tkwkwaskmanagement group by createdtime order by x",
            "创建时间",
        )
    if obj.get("optype") == "tkwkwaskmanagement.updatedtime_line":
        res = get_line(
            "select updatedtime x,count(*) y from vm772_58dd091a279b5392.tkwkwaskmanagement group by updatedtime order by x",
            "更新时间",
        )
    # tkwkwaskmanagement(任务管理表)->kwkwassociateduserid(关联用户ID如任务创建者)

    if obj.get("optype") == "tkwkwaskmanagement.kwkwassociateduserid_pie":
        res = get_pie(
            "select kwkwassociateduserid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskmanagement group by kwkwassociateduserid order by x desc",
            "关联用户ID如任务创建者",
        )
    if obj.get("optype") == "tkwkwaskmanagement.kwkwassociateduserid_pie_v1":
        res = get_pie_v1(
            "select kwkwassociateduserid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskmanagement group by kwkwassociateduserid",
            "关联用户ID如任务创建者",
        )
    if obj.get("optype") == "tkwkwaskmanagement.kwkwassociateduserid_pie_v2":
        res = get_pie_v2(
            "select kwkwassociateduserid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskmanagement group by kwkwassociateduserid",
            "关联用户ID如任务创建者",
        )
    if obj.get("optype") == "tkwkwaskmanagement.kwkwassociateduserid_line":
        res = get_line(
            "select kwkwassociateduserid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskmanagement group by kwkwassociateduserid",
            "关联用户ID如任务创建者",
        )
    if obj.get("optype") == "tkwkwaskmanagement.kwkwassociateduserid_bar":
        res = get_bar(
            "select kwkwassociateduserid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskmanagement group by kwkwassociateduserid",
            "关联用户ID如任务创建者",
        )
    if obj.get("optype") == "tkwkwaskmanagement.kwkwassociateduserid_bar_v1":
        res = get_bar_v1(
            "select kwkwassociateduserid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskmanagement group by kwkwassociateduserid",
            "关联用户ID如任务创建者",
        )
    # tkwkwaskexecutionreckwkword(任务执行记录表)->tkwkwaskid(任务ID)

    if obj.get("optype") == "tkwkwaskexecutionreckwkword.tkwkwaskid_pie":
        res = get_pie(
            "select tkwkwaskid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by tkwkwaskid order by x desc",
            "任务ID",
        )
    if obj.get("optype") == "tkwkwaskexecutionreckwkword.tkwkwaskid_pie_v1":
        res = get_pie_v1(
            "select tkwkwaskid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by tkwkwaskid",
            "任务ID",
        )
    if obj.get("optype") == "tkwkwaskexecutionreckwkword.tkwkwaskid_pie_v2":
        res = get_pie_v2(
            "select tkwkwaskid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by tkwkwaskid",
            "任务ID",
        )
    if obj.get("optype") == "tkwkwaskexecutionreckwkword.tkwkwaskid_line":
        res = get_line(
            "select tkwkwaskid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by tkwkwaskid",
            "任务ID",
        )
    if obj.get("optype") == "tkwkwaskexecutionreckwkword.tkwkwaskid_bar":
        res = get_bar(
            "select tkwkwaskid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by tkwkwaskid",
            "任务ID",
        )
    if obj.get("optype") == "tkwkwaskexecutionreckwkword.tkwkwaskid_bar_v1":
        res = get_bar_v1(
            "select tkwkwaskid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by tkwkwaskid",
            "任务ID",
        )
    if obj.get("optype") == "tkwkwaskexecutionreckwkword.executiontime_line":
        res = get_line(
            "select executiontime x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by executiontime order by x",
            "执行时间",
        )
    # tkwkwaskexecutionreckwkword(任务执行记录表)->status(执行状态)

    if obj.get("optype") == "tkwkwaskexecutionreckwkword.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by status order by x desc",
            "执行状态",
        )
    if obj.get("optype") == "tkwkwaskexecutionreckwkword.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by status",
            "执行状态",
        )
    if obj.get("optype") == "tkwkwaskexecutionreckwkword.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by status",
            "执行状态",
        )
    if obj.get("optype") == "tkwkwaskexecutionreckwkword.status_line":
        res = get_line(
            "select status x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by status",
            "执行状态",
        )
    if obj.get("optype") == "tkwkwaskexecutionreckwkword.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by status",
            "执行状态",
        )
    if obj.get("optype") == "tkwkwaskexecutionreckwkword.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by status",
            "执行状态",
        )
    # tkwkwaskexecutionreckwkword(任务执行记录表)->userid(用户ID)

    if obj.get("optype") == "tkwkwaskexecutionreckwkword.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by userid order by x desc",
            "用户ID",
        )
    if obj.get("optype") == "tkwkwaskexecutionreckwkword.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by userid",
            "用户ID",
        )
    if obj.get("optype") == "tkwkwaskexecutionreckwkword.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by userid",
            "用户ID",
        )
    if obj.get("optype") == "tkwkwaskexecutionreckwkword.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by userid",
            "用户ID",
        )
    if obj.get("optype") == "tkwkwaskexecutionreckwkword.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by userid",
            "用户ID",
        )
    if obj.get("optype") == "tkwkwaskexecutionreckwkword.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by userid",
            "用户ID",
        )
    # tkwkwaskexecutionreckwkword(任务执行记录表)->platkwkwfkwkworm(平台)

    if obj.get("optype") == "tkwkwaskexecutionreckwkword.platkwkwfkwkworm_pie":
        res = get_pie(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by platkwkwfkwkworm order by x desc",
            "平台",
        )
    if obj.get("optype") == "tkwkwaskexecutionreckwkword.platkwkwfkwkworm_pie_v1":
        res = get_pie_v1(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by platkwkwfkwkworm",
            "平台",
        )
    if obj.get("optype") == "tkwkwaskexecutionreckwkword.platkwkwfkwkworm_pie_v2":
        res = get_pie_v2(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by platkwkwfkwkworm",
            "平台",
        )
    if obj.get("optype") == "tkwkwaskexecutionreckwkword.platkwkwfkwkworm_line":
        res = get_line(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by platkwkwfkwkworm",
            "平台",
        )
    if obj.get("optype") == "tkwkwaskexecutionreckwkword.platkwkwfkwkworm_bar":
        res = get_bar(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by platkwkwfkwkworm",
            "平台",
        )
    if obj.get("optype") == "tkwkwaskexecutionreckwkword.platkwkwfkwkworm_bar_v1":
        res = get_bar_v1(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by platkwkwfkwkworm",
            "平台",
        )
    if obj.get("optype") == "tkwkwaskexecutionreckwkword.messagecontent_wordcloud":
        textlist = get_data(
            "SELECT messagecontent result FROM vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # tkwkwaskexecutionreckwkword(任务执行记录表)->recipientid(接收者ID)

    if obj.get("optype") == "tkwkwaskexecutionreckwkword.recipientid_pie":
        res = get_pie(
            "select recipientid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by recipientid order by x desc",
            "接收者ID",
        )
    if obj.get("optype") == "tkwkwaskexecutionreckwkword.recipientid_pie_v1":
        res = get_pie_v1(
            "select recipientid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by recipientid",
            "接收者ID",
        )
    if obj.get("optype") == "tkwkwaskexecutionreckwkword.recipientid_pie_v2":
        res = get_pie_v2(
            "select recipientid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by recipientid",
            "接收者ID",
        )
    if obj.get("optype") == "tkwkwaskexecutionreckwkword.recipientid_line":
        res = get_line(
            "select recipientid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by recipientid",
            "接收者ID",
        )
    if obj.get("optype") == "tkwkwaskexecutionreckwkword.recipientid_bar":
        res = get_bar(
            "select recipientid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by recipientid",
            "接收者ID",
        )
    if obj.get("optype") == "tkwkwaskexecutionreckwkword.recipientid_bar_v1":
        res = get_bar_v1(
            "select recipientid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by recipientid",
            "接收者ID",
        )
    # tkwkwaskexecutionreckwkword(任务执行记录表)->senderid(发送者ID)

    if obj.get("optype") == "tkwkwaskexecutionreckwkword.senderid_pie":
        res = get_pie(
            "select senderid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by senderid order by x desc",
            "发送者ID",
        )
    if obj.get("optype") == "tkwkwaskexecutionreckwkword.senderid_pie_v1":
        res = get_pie_v1(
            "select senderid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by senderid",
            "发送者ID",
        )
    if obj.get("optype") == "tkwkwaskexecutionreckwkword.senderid_pie_v2":
        res = get_pie_v2(
            "select senderid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by senderid",
            "发送者ID",
        )
    if obj.get("optype") == "tkwkwaskexecutionreckwkword.senderid_line":
        res = get_line(
            "select senderid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by senderid",
            "发送者ID",
        )
    if obj.get("optype") == "tkwkwaskexecutionreckwkword.senderid_bar":
        res = get_bar(
            "select senderid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by senderid",
            "发送者ID",
        )
    if obj.get("optype") == "tkwkwaskexecutionreckwkword.senderid_bar_v1":
        res = get_bar_v1(
            "select senderid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by senderid",
            "发送者ID",
        )
    # tkwkwaskexecutionreckwkword(任务执行记录表)->tkwkwasktemplateid(任务模板ID)

    if obj.get("optype") == "tkwkwaskexecutionreckwkword.tkwkwasktemplateid_pie":
        res = get_pie(
            "select tkwkwasktemplateid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by tkwkwasktemplateid order by x desc",
            "任务模板ID",
        )
    if obj.get("optype") == "tkwkwaskexecutionreckwkword.tkwkwasktemplateid_pie_v1":
        res = get_pie_v1(
            "select tkwkwasktemplateid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by tkwkwasktemplateid",
            "任务模板ID",
        )
    if obj.get("optype") == "tkwkwaskexecutionreckwkword.tkwkwasktemplateid_pie_v2":
        res = get_pie_v2(
            "select tkwkwasktemplateid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by tkwkwasktemplateid",
            "任务模板ID",
        )
    if obj.get("optype") == "tkwkwaskexecutionreckwkword.tkwkwasktemplateid_line":
        res = get_line(
            "select tkwkwasktemplateid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by tkwkwasktemplateid",
            "任务模板ID",
        )
    if obj.get("optype") == "tkwkwaskexecutionreckwkword.tkwkwasktemplateid_bar":
        res = get_bar(
            "select tkwkwasktemplateid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by tkwkwasktemplateid",
            "任务模板ID",
        )
    if obj.get("optype") == "tkwkwaskexecutionreckwkword.tkwkwasktemplateid_bar_v1":
        res = get_bar_v1(
            "select tkwkwasktemplateid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by tkwkwasktemplateid",
            "任务模板ID",
        )
    # tkwkwaskexecutionreckwkword(任务执行记录表)->errkwkwormessage(错误信息)

    if obj.get("optype") == "tkwkwaskexecutionreckwkword.errkwkwormessage_pie":
        res = get_pie(
            "select errkwkwormessage x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by errkwkwormessage order by x desc",
            "错误信息",
        )
    if obj.get("optype") == "tkwkwaskexecutionreckwkword.errkwkwormessage_pie_v1":
        res = get_pie_v1(
            "select errkwkwormessage x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by errkwkwormessage",
            "错误信息",
        )
    if obj.get("optype") == "tkwkwaskexecutionreckwkword.errkwkwormessage_pie_v2":
        res = get_pie_v2(
            "select errkwkwormessage x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by errkwkwormessage",
            "错误信息",
        )
    if obj.get("optype") == "tkwkwaskexecutionreckwkword.errkwkwormessage_line":
        res = get_line(
            "select errkwkwormessage x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by errkwkwormessage",
            "错误信息",
        )
    if obj.get("optype") == "tkwkwaskexecutionreckwkword.errkwkwormessage_bar":
        res = get_bar(
            "select errkwkwormessage x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by errkwkwormessage",
            "错误信息",
        )
    if obj.get("optype") == "tkwkwaskexecutionreckwkword.errkwkwormessage_bar_v1":
        res = get_bar_v1(
            "select errkwkwormessage x,count(*) y from vm772_58dd091a279b5392.tkwkwaskexecutionreckwkword group by errkwkwormessage",
            "错误信息",
        )
    # tkwkwaskstatus(任务状态表)->tkwkwaskid(任务ID)

    if obj.get("optype") == "tkwkwaskstatus.tkwkwaskid_pie":
        res = get_pie(
            "select tkwkwaskid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskstatus group by tkwkwaskid order by x desc",
            "任务ID",
        )
    if obj.get("optype") == "tkwkwaskstatus.tkwkwaskid_pie_v1":
        res = get_pie_v1(
            "select tkwkwaskid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskstatus group by tkwkwaskid",
            "任务ID",
        )
    if obj.get("optype") == "tkwkwaskstatus.tkwkwaskid_pie_v2":
        res = get_pie_v2(
            "select tkwkwaskid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskstatus group by tkwkwaskid",
            "任务ID",
        )
    if obj.get("optype") == "tkwkwaskstatus.tkwkwaskid_line":
        res = get_line(
            "select tkwkwaskid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskstatus group by tkwkwaskid",
            "任务ID",
        )
    if obj.get("optype") == "tkwkwaskstatus.tkwkwaskid_bar":
        res = get_bar(
            "select tkwkwaskid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskstatus group by tkwkwaskid",
            "任务ID",
        )
    if obj.get("optype") == "tkwkwaskstatus.tkwkwaskid_bar_v1":
        res = get_bar_v1(
            "select tkwkwaskid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskstatus group by tkwkwaskid",
            "任务ID",
        )
    # tkwkwaskstatus(任务状态表)->statuscode(状态码)

    if obj.get("optype") == "tkwkwaskstatus.statuscode_pie":
        res = get_pie(
            "select statuscode x,count(*) y from vm772_58dd091a279b5392.tkwkwaskstatus group by statuscode order by x desc",
            "状态码",
        )
    if obj.get("optype") == "tkwkwaskstatus.statuscode_pie_v1":
        res = get_pie_v1(
            "select statuscode x,count(*) y from vm772_58dd091a279b5392.tkwkwaskstatus group by statuscode",
            "状态码",
        )
    if obj.get("optype") == "tkwkwaskstatus.statuscode_pie_v2":
        res = get_pie_v2(
            "select statuscode x,count(*) y from vm772_58dd091a279b5392.tkwkwaskstatus group by statuscode",
            "状态码",
        )
    if obj.get("optype") == "tkwkwaskstatus.statuscode_line":
        res = get_line(
            "select statuscode x,count(*) y from vm772_58dd091a279b5392.tkwkwaskstatus group by statuscode",
            "状态码",
        )
    if obj.get("optype") == "tkwkwaskstatus.statuscode_bar":
        res = get_bar(
            "select statuscode x,count(*) y from vm772_58dd091a279b5392.tkwkwaskstatus group by statuscode",
            "状态码",
        )
    if obj.get("optype") == "tkwkwaskstatus.statuscode_bar_v1":
        res = get_bar_v1(
            "select statuscode x,count(*) y from vm772_58dd091a279b5392.tkwkwaskstatus group by statuscode",
            "状态码",
        )
    # tkwkwaskstatus(任务状态表)->statusname(状态名称)

    if obj.get("optype") == "tkwkwaskstatus.statusname_pie":
        res = get_pie(
            "select statusname x,count(*) y from vm772_58dd091a279b5392.tkwkwaskstatus group by statusname order by x desc",
            "状态名称",
        )
    if obj.get("optype") == "tkwkwaskstatus.statusname_pie_v1":
        res = get_pie_v1(
            "select statusname x,count(*) y from vm772_58dd091a279b5392.tkwkwaskstatus group by statusname",
            "状态名称",
        )
    if obj.get("optype") == "tkwkwaskstatus.statusname_pie_v2":
        res = get_pie_v2(
            "select statusname x,count(*) y from vm772_58dd091a279b5392.tkwkwaskstatus group by statusname",
            "状态名称",
        )
    if obj.get("optype") == "tkwkwaskstatus.statusname_line":
        res = get_line(
            "select statusname x,count(*) y from vm772_58dd091a279b5392.tkwkwaskstatus group by statusname",
            "状态名称",
        )
    if obj.get("optype") == "tkwkwaskstatus.statusname_bar":
        res = get_bar(
            "select statusname x,count(*) y from vm772_58dd091a279b5392.tkwkwaskstatus group by statusname",
            "状态名称",
        )
    if obj.get("optype") == "tkwkwaskstatus.statusname_bar_v1":
        res = get_bar_v1(
            "select statusname x,count(*) y from vm772_58dd091a279b5392.tkwkwaskstatus group by statusname",
            "状态名称",
        )
    if obj.get("optype") == "tkwkwaskstatus.createdat_line":
        res = get_line(
            "select createdat x,count(*) y from vm772_58dd091a279b5392.tkwkwaskstatus group by createdat order by x",
            "创建时间",
        )
    if obj.get("optype") == "tkwkwaskstatus.updatedat_line":
        res = get_line(
            "select updatedat x,count(*) y from vm772_58dd091a279b5392.tkwkwaskstatus group by updatedat order by x",
            "更新时间",
        )
    if obj.get("optype") == "tkwkwaskstatus.completedat_line":
        res = get_line(
            "select completedat x,count(*) y from vm772_58dd091a279b5392.tkwkwaskstatus group by completedat order by x",
            "完成时间",
        )
    # tkwkwaskstatus(任务状态表)->userid(用户ID)

    if obj.get("optype") == "tkwkwaskstatus.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskstatus group by userid order by x desc",
            "用户ID",
        )
    if obj.get("optype") == "tkwkwaskstatus.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskstatus group by userid",
            "用户ID",
        )
    if obj.get("optype") == "tkwkwaskstatus.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskstatus group by userid",
            "用户ID",
        )
    if obj.get("optype") == "tkwkwaskstatus.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskstatus group by userid",
            "用户ID",
        )
    if obj.get("optype") == "tkwkwaskstatus.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskstatus group by userid",
            "用户ID",
        )
    if obj.get("optype") == "tkwkwaskstatus.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskstatus group by userid",
            "用户ID",
        )
    # tkwkwaskstatus(任务状态表)->platkwkwfkwkwormid(平台ID)

    if obj.get("optype") == "tkwkwaskstatus.platkwkwfkwkwormid_pie":
        res = get_pie(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskstatus group by platkwkwfkwkwormid order by x desc",
            "平台ID",
        )
    if obj.get("optype") == "tkwkwaskstatus.platkwkwfkwkwormid_pie_v1":
        res = get_pie_v1(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskstatus group by platkwkwfkwkwormid",
            "平台ID",
        )
    if obj.get("optype") == "tkwkwaskstatus.platkwkwfkwkwormid_pie_v2":
        res = get_pie_v2(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskstatus group by platkwkwfkwkwormid",
            "平台ID",
        )
    if obj.get("optype") == "tkwkwaskstatus.platkwkwfkwkwormid_line":
        res = get_line(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskstatus group by platkwkwfkwkwormid",
            "平台ID",
        )
    if obj.get("optype") == "tkwkwaskstatus.platkwkwfkwkwormid_bar":
        res = get_bar(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskstatus group by platkwkwfkwkwormid",
            "平台ID",
        )
    if obj.get("optype") == "tkwkwaskstatus.platkwkwfkwkwormid_bar_v1":
        res = get_bar_v1(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.tkwkwaskstatus group by platkwkwfkwkwormid",
            "平台ID",
        )
    if obj.get("optype") == "tkwkwaskstatus.messagecontent_wordcloud":
        textlist = get_data(
            "SELECT messagecontent result FROM vm772_58dd091a279b5392.tkwkwaskstatus;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # tkwkwaskstatus(任务状态表)->kwkwisactive(是否激活)

    if obj.get("optype") == "tkwkwaskstatus.kwkwisactive_pie":
        res = get_pie(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.tkwkwaskstatus group by kwkwisactive order by x desc",
            "是否激活",
        )
    if obj.get("optype") == "tkwkwaskstatus.kwkwisactive_pie_v1":
        res = get_pie_v1(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.tkwkwaskstatus group by kwkwisactive",
            "是否激活",
        )
    if obj.get("optype") == "tkwkwaskstatus.kwkwisactive_pie_v2":
        res = get_pie_v2(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.tkwkwaskstatus group by kwkwisactive",
            "是否激活",
        )
    if obj.get("optype") == "tkwkwaskstatus.kwkwisactive_line":
        res = get_line(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.tkwkwaskstatus group by kwkwisactive",
            "是否激活",
        )
    if obj.get("optype") == "tkwkwaskstatus.kwkwisactive_bar":
        res = get_bar(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.tkwkwaskstatus group by kwkwisactive",
            "是否激活",
        )
    if obj.get("optype") == "tkwkwaskstatus.kwkwisactive_bar_v1":
        res = get_bar_v1(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.tkwkwaskstatus group by kwkwisactive",
            "是否激活",
        )
    # scheduledtkwkwask(定时任务表)->tkwkwaskid(任务ID)

    if obj.get("optype") == "scheduledtkwkwask.tkwkwaskid_pie":
        res = get_pie(
            "select tkwkwaskid x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by tkwkwaskid order by x desc",
            "任务ID",
        )
    if obj.get("optype") == "scheduledtkwkwask.tkwkwaskid_pie_v1":
        res = get_pie_v1(
            "select tkwkwaskid x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by tkwkwaskid",
            "任务ID",
        )
    if obj.get("optype") == "scheduledtkwkwask.tkwkwaskid_pie_v2":
        res = get_pie_v2(
            "select tkwkwaskid x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by tkwkwaskid",
            "任务ID",
        )
    if obj.get("optype") == "scheduledtkwkwask.tkwkwaskid_line":
        res = get_line(
            "select tkwkwaskid x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by tkwkwaskid",
            "任务ID",
        )
    if obj.get("optype") == "scheduledtkwkwask.tkwkwaskid_bar":
        res = get_bar(
            "select tkwkwaskid x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by tkwkwaskid",
            "任务ID",
        )
    if obj.get("optype") == "scheduledtkwkwask.tkwkwaskid_bar_v1":
        res = get_bar_v1(
            "select tkwkwaskid x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by tkwkwaskid",
            "任务ID",
        )
    # scheduledtkwkwask(定时任务表)->tkwkwaskname(任务名称)

    if obj.get("optype") == "scheduledtkwkwask.tkwkwaskname_pie":
        res = get_pie(
            "select tkwkwaskname x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by tkwkwaskname order by x desc",
            "任务名称",
        )
    if obj.get("optype") == "scheduledtkwkwask.tkwkwaskname_pie_v1":
        res = get_pie_v1(
            "select tkwkwaskname x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by tkwkwaskname",
            "任务名称",
        )
    if obj.get("optype") == "scheduledtkwkwask.tkwkwaskname_pie_v2":
        res = get_pie_v2(
            "select tkwkwaskname x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by tkwkwaskname",
            "任务名称",
        )
    if obj.get("optype") == "scheduledtkwkwask.tkwkwaskname_line":
        res = get_line(
            "select tkwkwaskname x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by tkwkwaskname",
            "任务名称",
        )
    if obj.get("optype") == "scheduledtkwkwask.tkwkwaskname_bar":
        res = get_bar(
            "select tkwkwaskname x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by tkwkwaskname",
            "任务名称",
        )
    if obj.get("optype") == "scheduledtkwkwask.tkwkwaskname_bar_v1":
        res = get_bar_v1(
            "select tkwkwaskname x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by tkwkwaskname",
            "任务名称",
        )
    # scheduledtkwkwask(定时任务表)->targetplatkwkwfkwkworm(目标平台)

    if obj.get("optype") == "scheduledtkwkwask.targetplatkwkwfkwkworm_pie":
        res = get_pie(
            "select targetplatkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by targetplatkwkwfkwkworm order by x desc",
            "目标平台",
        )
    if obj.get("optype") == "scheduledtkwkwask.targetplatkwkwfkwkworm_pie_v1":
        res = get_pie_v1(
            "select targetplatkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by targetplatkwkwfkwkworm",
            "目标平台",
        )
    if obj.get("optype") == "scheduledtkwkwask.targetplatkwkwfkwkworm_pie_v2":
        res = get_pie_v2(
            "select targetplatkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by targetplatkwkwfkwkworm",
            "目标平台",
        )
    if obj.get("optype") == "scheduledtkwkwask.targetplatkwkwfkwkworm_line":
        res = get_line(
            "select targetplatkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by targetplatkwkwfkwkworm",
            "目标平台",
        )
    if obj.get("optype") == "scheduledtkwkwask.targetplatkwkwfkwkworm_bar":
        res = get_bar(
            "select targetplatkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by targetplatkwkwfkwkworm",
            "目标平台",
        )
    if obj.get("optype") == "scheduledtkwkwask.targetplatkwkwfkwkworm_bar_v1":
        res = get_bar_v1(
            "select targetplatkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by targetplatkwkwfkwkworm",
            "目标平台",
        )
    if obj.get("optype") == "scheduledtkwkwask.scheduletime_line":
        res = get_line(
            "select scheduletime x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by scheduletime order by x",
            "计划执行时间",
        )
    # scheduledtkwkwask(定时任务表)->executestatus(执行状态)

    if obj.get("optype") == "scheduledtkwkwask.executestatus_pie":
        res = get_pie(
            "select executestatus x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by executestatus order by x desc",
            "执行状态",
        )
    if obj.get("optype") == "scheduledtkwkwask.executestatus_pie_v1":
        res = get_pie_v1(
            "select executestatus x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by executestatus",
            "执行状态",
        )
    if obj.get("optype") == "scheduledtkwkwask.executestatus_pie_v2":
        res = get_pie_v2(
            "select executestatus x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by executestatus",
            "执行状态",
        )
    if obj.get("optype") == "scheduledtkwkwask.executestatus_line":
        res = get_line(
            "select executestatus x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by executestatus",
            "执行状态",
        )
    if obj.get("optype") == "scheduledtkwkwask.executestatus_bar":
        res = get_bar(
            "select executestatus x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by executestatus",
            "执行状态",
        )
    if obj.get("optype") == "scheduledtkwkwask.executestatus_bar_v1":
        res = get_bar_v1(
            "select executestatus x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by executestatus",
            "执行状态",
        )
    # scheduledtkwkwask(定时任务表)->lkwkwasterrkwkwor(最近一次错误信息)

    if obj.get("optype") == "scheduledtkwkwask.lkwkwasterrkwkwor_pie":
        res = get_pie(
            "select lkwkwasterrkwkwor x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by lkwkwasterrkwkwor order by x desc",
            "最近一次错误信息",
        )
    if obj.get("optype") == "scheduledtkwkwask.lkwkwasterrkwkwor_pie_v1":
        res = get_pie_v1(
            "select lkwkwasterrkwkwor x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by lkwkwasterrkwkwor",
            "最近一次错误信息",
        )
    if obj.get("optype") == "scheduledtkwkwask.lkwkwasterrkwkwor_pie_v2":
        res = get_pie_v2(
            "select lkwkwasterrkwkwor x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by lkwkwasterrkwkwor",
            "最近一次错误信息",
        )
    if obj.get("optype") == "scheduledtkwkwask.lkwkwasterrkwkwor_line":
        res = get_line(
            "select lkwkwasterrkwkwor x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by lkwkwasterrkwkwor",
            "最近一次错误信息",
        )
    if obj.get("optype") == "scheduledtkwkwask.lkwkwasterrkwkwor_bar":
        res = get_bar(
            "select lkwkwasterrkwkwor x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by lkwkwasterrkwkwor",
            "最近一次错误信息",
        )
    if obj.get("optype") == "scheduledtkwkwask.lkwkwasterrkwkwor_bar_v1":
        res = get_bar_v1(
            "select lkwkwasterrkwkwor x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by lkwkwasterrkwkwor",
            "最近一次错误信息",
        )
    # scheduledtkwkwask(定时任务表)->creatkwkwor(创建者)

    if obj.get("optype") == "scheduledtkwkwask.creatkwkwor_pie":
        res = get_pie(
            "select creatkwkwor x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by creatkwkwor order by x desc",
            "创建者",
        )
    if obj.get("optype") == "scheduledtkwkwask.creatkwkwor_pie_v1":
        res = get_pie_v1(
            "select creatkwkwor x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by creatkwkwor",
            "创建者",
        )
    if obj.get("optype") == "scheduledtkwkwask.creatkwkwor_pie_v2":
        res = get_pie_v2(
            "select creatkwkwor x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by creatkwkwor",
            "创建者",
        )
    if obj.get("optype") == "scheduledtkwkwask.creatkwkwor_line":
        res = get_line(
            "select creatkwkwor x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by creatkwkwor",
            "创建者",
        )
    if obj.get("optype") == "scheduledtkwkwask.creatkwkwor_bar":
        res = get_bar(
            "select creatkwkwor x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by creatkwkwor",
            "创建者",
        )
    if obj.get("optype") == "scheduledtkwkwask.creatkwkwor_bar_v1":
        res = get_bar_v1(
            "select creatkwkwor x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by creatkwkwor",
            "创建者",
        )
    if obj.get("optype") == "scheduledtkwkwask.createtime_line":
        res = get_line(
            "select createtime x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by createtime order by x",
            "创建时间",
        )
    if obj.get("optype") == "scheduledtkwkwask.updatetime_line":
        res = get_line(
            "select updatetime x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by updatetime order by x",
            "更新时间",
        )
    # scheduledtkwkwask(定时任务表)->relateduserid(关联用户ID)

    if obj.get("optype") == "scheduledtkwkwask.relateduserid_pie":
        res = get_pie(
            "select relateduserid x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by relateduserid order by x desc",
            "关联用户ID",
        )
    if obj.get("optype") == "scheduledtkwkwask.relateduserid_pie_v1":
        res = get_pie_v1(
            "select relateduserid x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by relateduserid",
            "关联用户ID",
        )
    if obj.get("optype") == "scheduledtkwkwask.relateduserid_pie_v2":
        res = get_pie_v2(
            "select relateduserid x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by relateduserid",
            "关联用户ID",
        )
    if obj.get("optype") == "scheduledtkwkwask.relateduserid_line":
        res = get_line(
            "select relateduserid x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by relateduserid",
            "关联用户ID",
        )
    if obj.get("optype") == "scheduledtkwkwask.relateduserid_bar":
        res = get_bar(
            "select relateduserid x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by relateduserid",
            "关联用户ID",
        )
    if obj.get("optype") == "scheduledtkwkwask.relateduserid_bar_v1":
        res = get_bar_v1(
            "select relateduserid x,count(*) y from vm772_58dd091a279b5392.scheduledtkwkwask group by relateduserid",
            "关联用户ID",
        )
    # messagesendreckwkword(消息发送记录表)->platkwkwfkwkwormid(平台ID关联字段指向不同社交媒体或消息平台的ID)

    if obj.get("optype") == "messagesendreckwkword.platkwkwfkwkwormid_pie":
        res = get_pie(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.messagesendreckwkword group by platkwkwfkwkwormid order by x desc",
            "平台ID关联字段指向不同社交媒体或消息平台的ID",
        )
    if obj.get("optype") == "messagesendreckwkword.platkwkwfkwkwormid_pie_v1":
        res = get_pie_v1(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.messagesendreckwkword group by platkwkwfkwkwormid",
            "平台ID关联字段指向不同社交媒体或消息平台的ID",
        )
    if obj.get("optype") == "messagesendreckwkword.platkwkwfkwkwormid_pie_v2":
        res = get_pie_v2(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.messagesendreckwkword group by platkwkwfkwkwormid",
            "平台ID关联字段指向不同社交媒体或消息平台的ID",
        )
    if obj.get("optype") == "messagesendreckwkword.platkwkwfkwkwormid_line":
        res = get_line(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.messagesendreckwkword group by platkwkwfkwkwormid",
            "平台ID关联字段指向不同社交媒体或消息平台的ID",
        )
    if obj.get("optype") == "messagesendreckwkword.platkwkwfkwkwormid_bar":
        res = get_bar(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.messagesendreckwkword group by platkwkwfkwkwormid",
            "平台ID关联字段指向不同社交媒体或消息平台的ID",
        )
    if obj.get("optype") == "messagesendreckwkword.platkwkwfkwkwormid_bar_v1":
        res = get_bar_v1(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.messagesendreckwkword group by platkwkwfkwkwormid",
            "平台ID关联字段指向不同社交媒体或消息平台的ID",
        )
    # messagesendreckwkword(消息发送记录表)->userid(用户ID关联字段指向系统中用户的ID)

    if obj.get("optype") == "messagesendreckwkword.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagesendreckwkword group by userid order by x desc",
            "用户ID关联字段指向系统中用户的ID",
        )
    if obj.get("optype") == "messagesendreckwkword.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagesendreckwkword group by userid",
            "用户ID关联字段指向系统中用户的ID",
        )
    if obj.get("optype") == "messagesendreckwkword.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagesendreckwkword group by userid",
            "用户ID关联字段指向系统中用户的ID",
        )
    if obj.get("optype") == "messagesendreckwkword.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagesendreckwkword group by userid",
            "用户ID关联字段指向系统中用户的ID",
        )
    if obj.get("optype") == "messagesendreckwkword.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagesendreckwkword group by userid",
            "用户ID关联字段指向系统中用户的ID",
        )
    if obj.get("optype") == "messagesendreckwkword.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagesendreckwkword group by userid",
            "用户ID关联字段指向系统中用户的ID",
        )
    # messagesendreckwkword(消息发送记录表)->targetuserid(目标用户ID如果是私信则为目标接收者的ID)

    if obj.get("optype") == "messagesendreckwkword.targetuserid_pie":
        res = get_pie(
            "select targetuserid x,count(*) y from vm772_58dd091a279b5392.messagesendreckwkword group by targetuserid order by x desc",
            "目标用户ID如果是私信则为目标接收者的ID",
        )
    if obj.get("optype") == "messagesendreckwkword.targetuserid_pie_v1":
        res = get_pie_v1(
            "select targetuserid x,count(*) y from vm772_58dd091a279b5392.messagesendreckwkword group by targetuserid",
            "目标用户ID如果是私信则为目标接收者的ID",
        )
    if obj.get("optype") == "messagesendreckwkword.targetuserid_pie_v2":
        res = get_pie_v2(
            "select targetuserid x,count(*) y from vm772_58dd091a279b5392.messagesendreckwkword group by targetuserid",
            "目标用户ID如果是私信则为目标接收者的ID",
        )
    if obj.get("optype") == "messagesendreckwkword.targetuserid_line":
        res = get_line(
            "select targetuserid x,count(*) y from vm772_58dd091a279b5392.messagesendreckwkword group by targetuserid",
            "目标用户ID如果是私信则为目标接收者的ID",
        )
    if obj.get("optype") == "messagesendreckwkword.targetuserid_bar":
        res = get_bar(
            "select targetuserid x,count(*) y from vm772_58dd091a279b5392.messagesendreckwkword group by targetuserid",
            "目标用户ID如果是私信则为目标接收者的ID",
        )
    if obj.get("optype") == "messagesendreckwkword.targetuserid_bar_v1":
        res = get_bar_v1(
            "select targetuserid x,count(*) y from vm772_58dd091a279b5392.messagesendreckwkword group by targetuserid",
            "目标用户ID如果是私信则为目标接收者的ID",
        )
    if obj.get("optype") == "messagesendreckwkword.messagecontent_wordcloud":
        textlist = get_data(
            "SELECT messagecontent result FROM vm772_58dd091a279b5392.messagesendreckwkword;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "messagesendreckwkword.sendtime_line":
        res = get_line(
            "select sendtime x,count(*) y from vm772_58dd091a279b5392.messagesendreckwkword group by sendtime order by x",
            "发送时间",
        )
    # messagesendreckwkword(消息发送记录表)->status(发送状态如待发送、发送中、已发送、发送失败)

    if obj.get("optype") == "messagesendreckwkword.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagesendreckwkword group by status order by x desc",
            "发送状态如待发送、发送中、已发送、发送失败",
        )
    if obj.get("optype") == "messagesendreckwkword.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagesendreckwkword group by status",
            "发送状态如待发送、发送中、已发送、发送失败",
        )
    if obj.get("optype") == "messagesendreckwkword.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagesendreckwkword group by status",
            "发送状态如待发送、发送中、已发送、发送失败",
        )
    if obj.get("optype") == "messagesendreckwkword.status_line":
        res = get_line(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagesendreckwkword group by status",
            "发送状态如待发送、发送中、已发送、发送失败",
        )
    if obj.get("optype") == "messagesendreckwkword.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagesendreckwkword group by status",
            "发送状态如待发送、发送中、已发送、发送失败",
        )
    if obj.get("optype") == "messagesendreckwkword.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagesendreckwkword group by status",
            "发送状态如待发送、发送中、已发送、发送失败",
        )
    # messagesendreckwkword(消息发送记录表)->rekwkwtrycount(重试次数记录消息发送失败后的重试次数)

    if obj.get("optype") == "messagesendreckwkword.rekwkwtrycount_pie":
        res = get_pie(
            "select rekwkwtrycount x,count(*) y from vm772_58dd091a279b5392.messagesendreckwkword group by rekwkwtrycount order by x desc",
            "重试次数记录消息发送失败后的重试次数",
        )
    if obj.get("optype") == "messagesendreckwkword.rekwkwtrycount_pie_v1":
        res = get_pie_v1(
            "select rekwkwtrycount x,count(*) y from vm772_58dd091a279b5392.messagesendreckwkword group by rekwkwtrycount",
            "重试次数记录消息发送失败后的重试次数",
        )
    if obj.get("optype") == "messagesendreckwkword.rekwkwtrycount_pie_v2":
        res = get_pie_v2(
            "select rekwkwtrycount x,count(*) y from vm772_58dd091a279b5392.messagesendreckwkword group by rekwkwtrycount",
            "重试次数记录消息发送失败后的重试次数",
        )
    if obj.get("optype") == "messagesendreckwkword.rekwkwtrycount_line":
        res = get_line(
            "select rekwkwtrycount x,count(*) y from vm772_58dd091a279b5392.messagesendreckwkword group by rekwkwtrycount",
            "重试次数记录消息发送失败后的重试次数",
        )
    if obj.get("optype") == "messagesendreckwkword.rekwkwtrycount_bar":
        res = get_bar(
            "select rekwkwtrycount x,count(*) y from vm772_58dd091a279b5392.messagesendreckwkword group by rekwkwtrycount",
            "重试次数记录消息发送失败后的重试次数",
        )
    if obj.get("optype") == "messagesendreckwkword.rekwkwtrycount_bar_v1":
        res = get_bar_v1(
            "select rekwkwtrycount x,count(*) y from vm772_58dd091a279b5392.messagesendreckwkword group by rekwkwtrycount",
            "重试次数记录消息发送失败后的重试次数",
        )
    if obj.get("optype") == "messagesendreckwkword.lkwkwastrekwkwtrytime_line":
        res = get_line(
            "select lkwkwastrekwkwtrytime x,count(*) y from vm772_58dd091a279b5392.messagesendreckwkword group by lkwkwastrekwkwtrytime order by x",
            "上次重试时间记录最后一次尝试发送的时间",
        )
    # messagesendreckwkword(消息发送记录表)->errkwkwormessage(错误信息如果发送失败记录失败的具体原因)

    if obj.get("optype") == "messagesendreckwkword.errkwkwormessage_pie":
        res = get_pie(
            "select errkwkwormessage x,count(*) y from vm772_58dd091a279b5392.messagesendreckwkword group by errkwkwormessage order by x desc",
            "错误信息如果发送失败记录失败的具体原因",
        )
    if obj.get("optype") == "messagesendreckwkword.errkwkwormessage_pie_v1":
        res = get_pie_v1(
            "select errkwkwormessage x,count(*) y from vm772_58dd091a279b5392.messagesendreckwkword group by errkwkwormessage",
            "错误信息如果发送失败记录失败的具体原因",
        )
    if obj.get("optype") == "messagesendreckwkword.errkwkwormessage_pie_v2":
        res = get_pie_v2(
            "select errkwkwormessage x,count(*) y from vm772_58dd091a279b5392.messagesendreckwkword group by errkwkwormessage",
            "错误信息如果发送失败记录失败的具体原因",
        )
    if obj.get("optype") == "messagesendreckwkword.errkwkwormessage_line":
        res = get_line(
            "select errkwkwormessage x,count(*) y from vm772_58dd091a279b5392.messagesendreckwkword group by errkwkwormessage",
            "错误信息如果发送失败记录失败的具体原因",
        )
    if obj.get("optype") == "messagesendreckwkword.errkwkwormessage_bar":
        res = get_bar(
            "select errkwkwormessage x,count(*) y from vm772_58dd091a279b5392.messagesendreckwkword group by errkwkwormessage",
            "错误信息如果发送失败记录失败的具体原因",
        )
    if obj.get("optype") == "messagesendreckwkword.errkwkwormessage_bar_v1":
        res = get_bar_v1(
            "select errkwkwormessage x,count(*) y from vm772_58dd091a279b5392.messagesendreckwkword group by errkwkwormessage",
            "错误信息如果发送失败记录失败的具体原因",
        )
    # messagereceivereckwkword(消息接收记录表)->userid(用户ID关联用户)

    if obj.get("optype") == "messagereceivereckwkword.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagereceivereckwkword group by userid order by x desc",
            "用户ID关联用户",
        )
    if obj.get("optype") == "messagereceivereckwkword.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagereceivereckwkword group by userid",
            "用户ID关联用户",
        )
    if obj.get("optype") == "messagereceivereckwkword.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagereceivereckwkword group by userid",
            "用户ID关联用户",
        )
    if obj.get("optype") == "messagereceivereckwkword.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagereceivereckwkword group by userid",
            "用户ID关联用户",
        )
    if obj.get("optype") == "messagereceivereckwkword.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagereceivereckwkword group by userid",
            "用户ID关联用户",
        )
    if obj.get("optype") == "messagereceivereckwkword.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagereceivereckwkword group by userid",
            "用户ID关联用户",
        )
    # messagereceivereckwkword(消息接收记录表)->platkwkwfkwkwormid(平台ID关联平台)

    if obj.get("optype") == "messagereceivereckwkword.platkwkwfkwkwormid_pie":
        res = get_pie(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.messagereceivereckwkword group by platkwkwfkwkwormid order by x desc",
            "平台ID关联平台",
        )
    if obj.get("optype") == "messagereceivereckwkword.platkwkwfkwkwormid_pie_v1":
        res = get_pie_v1(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.messagereceivereckwkword group by platkwkwfkwkwormid",
            "平台ID关联平台",
        )
    if obj.get("optype") == "messagereceivereckwkword.platkwkwfkwkwormid_pie_v2":
        res = get_pie_v2(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.messagereceivereckwkword group by platkwkwfkwkwormid",
            "平台ID关联平台",
        )
    if obj.get("optype") == "messagereceivereckwkword.platkwkwfkwkwormid_line":
        res = get_line(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.messagereceivereckwkword group by platkwkwfkwkwormid",
            "平台ID关联平台",
        )
    if obj.get("optype") == "messagereceivereckwkword.platkwkwfkwkwormid_bar":
        res = get_bar(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.messagereceivereckwkword group by platkwkwfkwkwormid",
            "平台ID关联平台",
        )
    if obj.get("optype") == "messagereceivereckwkword.platkwkwfkwkwormid_bar_v1":
        res = get_bar_v1(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.messagereceivereckwkword group by platkwkwfkwkwormid",
            "平台ID关联平台",
        )
    if obj.get("optype") == "messagereceivereckwkword.messagecontent_wordcloud":
        textlist = get_data(
            "SELECT messagecontent result FROM vm772_58dd091a279b5392.messagereceivereckwkword;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "messagereceivereckwkword.receivetime_line":
        res = get_line(
            "select receivetime x,count(*) y from vm772_58dd091a279b5392.messagereceivereckwkword group by receivetime order by x",
            "接收时间",
        )
    # messagereceivereckwkword(消息接收记录表)->status(接收状态如已接收、未处理、已处理等)

    if obj.get("optype") == "messagereceivereckwkword.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagereceivereckwkword group by status order by x desc",
            "接收状态如已接收、未处理、已处理等",
        )
    if obj.get("optype") == "messagereceivereckwkword.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagereceivereckwkword group by status",
            "接收状态如已接收、未处理、已处理等",
        )
    if obj.get("optype") == "messagereceivereckwkword.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagereceivereckwkword group by status",
            "接收状态如已接收、未处理、已处理等",
        )
    if obj.get("optype") == "messagereceivereckwkword.status_line":
        res = get_line(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagereceivereckwkword group by status",
            "接收状态如已接收、未处理、已处理等",
        )
    if obj.get("optype") == "messagereceivereckwkword.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagereceivereckwkword group by status",
            "接收状态如已接收、未处理、已处理等",
        )
    if obj.get("optype") == "messagereceivereckwkword.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagereceivereckwkword group by status",
            "接收状态如已接收、未处理、已处理等",
        )
    if obj.get("optype") == "messagereceivereckwkword.responsecontent_wordcloud":
        textlist = get_data(
            "SELECT responsecontent result FROM vm772_58dd091a279b5392.messagereceivereckwkword;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "messagereceivereckwkword.responsetime_line":
        res = get_line(
            "select responsetime x,count(*) y from vm772_58dd091a279b5392.messagereceivereckwkword group by responsetime order by x",
            "回复时间",
        )
    # messagereceivereckwkword(消息接收记录表)->kwkwisread(是否已读示用户是否已读该消息)

    if obj.get("optype") == "messagereceivereckwkword.kwkwisread_pie":
        res = get_pie(
            "select kwkwisread x,count(*) y from vm772_58dd091a279b5392.messagereceivereckwkword group by kwkwisread order by x desc",
            "是否已读示用户是否已读该消息",
        )
    if obj.get("optype") == "messagereceivereckwkword.kwkwisread_pie_v1":
        res = get_pie_v1(
            "select kwkwisread x,count(*) y from vm772_58dd091a279b5392.messagereceivereckwkword group by kwkwisread",
            "是否已读示用户是否已读该消息",
        )
    if obj.get("optype") == "messagereceivereckwkword.kwkwisread_pie_v2":
        res = get_pie_v2(
            "select kwkwisread x,count(*) y from vm772_58dd091a279b5392.messagereceivereckwkword group by kwkwisread",
            "是否已读示用户是否已读该消息",
        )
    if obj.get("optype") == "messagereceivereckwkword.kwkwisread_line":
        res = get_line(
            "select kwkwisread x,count(*) y from vm772_58dd091a279b5392.messagereceivereckwkword group by kwkwisread",
            "是否已读示用户是否已读该消息",
        )
    if obj.get("optype") == "messagereceivereckwkword.kwkwisread_bar":
        res = get_bar(
            "select kwkwisread x,count(*) y from vm772_58dd091a279b5392.messagereceivereckwkword group by kwkwisread",
            "是否已读示用户是否已读该消息",
        )
    if obj.get("optype") == "messagereceivereckwkword.kwkwisread_bar_v1":
        res = get_bar_v1(
            "select kwkwisread x,count(*) y from vm772_58dd091a279b5392.messagereceivereckwkword group by kwkwisread",
            "是否已读示用户是否已读该消息",
        )
    # userpreference(用户偏好设置表)->userid(用户ID)

    if obj.get("optype") == "userpreference.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm772_58dd091a279b5392.userpreference group by userid order by x desc",
            "用户ID",
        )
    if obj.get("optype") == "userpreference.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm772_58dd091a279b5392.userpreference group by userid",
            "用户ID",
        )
    if obj.get("optype") == "userpreference.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm772_58dd091a279b5392.userpreference group by userid",
            "用户ID",
        )
    if obj.get("optype") == "userpreference.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm772_58dd091a279b5392.userpreference group by userid",
            "用户ID",
        )
    if obj.get("optype") == "userpreference.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm772_58dd091a279b5392.userpreference group by userid",
            "用户ID",
        )
    if obj.get("optype") == "userpreference.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm772_58dd091a279b5392.userpreference group by userid",
            "用户ID",
        )
    # userpreference(用户偏好设置表)->preferencename(偏好名称)

    if obj.get("optype") == "userpreference.preferencename_pie":
        res = get_pie(
            "select preferencename x,count(*) y from vm772_58dd091a279b5392.userpreference group by preferencename order by x desc",
            "偏好名称",
        )
    if obj.get("optype") == "userpreference.preferencename_pie_v1":
        res = get_pie_v1(
            "select preferencename x,count(*) y from vm772_58dd091a279b5392.userpreference group by preferencename",
            "偏好名称",
        )
    if obj.get("optype") == "userpreference.preferencename_pie_v2":
        res = get_pie_v2(
            "select preferencename x,count(*) y from vm772_58dd091a279b5392.userpreference group by preferencename",
            "偏好名称",
        )
    if obj.get("optype") == "userpreference.preferencename_line":
        res = get_line(
            "select preferencename x,count(*) y from vm772_58dd091a279b5392.userpreference group by preferencename",
            "偏好名称",
        )
    if obj.get("optype") == "userpreference.preferencename_bar":
        res = get_bar(
            "select preferencename x,count(*) y from vm772_58dd091a279b5392.userpreference group by preferencename",
            "偏好名称",
        )
    if obj.get("optype") == "userpreference.preferencename_bar_v1":
        res = get_bar_v1(
            "select preferencename x,count(*) y from vm772_58dd091a279b5392.userpreference group by preferencename",
            "偏好名称",
        )
    # userpreference(用户偏好设置表)->preferencevalue(偏好值)

    if obj.get("optype") == "userpreference.preferencevalue_pie":
        res = get_pie(
            "select preferencevalue x,count(*) y from vm772_58dd091a279b5392.userpreference group by preferencevalue order by x desc",
            "偏好值",
        )
    if obj.get("optype") == "userpreference.preferencevalue_pie_v1":
        res = get_pie_v1(
            "select preferencevalue x,count(*) y from vm772_58dd091a279b5392.userpreference group by preferencevalue",
            "偏好值",
        )
    if obj.get("optype") == "userpreference.preferencevalue_pie_v2":
        res = get_pie_v2(
            "select preferencevalue x,count(*) y from vm772_58dd091a279b5392.userpreference group by preferencevalue",
            "偏好值",
        )
    if obj.get("optype") == "userpreference.preferencevalue_line":
        res = get_line(
            "select preferencevalue x,count(*) y from vm772_58dd091a279b5392.userpreference group by preferencevalue",
            "偏好值",
        )
    if obj.get("optype") == "userpreference.preferencevalue_bar":
        res = get_bar(
            "select preferencevalue x,count(*) y from vm772_58dd091a279b5392.userpreference group by preferencevalue",
            "偏好值",
        )
    if obj.get("optype") == "userpreference.preferencevalue_bar_v1":
        res = get_bar_v1(
            "select preferencevalue x,count(*) y from vm772_58dd091a279b5392.userpreference group by preferencevalue",
            "偏好值",
        )
    # userpreference(用户偏好设置表)->preferencetype(偏好类型)

    if obj.get("optype") == "userpreference.preferencetype_pie":
        res = get_pie(
            "select preferencetype x,count(*) y from vm772_58dd091a279b5392.userpreference group by preferencetype order by x desc",
            "偏好类型",
        )
    if obj.get("optype") == "userpreference.preferencetype_pie_v1":
        res = get_pie_v1(
            "select preferencetype x,count(*) y from vm772_58dd091a279b5392.userpreference group by preferencetype",
            "偏好类型",
        )
    if obj.get("optype") == "userpreference.preferencetype_pie_v2":
        res = get_pie_v2(
            "select preferencetype x,count(*) y from vm772_58dd091a279b5392.userpreference group by preferencetype",
            "偏好类型",
        )
    if obj.get("optype") == "userpreference.preferencetype_line":
        res = get_line(
            "select preferencetype x,count(*) y from vm772_58dd091a279b5392.userpreference group by preferencetype",
            "偏好类型",
        )
    if obj.get("optype") == "userpreference.preferencetype_bar":
        res = get_bar(
            "select preferencetype x,count(*) y from vm772_58dd091a279b5392.userpreference group by preferencetype",
            "偏好类型",
        )
    if obj.get("optype") == "userpreference.preferencetype_bar_v1":
        res = get_bar_v1(
            "select preferencetype x,count(*) y from vm772_58dd091a279b5392.userpreference group by preferencetype",
            "偏好类型",
        )
    if obj.get("optype") == "userpreference.createtime_line":
        res = get_line(
            "select createtime x,count(*) y from vm772_58dd091a279b5392.userpreference group by createtime order by x",
            "创建时间",
        )
    if obj.get("optype") == "userpreference.updatetime_line":
        res = get_line(
            "select updatetime x,count(*) y from vm772_58dd091a279b5392.userpreference group by updatetime order by x",
            "更新时间",
        )
    # userpreference(用户偏好设置表)->kwkwisactive(是否激活)

    if obj.get("optype") == "userpreference.kwkwisactive_pie":
        res = get_pie(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.userpreference group by kwkwisactive order by x desc",
            "是否激活",
        )
    if obj.get("optype") == "userpreference.kwkwisactive_pie_v1":
        res = get_pie_v1(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.userpreference group by kwkwisactive",
            "是否激活",
        )
    if obj.get("optype") == "userpreference.kwkwisactive_pie_v2":
        res = get_pie_v2(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.userpreference group by kwkwisactive",
            "是否激活",
        )
    if obj.get("optype") == "userpreference.kwkwisactive_line":
        res = get_line(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.userpreference group by kwkwisactive",
            "是否激活",
        )
    if obj.get("optype") == "userpreference.kwkwisactive_bar":
        res = get_bar(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.userpreference group by kwkwisactive",
            "是否激活",
        )
    if obj.get("optype") == "userpreference.kwkwisactive_bar_v1":
        res = get_bar_v1(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.userpreference group by kwkwisactive",
            "是否激活",
        )
    if obj.get("optype") == "userpreference.description_wordcloud":
        textlist = get_data(
            "SELECT description result FROM vm772_58dd091a279b5392.userpreference;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # userpreference(用户偏好设置表)->platkwkwfkwkwormid(关联平台ID)

    if obj.get("optype") == "userpreference.platkwkwfkwkwormid_pie":
        res = get_pie(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.userpreference group by platkwkwfkwkwormid order by x desc",
            "关联平台ID",
        )
    if obj.get("optype") == "userpreference.platkwkwfkwkwormid_pie_v1":
        res = get_pie_v1(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.userpreference group by platkwkwfkwkwormid",
            "关联平台ID",
        )
    if obj.get("optype") == "userpreference.platkwkwfkwkwormid_pie_v2":
        res = get_pie_v2(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.userpreference group by platkwkwfkwkwormid",
            "关联平台ID",
        )
    if obj.get("optype") == "userpreference.platkwkwfkwkwormid_line":
        res = get_line(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.userpreference group by platkwkwfkwkwormid",
            "关联平台ID",
        )
    if obj.get("optype") == "userpreference.platkwkwfkwkwormid_bar":
        res = get_bar(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.userpreference group by platkwkwfkwkwormid",
            "关联平台ID",
        )
    if obj.get("optype") == "userpreference.platkwkwfkwkwormid_bar_v1":
        res = get_bar_v1(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.userpreference group by platkwkwfkwkwormid",
            "关联平台ID",
        )
    # accountbkwkwindkwkwing(账号绑定关系表)->accountid(账号ID)

    if obj.get("optype") == "accountbkwkwindkwkwing.accountid_pie":
        res = get_pie(
            "select accountid x,count(*) y from vm772_58dd091a279b5392.accountbkwkwindkwkwing group by accountid order by x desc",
            "账号ID",
        )
    if obj.get("optype") == "accountbkwkwindkwkwing.accountid_pie_v1":
        res = get_pie_v1(
            "select accountid x,count(*) y from vm772_58dd091a279b5392.accountbkwkwindkwkwing group by accountid",
            "账号ID",
        )
    if obj.get("optype") == "accountbkwkwindkwkwing.accountid_pie_v2":
        res = get_pie_v2(
            "select accountid x,count(*) y from vm772_58dd091a279b5392.accountbkwkwindkwkwing group by accountid",
            "账号ID",
        )
    if obj.get("optype") == "accountbkwkwindkwkwing.accountid_line":
        res = get_line(
            "select accountid x,count(*) y from vm772_58dd091a279b5392.accountbkwkwindkwkwing group by accountid",
            "账号ID",
        )
    if obj.get("optype") == "accountbkwkwindkwkwing.accountid_bar":
        res = get_bar(
            "select accountid x,count(*) y from vm772_58dd091a279b5392.accountbkwkwindkwkwing group by accountid",
            "账号ID",
        )
    if obj.get("optype") == "accountbkwkwindkwkwing.accountid_bar_v1":
        res = get_bar_v1(
            "select accountid x,count(*) y from vm772_58dd091a279b5392.accountbkwkwindkwkwing group by accountid",
            "账号ID",
        )
    # accountbkwkwindkwkwing(账号绑定关系表)->platkwkwfkwkwormid(平台ID)

    if obj.get("optype") == "accountbkwkwindkwkwing.platkwkwfkwkwormid_pie":
        res = get_pie(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.accountbkwkwindkwkwing group by platkwkwfkwkwormid order by x desc",
            "平台ID",
        )
    if obj.get("optype") == "accountbkwkwindkwkwing.platkwkwfkwkwormid_pie_v1":
        res = get_pie_v1(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.accountbkwkwindkwkwing group by platkwkwfkwkwormid",
            "平台ID",
        )
    if obj.get("optype") == "accountbkwkwindkwkwing.platkwkwfkwkwormid_pie_v2":
        res = get_pie_v2(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.accountbkwkwindkwkwing group by platkwkwfkwkwormid",
            "平台ID",
        )
    if obj.get("optype") == "accountbkwkwindkwkwing.platkwkwfkwkwormid_line":
        res = get_line(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.accountbkwkwindkwkwing group by platkwkwfkwkwormid",
            "平台ID",
        )
    if obj.get("optype") == "accountbkwkwindkwkwing.platkwkwfkwkwormid_bar":
        res = get_bar(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.accountbkwkwindkwkwing group by platkwkwfkwkwormid",
            "平台ID",
        )
    if obj.get("optype") == "accountbkwkwindkwkwing.platkwkwfkwkwormid_bar_v1":
        res = get_bar_v1(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.accountbkwkwindkwkwing group by platkwkwfkwkwormid",
            "平台ID",
        )
    # accountbkwkwindkwkwing(账号绑定关系表)->bkwkwindkwkwingtype(绑定类型)

    if obj.get("optype") == "accountbkwkwindkwkwing.bkwkwindkwkwingtype_pie":
        res = get_pie(
            "select bkwkwindkwkwingtype x,count(*) y from vm772_58dd091a279b5392.accountbkwkwindkwkwing group by bkwkwindkwkwingtype order by x desc",
            "绑定类型",
        )
    if obj.get("optype") == "accountbkwkwindkwkwing.bkwkwindkwkwingtype_pie_v1":
        res = get_pie_v1(
            "select bkwkwindkwkwingtype x,count(*) y from vm772_58dd091a279b5392.accountbkwkwindkwkwing group by bkwkwindkwkwingtype",
            "绑定类型",
        )
    if obj.get("optype") == "accountbkwkwindkwkwing.bkwkwindkwkwingtype_pie_v2":
        res = get_pie_v2(
            "select bkwkwindkwkwingtype x,count(*) y from vm772_58dd091a279b5392.accountbkwkwindkwkwing group by bkwkwindkwkwingtype",
            "绑定类型",
        )
    if obj.get("optype") == "accountbkwkwindkwkwing.bkwkwindkwkwingtype_line":
        res = get_line(
            "select bkwkwindkwkwingtype x,count(*) y from vm772_58dd091a279b5392.accountbkwkwindkwkwing group by bkwkwindkwkwingtype",
            "绑定类型",
        )
    if obj.get("optype") == "accountbkwkwindkwkwing.bkwkwindkwkwingtype_bar":
        res = get_bar(
            "select bkwkwindkwkwingtype x,count(*) y from vm772_58dd091a279b5392.accountbkwkwindkwkwing group by bkwkwindkwkwingtype",
            "绑定类型",
        )
    if obj.get("optype") == "accountbkwkwindkwkwing.bkwkwindkwkwingtype_bar_v1":
        res = get_bar_v1(
            "select bkwkwindkwkwingtype x,count(*) y from vm772_58dd091a279b5392.accountbkwkwindkwkwing group by bkwkwindkwkwingtype",
            "绑定类型",
        )
    # accountbkwkwindkwkwing(账号绑定关系表)->bkwkwindkwkwingstatus(绑定状态)

    if obj.get("optype") == "accountbkwkwindkwkwing.bkwkwindkwkwingstatus_pie":
        res = get_pie(
            "select bkwkwindkwkwingstatus x,count(*) y from vm772_58dd091a279b5392.accountbkwkwindkwkwing group by bkwkwindkwkwingstatus order by x desc",
            "绑定状态",
        )
    if obj.get("optype") == "accountbkwkwindkwkwing.bkwkwindkwkwingstatus_pie_v1":
        res = get_pie_v1(
            "select bkwkwindkwkwingstatus x,count(*) y from vm772_58dd091a279b5392.accountbkwkwindkwkwing group by bkwkwindkwkwingstatus",
            "绑定状态",
        )
    if obj.get("optype") == "accountbkwkwindkwkwing.bkwkwindkwkwingstatus_pie_v2":
        res = get_pie_v2(
            "select bkwkwindkwkwingstatus x,count(*) y from vm772_58dd091a279b5392.accountbkwkwindkwkwing group by bkwkwindkwkwingstatus",
            "绑定状态",
        )
    if obj.get("optype") == "accountbkwkwindkwkwing.bkwkwindkwkwingstatus_line":
        res = get_line(
            "select bkwkwindkwkwingstatus x,count(*) y from vm772_58dd091a279b5392.accountbkwkwindkwkwing group by bkwkwindkwkwingstatus",
            "绑定状态",
        )
    if obj.get("optype") == "accountbkwkwindkwkwing.bkwkwindkwkwingstatus_bar":
        res = get_bar(
            "select bkwkwindkwkwingstatus x,count(*) y from vm772_58dd091a279b5392.accountbkwkwindkwkwing group by bkwkwindkwkwingstatus",
            "绑定状态",
        )
    if obj.get("optype") == "accountbkwkwindkwkwing.bkwkwindkwkwingstatus_bar_v1":
        res = get_bar_v1(
            "select bkwkwindkwkwingstatus x,count(*) y from vm772_58dd091a279b5392.accountbkwkwindkwkwing group by bkwkwindkwkwingstatus",
            "绑定状态",
        )
    if obj.get("optype") == "accountbkwkwindkwkwing.createdat_line":
        res = get_line(
            "select createdat x,count(*) y from vm772_58dd091a279b5392.accountbkwkwindkwkwing group by createdat order by x",
            "创建时间",
        )
    if obj.get("optype") == "accountbkwkwindkwkwing.updatedat_line":
        res = get_line(
            "select updatedat x,count(*) y from vm772_58dd091a279b5392.accountbkwkwindkwkwing group by updatedat order by x",
            "更新时间",
        )
    # accountbkwkwindkwkwing(账号绑定关系表)->userid(用户ID)

    if obj.get("optype") == "accountbkwkwindkwkwing.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm772_58dd091a279b5392.accountbkwkwindkwkwing group by userid order by x desc",
            "用户ID",
        )
    if obj.get("optype") == "accountbkwkwindkwkwing.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm772_58dd091a279b5392.accountbkwkwindkwkwing group by userid",
            "用户ID",
        )
    if obj.get("optype") == "accountbkwkwindkwkwing.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm772_58dd091a279b5392.accountbkwkwindkwkwing group by userid",
            "用户ID",
        )
    if obj.get("optype") == "accountbkwkwindkwkwing.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm772_58dd091a279b5392.accountbkwkwindkwkwing group by userid",
            "用户ID",
        )
    if obj.get("optype") == "accountbkwkwindkwkwing.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm772_58dd091a279b5392.accountbkwkwindkwkwing group by userid",
            "用户ID",
        )
    if obj.get("optype") == "accountbkwkwindkwkwing.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm772_58dd091a279b5392.accountbkwkwindkwkwing group by userid",
            "用户ID",
        )
    if obj.get("optype") == "messagecontentreview.content_wordcloud":
        textlist = get_data(
            "SELECT content result FROM vm772_58dd091a279b5392.messagecontentreview;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # messagecontentreview(消息内容审核表)->userid(用户ID)

    if obj.get("optype") == "messagecontentreview.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagecontentreview group by userid order by x desc",
            "用户ID",
        )
    if obj.get("optype") == "messagecontentreview.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagecontentreview group by userid",
            "用户ID",
        )
    if obj.get("optype") == "messagecontentreview.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagecontentreview group by userid",
            "用户ID",
        )
    if obj.get("optype") == "messagecontentreview.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagecontentreview group by userid",
            "用户ID",
        )
    if obj.get("optype") == "messagecontentreview.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagecontentreview group by userid",
            "用户ID",
        )
    if obj.get("optype") == "messagecontentreview.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagecontentreview group by userid",
            "用户ID",
        )
    # messagecontentreview(消息内容审核表)->platkwkwfkwkworm(平台名称)

    if obj.get("optype") == "messagecontentreview.platkwkwfkwkworm_pie":
        res = get_pie(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.messagecontentreview group by platkwkwfkwkworm order by x desc",
            "平台名称",
        )
    if obj.get("optype") == "messagecontentreview.platkwkwfkwkworm_pie_v1":
        res = get_pie_v1(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.messagecontentreview group by platkwkwfkwkworm",
            "平台名称",
        )
    if obj.get("optype") == "messagecontentreview.platkwkwfkwkworm_pie_v2":
        res = get_pie_v2(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.messagecontentreview group by platkwkwfkwkworm",
            "平台名称",
        )
    if obj.get("optype") == "messagecontentreview.platkwkwfkwkworm_line":
        res = get_line(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.messagecontentreview group by platkwkwfkwkworm",
            "平台名称",
        )
    if obj.get("optype") == "messagecontentreview.platkwkwfkwkworm_bar":
        res = get_bar(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.messagecontentreview group by platkwkwfkwkworm",
            "平台名称",
        )
    if obj.get("optype") == "messagecontentreview.platkwkwfkwkworm_bar_v1":
        res = get_bar_v1(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.messagecontentreview group by platkwkwfkwkworm",
            "平台名称",
        )
    # messagecontentreview(消息内容审核表)->reviewstatus(审核状态)

    if obj.get("optype") == "messagecontentreview.reviewstatus_pie":
        res = get_pie(
            "select reviewstatus x,count(*) y from vm772_58dd091a279b5392.messagecontentreview group by reviewstatus order by x desc",
            "审核状态",
        )
    if obj.get("optype") == "messagecontentreview.reviewstatus_pie_v1":
        res = get_pie_v1(
            "select reviewstatus x,count(*) y from vm772_58dd091a279b5392.messagecontentreview group by reviewstatus",
            "审核状态",
        )
    if obj.get("optype") == "messagecontentreview.reviewstatus_pie_v2":
        res = get_pie_v2(
            "select reviewstatus x,count(*) y from vm772_58dd091a279b5392.messagecontentreview group by reviewstatus",
            "审核状态",
        )
    if obj.get("optype") == "messagecontentreview.reviewstatus_line":
        res = get_line(
            "select reviewstatus x,count(*) y from vm772_58dd091a279b5392.messagecontentreview group by reviewstatus",
            "审核状态",
        )
    if obj.get("optype") == "messagecontentreview.reviewstatus_bar":
        res = get_bar(
            "select reviewstatus x,count(*) y from vm772_58dd091a279b5392.messagecontentreview group by reviewstatus",
            "审核状态",
        )
    if obj.get("optype") == "messagecontentreview.reviewstatus_bar_v1":
        res = get_bar_v1(
            "select reviewstatus x,count(*) y from vm772_58dd091a279b5392.messagecontentreview group by reviewstatus",
            "审核状态",
        )
    if obj.get("optype") == "messagecontentreview.reviewtime_line":
        res = get_line(
            "select reviewtime x,count(*) y from vm772_58dd091a279b5392.messagecontentreview group by reviewtime order by x",
            "审核时间",
        )
    # messagecontentreview(消息内容审核表)->reviewerid(审核员ID)

    if obj.get("optype") == "messagecontentreview.reviewerid_pie":
        res = get_pie(
            "select reviewerid x,count(*) y from vm772_58dd091a279b5392.messagecontentreview group by reviewerid order by x desc",
            "审核员ID",
        )
    if obj.get("optype") == "messagecontentreview.reviewerid_pie_v1":
        res = get_pie_v1(
            "select reviewerid x,count(*) y from vm772_58dd091a279b5392.messagecontentreview group by reviewerid",
            "审核员ID",
        )
    if obj.get("optype") == "messagecontentreview.reviewerid_pie_v2":
        res = get_pie_v2(
            "select reviewerid x,count(*) y from vm772_58dd091a279b5392.messagecontentreview group by reviewerid",
            "审核员ID",
        )
    if obj.get("optype") == "messagecontentreview.reviewerid_line":
        res = get_line(
            "select reviewerid x,count(*) y from vm772_58dd091a279b5392.messagecontentreview group by reviewerid",
            "审核员ID",
        )
    if obj.get("optype") == "messagecontentreview.reviewerid_bar":
        res = get_bar(
            "select reviewerid x,count(*) y from vm772_58dd091a279b5392.messagecontentreview group by reviewerid",
            "审核员ID",
        )
    if obj.get("optype") == "messagecontentreview.reviewerid_bar_v1":
        res = get_bar_v1(
            "select reviewerid x,count(*) y from vm772_58dd091a279b5392.messagecontentreview group by reviewerid",
            "审核员ID",
        )
    # messagecontentreview(消息内容审核表)->rejectionrekwkwason(拒绝原因)

    if obj.get("optype") == "messagecontentreview.rejectionrekwkwason_pie":
        res = get_pie(
            "select rejectionrekwkwason x,count(*) y from vm772_58dd091a279b5392.messagecontentreview group by rejectionrekwkwason order by x desc",
            "拒绝原因",
        )
    if obj.get("optype") == "messagecontentreview.rejectionrekwkwason_pie_v1":
        res = get_pie_v1(
            "select rejectionrekwkwason x,count(*) y from vm772_58dd091a279b5392.messagecontentreview group by rejectionrekwkwason",
            "拒绝原因",
        )
    if obj.get("optype") == "messagecontentreview.rejectionrekwkwason_pie_v2":
        res = get_pie_v2(
            "select rejectionrekwkwason x,count(*) y from vm772_58dd091a279b5392.messagecontentreview group by rejectionrekwkwason",
            "拒绝原因",
        )
    if obj.get("optype") == "messagecontentreview.rejectionrekwkwason_line":
        res = get_line(
            "select rejectionrekwkwason x,count(*) y from vm772_58dd091a279b5392.messagecontentreview group by rejectionrekwkwason",
            "拒绝原因",
        )
    if obj.get("optype") == "messagecontentreview.rejectionrekwkwason_bar":
        res = get_bar(
            "select rejectionrekwkwason x,count(*) y from vm772_58dd091a279b5392.messagecontentreview group by rejectionrekwkwason",
            "拒绝原因",
        )
    if obj.get("optype") == "messagecontentreview.rejectionrekwkwason_bar_v1":
        res = get_bar_v1(
            "select rejectionrekwkwason x,count(*) y from vm772_58dd091a279b5392.messagecontentreview group by rejectionrekwkwason",
            "拒绝原因",
        )
    if obj.get("optype") == "messagecontentreview.kwkwissensitive_wordcloud":
        textlist = get_data(
            "SELECT kwkwissensitive result FROM vm772_58dd091a279b5392.messagecontentreview;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "messagecontentreview.createdat_line":
        res = get_line(
            "select createdat x,count(*) y from vm772_58dd091a279b5392.messagecontentreview group by createdat order by x",
            "创建时间",
        )
    # messagesendfailurelog(消息发送失败日志表)->messageid(消息ID)

    if obj.get("optype") == "messagesendfailurelog.messageid_pie":
        res = get_pie(
            "select messageid x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by messageid order by x desc",
            "消息ID",
        )
    if obj.get("optype") == "messagesendfailurelog.messageid_pie_v1":
        res = get_pie_v1(
            "select messageid x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by messageid",
            "消息ID",
        )
    if obj.get("optype") == "messagesendfailurelog.messageid_pie_v2":
        res = get_pie_v2(
            "select messageid x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by messageid",
            "消息ID",
        )
    if obj.get("optype") == "messagesendfailurelog.messageid_line":
        res = get_line(
            "select messageid x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by messageid",
            "消息ID",
        )
    if obj.get("optype") == "messagesendfailurelog.messageid_bar":
        res = get_bar(
            "select messageid x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by messageid",
            "消息ID",
        )
    if obj.get("optype") == "messagesendfailurelog.messageid_bar_v1":
        res = get_bar_v1(
            "select messageid x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by messageid",
            "消息ID",
        )
    # messagesendfailurelog(消息发送失败日志表)->platkwkwfkwkworm(平台名称)

    if obj.get("optype") == "messagesendfailurelog.platkwkwfkwkworm_pie":
        res = get_pie(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by platkwkwfkwkworm order by x desc",
            "平台名称",
        )
    if obj.get("optype") == "messagesendfailurelog.platkwkwfkwkworm_pie_v1":
        res = get_pie_v1(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by platkwkwfkwkworm",
            "平台名称",
        )
    if obj.get("optype") == "messagesendfailurelog.platkwkwfkwkworm_pie_v2":
        res = get_pie_v2(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by platkwkwfkwkworm",
            "平台名称",
        )
    if obj.get("optype") == "messagesendfailurelog.platkwkwfkwkworm_line":
        res = get_line(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by platkwkwfkwkworm",
            "平台名称",
        )
    if obj.get("optype") == "messagesendfailurelog.platkwkwfkwkworm_bar":
        res = get_bar(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by platkwkwfkwkworm",
            "平台名称",
        )
    if obj.get("optype") == "messagesendfailurelog.platkwkwfkwkworm_bar_v1":
        res = get_bar_v1(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by platkwkwfkwkworm",
            "平台名称",
        )
    # messagesendfailurelog(消息发送失败日志表)->userid(用户ID)

    if obj.get("optype") == "messagesendfailurelog.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by userid order by x desc",
            "用户ID",
        )
    if obj.get("optype") == "messagesendfailurelog.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by userid",
            "用户ID",
        )
    if obj.get("optype") == "messagesendfailurelog.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by userid",
            "用户ID",
        )
    if obj.get("optype") == "messagesendfailurelog.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by userid",
            "用户ID",
        )
    if obj.get("optype") == "messagesendfailurelog.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by userid",
            "用户ID",
        )
    if obj.get("optype") == "messagesendfailurelog.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by userid",
            "用户ID",
        )
    # messagesendfailurelog(消息发送失败日志表)->targetuserid(目标用户ID)

    if obj.get("optype") == "messagesendfailurelog.targetuserid_pie":
        res = get_pie(
            "select targetuserid x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by targetuserid order by x desc",
            "目标用户ID",
        )
    if obj.get("optype") == "messagesendfailurelog.targetuserid_pie_v1":
        res = get_pie_v1(
            "select targetuserid x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by targetuserid",
            "目标用户ID",
        )
    if obj.get("optype") == "messagesendfailurelog.targetuserid_pie_v2":
        res = get_pie_v2(
            "select targetuserid x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by targetuserid",
            "目标用户ID",
        )
    if obj.get("optype") == "messagesendfailurelog.targetuserid_line":
        res = get_line(
            "select targetuserid x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by targetuserid",
            "目标用户ID",
        )
    if obj.get("optype") == "messagesendfailurelog.targetuserid_bar":
        res = get_bar(
            "select targetuserid x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by targetuserid",
            "目标用户ID",
        )
    if obj.get("optype") == "messagesendfailurelog.targetuserid_bar_v1":
        res = get_bar_v1(
            "select targetuserid x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by targetuserid",
            "目标用户ID",
        )
    if obj.get("optype") == "messagesendfailurelog.sendtime_line":
        res = get_line(
            "select sendtime x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by sendtime order by x",
            "发送时间",
        )
    # messagesendfailurelog(消息发送失败日志表)->failurerekwkwason(失败原因)

    if obj.get("optype") == "messagesendfailurelog.failurerekwkwason_pie":
        res = get_pie(
            "select failurerekwkwason x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by failurerekwkwason order by x desc",
            "失败原因",
        )
    if obj.get("optype") == "messagesendfailurelog.failurerekwkwason_pie_v1":
        res = get_pie_v1(
            "select failurerekwkwason x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by failurerekwkwason",
            "失败原因",
        )
    if obj.get("optype") == "messagesendfailurelog.failurerekwkwason_pie_v2":
        res = get_pie_v2(
            "select failurerekwkwason x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by failurerekwkwason",
            "失败原因",
        )
    if obj.get("optype") == "messagesendfailurelog.failurerekwkwason_line":
        res = get_line(
            "select failurerekwkwason x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by failurerekwkwason",
            "失败原因",
        )
    if obj.get("optype") == "messagesendfailurelog.failurerekwkwason_bar":
        res = get_bar(
            "select failurerekwkwason x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by failurerekwkwason",
            "失败原因",
        )
    if obj.get("optype") == "messagesendfailurelog.failurerekwkwason_bar_v1":
        res = get_bar_v1(
            "select failurerekwkwason x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by failurerekwkwason",
            "失败原因",
        )
    # messagesendfailurelog(消息发送失败日志表)->rekwkwtrycount(重试次数)

    if obj.get("optype") == "messagesendfailurelog.rekwkwtrycount_pie":
        res = get_pie(
            "select rekwkwtrycount x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by rekwkwtrycount order by x desc",
            "重试次数",
        )
    if obj.get("optype") == "messagesendfailurelog.rekwkwtrycount_pie_v1":
        res = get_pie_v1(
            "select rekwkwtrycount x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by rekwkwtrycount",
            "重试次数",
        )
    if obj.get("optype") == "messagesendfailurelog.rekwkwtrycount_pie_v2":
        res = get_pie_v2(
            "select rekwkwtrycount x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by rekwkwtrycount",
            "重试次数",
        )
    if obj.get("optype") == "messagesendfailurelog.rekwkwtrycount_line":
        res = get_line(
            "select rekwkwtrycount x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by rekwkwtrycount",
            "重试次数",
        )
    if obj.get("optype") == "messagesendfailurelog.rekwkwtrycount_bar":
        res = get_bar(
            "select rekwkwtrycount x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by rekwkwtrycount",
            "重试次数",
        )
    if obj.get("optype") == "messagesendfailurelog.rekwkwtrycount_bar_v1":
        res = get_bar_v1(
            "select rekwkwtrycount x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by rekwkwtrycount",
            "重试次数",
        )
    if obj.get("optype") == "messagesendfailurelog.lkwkwastrekwkwtrytime_line":
        res = get_line(
            "select lkwkwastrekwkwtrytime x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by lkwkwastrekwkwtrytime order by x",
            "上次重试时间",
        )
    # messagesendfailurelog(消息发送失败日志表)->kwkwisresolved(是否已解决)

    if obj.get("optype") == "messagesendfailurelog.kwkwisresolved_pie":
        res = get_pie(
            "select kwkwisresolved x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by kwkwisresolved order by x desc",
            "是否已解决",
        )
    if obj.get("optype") == "messagesendfailurelog.kwkwisresolved_pie_v1":
        res = get_pie_v1(
            "select kwkwisresolved x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by kwkwisresolved",
            "是否已解决",
        )
    if obj.get("optype") == "messagesendfailurelog.kwkwisresolved_pie_v2":
        res = get_pie_v2(
            "select kwkwisresolved x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by kwkwisresolved",
            "是否已解决",
        )
    if obj.get("optype") == "messagesendfailurelog.kwkwisresolved_line":
        res = get_line(
            "select kwkwisresolved x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by kwkwisresolved",
            "是否已解决",
        )
    if obj.get("optype") == "messagesendfailurelog.kwkwisresolved_bar":
        res = get_bar(
            "select kwkwisresolved x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by kwkwisresolved",
            "是否已解决",
        )
    if obj.get("optype") == "messagesendfailurelog.kwkwisresolved_bar_v1":
        res = get_bar_v1(
            "select kwkwisresolved x,count(*) y from vm772_58dd091a279b5392.messagesendfailurelog group by kwkwisresolved",
            "是否已解决",
        )
    # messagesendsuccesslog(消息发送成功日志表)->messageid(消息ID)

    if obj.get("optype") == "messagesendsuccesslog.messageid_pie":
        res = get_pie(
            "select messageid x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by messageid order by x desc",
            "消息ID",
        )
    if obj.get("optype") == "messagesendsuccesslog.messageid_pie_v1":
        res = get_pie_v1(
            "select messageid x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by messageid",
            "消息ID",
        )
    if obj.get("optype") == "messagesendsuccesslog.messageid_pie_v2":
        res = get_pie_v2(
            "select messageid x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by messageid",
            "消息ID",
        )
    if obj.get("optype") == "messagesendsuccesslog.messageid_line":
        res = get_line(
            "select messageid x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by messageid",
            "消息ID",
        )
    if obj.get("optype") == "messagesendsuccesslog.messageid_bar":
        res = get_bar(
            "select messageid x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by messageid",
            "消息ID",
        )
    if obj.get("optype") == "messagesendsuccesslog.messageid_bar_v1":
        res = get_bar_v1(
            "select messageid x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by messageid",
            "消息ID",
        )
    # messagesendsuccesslog(消息发送成功日志表)->platkwkwfkwkworm(平台名称)

    if obj.get("optype") == "messagesendsuccesslog.platkwkwfkwkworm_pie":
        res = get_pie(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by platkwkwfkwkworm order by x desc",
            "平台名称",
        )
    if obj.get("optype") == "messagesendsuccesslog.platkwkwfkwkworm_pie_v1":
        res = get_pie_v1(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by platkwkwfkwkworm",
            "平台名称",
        )
    if obj.get("optype") == "messagesendsuccesslog.platkwkwfkwkworm_pie_v2":
        res = get_pie_v2(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by platkwkwfkwkworm",
            "平台名称",
        )
    if obj.get("optype") == "messagesendsuccesslog.platkwkwfkwkworm_line":
        res = get_line(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by platkwkwfkwkworm",
            "平台名称",
        )
    if obj.get("optype") == "messagesendsuccesslog.platkwkwfkwkworm_bar":
        res = get_bar(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by platkwkwfkwkworm",
            "平台名称",
        )
    if obj.get("optype") == "messagesendsuccesslog.platkwkwfkwkworm_bar_v1":
        res = get_bar_v1(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by platkwkwfkwkworm",
            "平台名称",
        )
    # messagesendsuccesslog(消息发送成功日志表)->userid(用户ID)

    if obj.get("optype") == "messagesendsuccesslog.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by userid order by x desc",
            "用户ID",
        )
    if obj.get("optype") == "messagesendsuccesslog.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by userid",
            "用户ID",
        )
    if obj.get("optype") == "messagesendsuccesslog.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by userid",
            "用户ID",
        )
    if obj.get("optype") == "messagesendsuccesslog.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by userid",
            "用户ID",
        )
    if obj.get("optype") == "messagesendsuccesslog.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by userid",
            "用户ID",
        )
    if obj.get("optype") == "messagesendsuccesslog.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by userid",
            "用户ID",
        )
    # messagesendsuccesslog(消息发送成功日志表)->receiverid(接收者ID)

    if obj.get("optype") == "messagesendsuccesslog.receiverid_pie":
        res = get_pie(
            "select receiverid x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by receiverid order by x desc",
            "接收者ID",
        )
    if obj.get("optype") == "messagesendsuccesslog.receiverid_pie_v1":
        res = get_pie_v1(
            "select receiverid x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by receiverid",
            "接收者ID",
        )
    if obj.get("optype") == "messagesendsuccesslog.receiverid_pie_v2":
        res = get_pie_v2(
            "select receiverid x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by receiverid",
            "接收者ID",
        )
    if obj.get("optype") == "messagesendsuccesslog.receiverid_line":
        res = get_line(
            "select receiverid x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by receiverid",
            "接收者ID",
        )
    if obj.get("optype") == "messagesendsuccesslog.receiverid_bar":
        res = get_bar(
            "select receiverid x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by receiverid",
            "接收者ID",
        )
    if obj.get("optype") == "messagesendsuccesslog.receiverid_bar_v1":
        res = get_bar_v1(
            "select receiverid x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by receiverid",
            "接收者ID",
        )
    if obj.get("optype") == "messagesendsuccesslog.sendtime_line":
        res = get_line(
            "select sendtime x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by sendtime order by x",
            "发送时间",
        )
    if obj.get("optype") == "messagesendsuccesslog.content_wordcloud":
        textlist = get_data(
            "SELECT content result FROM vm772_58dd091a279b5392.messagesendsuccesslog;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # messagesendsuccesslog(消息发送成功日志表)->status(发送状态)

    if obj.get("optype") == "messagesendsuccesslog.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by status order by x desc",
            "发送状态",
        )
    if obj.get("optype") == "messagesendsuccesslog.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by status",
            "发送状态",
        )
    if obj.get("optype") == "messagesendsuccesslog.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by status",
            "发送状态",
        )
    if obj.get("optype") == "messagesendsuccesslog.status_line":
        res = get_line(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by status",
            "发送状态",
        )
    if obj.get("optype") == "messagesendsuccesslog.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by status",
            "发送状态",
        )
    if obj.get("optype") == "messagesendsuccesslog.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by status",
            "发送状态",
        )
    # messagesendsuccesslog(消息发送成功日志表)->errkwkworkwkwinfo(错误信息)

    if obj.get("optype") == "messagesendsuccesslog.errkwkworkwkwinfo_pie":
        res = get_pie(
            "select errkwkworkwkwinfo x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by errkwkworkwkwinfo order by x desc",
            "错误信息",
        )
    if obj.get("optype") == "messagesendsuccesslog.errkwkworkwkwinfo_pie_v1":
        res = get_pie_v1(
            "select errkwkworkwkwinfo x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by errkwkworkwkwinfo",
            "错误信息",
        )
    if obj.get("optype") == "messagesendsuccesslog.errkwkworkwkwinfo_pie_v2":
        res = get_pie_v2(
            "select errkwkworkwkwinfo x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by errkwkworkwkwinfo",
            "错误信息",
        )
    if obj.get("optype") == "messagesendsuccesslog.errkwkworkwkwinfo_line":
        res = get_line(
            "select errkwkworkwkwinfo x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by errkwkworkwkwinfo",
            "错误信息",
        )
    if obj.get("optype") == "messagesendsuccesslog.errkwkworkwkwinfo_bar":
        res = get_bar(
            "select errkwkworkwkwinfo x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by errkwkworkwkwinfo",
            "错误信息",
        )
    if obj.get("optype") == "messagesendsuccesslog.errkwkworkwkwinfo_bar_v1":
        res = get_bar_v1(
            "select errkwkworkwkwinfo x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by errkwkworkwkwinfo",
            "错误信息",
        )
    # messagesendsuccesslog(消息发送成功日志表)->relatedtkwkwaskid(关联任务ID)

    if obj.get("optype") == "messagesendsuccesslog.relatedtkwkwaskid_pie":
        res = get_pie(
            "select relatedtkwkwaskid x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by relatedtkwkwaskid order by x desc",
            "关联任务ID",
        )
    if obj.get("optype") == "messagesendsuccesslog.relatedtkwkwaskid_pie_v1":
        res = get_pie_v1(
            "select relatedtkwkwaskid x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by relatedtkwkwaskid",
            "关联任务ID",
        )
    if obj.get("optype") == "messagesendsuccesslog.relatedtkwkwaskid_pie_v2":
        res = get_pie_v2(
            "select relatedtkwkwaskid x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by relatedtkwkwaskid",
            "关联任务ID",
        )
    if obj.get("optype") == "messagesendsuccesslog.relatedtkwkwaskid_line":
        res = get_line(
            "select relatedtkwkwaskid x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by relatedtkwkwaskid",
            "关联任务ID",
        )
    if obj.get("optype") == "messagesendsuccesslog.relatedtkwkwaskid_bar":
        res = get_bar(
            "select relatedtkwkwaskid x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by relatedtkwkwaskid",
            "关联任务ID",
        )
    if obj.get("optype") == "messagesendsuccesslog.relatedtkwkwaskid_bar_v1":
        res = get_bar_v1(
            "select relatedtkwkwaskid x,count(*) y from vm772_58dd091a279b5392.messagesendsuccesslog group by relatedtkwkwaskid",
            "关联任务ID",
        )
    # messagetemplatecategkwkwory(消息模板分类表)->name(分类名称)

    if obj.get("optype") == "messagetemplatecategkwkwory.name_pie":
        res = get_pie(
            "select name x,count(*) y from vm772_58dd091a279b5392.messagetemplatecategkwkwory group by name order by x desc",
            "分类名称",
        )
    if obj.get("optype") == "messagetemplatecategkwkwory.name_pie_v1":
        res = get_pie_v1(
            "select name x,count(*) y from vm772_58dd091a279b5392.messagetemplatecategkwkwory group by name",
            "分类名称",
        )
    if obj.get("optype") == "messagetemplatecategkwkwory.name_pie_v2":
        res = get_pie_v2(
            "select name x,count(*) y from vm772_58dd091a279b5392.messagetemplatecategkwkwory group by name",
            "分类名称",
        )
    if obj.get("optype") == "messagetemplatecategkwkwory.name_line":
        res = get_line(
            "select name x,count(*) y from vm772_58dd091a279b5392.messagetemplatecategkwkwory group by name",
            "分类名称",
        )
    if obj.get("optype") == "messagetemplatecategkwkwory.name_bar":
        res = get_bar(
            "select name x,count(*) y from vm772_58dd091a279b5392.messagetemplatecategkwkwory group by name",
            "分类名称",
        )
    if obj.get("optype") == "messagetemplatecategkwkwory.name_bar_v1":
        res = get_bar_v1(
            "select name x,count(*) y from vm772_58dd091a279b5392.messagetemplatecategkwkwory group by name",
            "分类名称",
        )
    if obj.get("optype") == "messagetemplatecategkwkwory.description_wordcloud":
        textlist = get_data(
            "SELECT description result FROM vm772_58dd091a279b5392.messagetemplatecategkwkwory;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "messagetemplatecategkwkwory.createdat_line":
        res = get_line(
            "select createdat x,count(*) y from vm772_58dd091a279b5392.messagetemplatecategkwkwory group by createdat order by x",
            "创建时间",
        )
    if obj.get("optype") == "messagetemplatecategkwkwory.updatedat_line":
        res = get_line(
            "select updatedat x,count(*) y from vm772_58dd091a279b5392.messagetemplatecategkwkwory group by updatedat order by x",
            "更新时间",
        )
    # messagetemplatecategkwkwory(消息模板分类表)->kwkwisactive(是否激活用于控制分类是否可用)

    if obj.get("optype") == "messagetemplatecategkwkwory.kwkwisactive_pie":
        res = get_pie(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.messagetemplatecategkwkwory group by kwkwisactive order by x desc",
            "是否激活用于控制分类是否可用",
        )
    if obj.get("optype") == "messagetemplatecategkwkwory.kwkwisactive_pie_v1":
        res = get_pie_v1(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.messagetemplatecategkwkwory group by kwkwisactive",
            "是否激活用于控制分类是否可用",
        )
    if obj.get("optype") == "messagetemplatecategkwkwory.kwkwisactive_pie_v2":
        res = get_pie_v2(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.messagetemplatecategkwkwory group by kwkwisactive",
            "是否激活用于控制分类是否可用",
        )
    if obj.get("optype") == "messagetemplatecategkwkwory.kwkwisactive_line":
        res = get_line(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.messagetemplatecategkwkwory group by kwkwisactive",
            "是否激活用于控制分类是否可用",
        )
    if obj.get("optype") == "messagetemplatecategkwkwory.kwkwisactive_bar":
        res = get_bar(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.messagetemplatecategkwkwory group by kwkwisactive",
            "是否激活用于控制分类是否可用",
        )
    if obj.get("optype") == "messagetemplatecategkwkwory.kwkwisactive_bar_v1":
        res = get_bar_v1(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.messagetemplatecategkwkwory group by kwkwisactive",
            "是否激活用于控制分类是否可用",
        )
    # messagetemplatecategkwkwory(消息模板分类表)->parentid(父级分类ID用于构建分类层级结构)

    if obj.get("optype") == "messagetemplatecategkwkwory.parentid_pie":
        res = get_pie(
            "select parentid x,count(*) y from vm772_58dd091a279b5392.messagetemplatecategkwkwory group by parentid order by x desc",
            "父级分类ID用于构建分类层级结构",
        )
    if obj.get("optype") == "messagetemplatecategkwkwory.parentid_pie_v1":
        res = get_pie_v1(
            "select parentid x,count(*) y from vm772_58dd091a279b5392.messagetemplatecategkwkwory group by parentid",
            "父级分类ID用于构建分类层级结构",
        )
    if obj.get("optype") == "messagetemplatecategkwkwory.parentid_pie_v2":
        res = get_pie_v2(
            "select parentid x,count(*) y from vm772_58dd091a279b5392.messagetemplatecategkwkwory group by parentid",
            "父级分类ID用于构建分类层级结构",
        )
    if obj.get("optype") == "messagetemplatecategkwkwory.parentid_line":
        res = get_line(
            "select parentid x,count(*) y from vm772_58dd091a279b5392.messagetemplatecategkwkwory group by parentid",
            "父级分类ID用于构建分类层级结构",
        )
    if obj.get("optype") == "messagetemplatecategkwkwory.parentid_bar":
        res = get_bar(
            "select parentid x,count(*) y from vm772_58dd091a279b5392.messagetemplatecategkwkwory group by parentid",
            "父级分类ID用于构建分类层级结构",
        )
    if obj.get("optype") == "messagetemplatecategkwkwory.parentid_bar_v1":
        res = get_bar_v1(
            "select parentid x,count(*) y from vm772_58dd091a279b5392.messagetemplatecategkwkwory group by parentid",
            "父级分类ID用于构建分类层级结构",
        )
    # messagetemplatecategkwkwory(消息模板分类表)->skwkwortkwkworder(排序顺序用于控制分类在列中的显示顺序)

    if obj.get("optype") == "messagetemplatecategkwkwory.skwkwortkwkworder_pie":
        res = get_pie(
            "select skwkwortkwkworder x,count(*) y from vm772_58dd091a279b5392.messagetemplatecategkwkwory group by skwkwortkwkworder order by x desc",
            "排序顺序用于控制分类在列中的显示顺序",
        )
    if obj.get("optype") == "messagetemplatecategkwkwory.skwkwortkwkworder_pie_v1":
        res = get_pie_v1(
            "select skwkwortkwkworder x,count(*) y from vm772_58dd091a279b5392.messagetemplatecategkwkwory group by skwkwortkwkworder",
            "排序顺序用于控制分类在列中的显示顺序",
        )
    if obj.get("optype") == "messagetemplatecategkwkwory.skwkwortkwkworder_pie_v2":
        res = get_pie_v2(
            "select skwkwortkwkworder x,count(*) y from vm772_58dd091a279b5392.messagetemplatecategkwkwory group by skwkwortkwkworder",
            "排序顺序用于控制分类在列中的显示顺序",
        )
    if obj.get("optype") == "messagetemplatecategkwkwory.skwkwortkwkworder_line":
        res = get_line(
            "select skwkwortkwkworder x,count(*) y from vm772_58dd091a279b5392.messagetemplatecategkwkwory group by skwkwortkwkworder",
            "排序顺序用于控制分类在列中的显示顺序",
        )
    if obj.get("optype") == "messagetemplatecategkwkwory.skwkwortkwkworder_bar":
        res = get_bar(
            "select skwkwortkwkworder x,count(*) y from vm772_58dd091a279b5392.messagetemplatecategkwkwory group by skwkwortkwkworder",
            "排序顺序用于控制分类在列中的显示顺序",
        )
    if obj.get("optype") == "messagetemplatecategkwkwory.skwkwortkwkworder_bar_v1":
        res = get_bar_v1(
            "select skwkwortkwkworder x,count(*) y from vm772_58dd091a279b5392.messagetemplatecategkwkwory group by skwkwortkwkworder",
            "排序顺序用于控制分类在列中的显示顺序",
        )
    # messagetemplatecategkwkwory(消息模板分类表)->templatecount(模板数量可选统计属于该分类的消息模板数量可通过触发器或应用逻辑维护)

    if obj.get("optype") == "messagetemplatecategkwkwory.templatecount_pie":
        res = get_pie(
            "select templatecount x,count(*) y from vm772_58dd091a279b5392.messagetemplatecategkwkwory group by templatecount order by x desc",
            "模板数量可选统计属于该分类的消息模板数量可通过触发器或应用逻辑维护",
        )
    if obj.get("optype") == "messagetemplatecategkwkwory.templatecount_pie_v1":
        res = get_pie_v1(
            "select templatecount x,count(*) y from vm772_58dd091a279b5392.messagetemplatecategkwkwory group by templatecount",
            "模板数量可选统计属于该分类的消息模板数量可通过触发器或应用逻辑维护",
        )
    if obj.get("optype") == "messagetemplatecategkwkwory.templatecount_pie_v2":
        res = get_pie_v2(
            "select templatecount x,count(*) y from vm772_58dd091a279b5392.messagetemplatecategkwkwory group by templatecount",
            "模板数量可选统计属于该分类的消息模板数量可通过触发器或应用逻辑维护",
        )
    if obj.get("optype") == "messagetemplatecategkwkwory.templatecount_line":
        res = get_line(
            "select templatecount x,count(*) y from vm772_58dd091a279b5392.messagetemplatecategkwkwory group by templatecount",
            "模板数量可选统计属于该分类的消息模板数量可通过触发器或应用逻辑维护",
        )
    if obj.get("optype") == "messagetemplatecategkwkwory.templatecount_bar":
        res = get_bar(
            "select templatecount x,count(*) y from vm772_58dd091a279b5392.messagetemplatecategkwkwory group by templatecount",
            "模板数量可选统计属于该分类的消息模板数量可通过触发器或应用逻辑维护",
        )
    if obj.get("optype") == "messagetemplatecategkwkwory.templatecount_bar_v1":
        res = get_bar_v1(
            "select templatecount x,count(*) y from vm772_58dd091a279b5392.messagetemplatecategkwkwory group by templatecount",
            "模板数量可选统计属于该分类的消息模板数量可通过触发器或应用逻辑维护",
        )
    # messagetemplatetag(消息模板标签表)->templateid(消息模板ID关联字段指向消息模板的ID)

    if obj.get("optype") == "messagetemplatetag.templateid_pie":
        res = get_pie(
            "select templateid x,count(*) y from vm772_58dd091a279b5392.messagetemplatetag group by templateid order by x desc",
            "消息模板ID关联字段指向消息模板的ID",
        )
    if obj.get("optype") == "messagetemplatetag.templateid_pie_v1":
        res = get_pie_v1(
            "select templateid x,count(*) y from vm772_58dd091a279b5392.messagetemplatetag group by templateid",
            "消息模板ID关联字段指向消息模板的ID",
        )
    if obj.get("optype") == "messagetemplatetag.templateid_pie_v2":
        res = get_pie_v2(
            "select templateid x,count(*) y from vm772_58dd091a279b5392.messagetemplatetag group by templateid",
            "消息模板ID关联字段指向消息模板的ID",
        )
    if obj.get("optype") == "messagetemplatetag.templateid_line":
        res = get_line(
            "select templateid x,count(*) y from vm772_58dd091a279b5392.messagetemplatetag group by templateid",
            "消息模板ID关联字段指向消息模板的ID",
        )
    if obj.get("optype") == "messagetemplatetag.templateid_bar":
        res = get_bar(
            "select templateid x,count(*) y from vm772_58dd091a279b5392.messagetemplatetag group by templateid",
            "消息模板ID关联字段指向消息模板的ID",
        )
    if obj.get("optype") == "messagetemplatetag.templateid_bar_v1":
        res = get_bar_v1(
            "select templateid x,count(*) y from vm772_58dd091a279b5392.messagetemplatetag group by templateid",
            "消息模板ID关联字段指向消息模板的ID",
        )
    # messagetemplatetag(消息模板标签表)->tagname(标签名称)

    if obj.get("optype") == "messagetemplatetag.tagname_pie":
        res = get_pie(
            "select tagname x,count(*) y from vm772_58dd091a279b5392.messagetemplatetag group by tagname order by x desc",
            "标签名称",
        )
    if obj.get("optype") == "messagetemplatetag.tagname_pie_v1":
        res = get_pie_v1(
            "select tagname x,count(*) y from vm772_58dd091a279b5392.messagetemplatetag group by tagname",
            "标签名称",
        )
    if obj.get("optype") == "messagetemplatetag.tagname_pie_v2":
        res = get_pie_v2(
            "select tagname x,count(*) y from vm772_58dd091a279b5392.messagetemplatetag group by tagname",
            "标签名称",
        )
    if obj.get("optype") == "messagetemplatetag.tagname_line":
        res = get_line(
            "select tagname x,count(*) y from vm772_58dd091a279b5392.messagetemplatetag group by tagname",
            "标签名称",
        )
    if obj.get("optype") == "messagetemplatetag.tagname_bar":
        res = get_bar(
            "select tagname x,count(*) y from vm772_58dd091a279b5392.messagetemplatetag group by tagname",
            "标签名称",
        )
    if obj.get("optype") == "messagetemplatetag.tagname_bar_v1":
        res = get_bar_v1(
            "select tagname x,count(*) y from vm772_58dd091a279b5392.messagetemplatetag group by tagname",
            "标签名称",
        )
    if obj.get("optype") == "messagetemplatetag.description_wordcloud":
        textlist = get_data(
            "SELECT description result FROM vm772_58dd091a279b5392.messagetemplatetag;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "messagetemplatetag.createdat_line":
        res = get_line(
            "select createdat x,count(*) y from vm772_58dd091a279b5392.messagetemplatetag group by createdat order by x",
            "创建时间",
        )
    if obj.get("optype") == "messagetemplatetag.updatedat_line":
        res = get_line(
            "select updatedat x,count(*) y from vm772_58dd091a279b5392.messagetemplatetag group by updatedat order by x",
            "更新时间",
        )
    # messagetemplatetag(消息模板标签表)->kwkwisactive(是否激活用于控制标签是否可用)

    if obj.get("optype") == "messagetemplatetag.kwkwisactive_pie":
        res = get_pie(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.messagetemplatetag group by kwkwisactive order by x desc",
            "是否激活用于控制标签是否可用",
        )
    if obj.get("optype") == "messagetemplatetag.kwkwisactive_pie_v1":
        res = get_pie_v1(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.messagetemplatetag group by kwkwisactive",
            "是否激活用于控制标签是否可用",
        )
    if obj.get("optype") == "messagetemplatetag.kwkwisactive_pie_v2":
        res = get_pie_v2(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.messagetemplatetag group by kwkwisactive",
            "是否激活用于控制标签是否可用",
        )
    if obj.get("optype") == "messagetemplatetag.kwkwisactive_line":
        res = get_line(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.messagetemplatetag group by kwkwisactive",
            "是否激活用于控制标签是否可用",
        )
    if obj.get("optype") == "messagetemplatetag.kwkwisactive_bar":
        res = get_bar(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.messagetemplatetag group by kwkwisactive",
            "是否激活用于控制标签是否可用",
        )
    if obj.get("optype") == "messagetemplatetag.kwkwisactive_bar_v1":
        res = get_bar_v1(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.messagetemplatetag group by kwkwisactive",
            "是否激活用于控制标签是否可用",
        )
    # messagetemplatetag(消息模板标签表)->usagecount(使用次数记录该标签被用于消息模板的次数)

    if obj.get("optype") == "messagetemplatetag.usagecount_pie":
        res = get_pie(
            "select usagecount x,count(*) y from vm772_58dd091a279b5392.messagetemplatetag group by usagecount order by x desc",
            "使用次数记录该标签被用于消息模板的次数",
        )
    if obj.get("optype") == "messagetemplatetag.usagecount_pie_v1":
        res = get_pie_v1(
            "select usagecount x,count(*) y from vm772_58dd091a279b5392.messagetemplatetag group by usagecount",
            "使用次数记录该标签被用于消息模板的次数",
        )
    if obj.get("optype") == "messagetemplatetag.usagecount_pie_v2":
        res = get_pie_v2(
            "select usagecount x,count(*) y from vm772_58dd091a279b5392.messagetemplatetag group by usagecount",
            "使用次数记录该标签被用于消息模板的次数",
        )
    if obj.get("optype") == "messagetemplatetag.usagecount_line":
        res = get_line(
            "select usagecount x,count(*) y from vm772_58dd091a279b5392.messagetemplatetag group by usagecount",
            "使用次数记录该标签被用于消息模板的次数",
        )
    if obj.get("optype") == "messagetemplatetag.usagecount_bar":
        res = get_bar(
            "select usagecount x,count(*) y from vm772_58dd091a279b5392.messagetemplatetag group by usagecount",
            "使用次数记录该标签被用于消息模板的次数",
        )
    if obj.get("optype") == "messagetemplatetag.usagecount_bar_v1":
        res = get_bar_v1(
            "select usagecount x,count(*) y from vm772_58dd091a279b5392.messagetemplatetag group by usagecount",
            "使用次数记录该标签被用于消息模板的次数",
        )
    # messagetemplatetag(消息模板标签表)->creatkwkworid(创建者ID关联字段指向用户的ID)

    if obj.get("optype") == "messagetemplatetag.creatkwkworid_pie":
        res = get_pie(
            "select creatkwkworid x,count(*) y from vm772_58dd091a279b5392.messagetemplatetag group by creatkwkworid order by x desc",
            "创建者ID关联字段指向用户的ID",
        )
    if obj.get("optype") == "messagetemplatetag.creatkwkworid_pie_v1":
        res = get_pie_v1(
            "select creatkwkworid x,count(*) y from vm772_58dd091a279b5392.messagetemplatetag group by creatkwkworid",
            "创建者ID关联字段指向用户的ID",
        )
    if obj.get("optype") == "messagetemplatetag.creatkwkworid_pie_v2":
        res = get_pie_v2(
            "select creatkwkworid x,count(*) y from vm772_58dd091a279b5392.messagetemplatetag group by creatkwkworid",
            "创建者ID关联字段指向用户的ID",
        )
    if obj.get("optype") == "messagetemplatetag.creatkwkworid_line":
        res = get_line(
            "select creatkwkworid x,count(*) y from vm772_58dd091a279b5392.messagetemplatetag group by creatkwkworid",
            "创建者ID关联字段指向用户的ID",
        )
    if obj.get("optype") == "messagetemplatetag.creatkwkworid_bar":
        res = get_bar(
            "select creatkwkworid x,count(*) y from vm772_58dd091a279b5392.messagetemplatetag group by creatkwkworid",
            "创建者ID关联字段指向用户的ID",
        )
    if obj.get("optype") == "messagetemplatetag.creatkwkworid_bar_v1":
        res = get_bar_v1(
            "select creatkwkworid x,count(*) y from vm772_58dd091a279b5392.messagetemplatetag group by creatkwkworid",
            "创建者ID关联字段指向用户的ID",
        )
    # userpermkwkwission(用户权限表)->userid(用户ID)

    if obj.get("optype") == "userpermkwkwission.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm772_58dd091a279b5392.userpermkwkwission group by userid order by x desc",
            "用户ID",
        )
    if obj.get("optype") == "userpermkwkwission.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm772_58dd091a279b5392.userpermkwkwission group by userid",
            "用户ID",
        )
    if obj.get("optype") == "userpermkwkwission.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm772_58dd091a279b5392.userpermkwkwission group by userid",
            "用户ID",
        )
    if obj.get("optype") == "userpermkwkwission.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm772_58dd091a279b5392.userpermkwkwission group by userid",
            "用户ID",
        )
    if obj.get("optype") == "userpermkwkwission.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm772_58dd091a279b5392.userpermkwkwission group by userid",
            "用户ID",
        )
    if obj.get("optype") == "userpermkwkwission.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm772_58dd091a279b5392.userpermkwkwission group by userid",
            "用户ID",
        )
    # userpermkwkwission(用户权限表)->permkwkwissionid(权限ID)

    if obj.get("optype") == "userpermkwkwission.permkwkwissionid_pie":
        res = get_pie(
            "select permkwkwissionid x,count(*) y from vm772_58dd091a279b5392.userpermkwkwission group by permkwkwissionid order by x desc",
            "权限ID",
        )
    if obj.get("optype") == "userpermkwkwission.permkwkwissionid_pie_v1":
        res = get_pie_v1(
            "select permkwkwissionid x,count(*) y from vm772_58dd091a279b5392.userpermkwkwission group by permkwkwissionid",
            "权限ID",
        )
    if obj.get("optype") == "userpermkwkwission.permkwkwissionid_pie_v2":
        res = get_pie_v2(
            "select permkwkwissionid x,count(*) y from vm772_58dd091a279b5392.userpermkwkwission group by permkwkwissionid",
            "权限ID",
        )
    if obj.get("optype") == "userpermkwkwission.permkwkwissionid_line":
        res = get_line(
            "select permkwkwissionid x,count(*) y from vm772_58dd091a279b5392.userpermkwkwission group by permkwkwissionid",
            "权限ID",
        )
    if obj.get("optype") == "userpermkwkwission.permkwkwissionid_bar":
        res = get_bar(
            "select permkwkwissionid x,count(*) y from vm772_58dd091a279b5392.userpermkwkwission group by permkwkwissionid",
            "权限ID",
        )
    if obj.get("optype") == "userpermkwkwission.permkwkwissionid_bar_v1":
        res = get_bar_v1(
            "select permkwkwissionid x,count(*) y from vm772_58dd091a279b5392.userpermkwkwission group by permkwkwissionid",
            "权限ID",
        )
    # userpermkwkwission(用户权限表)->permkwkwissionname(权限名称)

    if obj.get("optype") == "userpermkwkwission.permkwkwissionname_pie":
        res = get_pie(
            "select permkwkwissionname x,count(*) y from vm772_58dd091a279b5392.userpermkwkwission group by permkwkwissionname order by x desc",
            "权限名称",
        )
    if obj.get("optype") == "userpermkwkwission.permkwkwissionname_pie_v1":
        res = get_pie_v1(
            "select permkwkwissionname x,count(*) y from vm772_58dd091a279b5392.userpermkwkwission group by permkwkwissionname",
            "权限名称",
        )
    if obj.get("optype") == "userpermkwkwission.permkwkwissionname_pie_v2":
        res = get_pie_v2(
            "select permkwkwissionname x,count(*) y from vm772_58dd091a279b5392.userpermkwkwission group by permkwkwissionname",
            "权限名称",
        )
    if obj.get("optype") == "userpermkwkwission.permkwkwissionname_line":
        res = get_line(
            "select permkwkwissionname x,count(*) y from vm772_58dd091a279b5392.userpermkwkwission group by permkwkwissionname",
            "权限名称",
        )
    if obj.get("optype") == "userpermkwkwission.permkwkwissionname_bar":
        res = get_bar(
            "select permkwkwissionname x,count(*) y from vm772_58dd091a279b5392.userpermkwkwission group by permkwkwissionname",
            "权限名称",
        )
    if obj.get("optype") == "userpermkwkwission.permkwkwissionname_bar_v1":
        res = get_bar_v1(
            "select permkwkwissionname x,count(*) y from vm772_58dd091a279b5392.userpermkwkwission group by permkwkwissionname",
            "权限名称",
        )
    if obj.get("optype") == "userpermkwkwission.permkwkwissiondescription_wordcloud":
        textlist = get_data(
            "SELECT permkwkwissiondescription result FROM vm772_58dd091a279b5392.userpermkwkwission;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "userpermkwkwission.createtime_line":
        res = get_line(
            "select createtime x,count(*) y from vm772_58dd091a279b5392.userpermkwkwission group by createtime order by x",
            "创建时间",
        )
    if obj.get("optype") == "userpermkwkwission.updatetime_line":
        res = get_line(
            "select updatetime x,count(*) y from vm772_58dd091a279b5392.userpermkwkwission group by updatetime order by x",
            "更新时间",
        )
    # userpermkwkwission(用户权限表)->isactive(是否激活)

    if obj.get("optype") == "userpermkwkwission.isactive_pie":
        res = get_pie(
            "select isactive x,count(*) y from vm772_58dd091a279b5392.userpermkwkwission group by isactive order by x desc",
            "是否激活",
        )
    if obj.get("optype") == "userpermkwkwission.isactive_pie_v1":
        res = get_pie_v1(
            "select isactive x,count(*) y from vm772_58dd091a279b5392.userpermkwkwission group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "userpermkwkwission.isactive_pie_v2":
        res = get_pie_v2(
            "select isactive x,count(*) y from vm772_58dd091a279b5392.userpermkwkwission group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "userpermkwkwission.isactive_line":
        res = get_line(
            "select isactive x,count(*) y from vm772_58dd091a279b5392.userpermkwkwission group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "userpermkwkwission.isactive_bar":
        res = get_bar(
            "select isactive x,count(*) y from vm772_58dd091a279b5392.userpermkwkwission group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "userpermkwkwission.isactive_bar_v1":
        res = get_bar_v1(
            "select isactive x,count(*) y from vm772_58dd091a279b5392.userpermkwkwission group by isactive",
            "是否激活",
        )
    # userpermkwkwission(用户权限表)->isdeleted(是否删除)

    if obj.get("optype") == "userpermkwkwission.isdeleted_pie":
        res = get_pie(
            "select isdeleted x,count(*) y from vm772_58dd091a279b5392.userpermkwkwission group by isdeleted order by x desc",
            "是否删除",
        )
    if obj.get("optype") == "userpermkwkwission.isdeleted_pie_v1":
        res = get_pie_v1(
            "select isdeleted x,count(*) y from vm772_58dd091a279b5392.userpermkwkwission group by isdeleted",
            "是否删除",
        )
    if obj.get("optype") == "userpermkwkwission.isdeleted_pie_v2":
        res = get_pie_v2(
            "select isdeleted x,count(*) y from vm772_58dd091a279b5392.userpermkwkwission group by isdeleted",
            "是否删除",
        )
    if obj.get("optype") == "userpermkwkwission.isdeleted_line":
        res = get_line(
            "select isdeleted x,count(*) y from vm772_58dd091a279b5392.userpermkwkwission group by isdeleted",
            "是否删除",
        )
    if obj.get("optype") == "userpermkwkwission.isdeleted_bar":
        res = get_bar(
            "select isdeleted x,count(*) y from vm772_58dd091a279b5392.userpermkwkwission group by isdeleted",
            "是否删除",
        )
    if obj.get("optype") == "userpermkwkwission.isdeleted_bar_v1":
        res = get_bar_v1(
            "select isdeleted x,count(*) y from vm772_58dd091a279b5392.userpermkwkwission group by isdeleted",
            "是否删除",
        )
    # userpermkwkwission(用户权限表)->rolename(角色名称关联字段)

    if obj.get("optype") == "userpermkwkwission.rolename_pie":
        res = get_pie(
            "select rolename x,count(*) y from vm772_58dd091a279b5392.userpermkwkwission group by rolename order by x desc",
            "角色名称关联字段",
        )
    if obj.get("optype") == "userpermkwkwission.rolename_pie_v1":
        res = get_pie_v1(
            "select rolename x,count(*) y from vm772_58dd091a279b5392.userpermkwkwission group by rolename",
            "角色名称关联字段",
        )
    if obj.get("optype") == "userpermkwkwission.rolename_pie_v2":
        res = get_pie_v2(
            "select rolename x,count(*) y from vm772_58dd091a279b5392.userpermkwkwission group by rolename",
            "角色名称关联字段",
        )
    if obj.get("optype") == "userpermkwkwission.rolename_line":
        res = get_line(
            "select rolename x,count(*) y from vm772_58dd091a279b5392.userpermkwkwission group by rolename",
            "角色名称关联字段",
        )
    if obj.get("optype") == "userpermkwkwission.rolename_bar":
        res = get_bar(
            "select rolename x,count(*) y from vm772_58dd091a279b5392.userpermkwkwission group by rolename",
            "角色名称关联字段",
        )
    if obj.get("optype") == "userpermkwkwission.rolename_bar_v1":
        res = get_bar_v1(
            "select rolename x,count(*) y from vm772_58dd091a279b5392.userpermkwkwission group by rolename",
            "角色名称关联字段",
        )
    # systemconfig(系统配置表)->configname(配置名称)

    if obj.get("optype") == "systemconfig.configname_pie":
        res = get_pie(
            "select configname x,count(*) y from vm772_58dd091a279b5392.systemconfig group by configname order by x desc",
            "配置名称",
        )
    if obj.get("optype") == "systemconfig.configname_pie_v1":
        res = get_pie_v1(
            "select configname x,count(*) y from vm772_58dd091a279b5392.systemconfig group by configname",
            "配置名称",
        )
    if obj.get("optype") == "systemconfig.configname_pie_v2":
        res = get_pie_v2(
            "select configname x,count(*) y from vm772_58dd091a279b5392.systemconfig group by configname",
            "配置名称",
        )
    if obj.get("optype") == "systemconfig.configname_line":
        res = get_line(
            "select configname x,count(*) y from vm772_58dd091a279b5392.systemconfig group by configname",
            "配置名称",
        )
    if obj.get("optype") == "systemconfig.configname_bar":
        res = get_bar(
            "select configname x,count(*) y from vm772_58dd091a279b5392.systemconfig group by configname",
            "配置名称",
        )
    if obj.get("optype") == "systemconfig.configname_bar_v1":
        res = get_bar_v1(
            "select configname x,count(*) y from vm772_58dd091a279b5392.systemconfig group by configname",
            "配置名称",
        )
    # systemconfig(系统配置表)->configvalue(配置值)

    if obj.get("optype") == "systemconfig.configvalue_pie":
        res = get_pie(
            "select configvalue x,count(*) y from vm772_58dd091a279b5392.systemconfig group by configvalue order by x desc",
            "配置值",
        )
    if obj.get("optype") == "systemconfig.configvalue_pie_v1":
        res = get_pie_v1(
            "select configvalue x,count(*) y from vm772_58dd091a279b5392.systemconfig group by configvalue",
            "配置值",
        )
    if obj.get("optype") == "systemconfig.configvalue_pie_v2":
        res = get_pie_v2(
            "select configvalue x,count(*) y from vm772_58dd091a279b5392.systemconfig group by configvalue",
            "配置值",
        )
    if obj.get("optype") == "systemconfig.configvalue_line":
        res = get_line(
            "select configvalue x,count(*) y from vm772_58dd091a279b5392.systemconfig group by configvalue",
            "配置值",
        )
    if obj.get("optype") == "systemconfig.configvalue_bar":
        res = get_bar(
            "select configvalue x,count(*) y from vm772_58dd091a279b5392.systemconfig group by configvalue",
            "配置值",
        )
    if obj.get("optype") == "systemconfig.configvalue_bar_v1":
        res = get_bar_v1(
            "select configvalue x,count(*) y from vm772_58dd091a279b5392.systemconfig group by configvalue",
            "配置值",
        )
    if obj.get("optype") == "systemconfig.description_wordcloud":
        textlist = get_data(
            "SELECT description result FROM vm772_58dd091a279b5392.systemconfig;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "systemconfig.createtime_line":
        res = get_line(
            "select createtime x,count(*) y from vm772_58dd091a279b5392.systemconfig group by createtime order by x",
            "创建时间",
        )
    if obj.get("optype") == "systemconfig.updatetime_line":
        res = get_line(
            "select updatetime x,count(*) y from vm772_58dd091a279b5392.systemconfig group by updatetime order by x",
            "更新时间",
        )
    # systemconfig(系统配置表)->kwkwisactive(是否激活1为激活0为未激活)

    if obj.get("optype") == "systemconfig.kwkwisactive_pie":
        res = get_pie(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.systemconfig group by kwkwisactive order by x desc",
            "是否激活1为激活0为未激活",
        )
    if obj.get("optype") == "systemconfig.kwkwisactive_pie_v1":
        res = get_pie_v1(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.systemconfig group by kwkwisactive",
            "是否激活1为激活0为未激活",
        )
    if obj.get("optype") == "systemconfig.kwkwisactive_pie_v2":
        res = get_pie_v2(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.systemconfig group by kwkwisactive",
            "是否激活1为激活0为未激活",
        )
    if obj.get("optype") == "systemconfig.kwkwisactive_line":
        res = get_line(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.systemconfig group by kwkwisactive",
            "是否激活1为激活0为未激活",
        )
    if obj.get("optype") == "systemconfig.kwkwisactive_bar":
        res = get_bar(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.systemconfig group by kwkwisactive",
            "是否激活1为激活0为未激活",
        )
    if obj.get("optype") == "systemconfig.kwkwisactive_bar_v1":
        res = get_bar_v1(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.systemconfig group by kwkwisactive",
            "是否激活1为激活0为未激活",
        )
    # systemconfig(系统配置表)->creatkwkworid(创建者ID)

    if obj.get("optype") == "systemconfig.creatkwkworid_pie":
        res = get_pie(
            "select creatkwkworid x,count(*) y from vm772_58dd091a279b5392.systemconfig group by creatkwkworid order by x desc",
            "创建者ID",
        )
    if obj.get("optype") == "systemconfig.creatkwkworid_pie_v1":
        res = get_pie_v1(
            "select creatkwkworid x,count(*) y from vm772_58dd091a279b5392.systemconfig group by creatkwkworid",
            "创建者ID",
        )
    if obj.get("optype") == "systemconfig.creatkwkworid_pie_v2":
        res = get_pie_v2(
            "select creatkwkworid x,count(*) y from vm772_58dd091a279b5392.systemconfig group by creatkwkworid",
            "创建者ID",
        )
    if obj.get("optype") == "systemconfig.creatkwkworid_line":
        res = get_line(
            "select creatkwkworid x,count(*) y from vm772_58dd091a279b5392.systemconfig group by creatkwkworid",
            "创建者ID",
        )
    if obj.get("optype") == "systemconfig.creatkwkworid_bar":
        res = get_bar(
            "select creatkwkworid x,count(*) y from vm772_58dd091a279b5392.systemconfig group by creatkwkworid",
            "创建者ID",
        )
    if obj.get("optype") == "systemconfig.creatkwkworid_bar_v1":
        res = get_bar_v1(
            "select creatkwkworid x,count(*) y from vm772_58dd091a279b5392.systemconfig group by creatkwkworid",
            "创建者ID",
        )
    # systemconfig(系统配置表)->relatedsystemid(关联系统ID)

    if obj.get("optype") == "systemconfig.relatedsystemid_pie":
        res = get_pie(
            "select relatedsystemid x,count(*) y from vm772_58dd091a279b5392.systemconfig group by relatedsystemid order by x desc",
            "关联系统ID",
        )
    if obj.get("optype") == "systemconfig.relatedsystemid_pie_v1":
        res = get_pie_v1(
            "select relatedsystemid x,count(*) y from vm772_58dd091a279b5392.systemconfig group by relatedsystemid",
            "关联系统ID",
        )
    if obj.get("optype") == "systemconfig.relatedsystemid_pie_v2":
        res = get_pie_v2(
            "select relatedsystemid x,count(*) y from vm772_58dd091a279b5392.systemconfig group by relatedsystemid",
            "关联系统ID",
        )
    if obj.get("optype") == "systemconfig.relatedsystemid_line":
        res = get_line(
            "select relatedsystemid x,count(*) y from vm772_58dd091a279b5392.systemconfig group by relatedsystemid",
            "关联系统ID",
        )
    if obj.get("optype") == "systemconfig.relatedsystemid_bar":
        res = get_bar(
            "select relatedsystemid x,count(*) y from vm772_58dd091a279b5392.systemconfig group by relatedsystemid",
            "关联系统ID",
        )
    if obj.get("optype") == "systemconfig.relatedsystemid_bar_v1":
        res = get_bar_v1(
            "select relatedsystemid x,count(*) y from vm772_58dd091a279b5392.systemconfig group by relatedsystemid",
            "关联系统ID",
        )
    # notkwkwificationpush(通知推送表)->platkwkwfkwkwormid(平台ID关联字段指向平台的ID)

    if obj.get("optype") == "notkwkwificationpush.platkwkwfkwkwormid_pie":
        res = get_pie(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.notkwkwificationpush group by platkwkwfkwkwormid order by x desc",
            "平台ID关联字段指向平台的ID",
        )
    if obj.get("optype") == "notkwkwificationpush.platkwkwfkwkwormid_pie_v1":
        res = get_pie_v1(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.notkwkwificationpush group by platkwkwfkwkwormid",
            "平台ID关联字段指向平台的ID",
        )
    if obj.get("optype") == "notkwkwificationpush.platkwkwfkwkwormid_pie_v2":
        res = get_pie_v2(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.notkwkwificationpush group by platkwkwfkwkwormid",
            "平台ID关联字段指向平台的ID",
        )
    if obj.get("optype") == "notkwkwificationpush.platkwkwfkwkwormid_line":
        res = get_line(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.notkwkwificationpush group by platkwkwfkwkwormid",
            "平台ID关联字段指向平台的ID",
        )
    if obj.get("optype") == "notkwkwificationpush.platkwkwfkwkwormid_bar":
        res = get_bar(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.notkwkwificationpush group by platkwkwfkwkwormid",
            "平台ID关联字段指向平台的ID",
        )
    if obj.get("optype") == "notkwkwificationpush.platkwkwfkwkwormid_bar_v1":
        res = get_bar_v1(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.notkwkwificationpush group by platkwkwfkwkwormid",
            "平台ID关联字段指向平台的ID",
        )
    # notkwkwificationpush(通知推送表)->userid(用户ID关联字段指向用户的ID)

    if obj.get("optype") == "notkwkwificationpush.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm772_58dd091a279b5392.notkwkwificationpush group by userid order by x desc",
            "用户ID关联字段指向用户的ID",
        )
    if obj.get("optype") == "notkwkwificationpush.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm772_58dd091a279b5392.notkwkwificationpush group by userid",
            "用户ID关联字段指向用户的ID",
        )
    if obj.get("optype") == "notkwkwificationpush.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm772_58dd091a279b5392.notkwkwificationpush group by userid",
            "用户ID关联字段指向用户的ID",
        )
    if obj.get("optype") == "notkwkwificationpush.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm772_58dd091a279b5392.notkwkwificationpush group by userid",
            "用户ID关联字段指向用户的ID",
        )
    if obj.get("optype") == "notkwkwificationpush.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm772_58dd091a279b5392.notkwkwificationpush group by userid",
            "用户ID关联字段指向用户的ID",
        )
    if obj.get("optype") == "notkwkwificationpush.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm772_58dd091a279b5392.notkwkwificationpush group by userid",
            "用户ID关联字段指向用户的ID",
        )
    if obj.get("optype") == "notkwkwificationpush.messagecontent_wordcloud":
        textlist = get_data(
            "SELECT messagecontent result FROM vm772_58dd091a279b5392.notkwkwificationpush;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # notkwkwificationpush(通知推送表)->pushstatus(推送状态例如待推送、已推送、推送失败)

    if obj.get("optype") == "notkwkwificationpush.pushstatus_pie":
        res = get_pie(
            "select pushstatus x,count(*) y from vm772_58dd091a279b5392.notkwkwificationpush group by pushstatus order by x desc",
            "推送状态例如待推送、已推送、推送失败",
        )
    if obj.get("optype") == "notkwkwificationpush.pushstatus_pie_v1":
        res = get_pie_v1(
            "select pushstatus x,count(*) y from vm772_58dd091a279b5392.notkwkwificationpush group by pushstatus",
            "推送状态例如待推送、已推送、推送失败",
        )
    if obj.get("optype") == "notkwkwificationpush.pushstatus_pie_v2":
        res = get_pie_v2(
            "select pushstatus x,count(*) y from vm772_58dd091a279b5392.notkwkwificationpush group by pushstatus",
            "推送状态例如待推送、已推送、推送失败",
        )
    if obj.get("optype") == "notkwkwificationpush.pushstatus_line":
        res = get_line(
            "select pushstatus x,count(*) y from vm772_58dd091a279b5392.notkwkwificationpush group by pushstatus",
            "推送状态例如待推送、已推送、推送失败",
        )
    if obj.get("optype") == "notkwkwificationpush.pushstatus_bar":
        res = get_bar(
            "select pushstatus x,count(*) y from vm772_58dd091a279b5392.notkwkwificationpush group by pushstatus",
            "推送状态例如待推送、已推送、推送失败",
        )
    if obj.get("optype") == "notkwkwificationpush.pushstatus_bar_v1":
        res = get_bar_v1(
            "select pushstatus x,count(*) y from vm772_58dd091a279b5392.notkwkwificationpush group by pushstatus",
            "推送状态例如待推送、已推送、推送失败",
        )
    if obj.get("optype") == "notkwkwificationpush.pushtime_line":
        res = get_line(
            "select pushtime x,count(*) y from vm772_58dd091a279b5392.notkwkwificationpush group by pushtime order by x",
            "推送时间",
        )
    # notkwkwificationpush(通知推送表)->rekwkwtrycount(重试次数)

    if obj.get("optype") == "notkwkwificationpush.rekwkwtrycount_pie":
        res = get_pie(
            "select rekwkwtrycount x,count(*) y from vm772_58dd091a279b5392.notkwkwificationpush group by rekwkwtrycount order by x desc",
            "重试次数",
        )
    if obj.get("optype") == "notkwkwificationpush.rekwkwtrycount_pie_v1":
        res = get_pie_v1(
            "select rekwkwtrycount x,count(*) y from vm772_58dd091a279b5392.notkwkwificationpush group by rekwkwtrycount",
            "重试次数",
        )
    if obj.get("optype") == "notkwkwificationpush.rekwkwtrycount_pie_v2":
        res = get_pie_v2(
            "select rekwkwtrycount x,count(*) y from vm772_58dd091a279b5392.notkwkwificationpush group by rekwkwtrycount",
            "重试次数",
        )
    if obj.get("optype") == "notkwkwificationpush.rekwkwtrycount_line":
        res = get_line(
            "select rekwkwtrycount x,count(*) y from vm772_58dd091a279b5392.notkwkwificationpush group by rekwkwtrycount",
            "重试次数",
        )
    if obj.get("optype") == "notkwkwificationpush.rekwkwtrycount_bar":
        res = get_bar(
            "select rekwkwtrycount x,count(*) y from vm772_58dd091a279b5392.notkwkwificationpush group by rekwkwtrycount",
            "重试次数",
        )
    if obj.get("optype") == "notkwkwificationpush.rekwkwtrycount_bar_v1":
        res = get_bar_v1(
            "select rekwkwtrycount x,count(*) y from vm772_58dd091a279b5392.notkwkwificationpush group by rekwkwtrycount",
            "重试次数",
        )
    # notkwkwificationpush(通知推送表)->failrekwkwason(失败原因)

    if obj.get("optype") == "notkwkwificationpush.failrekwkwason_pie":
        res = get_pie(
            "select failrekwkwason x,count(*) y from vm772_58dd091a279b5392.notkwkwificationpush group by failrekwkwason order by x desc",
            "失败原因",
        )
    if obj.get("optype") == "notkwkwificationpush.failrekwkwason_pie_v1":
        res = get_pie_v1(
            "select failrekwkwason x,count(*) y from vm772_58dd091a279b5392.notkwkwificationpush group by failrekwkwason",
            "失败原因",
        )
    if obj.get("optype") == "notkwkwificationpush.failrekwkwason_pie_v2":
        res = get_pie_v2(
            "select failrekwkwason x,count(*) y from vm772_58dd091a279b5392.notkwkwificationpush group by failrekwkwason",
            "失败原因",
        )
    if obj.get("optype") == "notkwkwificationpush.failrekwkwason_line":
        res = get_line(
            "select failrekwkwason x,count(*) y from vm772_58dd091a279b5392.notkwkwificationpush group by failrekwkwason",
            "失败原因",
        )
    if obj.get("optype") == "notkwkwificationpush.failrekwkwason_bar":
        res = get_bar(
            "select failrekwkwason x,count(*) y from vm772_58dd091a279b5392.notkwkwificationpush group by failrekwkwason",
            "失败原因",
        )
    if obj.get("optype") == "notkwkwificationpush.failrekwkwason_bar_v1":
        res = get_bar_v1(
            "select failrekwkwason x,count(*) y from vm772_58dd091a279b5392.notkwkwificationpush group by failrekwkwason",
            "失败原因",
        )
    if obj.get("optype") == "notkwkwificationpush.createdat_line":
        res = get_line(
            "select createdat x,count(*) y from vm772_58dd091a279b5392.notkwkwificationpush group by createdat order by x",
            "创建时间",
        )
    if obj.get("optype") == "notkwkwificationpush.updatedat_line":
        res = get_line(
            "select updatedat x,count(*) y from vm772_58dd091a279b5392.notkwkwificationpush group by updatedat order by x",
            "更新时间",
        )
    # messagequeue(消息队列表)->platkwkwfkwkworm(平台名称记录消息需要发送的平台如微信、微博等)

    if obj.get("optype") == "messagequeue.platkwkwfkwkworm_pie":
        res = get_pie(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.messagequeue group by platkwkwfkwkworm order by x desc",
            "平台名称记录消息需要发送的平台如微信、微博等",
        )
    if obj.get("optype") == "messagequeue.platkwkwfkwkworm_pie_v1":
        res = get_pie_v1(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.messagequeue group by platkwkwfkwkworm",
            "平台名称记录消息需要发送的平台如微信、微博等",
        )
    if obj.get("optype") == "messagequeue.platkwkwfkwkworm_pie_v2":
        res = get_pie_v2(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.messagequeue group by platkwkwfkwkworm",
            "平台名称记录消息需要发送的平台如微信、微博等",
        )
    if obj.get("optype") == "messagequeue.platkwkwfkwkworm_line":
        res = get_line(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.messagequeue group by platkwkwfkwkworm",
            "平台名称记录消息需要发送的平台如微信、微博等",
        )
    if obj.get("optype") == "messagequeue.platkwkwfkwkworm_bar":
        res = get_bar(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.messagequeue group by platkwkwfkwkworm",
            "平台名称记录消息需要发送的平台如微信、微博等",
        )
    if obj.get("optype") == "messagequeue.platkwkwfkwkworm_bar_v1":
        res = get_bar_v1(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.messagequeue group by platkwkwfkwkworm",
            "平台名称记录消息需要发送的平台如微信、微博等",
        )
    # messagequeue(消息队列表)->userid(用户ID接收消息的用户ID用于标识消息接收者)

    if obj.get("optype") == "messagequeue.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagequeue group by userid order by x desc",
            "用户ID接收消息的用户ID用于标识消息接收者",
        )
    if obj.get("optype") == "messagequeue.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagequeue group by userid",
            "用户ID接收消息的用户ID用于标识消息接收者",
        )
    if obj.get("optype") == "messagequeue.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagequeue group by userid",
            "用户ID接收消息的用户ID用于标识消息接收者",
        )
    if obj.get("optype") == "messagequeue.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagequeue group by userid",
            "用户ID接收消息的用户ID用于标识消息接收者",
        )
    if obj.get("optype") == "messagequeue.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagequeue group by userid",
            "用户ID接收消息的用户ID用于标识消息接收者",
        )
    if obj.get("optype") == "messagequeue.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagequeue group by userid",
            "用户ID接收消息的用户ID用于标识消息接收者",
        )
    if obj.get("optype") == "messagequeue.messagecontent_wordcloud":
        textlist = get_data(
            "SELECT messagecontent result FROM vm772_58dd091a279b5392.messagequeue;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # messagequeue(消息队列表)->status(消息状态如待发送、发送中、已发送、发送失败等)

    if obj.get("optype") == "messagequeue.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagequeue group by status order by x desc",
            "消息状态如待发送、发送中、已发送、发送失败等",
        )
    if obj.get("optype") == "messagequeue.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagequeue group by status",
            "消息状态如待发送、发送中、已发送、发送失败等",
        )
    if obj.get("optype") == "messagequeue.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagequeue group by status",
            "消息状态如待发送、发送中、已发送、发送失败等",
        )
    if obj.get("optype") == "messagequeue.status_line":
        res = get_line(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagequeue group by status",
            "消息状态如待发送、发送中、已发送、发送失败等",
        )
    if obj.get("optype") == "messagequeue.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagequeue group by status",
            "消息状态如待发送、发送中、已发送、发送失败等",
        )
    if obj.get("optype") == "messagequeue.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagequeue group by status",
            "消息状态如待发送、发送中、已发送、发送失败等",
        )
    if obj.get("optype") == "messagequeue.createdat_line":
        res = get_line(
            "select createdat x,count(*) y from vm772_58dd091a279b5392.messagequeue group by createdat order by x",
            "创建时间消息加入队列的时间",
        )
    if obj.get("optype") == "messagequeue.updatedat_line":
        res = get_line(
            "select updatedat x,count(*) y from vm772_58dd091a279b5392.messagequeue group by updatedat order by x",
            "更新时间消息状态最后一次更新的时间",
        )
    # messagequeue(消息队列表)->rekwkwtrycount(重试次数如果消息发送失败记录重试的次数)

    if obj.get("optype") == "messagequeue.rekwkwtrycount_pie":
        res = get_pie(
            "select rekwkwtrycount x,count(*) y from vm772_58dd091a279b5392.messagequeue group by rekwkwtrycount order by x desc",
            "重试次数如果消息发送失败记录重试的次数",
        )
    if obj.get("optype") == "messagequeue.rekwkwtrycount_pie_v1":
        res = get_pie_v1(
            "select rekwkwtrycount x,count(*) y from vm772_58dd091a279b5392.messagequeue group by rekwkwtrycount",
            "重试次数如果消息发送失败记录重试的次数",
        )
    if obj.get("optype") == "messagequeue.rekwkwtrycount_pie_v2":
        res = get_pie_v2(
            "select rekwkwtrycount x,count(*) y from vm772_58dd091a279b5392.messagequeue group by rekwkwtrycount",
            "重试次数如果消息发送失败记录重试的次数",
        )
    if obj.get("optype") == "messagequeue.rekwkwtrycount_line":
        res = get_line(
            "select rekwkwtrycount x,count(*) y from vm772_58dd091a279b5392.messagequeue group by rekwkwtrycount",
            "重试次数如果消息发送失败记录重试的次数",
        )
    if obj.get("optype") == "messagequeue.rekwkwtrycount_bar":
        res = get_bar(
            "select rekwkwtrycount x,count(*) y from vm772_58dd091a279b5392.messagequeue group by rekwkwtrycount",
            "重试次数如果消息发送失败记录重试的次数",
        )
    if obj.get("optype") == "messagequeue.rekwkwtrycount_bar_v1":
        res = get_bar_v1(
            "select rekwkwtrycount x,count(*) y from vm772_58dd091a279b5392.messagequeue group by rekwkwtrycount",
            "重试次数如果消息发送失败记录重试的次数",
        )
    if obj.get("optype") == "messagequeue.nextrekwkwtrytime_line":
        res = get_line(
            "select nextrekwkwtrytime x,count(*) y from vm772_58dd091a279b5392.messagequeue group by nextrekwkwtrytime order by x",
            "下一次重试时间如果消息发送失败记录下一次尝试发送的时间",
        )
    # messagequeuestatus(消息队列状态表)->platkwkwfkwkwormid(平台ID关联字段指向不同平台的唯一标识)

    if obj.get("optype") == "messagequeuestatus.platkwkwfkwkwormid_pie":
        res = get_pie(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.messagequeuestatus group by platkwkwfkwkwormid order by x desc",
            "平台ID关联字段指向不同平台的唯一标识",
        )
    if obj.get("optype") == "messagequeuestatus.platkwkwfkwkwormid_pie_v1":
        res = get_pie_v1(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.messagequeuestatus group by platkwkwfkwkwormid",
            "平台ID关联字段指向不同平台的唯一标识",
        )
    if obj.get("optype") == "messagequeuestatus.platkwkwfkwkwormid_pie_v2":
        res = get_pie_v2(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.messagequeuestatus group by platkwkwfkwkwormid",
            "平台ID关联字段指向不同平台的唯一标识",
        )
    if obj.get("optype") == "messagequeuestatus.platkwkwfkwkwormid_line":
        res = get_line(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.messagequeuestatus group by platkwkwfkwkwormid",
            "平台ID关联字段指向不同平台的唯一标识",
        )
    if obj.get("optype") == "messagequeuestatus.platkwkwfkwkwormid_bar":
        res = get_bar(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.messagequeuestatus group by platkwkwfkwkwormid",
            "平台ID关联字段指向不同平台的唯一标识",
        )
    if obj.get("optype") == "messagequeuestatus.platkwkwfkwkwormid_bar_v1":
        res = get_bar_v1(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.messagequeuestatus group by platkwkwfkwkwormid",
            "平台ID关联字段指向不同平台的唯一标识",
        )
    # messagequeuestatus(消息队列状态表)->messageid(消息ID关联字段指向具体消息的唯一标识)

    if obj.get("optype") == "messagequeuestatus.messageid_pie":
        res = get_pie(
            "select messageid x,count(*) y from vm772_58dd091a279b5392.messagequeuestatus group by messageid order by x desc",
            "消息ID关联字段指向具体消息的唯一标识",
        )
    if obj.get("optype") == "messagequeuestatus.messageid_pie_v1":
        res = get_pie_v1(
            "select messageid x,count(*) y from vm772_58dd091a279b5392.messagequeuestatus group by messageid",
            "消息ID关联字段指向具体消息的唯一标识",
        )
    if obj.get("optype") == "messagequeuestatus.messageid_pie_v2":
        res = get_pie_v2(
            "select messageid x,count(*) y from vm772_58dd091a279b5392.messagequeuestatus group by messageid",
            "消息ID关联字段指向具体消息的唯一标识",
        )
    if obj.get("optype") == "messagequeuestatus.messageid_line":
        res = get_line(
            "select messageid x,count(*) y from vm772_58dd091a279b5392.messagequeuestatus group by messageid",
            "消息ID关联字段指向具体消息的唯一标识",
        )
    if obj.get("optype") == "messagequeuestatus.messageid_bar":
        res = get_bar(
            "select messageid x,count(*) y from vm772_58dd091a279b5392.messagequeuestatus group by messageid",
            "消息ID关联字段指向具体消息的唯一标识",
        )
    if obj.get("optype") == "messagequeuestatus.messageid_bar_v1":
        res = get_bar_v1(
            "select messageid x,count(*) y from vm772_58dd091a279b5392.messagequeuestatus group by messageid",
            "消息ID关联字段指向具体消息的唯一标识",
        )
    # messagequeuestatus(消息队列状态表)->status(状态如待发送、发送中、发送成功、发送失败)

    if obj.get("optype") == "messagequeuestatus.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagequeuestatus group by status order by x desc",
            "状态如待发送、发送中、发送成功、发送失败",
        )
    if obj.get("optype") == "messagequeuestatus.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagequeuestatus group by status",
            "状态如待发送、发送中、发送成功、发送失败",
        )
    if obj.get("optype") == "messagequeuestatus.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagequeuestatus group by status",
            "状态如待发送、发送中、发送成功、发送失败",
        )
    if obj.get("optype") == "messagequeuestatus.status_line":
        res = get_line(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagequeuestatus group by status",
            "状态如待发送、发送中、发送成功、发送失败",
        )
    if obj.get("optype") == "messagequeuestatus.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagequeuestatus group by status",
            "状态如待发送、发送中、发送成功、发送失败",
        )
    if obj.get("optype") == "messagequeuestatus.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagequeuestatus group by status",
            "状态如待发送、发送中、发送成功、发送失败",
        )
    if obj.get("optype") == "messagequeuestatus.createdat_line":
        res = get_line(
            "select createdat x,count(*) y from vm772_58dd091a279b5392.messagequeuestatus group by createdat order by x",
            "创建时间",
        )
    if obj.get("optype") == "messagequeuestatus.updatedat_line":
        res = get_line(
            "select updatedat x,count(*) y from vm772_58dd091a279b5392.messagequeuestatus group by updatedat order by x",
            "更新时间",
        )
    # messagequeuestatus(消息队列状态表)->rekwkwtrycount(重试次数)

    if obj.get("optype") == "messagequeuestatus.rekwkwtrycount_pie":
        res = get_pie(
            "select rekwkwtrycount x,count(*) y from vm772_58dd091a279b5392.messagequeuestatus group by rekwkwtrycount order by x desc",
            "重试次数",
        )
    if obj.get("optype") == "messagequeuestatus.rekwkwtrycount_pie_v1":
        res = get_pie_v1(
            "select rekwkwtrycount x,count(*) y from vm772_58dd091a279b5392.messagequeuestatus group by rekwkwtrycount",
            "重试次数",
        )
    if obj.get("optype") == "messagequeuestatus.rekwkwtrycount_pie_v2":
        res = get_pie_v2(
            "select rekwkwtrycount x,count(*) y from vm772_58dd091a279b5392.messagequeuestatus group by rekwkwtrycount",
            "重试次数",
        )
    if obj.get("optype") == "messagequeuestatus.rekwkwtrycount_line":
        res = get_line(
            "select rekwkwtrycount x,count(*) y from vm772_58dd091a279b5392.messagequeuestatus group by rekwkwtrycount",
            "重试次数",
        )
    if obj.get("optype") == "messagequeuestatus.rekwkwtrycount_bar":
        res = get_bar(
            "select rekwkwtrycount x,count(*) y from vm772_58dd091a279b5392.messagequeuestatus group by rekwkwtrycount",
            "重试次数",
        )
    if obj.get("optype") == "messagequeuestatus.rekwkwtrycount_bar_v1":
        res = get_bar_v1(
            "select rekwkwtrycount x,count(*) y from vm772_58dd091a279b5392.messagequeuestatus group by rekwkwtrycount",
            "重试次数",
        )
    if obj.get("optype") == "messagequeuestatus.nextrekwkwtrytime_line":
        res = get_line(
            "select nextrekwkwtrytime x,count(*) y from vm772_58dd091a279b5392.messagequeuestatus group by nextrekwkwtrytime order by x",
            "下一次重试时间",
        )
    # messagequeuestatus(消息队列状态表)->errkwkwormessage(错误信息如果发送失败记录失败原因)

    if obj.get("optype") == "messagequeuestatus.errkwkwormessage_pie":
        res = get_pie(
            "select errkwkwormessage x,count(*) y from vm772_58dd091a279b5392.messagequeuestatus group by errkwkwormessage order by x desc",
            "错误信息如果发送失败记录失败原因",
        )
    if obj.get("optype") == "messagequeuestatus.errkwkwormessage_pie_v1":
        res = get_pie_v1(
            "select errkwkwormessage x,count(*) y from vm772_58dd091a279b5392.messagequeuestatus group by errkwkwormessage",
            "错误信息如果发送失败记录失败原因",
        )
    if obj.get("optype") == "messagequeuestatus.errkwkwormessage_pie_v2":
        res = get_pie_v2(
            "select errkwkwormessage x,count(*) y from vm772_58dd091a279b5392.messagequeuestatus group by errkwkwormessage",
            "错误信息如果发送失败记录失败原因",
        )
    if obj.get("optype") == "messagequeuestatus.errkwkwormessage_line":
        res = get_line(
            "select errkwkwormessage x,count(*) y from vm772_58dd091a279b5392.messagequeuestatus group by errkwkwormessage",
            "错误信息如果发送失败记录失败原因",
        )
    if obj.get("optype") == "messagequeuestatus.errkwkwormessage_bar":
        res = get_bar(
            "select errkwkwormessage x,count(*) y from vm772_58dd091a279b5392.messagequeuestatus group by errkwkwormessage",
            "错误信息如果发送失败记录失败原因",
        )
    if obj.get("optype") == "messagequeuestatus.errkwkwormessage_bar_v1":
        res = get_bar_v1(
            "select errkwkwormessage x,count(*) y from vm772_58dd091a279b5392.messagequeuestatus group by errkwkwormessage",
            "错误信息如果发送失败记录失败原因",
        )
    # messagerekwkwtryreckwkword(消息重试记录表)->messageid(消息ID关联消息的ID)

    if obj.get("optype") == "messagerekwkwtryreckwkword.messageid_pie":
        res = get_pie(
            "select messageid x,count(*) y from vm772_58dd091a279b5392.messagerekwkwtryreckwkword group by messageid order by x desc",
            "消息ID关联消息的ID",
        )
    if obj.get("optype") == "messagerekwkwtryreckwkword.messageid_pie_v1":
        res = get_pie_v1(
            "select messageid x,count(*) y from vm772_58dd091a279b5392.messagerekwkwtryreckwkword group by messageid",
            "消息ID关联消息的ID",
        )
    if obj.get("optype") == "messagerekwkwtryreckwkword.messageid_pie_v2":
        res = get_pie_v2(
            "select messageid x,count(*) y from vm772_58dd091a279b5392.messagerekwkwtryreckwkword group by messageid",
            "消息ID关联消息的ID",
        )
    if obj.get("optype") == "messagerekwkwtryreckwkword.messageid_line":
        res = get_line(
            "select messageid x,count(*) y from vm772_58dd091a279b5392.messagerekwkwtryreckwkword group by messageid",
            "消息ID关联消息的ID",
        )
    if obj.get("optype") == "messagerekwkwtryreckwkword.messageid_bar":
        res = get_bar(
            "select messageid x,count(*) y from vm772_58dd091a279b5392.messagerekwkwtryreckwkword group by messageid",
            "消息ID关联消息的ID",
        )
    if obj.get("optype") == "messagerekwkwtryreckwkword.messageid_bar_v1":
        res = get_bar_v1(
            "select messageid x,count(*) y from vm772_58dd091a279b5392.messagerekwkwtryreckwkword group by messageid",
            "消息ID关联消息的ID",
        )
    # messagerekwkwtryreckwkword(消息重试记录表)->platkwkwfkwkworm(平台名称)

    if obj.get("optype") == "messagerekwkwtryreckwkword.platkwkwfkwkworm_pie":
        res = get_pie(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.messagerekwkwtryreckwkword group by platkwkwfkwkworm order by x desc",
            "平台名称",
        )
    if obj.get("optype") == "messagerekwkwtryreckwkword.platkwkwfkwkworm_pie_v1":
        res = get_pie_v1(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.messagerekwkwtryreckwkword group by platkwkwfkwkworm",
            "平台名称",
        )
    if obj.get("optype") == "messagerekwkwtryreckwkword.platkwkwfkwkworm_pie_v2":
        res = get_pie_v2(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.messagerekwkwtryreckwkword group by platkwkwfkwkworm",
            "平台名称",
        )
    if obj.get("optype") == "messagerekwkwtryreckwkword.platkwkwfkwkworm_line":
        res = get_line(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.messagerekwkwtryreckwkword group by platkwkwfkwkworm",
            "平台名称",
        )
    if obj.get("optype") == "messagerekwkwtryreckwkword.platkwkwfkwkworm_bar":
        res = get_bar(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.messagerekwkwtryreckwkword group by platkwkwfkwkworm",
            "平台名称",
        )
    if obj.get("optype") == "messagerekwkwtryreckwkword.platkwkwfkwkworm_bar_v1":
        res = get_bar_v1(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.messagerekwkwtryreckwkword group by platkwkwfkwkworm",
            "平台名称",
        )
    # messagerekwkwtryreckwkword(消息重试记录表)->targetuserid(目标用户ID)

    if obj.get("optype") == "messagerekwkwtryreckwkword.targetuserid_pie":
        res = get_pie(
            "select targetuserid x,count(*) y from vm772_58dd091a279b5392.messagerekwkwtryreckwkword group by targetuserid order by x desc",
            "目标用户ID",
        )
    if obj.get("optype") == "messagerekwkwtryreckwkword.targetuserid_pie_v1":
        res = get_pie_v1(
            "select targetuserid x,count(*) y from vm772_58dd091a279b5392.messagerekwkwtryreckwkword group by targetuserid",
            "目标用户ID",
        )
    if obj.get("optype") == "messagerekwkwtryreckwkword.targetuserid_pie_v2":
        res = get_pie_v2(
            "select targetuserid x,count(*) y from vm772_58dd091a279b5392.messagerekwkwtryreckwkword group by targetuserid",
            "目标用户ID",
        )
    if obj.get("optype") == "messagerekwkwtryreckwkword.targetuserid_line":
        res = get_line(
            "select targetuserid x,count(*) y from vm772_58dd091a279b5392.messagerekwkwtryreckwkword group by targetuserid",
            "目标用户ID",
        )
    if obj.get("optype") == "messagerekwkwtryreckwkword.targetuserid_bar":
        res = get_bar(
            "select targetuserid x,count(*) y from vm772_58dd091a279b5392.messagerekwkwtryreckwkword group by targetuserid",
            "目标用户ID",
        )
    if obj.get("optype") == "messagerekwkwtryreckwkword.targetuserid_bar_v1":
        res = get_bar_v1(
            "select targetuserid x,count(*) y from vm772_58dd091a279b5392.messagerekwkwtryreckwkword group by targetuserid",
            "目标用户ID",
        )
    if obj.get("optype") == "messagerekwkwtryreckwkword.content_wordcloud":
        textlist = get_data(
            "SELECT content result FROM vm772_58dd091a279b5392.messagerekwkwtryreckwkword;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # messagerekwkwtryreckwkword(消息重试记录表)->rekwkwtrycount(重试次数)

    if obj.get("optype") == "messagerekwkwtryreckwkword.rekwkwtrycount_pie":
        res = get_pie(
            "select rekwkwtrycount x,count(*) y from vm772_58dd091a279b5392.messagerekwkwtryreckwkword group by rekwkwtrycount order by x desc",
            "重试次数",
        )
    if obj.get("optype") == "messagerekwkwtryreckwkword.rekwkwtrycount_pie_v1":
        res = get_pie_v1(
            "select rekwkwtrycount x,count(*) y from vm772_58dd091a279b5392.messagerekwkwtryreckwkword group by rekwkwtrycount",
            "重试次数",
        )
    if obj.get("optype") == "messagerekwkwtryreckwkword.rekwkwtrycount_pie_v2":
        res = get_pie_v2(
            "select rekwkwtrycount x,count(*) y from vm772_58dd091a279b5392.messagerekwkwtryreckwkword group by rekwkwtrycount",
            "重试次数",
        )
    if obj.get("optype") == "messagerekwkwtryreckwkword.rekwkwtrycount_line":
        res = get_line(
            "select rekwkwtrycount x,count(*) y from vm772_58dd091a279b5392.messagerekwkwtryreckwkword group by rekwkwtrycount",
            "重试次数",
        )
    if obj.get("optype") == "messagerekwkwtryreckwkword.rekwkwtrycount_bar":
        res = get_bar(
            "select rekwkwtrycount x,count(*) y from vm772_58dd091a279b5392.messagerekwkwtryreckwkword group by rekwkwtrycount",
            "重试次数",
        )
    if obj.get("optype") == "messagerekwkwtryreckwkword.rekwkwtrycount_bar_v1":
        res = get_bar_v1(
            "select rekwkwtrycount x,count(*) y from vm772_58dd091a279b5392.messagerekwkwtryreckwkword group by rekwkwtrycount",
            "重试次数",
        )
    if obj.get("optype") == "messagerekwkwtryreckwkword.lkwkwastrekwkwtrytime_line":
        res = get_line(
            "select lkwkwastrekwkwtrytime x,count(*) y from vm772_58dd091a279b5392.messagerekwkwtryreckwkword group by lkwkwastrekwkwtrytime order by x",
            "上次重试时间",
        )
    if obj.get("optype") == "messagerekwkwtryreckwkword.nextrekwkwtrytime_line":
        res = get_line(
            "select nextrekwkwtrytime x,count(*) y from vm772_58dd091a279b5392.messagerekwkwtryreckwkword group by nextrekwkwtrytime order by x",
            "下一次重试时间",
        )
    # messagerekwkwtryreckwkword(消息重试记录表)->status(消息状态如待发送、发送中、发送成功、发送失败)

    if obj.get("optype") == "messagerekwkwtryreckwkword.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagerekwkwtryreckwkword group by status order by x desc",
            "消息状态如待发送、发送中、发送成功、发送失败",
        )
    if obj.get("optype") == "messagerekwkwtryreckwkword.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagerekwkwtryreckwkword group by status",
            "消息状态如待发送、发送中、发送成功、发送失败",
        )
    if obj.get("optype") == "messagerekwkwtryreckwkword.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagerekwkwtryreckwkword group by status",
            "消息状态如待发送、发送中、发送成功、发送失败",
        )
    if obj.get("optype") == "messagerekwkwtryreckwkword.status_line":
        res = get_line(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagerekwkwtryreckwkword group by status",
            "消息状态如待发送、发送中、发送成功、发送失败",
        )
    if obj.get("optype") == "messagerekwkwtryreckwkword.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagerekwkwtryreckwkword group by status",
            "消息状态如待发送、发送中、发送成功、发送失败",
        )
    if obj.get("optype") == "messagerekwkwtryreckwkword.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagerekwkwtryreckwkword group by status",
            "消息状态如待发送、发送中、发送成功、发送失败",
        )
    # messagerekwkwtryreckwkword(消息重试记录表)->errkwkworkwkwinfo(错误信息如果发送失败记录错误信息)

    if obj.get("optype") == "messagerekwkwtryreckwkword.errkwkworkwkwinfo_pie":
        res = get_pie(
            "select errkwkworkwkwinfo x,count(*) y from vm772_58dd091a279b5392.messagerekwkwtryreckwkword group by errkwkworkwkwinfo order by x desc",
            "错误信息如果发送失败记录错误信息",
        )
    if obj.get("optype") == "messagerekwkwtryreckwkword.errkwkworkwkwinfo_pie_v1":
        res = get_pie_v1(
            "select errkwkworkwkwinfo x,count(*) y from vm772_58dd091a279b5392.messagerekwkwtryreckwkword group by errkwkworkwkwinfo",
            "错误信息如果发送失败记录错误信息",
        )
    if obj.get("optype") == "messagerekwkwtryreckwkword.errkwkworkwkwinfo_pie_v2":
        res = get_pie_v2(
            "select errkwkworkwkwinfo x,count(*) y from vm772_58dd091a279b5392.messagerekwkwtryreckwkword group by errkwkworkwkwinfo",
            "错误信息如果发送失败记录错误信息",
        )
    if obj.get("optype") == "messagerekwkwtryreckwkword.errkwkworkwkwinfo_line":
        res = get_line(
            "select errkwkworkwkwinfo x,count(*) y from vm772_58dd091a279b5392.messagerekwkwtryreckwkword group by errkwkworkwkwinfo",
            "错误信息如果发送失败记录错误信息",
        )
    if obj.get("optype") == "messagerekwkwtryreckwkword.errkwkworkwkwinfo_bar":
        res = get_bar(
            "select errkwkworkwkwinfo x,count(*) y from vm772_58dd091a279b5392.messagerekwkwtryreckwkword group by errkwkworkwkwinfo",
            "错误信息如果发送失败记录错误信息",
        )
    if obj.get("optype") == "messagerekwkwtryreckwkword.errkwkworkwkwinfo_bar_v1":
        res = get_bar_v1(
            "select errkwkworkwkwinfo x,count(*) y from vm772_58dd091a279b5392.messagerekwkwtryreckwkword group by errkwkworkwkwinfo",
            "错误信息如果发送失败记录错误信息",
        )
    # accountblacklkwkwist(账号黑名单表)->accountid(账号ID)

    if obj.get("optype") == "accountblacklkwkwist.accountid_pie":
        res = get_pie(
            "select accountid x,count(*) y from vm772_58dd091a279b5392.accountblacklkwkwist group by accountid order by x desc",
            "账号ID",
        )
    if obj.get("optype") == "accountblacklkwkwist.accountid_pie_v1":
        res = get_pie_v1(
            "select accountid x,count(*) y from vm772_58dd091a279b5392.accountblacklkwkwist group by accountid",
            "账号ID",
        )
    if obj.get("optype") == "accountblacklkwkwist.accountid_pie_v2":
        res = get_pie_v2(
            "select accountid x,count(*) y from vm772_58dd091a279b5392.accountblacklkwkwist group by accountid",
            "账号ID",
        )
    if obj.get("optype") == "accountblacklkwkwist.accountid_line":
        res = get_line(
            "select accountid x,count(*) y from vm772_58dd091a279b5392.accountblacklkwkwist group by accountid",
            "账号ID",
        )
    if obj.get("optype") == "accountblacklkwkwist.accountid_bar":
        res = get_bar(
            "select accountid x,count(*) y from vm772_58dd091a279b5392.accountblacklkwkwist group by accountid",
            "账号ID",
        )
    if obj.get("optype") == "accountblacklkwkwist.accountid_bar_v1":
        res = get_bar_v1(
            "select accountid x,count(*) y from vm772_58dd091a279b5392.accountblacklkwkwist group by accountid",
            "账号ID",
        )
    # accountblacklkwkwist(账号黑名单表)->blacklkwkwisttype(黑名单类型)

    if obj.get("optype") == "accountblacklkwkwist.blacklkwkwisttype_pie":
        res = get_pie(
            "select blacklkwkwisttype x,count(*) y from vm772_58dd091a279b5392.accountblacklkwkwist group by blacklkwkwisttype order by x desc",
            "黑名单类型",
        )
    if obj.get("optype") == "accountblacklkwkwist.blacklkwkwisttype_pie_v1":
        res = get_pie_v1(
            "select blacklkwkwisttype x,count(*) y from vm772_58dd091a279b5392.accountblacklkwkwist group by blacklkwkwisttype",
            "黑名单类型",
        )
    if obj.get("optype") == "accountblacklkwkwist.blacklkwkwisttype_pie_v2":
        res = get_pie_v2(
            "select blacklkwkwisttype x,count(*) y from vm772_58dd091a279b5392.accountblacklkwkwist group by blacklkwkwisttype",
            "黑名单类型",
        )
    if obj.get("optype") == "accountblacklkwkwist.blacklkwkwisttype_line":
        res = get_line(
            "select blacklkwkwisttype x,count(*) y from vm772_58dd091a279b5392.accountblacklkwkwist group by blacklkwkwisttype",
            "黑名单类型",
        )
    if obj.get("optype") == "accountblacklkwkwist.blacklkwkwisttype_bar":
        res = get_bar(
            "select blacklkwkwisttype x,count(*) y from vm772_58dd091a279b5392.accountblacklkwkwist group by blacklkwkwisttype",
            "黑名单类型",
        )
    if obj.get("optype") == "accountblacklkwkwist.blacklkwkwisttype_bar_v1":
        res = get_bar_v1(
            "select blacklkwkwisttype x,count(*) y from vm772_58dd091a279b5392.accountblacklkwkwist group by blacklkwkwisttype",
            "黑名单类型",
        )
    # accountblacklkwkwist(账号黑名单表)->rekwkwason(加入黑名单原因)

    if obj.get("optype") == "accountblacklkwkwist.rekwkwason_pie":
        res = get_pie(
            "select rekwkwason x,count(*) y from vm772_58dd091a279b5392.accountblacklkwkwist group by rekwkwason order by x desc",
            "加入黑名单原因",
        )
    if obj.get("optype") == "accountblacklkwkwist.rekwkwason_pie_v1":
        res = get_pie_v1(
            "select rekwkwason x,count(*) y from vm772_58dd091a279b5392.accountblacklkwkwist group by rekwkwason",
            "加入黑名单原因",
        )
    if obj.get("optype") == "accountblacklkwkwist.rekwkwason_pie_v2":
        res = get_pie_v2(
            "select rekwkwason x,count(*) y from vm772_58dd091a279b5392.accountblacklkwkwist group by rekwkwason",
            "加入黑名单原因",
        )
    if obj.get("optype") == "accountblacklkwkwist.rekwkwason_line":
        res = get_line(
            "select rekwkwason x,count(*) y from vm772_58dd091a279b5392.accountblacklkwkwist group by rekwkwason",
            "加入黑名单原因",
        )
    if obj.get("optype") == "accountblacklkwkwist.rekwkwason_bar":
        res = get_bar(
            "select rekwkwason x,count(*) y from vm772_58dd091a279b5392.accountblacklkwkwist group by rekwkwason",
            "加入黑名单原因",
        )
    if obj.get("optype") == "accountblacklkwkwist.rekwkwason_bar_v1":
        res = get_bar_v1(
            "select rekwkwason x,count(*) y from vm772_58dd091a279b5392.accountblacklkwkwist group by rekwkwason",
            "加入黑名单原因",
        )
    if obj.get("optype") == "accountblacklkwkwist.createtime_line":
        res = get_line(
            "select createtime x,count(*) y from vm772_58dd091a279b5392.accountblacklkwkwist group by createtime order by x",
            "创建时间",
        )
    if obj.get("optype") == "accountblacklkwkwist.updatetime_line":
        res = get_line(
            "select updatetime x,count(*) y from vm772_58dd091a279b5392.accountblacklkwkwist group by updatetime order by x",
            "更新时间",
        )
    # accountblacklkwkwist(账号黑名单表)->kwkwisactive(是否有效用于标记黑名单记录是否仍然有效)

    if obj.get("optype") == "accountblacklkwkwist.kwkwisactive_pie":
        res = get_pie(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.accountblacklkwkwist group by kwkwisactive order by x desc",
            "是否有效用于标记黑名单记录是否仍然有效",
        )
    if obj.get("optype") == "accountblacklkwkwist.kwkwisactive_pie_v1":
        res = get_pie_v1(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.accountblacklkwkwist group by kwkwisactive",
            "是否有效用于标记黑名单记录是否仍然有效",
        )
    if obj.get("optype") == "accountblacklkwkwist.kwkwisactive_pie_v2":
        res = get_pie_v2(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.accountblacklkwkwist group by kwkwisactive",
            "是否有效用于标记黑名单记录是否仍然有效",
        )
    if obj.get("optype") == "accountblacklkwkwist.kwkwisactive_line":
        res = get_line(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.accountblacklkwkwist group by kwkwisactive",
            "是否有效用于标记黑名单记录是否仍然有效",
        )
    if obj.get("optype") == "accountblacklkwkwist.kwkwisactive_bar":
        res = get_bar(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.accountblacklkwkwist group by kwkwisactive",
            "是否有效用于标记黑名单记录是否仍然有效",
        )
    if obj.get("optype") == "accountblacklkwkwist.kwkwisactive_bar_v1":
        res = get_bar_v1(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.accountblacklkwkwist group by kwkwisactive",
            "是否有效用于标记黑名单记录是否仍然有效",
        )
    # accountblacklkwkwist(账号黑名单表)->creatkwkworid(创建者ID)

    if obj.get("optype") == "accountblacklkwkwist.creatkwkworid_pie":
        res = get_pie(
            "select creatkwkworid x,count(*) y from vm772_58dd091a279b5392.accountblacklkwkwist group by creatkwkworid order by x desc",
            "创建者ID",
        )
    if obj.get("optype") == "accountblacklkwkwist.creatkwkworid_pie_v1":
        res = get_pie_v1(
            "select creatkwkworid x,count(*) y from vm772_58dd091a279b5392.accountblacklkwkwist group by creatkwkworid",
            "创建者ID",
        )
    if obj.get("optype") == "accountblacklkwkwist.creatkwkworid_pie_v2":
        res = get_pie_v2(
            "select creatkwkworid x,count(*) y from vm772_58dd091a279b5392.accountblacklkwkwist group by creatkwkworid",
            "创建者ID",
        )
    if obj.get("optype") == "accountblacklkwkwist.creatkwkworid_line":
        res = get_line(
            "select creatkwkworid x,count(*) y from vm772_58dd091a279b5392.accountblacklkwkwist group by creatkwkworid",
            "创建者ID",
        )
    if obj.get("optype") == "accountblacklkwkwist.creatkwkworid_bar":
        res = get_bar(
            "select creatkwkworid x,count(*) y from vm772_58dd091a279b5392.accountblacklkwkwist group by creatkwkworid",
            "创建者ID",
        )
    if obj.get("optype") == "accountblacklkwkwist.creatkwkworid_bar_v1":
        res = get_bar_v1(
            "select creatkwkworid x,count(*) y from vm772_58dd091a279b5392.accountblacklkwkwist group by creatkwkworid",
            "创建者ID",
        )
    # accountblacklkwkwist(账号黑名单表)->relatedaccountid(相关账号ID如果黑名单与特定操作或另一账号相关)

    if obj.get("optype") == "accountblacklkwkwist.relatedaccountid_pie":
        res = get_pie(
            "select relatedaccountid x,count(*) y from vm772_58dd091a279b5392.accountblacklkwkwist group by relatedaccountid order by x desc",
            "相关账号ID如果黑名单与特定操作或另一账号相关",
        )
    if obj.get("optype") == "accountblacklkwkwist.relatedaccountid_pie_v1":
        res = get_pie_v1(
            "select relatedaccountid x,count(*) y from vm772_58dd091a279b5392.accountblacklkwkwist group by relatedaccountid",
            "相关账号ID如果黑名单与特定操作或另一账号相关",
        )
    if obj.get("optype") == "accountblacklkwkwist.relatedaccountid_pie_v2":
        res = get_pie_v2(
            "select relatedaccountid x,count(*) y from vm772_58dd091a279b5392.accountblacklkwkwist group by relatedaccountid",
            "相关账号ID如果黑名单与特定操作或另一账号相关",
        )
    if obj.get("optype") == "accountblacklkwkwist.relatedaccountid_line":
        res = get_line(
            "select relatedaccountid x,count(*) y from vm772_58dd091a279b5392.accountblacklkwkwist group by relatedaccountid",
            "相关账号ID如果黑名单与特定操作或另一账号相关",
        )
    if obj.get("optype") == "accountblacklkwkwist.relatedaccountid_bar":
        res = get_bar(
            "select relatedaccountid x,count(*) y from vm772_58dd091a279b5392.accountblacklkwkwist group by relatedaccountid",
            "相关账号ID如果黑名单与特定操作或另一账号相关",
        )
    if obj.get("optype") == "accountblacklkwkwist.relatedaccountid_bar_v1":
        res = get_bar_v1(
            "select relatedaccountid x,count(*) y from vm772_58dd091a279b5392.accountblacklkwkwist group by relatedaccountid",
            "相关账号ID如果黑名单与特定操作或另一账号相关",
        )
    # userfeedback(用户反馈表)->userid(用户ID关联用户)

    if obj.get("optype") == "userfeedback.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm772_58dd091a279b5392.userfeedback group by userid order by x desc",
            "用户ID关联用户",
        )
    if obj.get("optype") == "userfeedback.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm772_58dd091a279b5392.userfeedback group by userid",
            "用户ID关联用户",
        )
    if obj.get("optype") == "userfeedback.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm772_58dd091a279b5392.userfeedback group by userid",
            "用户ID关联用户",
        )
    if obj.get("optype") == "userfeedback.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm772_58dd091a279b5392.userfeedback group by userid",
            "用户ID关联用户",
        )
    if obj.get("optype") == "userfeedback.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm772_58dd091a279b5392.userfeedback group by userid",
            "用户ID关联用户",
        )
    if obj.get("optype") == "userfeedback.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm772_58dd091a279b5392.userfeedback group by userid",
            "用户ID关联用户",
        )
    if obj.get("optype") == "userfeedback.feedbackcontent_wordcloud":
        textlist = get_data(
            "SELECT feedbackcontent result FROM vm772_58dd091a279b5392.userfeedback;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "userfeedback.feedbacktype_wordcloud":
        textlist = get_data(
            "SELECT feedbacktype result FROM vm772_58dd091a279b5392.userfeedback;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "userfeedback.createdat_line":
        res = get_line(
            "select createdat x,count(*) y from vm772_58dd091a279b5392.userfeedback group by createdat order by x",
            "反馈创建时间",
        )
    # userfeedback(用户反馈表)->status(反馈状态如待处理、已处理、已忽略等)

    if obj.get("optype") == "userfeedback.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm772_58dd091a279b5392.userfeedback group by status order by x desc",
            "反馈状态如待处理、已处理、已忽略等",
        )
    if obj.get("optype") == "userfeedback.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm772_58dd091a279b5392.userfeedback group by status",
            "反馈状态如待处理、已处理、已忽略等",
        )
    if obj.get("optype") == "userfeedback.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm772_58dd091a279b5392.userfeedback group by status",
            "反馈状态如待处理、已处理、已忽略等",
        )
    if obj.get("optype") == "userfeedback.status_line":
        res = get_line(
            "select status x,count(*) y from vm772_58dd091a279b5392.userfeedback group by status",
            "反馈状态如待处理、已处理、已忽略等",
        )
    if obj.get("optype") == "userfeedback.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm772_58dd091a279b5392.userfeedback group by status",
            "反馈状态如待处理、已处理、已忽略等",
        )
    if obj.get("optype") == "userfeedback.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm772_58dd091a279b5392.userfeedback group by status",
            "反馈状态如待处理、已处理、已忽略等",
        )
    if obj.get("optype") == "userfeedback.responsecontent_wordcloud":
        textlist = get_data(
            "SELECT responsecontent result FROM vm772_58dd091a279b5392.userfeedback;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "userfeedback.responseat_line":
        res = get_line(
            "select responseat x,count(*) y from vm772_58dd091a279b5392.userfeedback group by responseat order by x",
            "回复时间",
        )
    # userfeedback(用户反馈表)->kwkwisresolved(是否已解决是否)

    if obj.get("optype") == "userfeedback.kwkwisresolved_pie":
        res = get_pie(
            "select kwkwisresolved x,count(*) y from vm772_58dd091a279b5392.userfeedback group by kwkwisresolved order by x desc",
            "是否已解决是否",
        )
    if obj.get("optype") == "userfeedback.kwkwisresolved_pie_v1":
        res = get_pie_v1(
            "select kwkwisresolved x,count(*) y from vm772_58dd091a279b5392.userfeedback group by kwkwisresolved",
            "是否已解决是否",
        )
    if obj.get("optype") == "userfeedback.kwkwisresolved_pie_v2":
        res = get_pie_v2(
            "select kwkwisresolved x,count(*) y from vm772_58dd091a279b5392.userfeedback group by kwkwisresolved",
            "是否已解决是否",
        )
    if obj.get("optype") == "userfeedback.kwkwisresolved_line":
        res = get_line(
            "select kwkwisresolved x,count(*) y from vm772_58dd091a279b5392.userfeedback group by kwkwisresolved",
            "是否已解决是否",
        )
    if obj.get("optype") == "userfeedback.kwkwisresolved_bar":
        res = get_bar(
            "select kwkwisresolved x,count(*) y from vm772_58dd091a279b5392.userfeedback group by kwkwisresolved",
            "是否已解决是否",
        )
    if obj.get("optype") == "userfeedback.kwkwisresolved_bar_v1":
        res = get_bar_v1(
            "select kwkwisresolved x,count(*) y from vm772_58dd091a279b5392.userfeedback group by kwkwisresolved",
            "是否已解决是否",
        )
    # accountsecuritylog(账号安全日志表)->accountid(账号ID)

    if obj.get("optype") == "accountsecuritylog.accountid_pie":
        res = get_pie(
            "select accountid x,count(*) y from vm772_58dd091a279b5392.accountsecuritylog group by accountid order by x desc",
            "账号ID",
        )
    if obj.get("optype") == "accountsecuritylog.accountid_pie_v1":
        res = get_pie_v1(
            "select accountid x,count(*) y from vm772_58dd091a279b5392.accountsecuritylog group by accountid",
            "账号ID",
        )
    if obj.get("optype") == "accountsecuritylog.accountid_pie_v2":
        res = get_pie_v2(
            "select accountid x,count(*) y from vm772_58dd091a279b5392.accountsecuritylog group by accountid",
            "账号ID",
        )
    if obj.get("optype") == "accountsecuritylog.accountid_line":
        res = get_line(
            "select accountid x,count(*) y from vm772_58dd091a279b5392.accountsecuritylog group by accountid",
            "账号ID",
        )
    if obj.get("optype") == "accountsecuritylog.accountid_bar":
        res = get_bar(
            "select accountid x,count(*) y from vm772_58dd091a279b5392.accountsecuritylog group by accountid",
            "账号ID",
        )
    if obj.get("optype") == "accountsecuritylog.accountid_bar_v1":
        res = get_bar_v1(
            "select accountid x,count(*) y from vm772_58dd091a279b5392.accountsecuritylog group by accountid",
            "账号ID",
        )
    # accountsecuritylog(账号安全日志表)->logtype(日志类型)

    if obj.get("optype") == "accountsecuritylog.logtype_pie":
        res = get_pie(
            "select logtype x,count(*) y from vm772_58dd091a279b5392.accountsecuritylog group by logtype order by x desc",
            "日志类型",
        )
    if obj.get("optype") == "accountsecuritylog.logtype_pie_v1":
        res = get_pie_v1(
            "select logtype x,count(*) y from vm772_58dd091a279b5392.accountsecuritylog group by logtype",
            "日志类型",
        )
    if obj.get("optype") == "accountsecuritylog.logtype_pie_v2":
        res = get_pie_v2(
            "select logtype x,count(*) y from vm772_58dd091a279b5392.accountsecuritylog group by logtype",
            "日志类型",
        )
    if obj.get("optype") == "accountsecuritylog.logtype_line":
        res = get_line(
            "select logtype x,count(*) y from vm772_58dd091a279b5392.accountsecuritylog group by logtype",
            "日志类型",
        )
    if obj.get("optype") == "accountsecuritylog.logtype_bar":
        res = get_bar(
            "select logtype x,count(*) y from vm772_58dd091a279b5392.accountsecuritylog group by logtype",
            "日志类型",
        )
    if obj.get("optype") == "accountsecuritylog.logtype_bar_v1":
        res = get_bar_v1(
            "select logtype x,count(*) y from vm772_58dd091a279b5392.accountsecuritylog group by logtype",
            "日志类型",
        )
    if obj.get("optype") == "accountsecuritylog.action_wordcloud":
        textlist = get_data(
            "SELECT action result FROM vm772_58dd091a279b5392.accountsecuritylog;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "accountsecuritylog.ipaddressip_wordcloud":
        textlist = get_data(
            "SELECT ipaddressip result FROM vm772_58dd091a279b5392.accountsecuritylog;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "accountsecuritylog.timestamp_line":
        res = get_line(
            "select timestamp x,count(*) y from vm772_58dd091a279b5392.accountsecuritylog group by timestamp order by x",
            "时间戳",
        )
    # accountsecuritylog(账号安全日志表)->result(结果状态)

    if obj.get("optype") == "accountsecuritylog.result_pie":
        res = get_pie(
            "select result x,count(*) y from vm772_58dd091a279b5392.accountsecuritylog group by result order by x desc",
            "结果状态",
        )
    if obj.get("optype") == "accountsecuritylog.result_pie_v1":
        res = get_pie_v1(
            "select result x,count(*) y from vm772_58dd091a279b5392.accountsecuritylog group by result",
            "结果状态",
        )
    if obj.get("optype") == "accountsecuritylog.result_pie_v2":
        res = get_pie_v2(
            "select result x,count(*) y from vm772_58dd091a279b5392.accountsecuritylog group by result",
            "结果状态",
        )
    if obj.get("optype") == "accountsecuritylog.result_line":
        res = get_line(
            "select result x,count(*) y from vm772_58dd091a279b5392.accountsecuritylog group by result",
            "结果状态",
        )
    if obj.get("optype") == "accountsecuritylog.result_bar":
        res = get_bar(
            "select result x,count(*) y from vm772_58dd091a279b5392.accountsecuritylog group by result",
            "结果状态",
        )
    if obj.get("optype") == "accountsecuritylog.result_bar_v1":
        res = get_bar_v1(
            "select result x,count(*) y from vm772_58dd091a279b5392.accountsecuritylog group by result",
            "结果状态",
        )
    if obj.get("optype") == "accountsecuritylog.description_wordcloud":
        textlist = get_data(
            "SELECT description result FROM vm772_58dd091a279b5392.accountsecuritylog;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # accountsecuritylog(账号安全日志表)->relatedaccountid(关联账号ID)

    if obj.get("optype") == "accountsecuritylog.relatedaccountid_pie":
        res = get_pie(
            "select relatedaccountid x,count(*) y from vm772_58dd091a279b5392.accountsecuritylog group by relatedaccountid order by x desc",
            "关联账号ID",
        )
    if obj.get("optype") == "accountsecuritylog.relatedaccountid_pie_v1":
        res = get_pie_v1(
            "select relatedaccountid x,count(*) y from vm772_58dd091a279b5392.accountsecuritylog group by relatedaccountid",
            "关联账号ID",
        )
    if obj.get("optype") == "accountsecuritylog.relatedaccountid_pie_v2":
        res = get_pie_v2(
            "select relatedaccountid x,count(*) y from vm772_58dd091a279b5392.accountsecuritylog group by relatedaccountid",
            "关联账号ID",
        )
    if obj.get("optype") == "accountsecuritylog.relatedaccountid_line":
        res = get_line(
            "select relatedaccountid x,count(*) y from vm772_58dd091a279b5392.accountsecuritylog group by relatedaccountid",
            "关联账号ID",
        )
    if obj.get("optype") == "accountsecuritylog.relatedaccountid_bar":
        res = get_bar(
            "select relatedaccountid x,count(*) y from vm772_58dd091a279b5392.accountsecuritylog group by relatedaccountid",
            "关联账号ID",
        )
    if obj.get("optype") == "accountsecuritylog.relatedaccountid_bar_v1":
        res = get_bar_v1(
            "select relatedaccountid x,count(*) y from vm772_58dd091a279b5392.accountsecuritylog group by relatedaccountid",
            "关联账号ID",
        )
    # messagetemplateedithkwkwistkwkwory(消息模板编辑历史表)->templateid(消息模板ID关联字段指向消息模板的ID)

    if obj.get("optype") == "messagetemplateedithkwkwistkwkwory.templateid_pie":
        res = get_pie(
            "select templateid x,count(*) y from vm772_58dd091a279b5392.messagetemplateedithkwkwistkwkwory group by templateid order by x desc",
            "消息模板ID关联字段指向消息模板的ID",
        )
    if obj.get("optype") == "messagetemplateedithkwkwistkwkwory.templateid_pie_v1":
        res = get_pie_v1(
            "select templateid x,count(*) y from vm772_58dd091a279b5392.messagetemplateedithkwkwistkwkwory group by templateid",
            "消息模板ID关联字段指向消息模板的ID",
        )
    if obj.get("optype") == "messagetemplateedithkwkwistkwkwory.templateid_pie_v2":
        res = get_pie_v2(
            "select templateid x,count(*) y from vm772_58dd091a279b5392.messagetemplateedithkwkwistkwkwory group by templateid",
            "消息模板ID关联字段指向消息模板的ID",
        )
    if obj.get("optype") == "messagetemplateedithkwkwistkwkwory.templateid_line":
        res = get_line(
            "select templateid x,count(*) y from vm772_58dd091a279b5392.messagetemplateedithkwkwistkwkwory group by templateid",
            "消息模板ID关联字段指向消息模板的ID",
        )
    if obj.get("optype") == "messagetemplateedithkwkwistkwkwory.templateid_bar":
        res = get_bar(
            "select templateid x,count(*) y from vm772_58dd091a279b5392.messagetemplateedithkwkwistkwkwory group by templateid",
            "消息模板ID关联字段指向消息模板的ID",
        )
    if obj.get("optype") == "messagetemplateedithkwkwistkwkwory.templateid_bar_v1":
        res = get_bar_v1(
            "select templateid x,count(*) y from vm772_58dd091a279b5392.messagetemplateedithkwkwistkwkwory group by templateid",
            "消息模板ID关联字段指向消息模板的ID",
        )
    # messagetemplateedithkwkwistkwkwory(消息模板编辑历史表)->editkwkworid(编辑者ID关联字段指向用户的ID)

    if obj.get("optype") == "messagetemplateedithkwkwistkwkwory.editkwkworid_pie":
        res = get_pie(
            "select editkwkworid x,count(*) y from vm772_58dd091a279b5392.messagetemplateedithkwkwistkwkwory group by editkwkworid order by x desc",
            "编辑者ID关联字段指向用户的ID",
        )
    if obj.get("optype") == "messagetemplateedithkwkwistkwkwory.editkwkworid_pie_v1":
        res = get_pie_v1(
            "select editkwkworid x,count(*) y from vm772_58dd091a279b5392.messagetemplateedithkwkwistkwkwory group by editkwkworid",
            "编辑者ID关联字段指向用户的ID",
        )
    if obj.get("optype") == "messagetemplateedithkwkwistkwkwory.editkwkworid_pie_v2":
        res = get_pie_v2(
            "select editkwkworid x,count(*) y from vm772_58dd091a279b5392.messagetemplateedithkwkwistkwkwory group by editkwkworid",
            "编辑者ID关联字段指向用户的ID",
        )
    if obj.get("optype") == "messagetemplateedithkwkwistkwkwory.editkwkworid_line":
        res = get_line(
            "select editkwkworid x,count(*) y from vm772_58dd091a279b5392.messagetemplateedithkwkwistkwkwory group by editkwkworid",
            "编辑者ID关联字段指向用户的ID",
        )
    if obj.get("optype") == "messagetemplateedithkwkwistkwkwory.editkwkworid_bar":
        res = get_bar(
            "select editkwkworid x,count(*) y from vm772_58dd091a279b5392.messagetemplateedithkwkwistkwkwory group by editkwkworid",
            "编辑者ID关联字段指向用户的ID",
        )
    if obj.get("optype") == "messagetemplateedithkwkwistkwkwory.editkwkworid_bar_v1":
        res = get_bar_v1(
            "select editkwkworid x,count(*) y from vm772_58dd091a279b5392.messagetemplateedithkwkwistkwkwory group by editkwkworid",
            "编辑者ID关联字段指向用户的ID",
        )
    if obj.get("optype") == "messagetemplateedithkwkwistkwkwory.edittime_line":
        res = get_line(
            "select edittime x,count(*) y from vm772_58dd091a279b5392.messagetemplateedithkwkwistkwkwory group by edittime order by x",
            "编辑时间",
        )
    if obj.get("optype") == "messagetemplateedithkwkwistkwkwory.editcontent_wordcloud":
        textlist = get_data(
            "SELECT editcontent result FROM vm772_58dd091a279b5392.messagetemplateedithkwkwistkwkwory;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # messagetemplateedithkwkwistkwkwory(消息模板编辑历史表)->version(版本号每次编辑递增)

    if obj.get("optype") == "messagetemplateedithkwkwistkwkwory.version_pie":
        res = get_pie(
            "select version x,count(*) y from vm772_58dd091a279b5392.messagetemplateedithkwkwistkwkwory group by version order by x desc",
            "版本号每次编辑递增",
        )
    if obj.get("optype") == "messagetemplateedithkwkwistkwkwory.version_pie_v1":
        res = get_pie_v1(
            "select version x,count(*) y from vm772_58dd091a279b5392.messagetemplateedithkwkwistkwkwory group by version",
            "版本号每次编辑递增",
        )
    if obj.get("optype") == "messagetemplateedithkwkwistkwkwory.version_pie_v2":
        res = get_pie_v2(
            "select version x,count(*) y from vm772_58dd091a279b5392.messagetemplateedithkwkwistkwkwory group by version",
            "版本号每次编辑递增",
        )
    if obj.get("optype") == "messagetemplateedithkwkwistkwkwory.version_line":
        res = get_line(
            "select version x,count(*) y from vm772_58dd091a279b5392.messagetemplateedithkwkwistkwkwory group by version",
            "版本号每次编辑递增",
        )
    if obj.get("optype") == "messagetemplateedithkwkwistkwkwory.version_bar":
        res = get_bar(
            "select version x,count(*) y from vm772_58dd091a279b5392.messagetemplateedithkwkwistkwkwory group by version",
            "版本号每次编辑递增",
        )
    if obj.get("optype") == "messagetemplateedithkwkwistkwkwory.version_bar_v1":
        res = get_bar_v1(
            "select version x,count(*) y from vm772_58dd091a279b5392.messagetemplateedithkwkwistkwkwory group by version",
            "版本号每次编辑递增",
        )
    # messagetemplateedithkwkwistkwkwory(消息模板编辑历史表)->status(状态如有效、已删除等)

    if obj.get("optype") == "messagetemplateedithkwkwistkwkwory.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagetemplateedithkwkwistkwkwory group by status order by x desc",
            "状态如有效、已删除等",
        )
    if obj.get("optype") == "messagetemplateedithkwkwistkwkwory.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagetemplateedithkwkwistkwkwory group by status",
            "状态如有效、已删除等",
        )
    if obj.get("optype") == "messagetemplateedithkwkwistkwkwory.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagetemplateedithkwkwistkwkwory group by status",
            "状态如有效、已删除等",
        )
    if obj.get("optype") == "messagetemplateedithkwkwistkwkwory.status_line":
        res = get_line(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagetemplateedithkwkwistkwkwory group by status",
            "状态如有效、已删除等",
        )
    if obj.get("optype") == "messagetemplateedithkwkwistkwkwory.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagetemplateedithkwkwistkwkwory group by status",
            "状态如有效、已删除等",
        )
    if obj.get("optype") == "messagetemplateedithkwkwistkwkwory.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagetemplateedithkwkwistkwkwory group by status",
            "状态如有效、已删除等",
        )
    # messagetemplateedithkwkwistkwkwory(消息模板编辑历史表)->remark(备注编辑时的额外说明或备注信息)

    if obj.get("optype") == "messagetemplateedithkwkwistkwkwory.remark_pie":
        res = get_pie(
            "select remark x,count(*) y from vm772_58dd091a279b5392.messagetemplateedithkwkwistkwkwory group by remark order by x desc",
            "备注编辑时的额外说明或备注信息",
        )
    if obj.get("optype") == "messagetemplateedithkwkwistkwkwory.remark_pie_v1":
        res = get_pie_v1(
            "select remark x,count(*) y from vm772_58dd091a279b5392.messagetemplateedithkwkwistkwkwory group by remark",
            "备注编辑时的额外说明或备注信息",
        )
    if obj.get("optype") == "messagetemplateedithkwkwistkwkwory.remark_pie_v2":
        res = get_pie_v2(
            "select remark x,count(*) y from vm772_58dd091a279b5392.messagetemplateedithkwkwistkwkwory group by remark",
            "备注编辑时的额外说明或备注信息",
        )
    if obj.get("optype") == "messagetemplateedithkwkwistkwkwory.remark_line":
        res = get_line(
            "select remark x,count(*) y from vm772_58dd091a279b5392.messagetemplateedithkwkwistkwkwory group by remark",
            "备注编辑时的额外说明或备注信息",
        )
    if obj.get("optype") == "messagetemplateedithkwkwistkwkwory.remark_bar":
        res = get_bar(
            "select remark x,count(*) y from vm772_58dd091a279b5392.messagetemplateedithkwkwistkwkwory group by remark",
            "备注编辑时的额外说明或备注信息",
        )
    if obj.get("optype") == "messagetemplateedithkwkwistkwkwory.remark_bar_v1":
        res = get_bar_v1(
            "select remark x,count(*) y from vm772_58dd091a279b5392.messagetemplateedithkwkwistkwkwory group by remark",
            "备注编辑时的额外说明或备注信息",
        )
    # messagetemplateedithkwkwistkwkwory(消息模板编辑历史表)->kwkwislatest(是否为最新版本标识当前记录是否为该模板的最新编辑版本)

    if obj.get("optype") == "messagetemplateedithkwkwistkwkwory.kwkwislatest_pie":
        res = get_pie(
            "select kwkwislatest x,count(*) y from vm772_58dd091a279b5392.messagetemplateedithkwkwistkwkwory group by kwkwislatest order by x desc",
            "是否为最新版本标识当前记录是否为该模板的最新编辑版本",
        )
    if obj.get("optype") == "messagetemplateedithkwkwistkwkwory.kwkwislatest_pie_v1":
        res = get_pie_v1(
            "select kwkwislatest x,count(*) y from vm772_58dd091a279b5392.messagetemplateedithkwkwistkwkwory group by kwkwislatest",
            "是否为最新版本标识当前记录是否为该模板的最新编辑版本",
        )
    if obj.get("optype") == "messagetemplateedithkwkwistkwkwory.kwkwislatest_pie_v2":
        res = get_pie_v2(
            "select kwkwislatest x,count(*) y from vm772_58dd091a279b5392.messagetemplateedithkwkwistkwkwory group by kwkwislatest",
            "是否为最新版本标识当前记录是否为该模板的最新编辑版本",
        )
    if obj.get("optype") == "messagetemplateedithkwkwistkwkwory.kwkwislatest_line":
        res = get_line(
            "select kwkwislatest x,count(*) y from vm772_58dd091a279b5392.messagetemplateedithkwkwistkwkwory group by kwkwislatest",
            "是否为最新版本标识当前记录是否为该模板的最新编辑版本",
        )
    if obj.get("optype") == "messagetemplateedithkwkwistkwkwory.kwkwislatest_bar":
        res = get_bar(
            "select kwkwislatest x,count(*) y from vm772_58dd091a279b5392.messagetemplateedithkwkwistkwkwory group by kwkwislatest",
            "是否为最新版本标识当前记录是否为该模板的最新编辑版本",
        )
    if obj.get("optype") == "messagetemplateedithkwkwistkwkwory.kwkwislatest_bar_v1":
        res = get_bar_v1(
            "select kwkwislatest x,count(*) y from vm772_58dd091a279b5392.messagetemplateedithkwkwistkwkwory group by kwkwislatest",
            "是否为最新版本标识当前记录是否为该模板的最新编辑版本",
        )
    # messagetemplatereviewreckwkword(消息模板审核记录表)->templateid(消息模板ID关联消息模板)

    if obj.get("optype") == "messagetemplatereviewreckwkword.templateid_pie":
        res = get_pie(
            "select templateid x,count(*) y from vm772_58dd091a279b5392.messagetemplatereviewreckwkword group by templateid order by x desc",
            "消息模板ID关联消息模板",
        )
    if obj.get("optype") == "messagetemplatereviewreckwkword.templateid_pie_v1":
        res = get_pie_v1(
            "select templateid x,count(*) y from vm772_58dd091a279b5392.messagetemplatereviewreckwkword group by templateid",
            "消息模板ID关联消息模板",
        )
    if obj.get("optype") == "messagetemplatereviewreckwkword.templateid_pie_v2":
        res = get_pie_v2(
            "select templateid x,count(*) y from vm772_58dd091a279b5392.messagetemplatereviewreckwkword group by templateid",
            "消息模板ID关联消息模板",
        )
    if obj.get("optype") == "messagetemplatereviewreckwkword.templateid_line":
        res = get_line(
            "select templateid x,count(*) y from vm772_58dd091a279b5392.messagetemplatereviewreckwkword group by templateid",
            "消息模板ID关联消息模板",
        )
    if obj.get("optype") == "messagetemplatereviewreckwkword.templateid_bar":
        res = get_bar(
            "select templateid x,count(*) y from vm772_58dd091a279b5392.messagetemplatereviewreckwkword group by templateid",
            "消息模板ID关联消息模板",
        )
    if obj.get("optype") == "messagetemplatereviewreckwkword.templateid_bar_v1":
        res = get_bar_v1(
            "select templateid x,count(*) y from vm772_58dd091a279b5392.messagetemplatereviewreckwkword group by templateid",
            "消息模板ID关联消息模板",
        )
    # messagetemplatereviewreckwkword(消息模板审核记录表)->reviewerid(审核者ID关联用户)

    if obj.get("optype") == "messagetemplatereviewreckwkword.reviewerid_pie":
        res = get_pie(
            "select reviewerid x,count(*) y from vm772_58dd091a279b5392.messagetemplatereviewreckwkword group by reviewerid order by x desc",
            "审核者ID关联用户",
        )
    if obj.get("optype") == "messagetemplatereviewreckwkword.reviewerid_pie_v1":
        res = get_pie_v1(
            "select reviewerid x,count(*) y from vm772_58dd091a279b5392.messagetemplatereviewreckwkword group by reviewerid",
            "审核者ID关联用户",
        )
    if obj.get("optype") == "messagetemplatereviewreckwkword.reviewerid_pie_v2":
        res = get_pie_v2(
            "select reviewerid x,count(*) y from vm772_58dd091a279b5392.messagetemplatereviewreckwkword group by reviewerid",
            "审核者ID关联用户",
        )
    if obj.get("optype") == "messagetemplatereviewreckwkword.reviewerid_line":
        res = get_line(
            "select reviewerid x,count(*) y from vm772_58dd091a279b5392.messagetemplatereviewreckwkword group by reviewerid",
            "审核者ID关联用户",
        )
    if obj.get("optype") == "messagetemplatereviewreckwkword.reviewerid_bar":
        res = get_bar(
            "select reviewerid x,count(*) y from vm772_58dd091a279b5392.messagetemplatereviewreckwkword group by reviewerid",
            "审核者ID关联用户",
        )
    if obj.get("optype") == "messagetemplatereviewreckwkword.reviewerid_bar_v1":
        res = get_bar_v1(
            "select reviewerid x,count(*) y from vm772_58dd091a279b5392.messagetemplatereviewreckwkword group by reviewerid",
            "审核者ID关联用户",
        )
    if obj.get("optype") == "messagetemplatereviewreckwkword.reviewtime_line":
        res = get_line(
            "select reviewtime x,count(*) y from vm772_58dd091a279b5392.messagetemplatereviewreckwkword group by reviewtime order by x",
            "审核时间",
        )
    # messagetemplatereviewreckwkword(消息模板审核记录表)->reviewstatus(审核状态如待审核、审核通过、审核拒绝)

    if obj.get("optype") == "messagetemplatereviewreckwkword.reviewstatus_pie":
        res = get_pie(
            "select reviewstatus x,count(*) y from vm772_58dd091a279b5392.messagetemplatereviewreckwkword group by reviewstatus order by x desc",
            "审核状态如待审核、审核通过、审核拒绝",
        )
    if obj.get("optype") == "messagetemplatereviewreckwkword.reviewstatus_pie_v1":
        res = get_pie_v1(
            "select reviewstatus x,count(*) y from vm772_58dd091a279b5392.messagetemplatereviewreckwkword group by reviewstatus",
            "审核状态如待审核、审核通过、审核拒绝",
        )
    if obj.get("optype") == "messagetemplatereviewreckwkword.reviewstatus_pie_v2":
        res = get_pie_v2(
            "select reviewstatus x,count(*) y from vm772_58dd091a279b5392.messagetemplatereviewreckwkword group by reviewstatus",
            "审核状态如待审核、审核通过、审核拒绝",
        )
    if obj.get("optype") == "messagetemplatereviewreckwkword.reviewstatus_line":
        res = get_line(
            "select reviewstatus x,count(*) y from vm772_58dd091a279b5392.messagetemplatereviewreckwkword group by reviewstatus",
            "审核状态如待审核、审核通过、审核拒绝",
        )
    if obj.get("optype") == "messagetemplatereviewreckwkword.reviewstatus_bar":
        res = get_bar(
            "select reviewstatus x,count(*) y from vm772_58dd091a279b5392.messagetemplatereviewreckwkword group by reviewstatus",
            "审核状态如待审核、审核通过、审核拒绝",
        )
    if obj.get("optype") == "messagetemplatereviewreckwkword.reviewstatus_bar_v1":
        res = get_bar_v1(
            "select reviewstatus x,count(*) y from vm772_58dd091a279b5392.messagetemplatereviewreckwkword group by reviewstatus",
            "审核状态如待审核、审核通过、审核拒绝",
        )
    # messagetemplatereviewreckwkword(消息模板审核记录表)->reviewcomment(审核意见)

    if obj.get("optype") == "messagetemplatereviewreckwkword.reviewcomment_pie":
        res = get_pie(
            "select reviewcomment x,count(*) y from vm772_58dd091a279b5392.messagetemplatereviewreckwkword group by reviewcomment order by x desc",
            "审核意见",
        )
    if obj.get("optype") == "messagetemplatereviewreckwkword.reviewcomment_pie_v1":
        res = get_pie_v1(
            "select reviewcomment x,count(*) y from vm772_58dd091a279b5392.messagetemplatereviewreckwkword group by reviewcomment",
            "审核意见",
        )
    if obj.get("optype") == "messagetemplatereviewreckwkword.reviewcomment_pie_v2":
        res = get_pie_v2(
            "select reviewcomment x,count(*) y from vm772_58dd091a279b5392.messagetemplatereviewreckwkword group by reviewcomment",
            "审核意见",
        )
    if obj.get("optype") == "messagetemplatereviewreckwkword.reviewcomment_line":
        res = get_line(
            "select reviewcomment x,count(*) y from vm772_58dd091a279b5392.messagetemplatereviewreckwkword group by reviewcomment",
            "审核意见",
        )
    if obj.get("optype") == "messagetemplatereviewreckwkword.reviewcomment_bar":
        res = get_bar(
            "select reviewcomment x,count(*) y from vm772_58dd091a279b5392.messagetemplatereviewreckwkword group by reviewcomment",
            "审核意见",
        )
    if obj.get("optype") == "messagetemplatereviewreckwkword.reviewcomment_bar_v1":
        res = get_bar_v1(
            "select reviewcomment x,count(*) y from vm772_58dd091a279b5392.messagetemplatereviewreckwkword group by reviewcomment",
            "审核意见",
        )
    if obj.get("optype") == "messagetemplatereviewreckwkword.createtime_line":
        res = get_line(
            "select createtime x,count(*) y from vm772_58dd091a279b5392.messagetemplatereviewreckwkword group by createtime order by x",
            "记录创建时间",
        )
    if obj.get("optype") == "messagetemplatereviewreckwkword.updatetime_line":
        res = get_line(
            "select updatetime x,count(*) y from vm772_58dd091a279b5392.messagetemplatereviewreckwkword group by updatetime order by x",
            "记录更新时间",
        )
    # messagetemplatereviewreckwkword(消息模板审核记录表)->kwkwiskwkwdeleted(是否删除逻辑删除标记)

    if obj.get("optype") == "messagetemplatereviewreckwkword.kwkwiskwkwdeleted_pie":
        res = get_pie(
            "select kwkwiskwkwdeleted x,count(*) y from vm772_58dd091a279b5392.messagetemplatereviewreckwkword group by kwkwiskwkwdeleted order by x desc",
            "是否删除逻辑删除标记",
        )
    if obj.get("optype") == "messagetemplatereviewreckwkword.kwkwiskwkwdeleted_pie_v1":
        res = get_pie_v1(
            "select kwkwiskwkwdeleted x,count(*) y from vm772_58dd091a279b5392.messagetemplatereviewreckwkword group by kwkwiskwkwdeleted",
            "是否删除逻辑删除标记",
        )
    if obj.get("optype") == "messagetemplatereviewreckwkword.kwkwiskwkwdeleted_pie_v2":
        res = get_pie_v2(
            "select kwkwiskwkwdeleted x,count(*) y from vm772_58dd091a279b5392.messagetemplatereviewreckwkword group by kwkwiskwkwdeleted",
            "是否删除逻辑删除标记",
        )
    if obj.get("optype") == "messagetemplatereviewreckwkword.kwkwiskwkwdeleted_line":
        res = get_line(
            "select kwkwiskwkwdeleted x,count(*) y from vm772_58dd091a279b5392.messagetemplatereviewreckwkword group by kwkwiskwkwdeleted",
            "是否删除逻辑删除标记",
        )
    if obj.get("optype") == "messagetemplatereviewreckwkword.kwkwiskwkwdeleted_bar":
        res = get_bar(
            "select kwkwiskwkwdeleted x,count(*) y from vm772_58dd091a279b5392.messagetemplatereviewreckwkword group by kwkwiskwkwdeleted",
            "是否删除逻辑删除标记",
        )
    if obj.get("optype") == "messagetemplatereviewreckwkword.kwkwiskwkwdeleted_bar_v1":
        res = get_bar_v1(
            "select kwkwiskwkwdeleted x,count(*) y from vm772_58dd091a279b5392.messagetemplatereviewreckwkword group by kwkwiskwkwdeleted",
            "是否删除逻辑删除标记",
        )
    # messagesendstrategy(消息发送策略表)->name(策略名称)

    if obj.get("optype") == "messagesendstrategy.name_pie":
        res = get_pie(
            "select name x,count(*) y from vm772_58dd091a279b5392.messagesendstrategy group by name order by x desc",
            "策略名称",
        )
    if obj.get("optype") == "messagesendstrategy.name_pie_v1":
        res = get_pie_v1(
            "select name x,count(*) y from vm772_58dd091a279b5392.messagesendstrategy group by name",
            "策略名称",
        )
    if obj.get("optype") == "messagesendstrategy.name_pie_v2":
        res = get_pie_v2(
            "select name x,count(*) y from vm772_58dd091a279b5392.messagesendstrategy group by name",
            "策略名称",
        )
    if obj.get("optype") == "messagesendstrategy.name_line":
        res = get_line(
            "select name x,count(*) y from vm772_58dd091a279b5392.messagesendstrategy group by name",
            "策略名称",
        )
    if obj.get("optype") == "messagesendstrategy.name_bar":
        res = get_bar(
            "select name x,count(*) y from vm772_58dd091a279b5392.messagesendstrategy group by name",
            "策略名称",
        )
    if obj.get("optype") == "messagesendstrategy.name_bar_v1":
        res = get_bar_v1(
            "select name x,count(*) y from vm772_58dd091a279b5392.messagesendstrategy group by name",
            "策略名称",
        )
    if obj.get("optype") == "messagesendstrategy.description_wordcloud":
        textlist = get_data(
            "SELECT description result FROM vm772_58dd091a279b5392.messagesendstrategy;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # messagesendstrategy(消息发送策略表)->platkwkwfkwkworm(平台类型)

    if obj.get("optype") == "messagesendstrategy.platkwkwfkwkworm_pie":
        res = get_pie(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.messagesendstrategy group by platkwkwfkwkworm order by x desc",
            "平台类型",
        )
    if obj.get("optype") == "messagesendstrategy.platkwkwfkwkworm_pie_v1":
        res = get_pie_v1(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.messagesendstrategy group by platkwkwfkwkworm",
            "平台类型",
        )
    if obj.get("optype") == "messagesendstrategy.platkwkwfkwkworm_pie_v2":
        res = get_pie_v2(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.messagesendstrategy group by platkwkwfkwkworm",
            "平台类型",
        )
    if obj.get("optype") == "messagesendstrategy.platkwkwfkwkworm_line":
        res = get_line(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.messagesendstrategy group by platkwkwfkwkworm",
            "平台类型",
        )
    if obj.get("optype") == "messagesendstrategy.platkwkwfkwkworm_bar":
        res = get_bar(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.messagesendstrategy group by platkwkwfkwkworm",
            "平台类型",
        )
    if obj.get("optype") == "messagesendstrategy.platkwkwfkwkworm_bar_v1":
        res = get_bar_v1(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.messagesendstrategy group by platkwkwfkwkworm",
            "平台类型",
        )
    # messagesendstrategy(消息发送策略表)->targettype(目标类型)

    if obj.get("optype") == "messagesendstrategy.targettype_pie":
        res = get_pie(
            "select targettype x,count(*) y from vm772_58dd091a279b5392.messagesendstrategy group by targettype order by x desc",
            "目标类型",
        )
    if obj.get("optype") == "messagesendstrategy.targettype_pie_v1":
        res = get_pie_v1(
            "select targettype x,count(*) y from vm772_58dd091a279b5392.messagesendstrategy group by targettype",
            "目标类型",
        )
    if obj.get("optype") == "messagesendstrategy.targettype_pie_v2":
        res = get_pie_v2(
            "select targettype x,count(*) y from vm772_58dd091a279b5392.messagesendstrategy group by targettype",
            "目标类型",
        )
    if obj.get("optype") == "messagesendstrategy.targettype_line":
        res = get_line(
            "select targettype x,count(*) y from vm772_58dd091a279b5392.messagesendstrategy group by targettype",
            "目标类型",
        )
    if obj.get("optype") == "messagesendstrategy.targettype_bar":
        res = get_bar(
            "select targettype x,count(*) y from vm772_58dd091a279b5392.messagesendstrategy group by targettype",
            "目标类型",
        )
    if obj.get("optype") == "messagesendstrategy.targettype_bar_v1":
        res = get_bar_v1(
            "select targettype x,count(*) y from vm772_58dd091a279b5392.messagesendstrategy group by targettype",
            "目标类型",
        )
    if obj.get("optype") == "messagesendstrategy.contenttemplate_wordcloud":
        textlist = get_data(
            "SELECT contenttemplate result FROM vm772_58dd091a279b5392.messagesendstrategy;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # messagesendstrategy(消息发送策略表)->scheduletype(计划类型如一次性、周期性)

    if obj.get("optype") == "messagesendstrategy.scheduletype_pie":
        res = get_pie(
            "select scheduletype x,count(*) y from vm772_58dd091a279b5392.messagesendstrategy group by scheduletype order by x desc",
            "计划类型如一次性、周期性",
        )
    if obj.get("optype") == "messagesendstrategy.scheduletype_pie_v1":
        res = get_pie_v1(
            "select scheduletype x,count(*) y from vm772_58dd091a279b5392.messagesendstrategy group by scheduletype",
            "计划类型如一次性、周期性",
        )
    if obj.get("optype") == "messagesendstrategy.scheduletype_pie_v2":
        res = get_pie_v2(
            "select scheduletype x,count(*) y from vm772_58dd091a279b5392.messagesendstrategy group by scheduletype",
            "计划类型如一次性、周期性",
        )
    if obj.get("optype") == "messagesendstrategy.scheduletype_line":
        res = get_line(
            "select scheduletype x,count(*) y from vm772_58dd091a279b5392.messagesendstrategy group by scheduletype",
            "计划类型如一次性、周期性",
        )
    if obj.get("optype") == "messagesendstrategy.scheduletype_bar":
        res = get_bar(
            "select scheduletype x,count(*) y from vm772_58dd091a279b5392.messagesendstrategy group by scheduletype",
            "计划类型如一次性、周期性",
        )
    if obj.get("optype") == "messagesendstrategy.scheduletype_bar_v1":
        res = get_bar_v1(
            "select scheduletype x,count(*) y from vm772_58dd091a279b5392.messagesendstrategy group by scheduletype",
            "计划类型如一次性、周期性",
        )
    if obj.get("optype") == "messagesendstrategy.starttime_line":
        res = get_line(
            "select starttime x,count(*) y from vm772_58dd091a279b5392.messagesendstrategy group by starttime order by x",
            "开始时间",
        )
    if obj.get("optype") == "messagesendstrategy.endtime_line":
        res = get_line(
            "select endtime x,count(*) y from vm772_58dd091a279b5392.messagesendstrategy group by endtime order by x",
            "结束时间",
        )
    # messagesendstrategy(消息发送策略表)->userid(用户ID关联用户)

    if obj.get("optype") == "messagesendstrategy.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagesendstrategy group by userid order by x desc",
            "用户ID关联用户",
        )
    if obj.get("optype") == "messagesendstrategy.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagesendstrategy group by userid",
            "用户ID关联用户",
        )
    if obj.get("optype") == "messagesendstrategy.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagesendstrategy group by userid",
            "用户ID关联用户",
        )
    if obj.get("optype") == "messagesendstrategy.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagesendstrategy group by userid",
            "用户ID关联用户",
        )
    if obj.get("optype") == "messagesendstrategy.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagesendstrategy group by userid",
            "用户ID关联用户",
        )
    if obj.get("optype") == "messagesendstrategy.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagesendstrategy group by userid",
            "用户ID关联用户",
        )
    # messagesendstrategy(消息发送策略表)->status(状态如启用、禁用)

    if obj.get("optype") == "messagesendstrategy.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagesendstrategy group by status order by x desc",
            "状态如启用、禁用",
        )
    if obj.get("optype") == "messagesendstrategy.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagesendstrategy group by status",
            "状态如启用、禁用",
        )
    if obj.get("optype") == "messagesendstrategy.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagesendstrategy group by status",
            "状态如启用、禁用",
        )
    if obj.get("optype") == "messagesendstrategy.status_line":
        res = get_line(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagesendstrategy group by status",
            "状态如启用、禁用",
        )
    if obj.get("optype") == "messagesendstrategy.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagesendstrategy group by status",
            "状态如启用、禁用",
        )
    if obj.get("optype") == "messagesendstrategy.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagesendstrategy group by status",
            "状态如启用、禁用",
        )
    if obj.get("optype") == "messagesendstrategy.createdat_line":
        res = get_line(
            "select createdat x,count(*) y from vm772_58dd091a279b5392.messagesendstrategy group by createdat order by x",
            "创建时间",
        )
    if obj.get("optype") == "messagesendstrategy.updatedat_line":
        res = get_line(
            "select updatedat x,count(*) y from vm772_58dd091a279b5392.messagesendstrategy group by updatedat order by x",
            "更新时间",
        )
    # messagesendfrequencylimit(消息发送频率限制表)->platkwkwfkwkwormid(平台ID关联到不同平台的用于区分不同平台的发送频率限制)

    if obj.get("optype") == "messagesendfrequencylimit.platkwkwfkwkwormid_pie":
        res = get_pie(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.messagesendfrequencylimit group by platkwkwfkwkwormid order by x desc",
            "平台ID关联到不同平台的用于区分不同平台的发送频率限制",
        )
    if obj.get("optype") == "messagesendfrequencylimit.platkwkwfkwkwormid_pie_v1":
        res = get_pie_v1(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.messagesendfrequencylimit group by platkwkwfkwkwormid",
            "平台ID关联到不同平台的用于区分不同平台的发送频率限制",
        )
    if obj.get("optype") == "messagesendfrequencylimit.platkwkwfkwkwormid_pie_v2":
        res = get_pie_v2(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.messagesendfrequencylimit group by platkwkwfkwkwormid",
            "平台ID关联到不同平台的用于区分不同平台的发送频率限制",
        )
    if obj.get("optype") == "messagesendfrequencylimit.platkwkwfkwkwormid_line":
        res = get_line(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.messagesendfrequencylimit group by platkwkwfkwkwormid",
            "平台ID关联到不同平台的用于区分不同平台的发送频率限制",
        )
    if obj.get("optype") == "messagesendfrequencylimit.platkwkwfkwkwormid_bar":
        res = get_bar(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.messagesendfrequencylimit group by platkwkwfkwkwormid",
            "平台ID关联到不同平台的用于区分不同平台的发送频率限制",
        )
    if obj.get("optype") == "messagesendfrequencylimit.platkwkwfkwkwormid_bar_v1":
        res = get_bar_v1(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.messagesendfrequencylimit group by platkwkwfkwkwormid",
            "平台ID关联到不同平台的用于区分不同平台的发送频率限制",
        )
    # messagesendfrequencylimit(消息发送频率限制表)->userid(用户ID关联到用户示该限制是针对哪个用户的)

    if obj.get("optype") == "messagesendfrequencylimit.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagesendfrequencylimit group by userid order by x desc",
            "用户ID关联到用户示该限制是针对哪个用户的",
        )
    if obj.get("optype") == "messagesendfrequencylimit.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagesendfrequencylimit group by userid",
            "用户ID关联到用户示该限制是针对哪个用户的",
        )
    if obj.get("optype") == "messagesendfrequencylimit.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagesendfrequencylimit group by userid",
            "用户ID关联到用户示该限制是针对哪个用户的",
        )
    if obj.get("optype") == "messagesendfrequencylimit.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagesendfrequencylimit group by userid",
            "用户ID关联到用户示该限制是针对哪个用户的",
        )
    if obj.get("optype") == "messagesendfrequencylimit.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagesendfrequencylimit group by userid",
            "用户ID关联到用户示该限制是针对哪个用户的",
        )
    if obj.get("optype") == "messagesendfrequencylimit.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagesendfrequencylimit group by userid",
            "用户ID关联到用户示该限制是针对哪个用户的",
        )
    # messagesendfrequencylimit(消息发送频率限制表)->messagetype(消息类型如文本、图片、视频等用于区分不同类型的消息发送频率)

    if obj.get("optype") == "messagesendfrequencylimit.messagetype_pie":
        res = get_pie(
            "select messagetype x,count(*) y from vm772_58dd091a279b5392.messagesendfrequencylimit group by messagetype order by x desc",
            "消息类型如文本、图片、视频等用于区分不同类型的消息发送频率",
        )
    if obj.get("optype") == "messagesendfrequencylimit.messagetype_pie_v1":
        res = get_pie_v1(
            "select messagetype x,count(*) y from vm772_58dd091a279b5392.messagesendfrequencylimit group by messagetype",
            "消息类型如文本、图片、视频等用于区分不同类型的消息发送频率",
        )
    if obj.get("optype") == "messagesendfrequencylimit.messagetype_pie_v2":
        res = get_pie_v2(
            "select messagetype x,count(*) y from vm772_58dd091a279b5392.messagesendfrequencylimit group by messagetype",
            "消息类型如文本、图片、视频等用于区分不同类型的消息发送频率",
        )
    if obj.get("optype") == "messagesendfrequencylimit.messagetype_line":
        res = get_line(
            "select messagetype x,count(*) y from vm772_58dd091a279b5392.messagesendfrequencylimit group by messagetype",
            "消息类型如文本、图片、视频等用于区分不同类型的消息发送频率",
        )
    if obj.get("optype") == "messagesendfrequencylimit.messagetype_bar":
        res = get_bar(
            "select messagetype x,count(*) y from vm772_58dd091a279b5392.messagesendfrequencylimit group by messagetype",
            "消息类型如文本、图片、视频等用于区分不同类型的消息发送频率",
        )
    if obj.get("optype") == "messagesendfrequencylimit.messagetype_bar_v1":
        res = get_bar_v1(
            "select messagetype x,count(*) y from vm772_58dd091a279b5392.messagesendfrequencylimit group by messagetype",
            "消息类型如文本、图片、视频等用于区分不同类型的消息发送频率",
        )
    if obj.get("optype") == "messagesendfrequencylimit.maxsendcount_line":
        res = get_line(
            "select maxsendcount x,count(*) y from vm772_58dd091a279b5392.messagesendfrequencylimit group by maxsendcount order by x",
            "最大发送次数在指定时间周期内允许的最大发送次数",
        )
    if obj.get("optype") == "messagesendfrequencylimit.timeperiod_line":
        res = get_line(
            "select timeperiod x,count(*) y from vm772_58dd091a279b5392.messagesendfrequencylimit group by timeperiod order by x",
            "时间周期如每天、每小时等示上述最大发送次数的时间范围",
        )
    if obj.get("optype") == "messagesendfrequencylimit.lkwkwastsendtime_line":
        res = get_line(
            "select lkwkwastsendtime x,count(*) y from vm772_58dd091a279b5392.messagesendfrequencylimit group by lkwkwastsendtime order by x",
            "上次发送时间记录最后一次发送消息的时间用于计算下一次发送的时间",
        )
    if obj.get("optype") == "messagesendfrequencylimit.resettime_line":
        res = get_line(
            "select resettime x,count(*) y from vm772_58dd091a279b5392.messagesendfrequencylimit group by resettime order by x",
            "重置时间时间周期的开始时间用于重置发送次数计数器",
        )
    # messagesendfrequencylimit(消息发送频率限制表)->status(状态如启用、禁用示该频率限制是否生效)

    if obj.get("optype") == "messagesendfrequencylimit.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagesendfrequencylimit group by status order by x desc",
            "状态如启用、禁用示该频率限制是否生效",
        )
    if obj.get("optype") == "messagesendfrequencylimit.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagesendfrequencylimit group by status",
            "状态如启用、禁用示该频率限制是否生效",
        )
    if obj.get("optype") == "messagesendfrequencylimit.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagesendfrequencylimit group by status",
            "状态如启用、禁用示该频率限制是否生效",
        )
    if obj.get("optype") == "messagesendfrequencylimit.status_line":
        res = get_line(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagesendfrequencylimit group by status",
            "状态如启用、禁用示该频率限制是否生效",
        )
    if obj.get("optype") == "messagesendfrequencylimit.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagesendfrequencylimit group by status",
            "状态如启用、禁用示该频率限制是否生效",
        )
    if obj.get("optype") == "messagesendfrequencylimit.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagesendfrequencylimit group by status",
            "状态如启用、禁用示该频率限制是否生效",
        )
    # messagesendfrequencylimit(消息发送频率限制表)->kwkwnote(备注用于记录该频率限制的其他相关信息或说明)

    if obj.get("optype") == "messagesendfrequencylimit.kwkwnote_pie":
        res = get_pie(
            "select kwkwnote x,count(*) y from vm772_58dd091a279b5392.messagesendfrequencylimit group by kwkwnote order by x desc",
            "备注用于记录该频率限制的其他相关信息或说明",
        )
    if obj.get("optype") == "messagesendfrequencylimit.kwkwnote_pie_v1":
        res = get_pie_v1(
            "select kwkwnote x,count(*) y from vm772_58dd091a279b5392.messagesendfrequencylimit group by kwkwnote",
            "备注用于记录该频率限制的其他相关信息或说明",
        )
    if obj.get("optype") == "messagesendfrequencylimit.kwkwnote_pie_v2":
        res = get_pie_v2(
            "select kwkwnote x,count(*) y from vm772_58dd091a279b5392.messagesendfrequencylimit group by kwkwnote",
            "备注用于记录该频率限制的其他相关信息或说明",
        )
    if obj.get("optype") == "messagesendfrequencylimit.kwkwnote_line":
        res = get_line(
            "select kwkwnote x,count(*) y from vm772_58dd091a279b5392.messagesendfrequencylimit group by kwkwnote",
            "备注用于记录该频率限制的其他相关信息或说明",
        )
    if obj.get("optype") == "messagesendfrequencylimit.kwkwnote_bar":
        res = get_bar(
            "select kwkwnote x,count(*) y from vm772_58dd091a279b5392.messagesendfrequencylimit group by kwkwnote",
            "备注用于记录该频率限制的其他相关信息或说明",
        )
    if obj.get("optype") == "messagesendfrequencylimit.kwkwnote_bar_v1":
        res = get_bar_v1(
            "select kwkwnote x,count(*) y from vm772_58dd091a279b5392.messagesendfrequencylimit group by kwkwnote",
            "备注用于记录该频率限制的其他相关信息或说明",
        )
    # messagesendprikwkwority(消息发送优先级表)->prikwkworitylevel(优先级等级)

    if obj.get("optype") == "messagesendprikwkwority.prikwkworitylevel_pie":
        res = get_pie(
            "select prikwkworitylevel x,count(*) y from vm772_58dd091a279b5392.messagesendprikwkwority group by prikwkworitylevel order by x desc",
            "优先级等级",
        )
    if obj.get("optype") == "messagesendprikwkwority.prikwkworitylevel_pie_v1":
        res = get_pie_v1(
            "select prikwkworitylevel x,count(*) y from vm772_58dd091a279b5392.messagesendprikwkwority group by prikwkworitylevel",
            "优先级等级",
        )
    if obj.get("optype") == "messagesendprikwkwority.prikwkworitylevel_pie_v2":
        res = get_pie_v2(
            "select prikwkworitylevel x,count(*) y from vm772_58dd091a279b5392.messagesendprikwkwority group by prikwkworitylevel",
            "优先级等级",
        )
    if obj.get("optype") == "messagesendprikwkwority.prikwkworitylevel_line":
        res = get_line(
            "select prikwkworitylevel x,count(*) y from vm772_58dd091a279b5392.messagesendprikwkwority group by prikwkworitylevel",
            "优先级等级",
        )
    if obj.get("optype") == "messagesendprikwkwority.prikwkworitylevel_bar":
        res = get_bar(
            "select prikwkworitylevel x,count(*) y from vm772_58dd091a279b5392.messagesendprikwkwority group by prikwkworitylevel",
            "优先级等级",
        )
    if obj.get("optype") == "messagesendprikwkwority.prikwkworitylevel_bar_v1":
        res = get_bar_v1(
            "select prikwkworitylevel x,count(*) y from vm772_58dd091a279b5392.messagesendprikwkwority group by prikwkworitylevel",
            "优先级等级",
        )
    if obj.get("optype") == "messagesendprikwkwority.description_wordcloud":
        textlist = get_data(
            "SELECT description result FROM vm772_58dd091a279b5392.messagesendprikwkwority;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "messagesendprikwkwority.createdat_line":
        res = get_line(
            "select createdat x,count(*) y from vm772_58dd091a279b5392.messagesendprikwkwority group by createdat order by x",
            "创建时间",
        )
    if obj.get("optype") == "messagesendprikwkwority.updatedat_line":
        res = get_line(
            "select updatedat x,count(*) y from vm772_58dd091a279b5392.messagesendprikwkwority group by updatedat order by x",
            "更新时间",
        )
    # messagesendprikwkwority(消息发送优先级表)->kwkwisactive(是否激活)

    if obj.get("optype") == "messagesendprikwkwority.kwkwisactive_pie":
        res = get_pie(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.messagesendprikwkwority group by kwkwisactive order by x desc",
            "是否激活",
        )
    if obj.get("optype") == "messagesendprikwkwority.kwkwisactive_pie_v1":
        res = get_pie_v1(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.messagesendprikwkwority group by kwkwisactive",
            "是否激活",
        )
    if obj.get("optype") == "messagesendprikwkwority.kwkwisactive_pie_v2":
        res = get_pie_v2(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.messagesendprikwkwority group by kwkwisactive",
            "是否激活",
        )
    if obj.get("optype") == "messagesendprikwkwority.kwkwisactive_line":
        res = get_line(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.messagesendprikwkwority group by kwkwisactive",
            "是否激活",
        )
    if obj.get("optype") == "messagesendprikwkwority.kwkwisactive_bar":
        res = get_bar(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.messagesendprikwkwority group by kwkwisactive",
            "是否激活",
        )
    if obj.get("optype") == "messagesendprikwkwority.kwkwisactive_bar_v1":
        res = get_bar_v1(
            "select kwkwisactive x,count(*) y from vm772_58dd091a279b5392.messagesendprikwkwority group by kwkwisactive",
            "是否激活",
        )
    # messagesendprikwkwority(消息发送优先级表)->platkwkwfkwkwormid(平台ID关联字段指向平台)

    if obj.get("optype") == "messagesendprikwkwority.platkwkwfkwkwormid_pie":
        res = get_pie(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.messagesendprikwkwority group by platkwkwfkwkwormid order by x desc",
            "平台ID关联字段指向平台",
        )
    if obj.get("optype") == "messagesendprikwkwority.platkwkwfkwkwormid_pie_v1":
        res = get_pie_v1(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.messagesendprikwkwority group by platkwkwfkwkwormid",
            "平台ID关联字段指向平台",
        )
    if obj.get("optype") == "messagesendprikwkwority.platkwkwfkwkwormid_pie_v2":
        res = get_pie_v2(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.messagesendprikwkwority group by platkwkwfkwkwormid",
            "平台ID关联字段指向平台",
        )
    if obj.get("optype") == "messagesendprikwkwority.platkwkwfkwkwormid_line":
        res = get_line(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.messagesendprikwkwority group by platkwkwfkwkwormid",
            "平台ID关联字段指向平台",
        )
    if obj.get("optype") == "messagesendprikwkwority.platkwkwfkwkwormid_bar":
        res = get_bar(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.messagesendprikwkwority group by platkwkwfkwkwormid",
            "平台ID关联字段指向平台",
        )
    if obj.get("optype") == "messagesendprikwkwority.platkwkwfkwkwormid_bar_v1":
        res = get_bar_v1(
            "select platkwkwfkwkwormid x,count(*) y from vm772_58dd091a279b5392.messagesendprikwkwority group by platkwkwfkwkwormid",
            "平台ID关联字段指向平台",
        )
    # messagesendprikwkwority(消息发送优先级表)->messagetypeid(消息类型ID关联字段指向消息类型)

    if obj.get("optype") == "messagesendprikwkwority.messagetypeid_pie":
        res = get_pie(
            "select messagetypeid x,count(*) y from vm772_58dd091a279b5392.messagesendprikwkwority group by messagetypeid order by x desc",
            "消息类型ID关联字段指向消息类型",
        )
    if obj.get("optype") == "messagesendprikwkwority.messagetypeid_pie_v1":
        res = get_pie_v1(
            "select messagetypeid x,count(*) y from vm772_58dd091a279b5392.messagesendprikwkwority group by messagetypeid",
            "消息类型ID关联字段指向消息类型",
        )
    if obj.get("optype") == "messagesendprikwkwority.messagetypeid_pie_v2":
        res = get_pie_v2(
            "select messagetypeid x,count(*) y from vm772_58dd091a279b5392.messagesendprikwkwority group by messagetypeid",
            "消息类型ID关联字段指向消息类型",
        )
    if obj.get("optype") == "messagesendprikwkwority.messagetypeid_line":
        res = get_line(
            "select messagetypeid x,count(*) y from vm772_58dd091a279b5392.messagesendprikwkwority group by messagetypeid",
            "消息类型ID关联字段指向消息类型",
        )
    if obj.get("optype") == "messagesendprikwkwority.messagetypeid_bar":
        res = get_bar(
            "select messagetypeid x,count(*) y from vm772_58dd091a279b5392.messagesendprikwkwority group by messagetypeid",
            "消息类型ID关联字段指向消息类型",
        )
    if obj.get("optype") == "messagesendprikwkwority.messagetypeid_bar_v1":
        res = get_bar_v1(
            "select messagetypeid x,count(*) y from vm772_58dd091a279b5392.messagesendprikwkwority group by messagetypeid",
            "消息类型ID关联字段指向消息类型",
        )
    if obj.get("optype") == "messagesendprikwkwority.kwkwdefaultkwkwdelay_line":
        res = get_line(
            "select kwkwdefaultkwkwdelay x,count(*) y from vm772_58dd091a279b5392.messagesendprikwkwority group by kwkwdefaultkwkwdelay order by x",
            "默认延迟时间秒",
        )
    # messagesendprikwkwority(消息发送优先级表)->maxrekwkwtrycount(最大重试次数)

    if obj.get("optype") == "messagesendprikwkwority.maxrekwkwtrycount_pie":
        res = get_pie(
            "select maxrekwkwtrycount x,count(*) y from vm772_58dd091a279b5392.messagesendprikwkwority group by maxrekwkwtrycount order by x desc",
            "最大重试次数",
        )
    if obj.get("optype") == "messagesendprikwkwority.maxrekwkwtrycount_pie_v1":
        res = get_pie_v1(
            "select maxrekwkwtrycount x,count(*) y from vm772_58dd091a279b5392.messagesendprikwkwority group by maxrekwkwtrycount",
            "最大重试次数",
        )
    if obj.get("optype") == "messagesendprikwkwority.maxrekwkwtrycount_pie_v2":
        res = get_pie_v2(
            "select maxrekwkwtrycount x,count(*) y from vm772_58dd091a279b5392.messagesendprikwkwority group by maxrekwkwtrycount",
            "最大重试次数",
        )
    if obj.get("optype") == "messagesendprikwkwority.maxrekwkwtrycount_line":
        res = get_line(
            "select maxrekwkwtrycount x,count(*) y from vm772_58dd091a279b5392.messagesendprikwkwority group by maxrekwkwtrycount",
            "最大重试次数",
        )
    if obj.get("optype") == "messagesendprikwkwority.maxrekwkwtrycount_bar":
        res = get_bar(
            "select maxrekwkwtrycount x,count(*) y from vm772_58dd091a279b5392.messagesendprikwkwority group by maxrekwkwtrycount",
            "最大重试次数",
        )
    if obj.get("optype") == "messagesendprikwkwority.maxrekwkwtrycount_bar_v1":
        res = get_bar_v1(
            "select maxrekwkwtrycount x,count(*) y from vm772_58dd091a279b5392.messagesendprikwkwority group by maxrekwkwtrycount",
            "最大重试次数",
        )
    # messagetemplateusagestatkwkwistics(消息模板使用统计表)->templateid(消息模板ID)

    if obj.get("optype") == "messagetemplateusagestatkwkwistics.templateid_pie":
        res = get_pie(
            "select templateid x,count(*) y from vm772_58dd091a279b5392.messagetemplateusagestatkwkwistics group by templateid order by x desc",
            "消息模板ID",
        )
    if obj.get("optype") == "messagetemplateusagestatkwkwistics.templateid_pie_v1":
        res = get_pie_v1(
            "select templateid x,count(*) y from vm772_58dd091a279b5392.messagetemplateusagestatkwkwistics group by templateid",
            "消息模板ID",
        )
    if obj.get("optype") == "messagetemplateusagestatkwkwistics.templateid_pie_v2":
        res = get_pie_v2(
            "select templateid x,count(*) y from vm772_58dd091a279b5392.messagetemplateusagestatkwkwistics group by templateid",
            "消息模板ID",
        )
    if obj.get("optype") == "messagetemplateusagestatkwkwistics.templateid_line":
        res = get_line(
            "select templateid x,count(*) y from vm772_58dd091a279b5392.messagetemplateusagestatkwkwistics group by templateid",
            "消息模板ID",
        )
    if obj.get("optype") == "messagetemplateusagestatkwkwistics.templateid_bar":
        res = get_bar(
            "select templateid x,count(*) y from vm772_58dd091a279b5392.messagetemplateusagestatkwkwistics group by templateid",
            "消息模板ID",
        )
    if obj.get("optype") == "messagetemplateusagestatkwkwistics.templateid_bar_v1":
        res = get_bar_v1(
            "select templateid x,count(*) y from vm772_58dd091a279b5392.messagetemplateusagestatkwkwistics group by templateid",
            "消息模板ID",
        )
    # messagetemplateusagestatkwkwistics(消息模板使用统计表)->usagecount(使用次数)

    if obj.get("optype") == "messagetemplateusagestatkwkwistics.usagecount_pie":
        res = get_pie(
            "select usagecount x,count(*) y from vm772_58dd091a279b5392.messagetemplateusagestatkwkwistics group by usagecount order by x desc",
            "使用次数",
        )
    if obj.get("optype") == "messagetemplateusagestatkwkwistics.usagecount_pie_v1":
        res = get_pie_v1(
            "select usagecount x,count(*) y from vm772_58dd091a279b5392.messagetemplateusagestatkwkwistics group by usagecount",
            "使用次数",
        )
    if obj.get("optype") == "messagetemplateusagestatkwkwistics.usagecount_pie_v2":
        res = get_pie_v2(
            "select usagecount x,count(*) y from vm772_58dd091a279b5392.messagetemplateusagestatkwkwistics group by usagecount",
            "使用次数",
        )
    if obj.get("optype") == "messagetemplateusagestatkwkwistics.usagecount_line":
        res = get_line(
            "select usagecount x,count(*) y from vm772_58dd091a279b5392.messagetemplateusagestatkwkwistics group by usagecount",
            "使用次数",
        )
    if obj.get("optype") == "messagetemplateusagestatkwkwistics.usagecount_bar":
        res = get_bar(
            "select usagecount x,count(*) y from vm772_58dd091a279b5392.messagetemplateusagestatkwkwistics group by usagecount",
            "使用次数",
        )
    if obj.get("optype") == "messagetemplateusagestatkwkwistics.usagecount_bar_v1":
        res = get_bar_v1(
            "select usagecount x,count(*) y from vm772_58dd091a279b5392.messagetemplateusagestatkwkwistics group by usagecount",
            "使用次数",
        )
    if obj.get("optype") == "messagetemplateusagestatkwkwistics.lkwkwastusedtime_line":
        res = get_line(
            "select lkwkwastusedtime x,count(*) y from vm772_58dd091a279b5392.messagetemplateusagestatkwkwistics group by lkwkwastusedtime order by x",
            "最后使用时间",
        )
    if obj.get("optype") == "messagetemplateusagestatkwkwistics.createdat_line":
        res = get_line(
            "select createdat x,count(*) y from vm772_58dd091a279b5392.messagetemplateusagestatkwkwistics group by createdat order by x",
            "创建时间",
        )
    if obj.get("optype") == "messagetemplateusagestatkwkwistics.updatedat_line":
        res = get_line(
            "select updatedat x,count(*) y from vm772_58dd091a279b5392.messagetemplateusagestatkwkwistics group by updatedat order by x",
            "更新时间",
        )
    # messagetemplateusagestatkwkwistics(消息模板使用统计表)->platkwkwfkwkworm(使用平台)

    if obj.get("optype") == "messagetemplateusagestatkwkwistics.platkwkwfkwkworm_pie":
        res = get_pie(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.messagetemplateusagestatkwkwistics group by platkwkwfkwkworm order by x desc",
            "使用平台",
        )
    if (
        obj.get("optype")
        == "messagetemplateusagestatkwkwistics.platkwkwfkwkworm_pie_v1"
    ):
        res = get_pie_v1(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.messagetemplateusagestatkwkwistics group by platkwkwfkwkworm",
            "使用平台",
        )
    if (
        obj.get("optype")
        == "messagetemplateusagestatkwkwistics.platkwkwfkwkworm_pie_v2"
    ):
        res = get_pie_v2(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.messagetemplateusagestatkwkwistics group by platkwkwfkwkworm",
            "使用平台",
        )
    if obj.get("optype") == "messagetemplateusagestatkwkwistics.platkwkwfkwkworm_line":
        res = get_line(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.messagetemplateusagestatkwkwistics group by platkwkwfkwkworm",
            "使用平台",
        )
    if obj.get("optype") == "messagetemplateusagestatkwkwistics.platkwkwfkwkworm_bar":
        res = get_bar(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.messagetemplateusagestatkwkwistics group by platkwkwfkwkworm",
            "使用平台",
        )
    if (
        obj.get("optype")
        == "messagetemplateusagestatkwkwistics.platkwkwfkwkworm_bar_v1"
    ):
        res = get_bar_v1(
            "select platkwkwfkwkworm x,count(*) y from vm772_58dd091a279b5392.messagetemplateusagestatkwkwistics group by platkwkwfkwkworm",
            "使用平台",
        )
    # messagetemplateusagestatkwkwistics(消息模板使用统计表)->userid(用户ID)

    if obj.get("optype") == "messagetemplateusagestatkwkwistics.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagetemplateusagestatkwkwistics group by userid order by x desc",
            "用户ID",
        )
    if obj.get("optype") == "messagetemplateusagestatkwkwistics.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagetemplateusagestatkwkwistics group by userid",
            "用户ID",
        )
    if obj.get("optype") == "messagetemplateusagestatkwkwistics.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagetemplateusagestatkwkwistics group by userid",
            "用户ID",
        )
    if obj.get("optype") == "messagetemplateusagestatkwkwistics.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagetemplateusagestatkwkwistics group by userid",
            "用户ID",
        )
    if obj.get("optype") == "messagetemplateusagestatkwkwistics.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagetemplateusagestatkwkwistics group by userid",
            "用户ID",
        )
    if obj.get("optype") == "messagetemplateusagestatkwkwistics.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm772_58dd091a279b5392.messagetemplateusagestatkwkwistics group by userid",
            "用户ID",
        )
    # messagetemplateusagestatkwkwistics(消息模板使用统计表)->status(状态)

    if obj.get("optype") == "messagetemplateusagestatkwkwistics.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagetemplateusagestatkwkwistics group by status order by x desc",
            "状态",
        )
    if obj.get("optype") == "messagetemplateusagestatkwkwistics.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagetemplateusagestatkwkwistics group by status",
            "状态",
        )
    if obj.get("optype") == "messagetemplateusagestatkwkwistics.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagetemplateusagestatkwkwistics group by status",
            "状态",
        )
    if obj.get("optype") == "messagetemplateusagestatkwkwistics.status_line":
        res = get_line(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagetemplateusagestatkwkwistics group by status",
            "状态",
        )
    if obj.get("optype") == "messagetemplateusagestatkwkwistics.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagetemplateusagestatkwkwistics group by status",
            "状态",
        )
    if obj.get("optype") == "messagetemplateusagestatkwkwistics.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm772_58dd091a279b5392.messagetemplateusagestatkwkwistics group by status",
            "状态",
        )
    # supermanager(系统管理员)->username(管理员姓名)

    if obj.get("optype") == "supermanager.username_pie":
        res = get_pie(
            "select username x,count(*) y from vm772_58dd091a279b5392.supermanager group by username order by x desc",
            "管理员姓名",
        )
    if obj.get("optype") == "supermanager.username_pie_v1":
        res = get_pie_v1(
            "select username x,count(*) y from vm772_58dd091a279b5392.supermanager group by username",
            "管理员姓名",
        )
    if obj.get("optype") == "supermanager.username_pie_v2":
        res = get_pie_v2(
            "select username x,count(*) y from vm772_58dd091a279b5392.supermanager group by username",
            "管理员姓名",
        )
    if obj.get("optype") == "supermanager.username_line":
        res = get_line(
            "select username x,count(*) y from vm772_58dd091a279b5392.supermanager group by username",
            "管理员姓名",
        )
    if obj.get("optype") == "supermanager.username_bar":
        res = get_bar(
            "select username x,count(*) y from vm772_58dd091a279b5392.supermanager group by username",
            "管理员姓名",
        )
    if obj.get("optype") == "supermanager.username_bar_v1":
        res = get_bar_v1(
            "select username x,count(*) y from vm772_58dd091a279b5392.supermanager group by username",
            "管理员姓名",
        )
    assert "title" in res
    return JsonResponse(res)


# __config_visual_views


def bi_level_2(request):
    if request.method == "GET":
        return HttpResponse(
            loader.get_template("config_visual/bi_level_2.html").render({}, request)
        )
    obj = mydict(request.POST)
    res = dict()

    return JsonResponse(res)


def bi_new(request):
    if request.method == "GET":
        return HttpResponse(loader.get_template("config_visual/bi_new.html").render())
    obj = mydict(request.POST)
    res = dict()

    # __mark_appcenter_views_all__level_new_bi

    return JsonResponse(res)


def view_userinfo(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpuserinfo.html", locals())


def view_platkwkwfkwkwormaccount(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tpplatkwkwfkwkwormaccount.html", locals()
        )


def view_messagetemplate(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpmessagetemplate.html", locals())


def view_tkwkwaskmanagement(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tptkwkwaskmanagement.html", locals())


def view_tkwkwaskexecutionreckwkword(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tptkwkwaskexecutionreckwkword.html", locals()
        )


def view_tkwkwaskstatus(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tptkwkwaskstatus.html", locals())


def view_scheduledtkwkwask(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpscheduledtkwkwask.html", locals())


def view_messagesendreckwkword(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tpmessagesendreckwkword.html", locals()
        )


def view_messagereceivereckwkword(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tpmessagereceivereckwkword.html", locals()
        )


def view_userpreference(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpuserpreference.html", locals())


def view_accountbkwkwindkwkwing(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tpaccountbkwkwindkwkwing.html", locals()
        )


def view_messagecontentreview(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tpmessagecontentreview.html", locals()
        )


def view_messagesendfailurelog(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tpmessagesendfailurelog.html", locals()
        )


def view_messagesendsuccesslog(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tpmessagesendsuccesslog.html", locals()
        )


def view_messagetemplatecategkwkwory(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tpmessagetemplatecategkwkwory.html", locals()
        )


def view_messagetemplatetag(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpmessagetemplatetag.html", locals())


def view_userpermkwkwission(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpuserpermkwkwission.html", locals())


def view_systemconfig(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpsystemconfig.html", locals())


def view_notkwkwificationpush(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tpnotkwkwificationpush.html", locals()
        )


def view_messagequeue(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpmessagequeue.html", locals())


def view_messagequeuestatus(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpmessagequeuestatus.html", locals())


def view_messagerekwkwtryreckwkword(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tpmessagerekwkwtryreckwkword.html", locals()
        )


def view_accountblacklkwkwist(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tpaccountblacklkwkwist.html", locals()
        )


def view_userfeedback(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpuserfeedback.html", locals())


def view_accountsecuritylog(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpaccountsecuritylog.html", locals())


def view_messagetemplateedithkwkwistkwkwory(request):
    if request.method == "GET":
        return render(
            request,
            "config_visual/bi__tpmessagetemplateedithkwkwistkwkwory.html",
            locals(),
        )


def view_messagetemplatereviewreckwkword(request):
    if request.method == "GET":
        return render(
            request,
            "config_visual/bi__tpmessagetemplatereviewreckwkword.html",
            locals(),
        )


def view_messagesendstrategy(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpmessagesendstrategy.html", locals())


def view_messagesendfrequencylimit(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tpmessagesendfrequencylimit.html", locals()
        )


def view_messagesendprikwkwority(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tpmessagesendprikwkwority.html", locals()
        )


def view_messagetemplateusagestatkwkwistics(request):
    if request.method == "GET":
        return render(
            request,
            "config_visual/bi__tpmessagetemplateusagestatkwkwistics.html",
            locals(),
        )


def view_supermanager(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpsupermanager.html", locals())
