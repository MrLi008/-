from datetime import datetime
import os
import time
import uuid

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import login_required
from .form import *
from .models import *
from appcenter.models import *
from sys_user.func import *


def resp(res, msg, url=None, **kwargs):
    return {"res": res, "msg": msg, "url": url, **kwargs}


# Create your views here.


def index(request):
    records = [
        {
            "id": 1,
        },
        {"id": 2},
    ]
    return render(request, "config_visual/index.html", locals())


@login_required
def view_userinfo(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 用户信息表 系统管理员(7895)

    if user_table_id == str(7895):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 用户ID唯一标识

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户名用户登录名或昵称

        mcauthfield_username = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 密码哈希存储加密后的密码

        mcauthfield_pkwkwasswkwkwordhkwkwash = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 电子邮件用户邮箱地址

        mcauthfield_email = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 手机号码用户联系电话

        mcauthfield_phonenumber = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 注册时间用户注册时的日期和时间

        mcauthfield_regkwkwistertime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后登录时间用户最后一次登录的日期和时间

        mcauthfield_lkwkwastlogkwkwintime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户状态如活跃、禁用等

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 头像URL用户头像图片的存储地址

        mcauthfield_avatarurl = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 角色ID关联到角色的ID示用户所属的角色

        mcauthfield_roleid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 用户信息表 用户信息表(7864)

    if user_table_id == str(7864):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 用户ID唯一标识

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户名用户登录名或昵称

        mcauthfield_username = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 密码哈希存储加密后的密码

        mcauthfield_pkwkwasswkwkwordhkwkwash = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 电子邮件用户邮箱地址

        mcauthfield_email = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 手机号码用户联系电话

        mcauthfield_phonenumber = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 注册时间用户注册时的日期和时间

        mcauthfield_regkwkwistertime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后登录时间用户最后一次登录的日期和时间

        mcauthfield_lkwkwastlogkwkwintime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户状态如活跃、禁用等

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 头像URL用户头像图片的存储地址

        mcauthfield_avatarurl = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 角色ID关联到角色的ID示用户所属的角色

        mcauthfield_roleid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_userinfo.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_userinfo().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_userinfo.objects.filter(**filter)
        else:
            records = mc_userinfo.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_userinfo_53075 = []
        for m in mc_userinfo.objects.all():
            mobj = m.toJson()
            data_mc_userinfo_53075.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("roleid"),
                }
            )
        return render(request, "config_busi/userinfo.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_userinfo()

        # 用户ID唯一标识

        if mcauthfield_userid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.userid = str(uuid.uuid4())
        # 用户名用户登录名或昵称

        if mcauthfield_username["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.username = obj.get("username")
        # 密码哈希存储加密后的密码

        if mcauthfield_pkwkwasswkwkwordhkwkwash["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.pkwkwasswkwkwordhkwkwash = obj.get(
                "pkwkwasswkwkwordhkwkwash"
            )
        # 电子邮件用户邮箱地址

        if mcauthfield_email["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.email = obj.get("email")
        # 手机号码用户联系电话

        if mcauthfield_phonenumber["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.phonenumber = obj.get("phonenumber")
        # 注册时间用户注册时的日期和时间

        if mcauthfield_regkwkwistertime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.regkwkwistertime = obj.get("regkwkwistertime")
        # 最后登录时间用户最后一次登录的日期和时间

        if mcauthfield_lkwkwastlogkwkwintime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.lkwkwastlogkwkwintime = obj.get("lkwkwastlogkwkwintime")
        # 用户状态如活跃、禁用等

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        # 头像URL用户头像图片的存储地址

        if mcauthfield_avatarurl["mcauthchange"]:

            # Save FileImageField 若上传了文件

            if "avatarurl" in request.FILES:
                ins_table_busi.avatarurl = request.FILES["avatarurl"]
        # 角色ID关联到角色的ID示用户所属的角色

        if mcauthfield_roleid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.roleid = obj.get("roleid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_userinfo.objects.get(id=obj.get("_id_upd"))

        # 用户ID唯一标识

        if mcauthfield_userid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.userid = str(uuid.uuid4())

            ins_table_busi.userid = str(ins_table_busi.userid)
        # 用户名用户登录名或昵称

        if mcauthfield_username["mcauthchange"]:

            # CharField

            ins_table_busi.username = obj.get("username")
        # 密码哈希存储加密后的密码

        if mcauthfield_pkwkwasswkwkwordhkwkwash["mcauthchange"]:

            # CharField

            ins_table_busi.pkwkwasswkwkwordhkwkwash = obj.get(
                "pkwkwasswkwkwordhkwkwash"
            )
        # 电子邮件用户邮箱地址

        if mcauthfield_email["mcauthchange"]:

            # TextField

            ins_table_busi.email = obj.get("email")
        # 手机号码用户联系电话

        if mcauthfield_phonenumber["mcauthchange"]:

            # CharField

            ins_table_busi.phonenumber = obj.get("phonenumber")
        # 注册时间用户注册时的日期和时间

        if mcauthfield_regkwkwistertime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.regkwkwistertime = obj.get("regkwkwistertime")
        # 最后登录时间用户最后一次登录的日期和时间

        if mcauthfield_lkwkwastlogkwkwintime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.lkwkwastlogkwkwintime = obj.get("lkwkwastlogkwkwintime")
        # 用户状态如活跃、禁用等

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        # 头像URL用户头像图片的存储地址

        if mcauthfield_avatarurl["mcauthchange"]:

            # Save File ImageField

            if "avatarurl" in request.FILES:
                ins_table_busi.avatarurl = request.FILES["avatarurl"]
        # 角色ID关联到角色的ID示用户所属的角色

        if mcauthfield_roleid["mcauthchange"]:

            # SelectField

            ins_table_busi.roleid = obj.get("roleid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_userinfo.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_userinfo.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/userinfo")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_platkwkwfkwkwormaccount(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 平台账号表 系统管理员(7895)

    if user_table_id == str(7895):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 平台ID

        mcauthfield_platkwkwfkwkwormid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 账号名称

        mcauthfield_accountname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 账号类型

        mcauthfield_accounttype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 所属平台名称

        mcauthfield_platkwkwfkwkwormname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户名

        mcauthfield_username = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 密码加密存储

        mcauthfield_pkwkwasswkwkword = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 访问令牌

        mcauthfield_accesstoken = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 账号状态如启用、禁用

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后登录时间

        mcauthfield_lkwkwastlogkwkwintime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联用户ID如果有用户与账号关联

        mcauthfield_kwkwassociateduserid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 平台账号表 用户信息表(7864)

    if user_table_id == str(7864):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 平台ID

        mcauthfield_platkwkwfkwkwormid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 账号名称

        mcauthfield_accountname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 账号类型

        mcauthfield_accounttype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 所属平台名称

        mcauthfield_platkwkwfkwkwormname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户名

        mcauthfield_username = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 密码加密存储

        mcauthfield_pkwkwasswkwkword = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 访问令牌

        mcauthfield_accesstoken = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 账号状态如启用、禁用

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后登录时间

        mcauthfield_lkwkwastlogkwkwintime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联用户ID如果有用户与账号关联

        mcauthfield_kwkwassociateduserid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_platkwkwfkwkwormaccount.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_platkwkwfkwkwormaccount().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_platkwkwfkwkwormaccount.objects.filter(**filter)
        else:
            records = mc_platkwkwfkwkwormaccount.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_userinfo_53087 = []
        for m in mc_userinfo.objects.all():
            mobj = m.toJson()
            data_mc_userinfo_53087.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        return render(request, "config_busi/platkwkwfkwkwormaccount.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_platkwkwfkwkwormaccount()

        # 平台ID

        if mcauthfield_platkwkwfkwkwormid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.platkwkwfkwkwormid = str(uuid.uuid4())
        # 账号名称

        if mcauthfield_accountname["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.accountname = obj.get("accountname")
        # 账号类型

        if mcauthfield_accounttype["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.accounttype = obj.get("accounttype")
        # 所属平台名称

        if mcauthfield_platkwkwfkwkwormname["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.platkwkwfkwkwormname = obj.get("platkwkwfkwkwormname")
        # 用户名

        if mcauthfield_username["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.username = obj.get("username")
        # 密码加密存储

        if mcauthfield_pkwkwasswkwkword["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.pkwkwasswkwkword = obj.get("pkwkwasswkwkword")
        # 访问令牌

        if mcauthfield_accesstoken["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.accesstoken = obj.get("accesstoken")
        # 账号状态如启用、禁用

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        # 最后登录时间

        if mcauthfield_lkwkwastlogkwkwintime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.lkwkwastlogkwkwintime = obj.get("lkwkwastlogkwkwintime")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatedat = obj.get("updatedat")
        # 关联用户ID如果有用户与账号关联

        if mcauthfield_kwkwassociateduserid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.kwkwassociateduserid = obj.get("kwkwassociateduserid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_platkwkwfkwkwormaccount.objects.get(id=obj.get("_id_upd"))

        # 平台ID

        if mcauthfield_platkwkwfkwkwormid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.platkwkwfkwkwormid = str(uuid.uuid4())

            ins_table_busi.platkwkwfkwkwormid = str(ins_table_busi.platkwkwfkwkwormid)
        # 账号名称

        if mcauthfield_accountname["mcauthchange"]:

            # CharField

            ins_table_busi.accountname = obj.get("accountname")
        # 账号类型

        if mcauthfield_accounttype["mcauthchange"]:

            # CharField

            ins_table_busi.accounttype = obj.get("accounttype")
        # 所属平台名称

        if mcauthfield_platkwkwfkwkwormname["mcauthchange"]:

            # CharField

            ins_table_busi.platkwkwfkwkwormname = obj.get("platkwkwfkwkwormname")
        # 用户名

        if mcauthfield_username["mcauthchange"]:

            # CharField

            ins_table_busi.username = obj.get("username")
        # 密码加密存储

        if mcauthfield_pkwkwasswkwkword["mcauthchange"]:

            # CharField

            ins_table_busi.pkwkwasswkwkword = obj.get("pkwkwasswkwkword")
        # 访问令牌

        if mcauthfield_accesstoken["mcauthchange"]:

            # CharField

            ins_table_busi.accesstoken = obj.get("accesstoken")
        # 账号状态如启用、禁用

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        # 最后登录时间

        if mcauthfield_lkwkwastlogkwkwintime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.lkwkwastlogkwkwintime = obj.get("lkwkwastlogkwkwintime")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatedat = obj.get("updatedat")
        # 关联用户ID如果有用户与账号关联

        if mcauthfield_kwkwassociateduserid["mcauthchange"]:

            # SelectField

            ins_table_busi.kwkwassociateduserid = obj.get("kwkwassociateduserid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_platkwkwfkwkwormaccount.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_platkwkwfkwkwormaccount.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/platkwkwfkwkwormaccount")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_messagetemplate(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 私信模板表 系统管理员(7895)

    if user_table_id == str(7895):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 模板ID

        mcauthfield_templateid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 模板名称

        mcauthfield_templatename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 模板内容

        mcauthfield_templatecontent = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者ID

        mcauthfield_creatkwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活

        mcauthfield_kwkwisactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 平台类型

        mcauthfield_platkwkwfkwkwormtype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 目标用户ID可选用于指定特定用户

        mcauthfield_targetuserid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 私信模板表 用户信息表(7864)

    if user_table_id == str(7864):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 模板ID

        mcauthfield_templateid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 模板名称

        mcauthfield_templatename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 模板内容

        mcauthfield_templatecontent = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者ID

        mcauthfield_creatkwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活

        mcauthfield_kwkwisactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 平台类型

        mcauthfield_platkwkwfkwkwormtype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 目标用户ID可选用于指定特定用户

        mcauthfield_targetuserid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_messagetemplate.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_messagetemplate().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_messagetemplate.objects.filter(**filter)
        else:
            records = mc_messagetemplate.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/messagetemplate.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_messagetemplate()

        # 模板ID

        if mcauthfield_templateid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.templateid = str(uuid.uuid4())
        # 模板名称

        if mcauthfield_templatename["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.templatename = obj.get("templatename")
        # 模板内容

        if mcauthfield_templatecontent["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.templatecontent = obj.get("templatecontent")
        # 创建者ID

        if mcauthfield_creatkwkworid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.creatkwkworid = str(uuid.uuid4())
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createtime = obj.get("createtime")
        # 更新时间

        if mcauthfield_updatetime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatetime = obj.get("updatetime")
        # 是否激活

        if mcauthfield_kwkwisactive["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.kwkwisactive = obj.get("kwkwisactive")
        # 平台类型

        if mcauthfield_platkwkwfkwkwormtype["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.platkwkwfkwkwormtype = obj.get("platkwkwfkwkwormtype")
        # 目标用户ID可选用于指定特定用户

        if mcauthfield_targetuserid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.targetuserid = str(uuid.uuid4())
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_messagetemplate.objects.get(id=obj.get("_id_upd"))

        # 模板ID

        if mcauthfield_templateid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.templateid = str(uuid.uuid4())

            ins_table_busi.templateid = str(ins_table_busi.templateid)
        # 模板名称

        if mcauthfield_templatename["mcauthchange"]:

            # CharField

            ins_table_busi.templatename = obj.get("templatename")
        # 模板内容

        if mcauthfield_templatecontent["mcauthchange"]:

            # TextField

            ins_table_busi.templatecontent = obj.get("templatecontent")
        # 创建者ID

        if mcauthfield_creatkwkworid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.creatkwkworid = str(uuid.uuid4())

            ins_table_busi.creatkwkworid = str(ins_table_busi.creatkwkworid)
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createtime = obj.get("createtime")
        # 更新时间

        if mcauthfield_updatetime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatetime = obj.get("updatetime")
        # 是否激活

        if mcauthfield_kwkwisactive["mcauthchange"]:

            # BooleanField

            ins_table_busi.kwkwisactive = obj.get("kwkwisactive")
        # 平台类型

        if mcauthfield_platkwkwfkwkwormtype["mcauthchange"]:

            # CharField

            ins_table_busi.platkwkwfkwkwormtype = obj.get("platkwkwfkwkwormtype")
        # 目标用户ID可选用于指定特定用户

        if mcauthfield_targetuserid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.targetuserid = str(uuid.uuid4())

            ins_table_busi.targetuserid = str(ins_table_busi.targetuserid)
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_messagetemplate.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_messagetemplate.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/messagetemplate")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_tkwkwaskmanagement(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 任务管理表 系统管理员(7895)

    if user_table_id == str(7895):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 任务ID

        mcauthfield_tkwkwaskid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 任务名称

        mcauthfield_tkwkwaskname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 平台

        mcauthfield_platkwkwfkwkworm = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 目标用户ID

        mcauthfield_targetuserid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 私信内容

        mcauthfield_messagecontent = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 计划执行时间

        mcauthfield_scheduledtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 任务状态

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联用户ID如任务创建者

        mcauthfield_kwkwassociateduserid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 任务管理表 用户信息表(7864)

    if user_table_id == str(7864):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 任务ID

        mcauthfield_tkwkwaskid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 任务名称

        mcauthfield_tkwkwaskname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 平台

        mcauthfield_platkwkwfkwkworm = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 目标用户ID

        mcauthfield_targetuserid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 私信内容

        mcauthfield_messagecontent = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 计划执行时间

        mcauthfield_scheduledtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 任务状态

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联用户ID如任务创建者

        mcauthfield_kwkwassociateduserid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_tkwkwaskmanagement.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_tkwkwaskmanagement().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_tkwkwaskmanagement.objects.filter(**filter)
        else:
            records = mc_tkwkwaskmanagement.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_userinfo_53106 = []
        for m in mc_userinfo.objects.all():
            mobj = m.toJson()
            data_mc_userinfo_53106.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        return render(request, "config_busi/tkwkwaskmanagement.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_tkwkwaskmanagement()

        # 任务ID

        if mcauthfield_tkwkwaskid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.tkwkwaskid = str(uuid.uuid4())
        # 任务名称

        if mcauthfield_tkwkwaskname["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.tkwkwaskname = obj.get("tkwkwaskname")
        # 平台

        if mcauthfield_platkwkwfkwkworm["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.platkwkwfkwkworm = obj.get("platkwkwfkwkworm")
        # 目标用户ID

        if mcauthfield_targetuserid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.targetuserid = str(uuid.uuid4())
        # 私信内容

        if mcauthfield_messagecontent["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.messagecontent = obj.get("messagecontent")
        # 计划执行时间

        if mcauthfield_scheduledtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.scheduledtime = obj.get("scheduledtime")
        # 任务状态

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        # 创建时间

        if mcauthfield_createdtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createdtime = obj.get("createdtime")
        # 更新时间

        if mcauthfield_updatedtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatedtime = obj.get("updatedtime")
        # 关联用户ID如任务创建者

        if mcauthfield_kwkwassociateduserid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.kwkwassociateduserid = obj.get("kwkwassociateduserid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_tkwkwaskmanagement.objects.get(id=obj.get("_id_upd"))

        # 任务ID

        if mcauthfield_tkwkwaskid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.tkwkwaskid = str(uuid.uuid4())

            ins_table_busi.tkwkwaskid = str(ins_table_busi.tkwkwaskid)
        # 任务名称

        if mcauthfield_tkwkwaskname["mcauthchange"]:

            # CharField

            ins_table_busi.tkwkwaskname = obj.get("tkwkwaskname")
        # 平台

        if mcauthfield_platkwkwfkwkworm["mcauthchange"]:

            # CharField

            ins_table_busi.platkwkwfkwkworm = obj.get("platkwkwfkwkworm")
        # 目标用户ID

        if mcauthfield_targetuserid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.targetuserid = str(uuid.uuid4())

            ins_table_busi.targetuserid = str(ins_table_busi.targetuserid)
        # 私信内容

        if mcauthfield_messagecontent["mcauthchange"]:

            # TextField

            ins_table_busi.messagecontent = obj.get("messagecontent")
        # 计划执行时间

        if mcauthfield_scheduledtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.scheduledtime = obj.get("scheduledtime")
        # 任务状态

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        # 创建时间

        if mcauthfield_createdtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createdtime = obj.get("createdtime")
        # 更新时间

        if mcauthfield_updatedtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatedtime = obj.get("updatedtime")
        # 关联用户ID如任务创建者

        if mcauthfield_kwkwassociateduserid["mcauthchange"]:

            # SelectField

            ins_table_busi.kwkwassociateduserid = obj.get("kwkwassociateduserid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_tkwkwaskmanagement.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_tkwkwaskmanagement.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/tkwkwaskmanagement")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_tkwkwaskexecutionreckwkword(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 任务执行记录表 系统管理员(7895)

    if user_table_id == str(7895):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 任务ID

        mcauthfield_tkwkwaskid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 执行时间

        mcauthfield_executiontime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 执行状态

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 平台

        mcauthfield_platkwkwfkwkworm = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 私信内容

        mcauthfield_messagecontent = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 接收者ID

        mcauthfield_recipientid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 发送者ID

        mcauthfield_senderid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 任务模板ID

        mcauthfield_tkwkwasktemplateid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 错误信息

        mcauthfield_errkwkwormessage = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 任务执行记录表 用户信息表(7864)

    if user_table_id == str(7864):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 任务ID

        mcauthfield_tkwkwaskid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 执行时间

        mcauthfield_executiontime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 执行状态

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 平台

        mcauthfield_platkwkwfkwkworm = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 私信内容

        mcauthfield_messagecontent = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 接收者ID

        mcauthfield_recipientid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 发送者ID

        mcauthfield_senderid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 任务模板ID

        mcauthfield_tkwkwasktemplateid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 错误信息

        mcauthfield_errkwkwormessage = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_tkwkwaskexecutionreckwkword.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_tkwkwaskexecutionreckwkword().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_tkwkwaskexecutionreckwkword.objects.filter(**filter)
        else:
            records = mc_tkwkwaskexecutionreckwkword.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/tkwkwaskexecutionreckwkword.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_tkwkwaskexecutionreckwkword()

        # 任务ID

        if mcauthfield_tkwkwaskid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.tkwkwaskid = str(uuid.uuid4())
        # 执行时间

        if mcauthfield_executiontime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.executiontime = obj.get("executiontime")
        # 执行状态

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        # 用户ID

        if mcauthfield_userid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.userid = str(uuid.uuid4())
        # 平台

        if mcauthfield_platkwkwfkwkworm["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.platkwkwfkwkworm = obj.get("platkwkwfkwkworm")
        # 私信内容

        if mcauthfield_messagecontent["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.messagecontent = obj.get("messagecontent")
        # 接收者ID

        if mcauthfield_recipientid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.recipientid = str(uuid.uuid4())
        # 发送者ID

        if mcauthfield_senderid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.senderid = str(uuid.uuid4())
        # 任务模板ID

        if mcauthfield_tkwkwasktemplateid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.tkwkwasktemplateid = str(uuid.uuid4())
        # 错误信息

        if mcauthfield_errkwkwormessage["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.errkwkwormessage = obj.get("errkwkwormessage")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_tkwkwaskexecutionreckwkword.objects.get(
            id=obj.get("_id_upd")
        )

        # 任务ID

        if mcauthfield_tkwkwaskid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.tkwkwaskid = str(uuid.uuid4())

            ins_table_busi.tkwkwaskid = str(ins_table_busi.tkwkwaskid)
        # 执行时间

        if mcauthfield_executiontime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.executiontime = obj.get("executiontime")
        # 执行状态

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        # 用户ID

        if mcauthfield_userid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.userid = str(uuid.uuid4())

            ins_table_busi.userid = str(ins_table_busi.userid)
        # 平台

        if mcauthfield_platkwkwfkwkworm["mcauthchange"]:

            # CharField

            ins_table_busi.platkwkwfkwkworm = obj.get("platkwkwfkwkworm")
        # 私信内容

        if mcauthfield_messagecontent["mcauthchange"]:

            # TextField

            ins_table_busi.messagecontent = obj.get("messagecontent")
        # 接收者ID

        if mcauthfield_recipientid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.recipientid = str(uuid.uuid4())

            ins_table_busi.recipientid = str(ins_table_busi.recipientid)
        # 发送者ID

        if mcauthfield_senderid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.senderid = str(uuid.uuid4())

            ins_table_busi.senderid = str(ins_table_busi.senderid)
        # 任务模板ID

        if mcauthfield_tkwkwasktemplateid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.tkwkwasktemplateid = str(uuid.uuid4())

            ins_table_busi.tkwkwasktemplateid = str(ins_table_busi.tkwkwasktemplateid)
        # 错误信息

        if mcauthfield_errkwkwormessage["mcauthchange"]:

            # CharField

            ins_table_busi.errkwkwormessage = obj.get("errkwkwormessage")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_tkwkwaskexecutionreckwkword.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_tkwkwaskexecutionreckwkword.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/tkwkwaskexecutionreckwkword")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_tkwkwaskstatus(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 任务状态表 系统管理员(7895)

    if user_table_id == str(7895):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 任务ID

        mcauthfield_tkwkwaskid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 状态码

        mcauthfield_statuscode = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 状态名称

        mcauthfield_statusname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 完成时间

        mcauthfield_completedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 平台ID

        mcauthfield_platkwkwfkwkwormid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 私信内容

        mcauthfield_messagecontent = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活

        mcauthfield_kwkwisactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 任务状态表 用户信息表(7864)

    if user_table_id == str(7864):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 任务ID

        mcauthfield_tkwkwaskid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 状态码

        mcauthfield_statuscode = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 状态名称

        mcauthfield_statusname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 完成时间

        mcauthfield_completedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 平台ID

        mcauthfield_platkwkwfkwkwormid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 私信内容

        mcauthfield_messagecontent = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活

        mcauthfield_kwkwisactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_tkwkwaskstatus.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_tkwkwaskstatus().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_tkwkwaskstatus.objects.filter(**filter)
        else:
            records = mc_tkwkwaskstatus.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/tkwkwaskstatus.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_tkwkwaskstatus()

        # 任务ID

        if mcauthfield_tkwkwaskid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.tkwkwaskid = str(uuid.uuid4())
        # 状态码

        if mcauthfield_statuscode["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.statuscode = obj.get("statuscode")
        # 状态名称

        if mcauthfield_statusname["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.statusname = obj.get("statusname")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatedat = obj.get("updatedat")
        # 完成时间

        if mcauthfield_completedat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.completedat = obj.get("completedat")
        # 用户ID

        if mcauthfield_userid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.userid = str(uuid.uuid4())
        # 平台ID

        if mcauthfield_platkwkwfkwkwormid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.platkwkwfkwkwormid = str(uuid.uuid4())
        # 私信内容

        if mcauthfield_messagecontent["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.messagecontent = obj.get("messagecontent")
        # 是否激活

        if mcauthfield_kwkwisactive["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.kwkwisactive = obj.get("kwkwisactive")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_tkwkwaskstatus.objects.get(id=obj.get("_id_upd"))

        # 任务ID

        if mcauthfield_tkwkwaskid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.tkwkwaskid = str(uuid.uuid4())

            ins_table_busi.tkwkwaskid = str(ins_table_busi.tkwkwaskid)
        # 状态码

        if mcauthfield_statuscode["mcauthchange"]:

            # CharField

            ins_table_busi.statuscode = obj.get("statuscode")
        # 状态名称

        if mcauthfield_statusname["mcauthchange"]:

            # CharField

            ins_table_busi.statusname = obj.get("statusname")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatedat = obj.get("updatedat")
        # 完成时间

        if mcauthfield_completedat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.completedat = obj.get("completedat")
        # 用户ID

        if mcauthfield_userid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.userid = str(uuid.uuid4())

            ins_table_busi.userid = str(ins_table_busi.userid)
        # 平台ID

        if mcauthfield_platkwkwfkwkwormid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.platkwkwfkwkwormid = str(uuid.uuid4())

            ins_table_busi.platkwkwfkwkwormid = str(ins_table_busi.platkwkwfkwkwormid)
        # 私信内容

        if mcauthfield_messagecontent["mcauthchange"]:

            # TextField

            ins_table_busi.messagecontent = obj.get("messagecontent")
        # 是否激活

        if mcauthfield_kwkwisactive["mcauthchange"]:

            # BooleanField

            ins_table_busi.kwkwisactive = obj.get("kwkwisactive")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_tkwkwaskstatus.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_tkwkwaskstatus.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/tkwkwaskstatus")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_scheduledtkwkwask(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 定时任务表 系统管理员(7895)

    if user_table_id == str(7895):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 任务ID

        mcauthfield_tkwkwaskid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 任务名称

        mcauthfield_tkwkwaskname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 目标平台

        mcauthfield_targetplatkwkwfkwkworm = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 计划执行时间

        mcauthfield_scheduletime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 执行状态

        mcauthfield_executestatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最近一次错误信息

        mcauthfield_lkwkwasterrkwkwor = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者

        mcauthfield_creatkwkwor = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联用户ID

        mcauthfield_relateduserid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 定时任务表 用户信息表(7864)

    if user_table_id == str(7864):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 任务ID

        mcauthfield_tkwkwaskid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 任务名称

        mcauthfield_tkwkwaskname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 目标平台

        mcauthfield_targetplatkwkwfkwkworm = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 计划执行时间

        mcauthfield_scheduletime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 执行状态

        mcauthfield_executestatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最近一次错误信息

        mcauthfield_lkwkwasterrkwkwor = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者

        mcauthfield_creatkwkwor = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联用户ID

        mcauthfield_relateduserid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_scheduledtkwkwask.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_scheduledtkwkwask().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_scheduledtkwkwask.objects.filter(**filter)
        else:
            records = mc_scheduledtkwkwask.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_userinfo_53136 = []
        for m in mc_userinfo.objects.all():
            mobj = m.toJson()
            data_mc_userinfo_53136.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        return render(request, "config_busi/scheduledtkwkwask.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_scheduledtkwkwask()

        # 任务ID

        if mcauthfield_tkwkwaskid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.tkwkwaskid = str(uuid.uuid4())
        # 任务名称

        if mcauthfield_tkwkwaskname["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.tkwkwaskname = obj.get("tkwkwaskname")
        # 目标平台

        if mcauthfield_targetplatkwkwfkwkworm["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.targetplatkwkwfkwkworm = obj.get("targetplatkwkwfkwkworm")
        # 计划执行时间

        if mcauthfield_scheduletime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.scheduletime = obj.get("scheduletime")
        # 执行状态

        if mcauthfield_executestatus["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.executestatus = obj.get("executestatus")
        # 最近一次错误信息

        if mcauthfield_lkwkwasterrkwkwor["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.lkwkwasterrkwkwor = obj.get("lkwkwasterrkwkwor")
        # 创建者

        if mcauthfield_creatkwkwor["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.creatkwkwor = obj.get("creatkwkwor")
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createtime = obj.get("createtime")
        # 更新时间

        if mcauthfield_updatetime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatetime = obj.get("updatetime")
        # 关联用户ID

        if mcauthfield_relateduserid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.relateduserid = obj.get("relateduserid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_scheduledtkwkwask.objects.get(id=obj.get("_id_upd"))

        # 任务ID

        if mcauthfield_tkwkwaskid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.tkwkwaskid = str(uuid.uuid4())

            ins_table_busi.tkwkwaskid = str(ins_table_busi.tkwkwaskid)
        # 任务名称

        if mcauthfield_tkwkwaskname["mcauthchange"]:

            # CharField

            ins_table_busi.tkwkwaskname = obj.get("tkwkwaskname")
        # 目标平台

        if mcauthfield_targetplatkwkwfkwkworm["mcauthchange"]:

            # CharField

            ins_table_busi.targetplatkwkwfkwkworm = obj.get("targetplatkwkwfkwkworm")
        # 计划执行时间

        if mcauthfield_scheduletime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.scheduletime = obj.get("scheduletime")
        # 执行状态

        if mcauthfield_executestatus["mcauthchange"]:

            # CharField

            ins_table_busi.executestatus = obj.get("executestatus")
        # 最近一次错误信息

        if mcauthfield_lkwkwasterrkwkwor["mcauthchange"]:

            # CharField

            ins_table_busi.lkwkwasterrkwkwor = obj.get("lkwkwasterrkwkwor")
        # 创建者

        if mcauthfield_creatkwkwor["mcauthchange"]:

            # CharField

            ins_table_busi.creatkwkwor = obj.get("creatkwkwor")
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createtime = obj.get("createtime")
        # 更新时间

        if mcauthfield_updatetime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatetime = obj.get("updatetime")
        # 关联用户ID

        if mcauthfield_relateduserid["mcauthchange"]:

            # SelectField

            ins_table_busi.relateduserid = obj.get("relateduserid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_scheduledtkwkwask.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_scheduledtkwkwask.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/scheduledtkwkwask")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_messagesendreckwkword(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 消息发送记录表 系统管理员(7895)

    if user_table_id == str(7895):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 平台ID关联字段指向不同社交媒体或消息平台的ID

        mcauthfield_platkwkwfkwkwormid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户ID关联字段指向系统中用户的ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 目标用户ID如果是私信则为目标接收者的ID

        mcauthfield_targetuserid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 消息内容

        mcauthfield_messagecontent = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 发送时间

        mcauthfield_sendtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 发送状态如待发送、发送中、已发送、发送失败

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 重试次数记录消息发送失败后的重试次数

        mcauthfield_rekwkwtrycount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 上次重试时间记录最后一次尝试发送的时间

        mcauthfield_lkwkwastrekwkwtrytime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 错误信息如果发送失败记录失败的具体原因

        mcauthfield_errkwkwormessage = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 消息发送记录表 用户信息表(7864)

    if user_table_id == str(7864):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 平台ID关联字段指向不同社交媒体或消息平台的ID

        mcauthfield_platkwkwfkwkwormid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户ID关联字段指向系统中用户的ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 目标用户ID如果是私信则为目标接收者的ID

        mcauthfield_targetuserid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 消息内容

        mcauthfield_messagecontent = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 发送时间

        mcauthfield_sendtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 发送状态如待发送、发送中、已发送、发送失败

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 重试次数记录消息发送失败后的重试次数

        mcauthfield_rekwkwtrycount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 上次重试时间记录最后一次尝试发送的时间

        mcauthfield_lkwkwastrekwkwtrytime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 错误信息如果发送失败记录失败的具体原因

        mcauthfield_errkwkwormessage = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_messagesendreckwkword.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_messagesendreckwkword().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_messagesendreckwkword.objects.filter(**filter)
        else:
            records = mc_messagesendreckwkword.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_platkwkwfkwkwormaccount_53138 = []
        for m in mc_platkwkwfkwkwormaccount.objects.all():
            mobj = m.toJson()
            data_mc_platkwkwfkwkwormaccount_53138.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("accountname"),
                }
            )
        data_mc_userinfo_53139 = []
        for m in mc_userinfo.objects.all():
            mobj = m.toJson()
            data_mc_userinfo_53139.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        return render(request, "config_busi/messagesendreckwkword.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_messagesendreckwkword()

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 平台ID关联字段指向不同社交媒体或消息平台的ID

        if mcauthfield_platkwkwfkwkwormid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.platkwkwfkwkwormid = obj.get("platkwkwfkwkwormid")
        # 用户ID关联字段指向系统中用户的ID

        if mcauthfield_userid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.userid = obj.get("userid")
        # 目标用户ID如果是私信则为目标接收者的ID

        if mcauthfield_targetuserid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.targetuserid = str(uuid.uuid4())
        # 消息内容

        if mcauthfield_messagecontent["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.messagecontent = obj.get("messagecontent")
        # 发送时间

        if mcauthfield_sendtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.sendtime = obj.get("sendtime")
        # 发送状态如待发送、发送中、已发送、发送失败

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        # 重试次数记录消息发送失败后的重试次数

        if mcauthfield_rekwkwtrycount["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.rekwkwtrycount = obj.get("rekwkwtrycount")
        # 上次重试时间记录最后一次尝试发送的时间

        if mcauthfield_lkwkwastrekwkwtrytime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.lkwkwastrekwkwtrytime = obj.get("lkwkwastrekwkwtrytime")
        # 错误信息如果发送失败记录失败的具体原因

        if mcauthfield_errkwkwormessage["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.errkwkwormessage = obj.get("errkwkwormessage")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_messagesendreckwkword.objects.get(id=obj.get("_id_upd"))

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 平台ID关联字段指向不同社交媒体或消息平台的ID

        if mcauthfield_platkwkwfkwkwormid["mcauthchange"]:

            # SelectField

            ins_table_busi.platkwkwfkwkwormid = obj.get("platkwkwfkwkwormid")
        # 用户ID关联字段指向系统中用户的ID

        if mcauthfield_userid["mcauthchange"]:

            # SelectField

            ins_table_busi.userid = obj.get("userid")
        # 目标用户ID如果是私信则为目标接收者的ID

        if mcauthfield_targetuserid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.targetuserid = str(uuid.uuid4())

            ins_table_busi.targetuserid = str(ins_table_busi.targetuserid)
        # 消息内容

        if mcauthfield_messagecontent["mcauthchange"]:

            # TextField

            ins_table_busi.messagecontent = obj.get("messagecontent")
        # 发送时间

        if mcauthfield_sendtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.sendtime = obj.get("sendtime")
        # 发送状态如待发送、发送中、已发送、发送失败

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        # 重试次数记录消息发送失败后的重试次数

        if mcauthfield_rekwkwtrycount["mcauthchange"]:

            # CharField

            ins_table_busi.rekwkwtrycount = obj.get("rekwkwtrycount")
        # 上次重试时间记录最后一次尝试发送的时间

        if mcauthfield_lkwkwastrekwkwtrytime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.lkwkwastrekwkwtrytime = obj.get("lkwkwastrekwkwtrytime")
        # 错误信息如果发送失败记录失败的具体原因

        if mcauthfield_errkwkwormessage["mcauthchange"]:

            # CharField

            ins_table_busi.errkwkwormessage = obj.get("errkwkwormessage")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_messagesendreckwkword.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_messagesendreckwkword.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/messagesendreckwkword")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_messagereceivereckwkword(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 消息接收记录表 系统管理员(7895)

    if user_table_id == str(7895):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户ID关联用户

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 平台ID关联平台

        mcauthfield_platkwkwfkwkwormid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 消息内容

        mcauthfield_messagecontent = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 接收时间

        mcauthfield_receivetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 接收状态如已接收、未处理、已处理等

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 回复内容

        mcauthfield_responsecontent = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 回复时间

        mcauthfield_responsetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否已读示用户是否已读该消息

        mcauthfield_kwkwisread = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 消息接收记录表 用户信息表(7864)

    if user_table_id == str(7864):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户ID关联用户

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 平台ID关联平台

        mcauthfield_platkwkwfkwkwormid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 消息内容

        mcauthfield_messagecontent = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 接收时间

        mcauthfield_receivetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 接收状态如已接收、未处理、已处理等

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 回复内容

        mcauthfield_responsecontent = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 回复时间

        mcauthfield_responsetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否已读示用户是否已读该消息

        mcauthfield_kwkwisread = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_messagereceivereckwkword.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_messagereceivereckwkword().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_messagereceivereckwkword.objects.filter(**filter)
        else:
            records = mc_messagereceivereckwkword.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_userinfo_53148 = []
        for m in mc_userinfo.objects.all():
            mobj = m.toJson()
            data_mc_userinfo_53148.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        data_mc_platkwkwfkwkwormaccount_53149 = []
        for m in mc_platkwkwfkwkwormaccount.objects.all():
            mobj = m.toJson()
            data_mc_platkwkwfkwkwormaccount_53149.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("accountname"),
                }
            )
        return render(request, "config_busi/messagereceivereckwkword.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_messagereceivereckwkword()

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 用户ID关联用户

        if mcauthfield_userid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.userid = obj.get("userid")
        # 平台ID关联平台

        if mcauthfield_platkwkwfkwkwormid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.platkwkwfkwkwormid = obj.get("platkwkwfkwkwormid")
        # 消息内容

        if mcauthfield_messagecontent["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.messagecontent = obj.get("messagecontent")
        # 接收时间

        if mcauthfield_receivetime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.receivetime = obj.get("receivetime")
        # 接收状态如已接收、未处理、已处理等

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        # 回复内容

        if mcauthfield_responsecontent["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.responsecontent = obj.get("responsecontent")
        # 回复时间

        if mcauthfield_responsetime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.responsetime = obj.get("responsetime")
        # 是否已读示用户是否已读该消息

        if mcauthfield_kwkwisread["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.kwkwisread = obj.get("kwkwisread")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_messagereceivereckwkword.objects.get(id=obj.get("_id_upd"))

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 用户ID关联用户

        if mcauthfield_userid["mcauthchange"]:

            # SelectField

            ins_table_busi.userid = obj.get("userid")
        # 平台ID关联平台

        if mcauthfield_platkwkwfkwkwormid["mcauthchange"]:

            # SelectField

            ins_table_busi.platkwkwfkwkwormid = obj.get("platkwkwfkwkwormid")
        # 消息内容

        if mcauthfield_messagecontent["mcauthchange"]:

            # TextField

            ins_table_busi.messagecontent = obj.get("messagecontent")
        # 接收时间

        if mcauthfield_receivetime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.receivetime = obj.get("receivetime")
        # 接收状态如已接收、未处理、已处理等

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        # 回复内容

        if mcauthfield_responsecontent["mcauthchange"]:

            # TextField

            ins_table_busi.responsecontent = obj.get("responsecontent")
        # 回复时间

        if mcauthfield_responsetime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.responsetime = obj.get("responsetime")
        # 是否已读示用户是否已读该消息

        if mcauthfield_kwkwisread["mcauthchange"]:

            # BooleanField

            ins_table_busi.kwkwisread = obj.get("kwkwisread")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_messagereceivereckwkword.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_messagereceivereckwkword.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/messagereceivereckwkword")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_userpreference(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 用户偏好设置表 系统管理员(7895)

    if user_table_id == str(7895):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 偏好名称

        mcauthfield_preferencename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 偏好值

        mcauthfield_preferencevalue = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 偏好类型

        mcauthfield_preferencetype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活

        mcauthfield_kwkwisactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 偏好描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联平台ID

        mcauthfield_platkwkwfkwkwormid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 用户偏好设置表 用户信息表(7864)

    if user_table_id == str(7864):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 偏好名称

        mcauthfield_preferencename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 偏好值

        mcauthfield_preferencevalue = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 偏好类型

        mcauthfield_preferencetype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活

        mcauthfield_kwkwisactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 偏好描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联平台ID

        mcauthfield_platkwkwfkwkwormid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_userpreference.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_userpreference().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_userpreference.objects.filter(**filter)
        else:
            records = mc_userpreference.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_platkwkwfkwkwormaccount_53164 = []
        for m in mc_platkwkwfkwkwormaccount.objects.all():
            mobj = m.toJson()
            data_mc_platkwkwfkwkwormaccount_53164.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("accountname"),
                }
            )
        return render(request, "config_busi/userpreference.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_userpreference()

        # 用户ID

        if mcauthfield_userid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.userid = str(uuid.uuid4())
        # 偏好名称

        if mcauthfield_preferencename["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.preferencename = obj.get("preferencename")
        # 偏好值

        if mcauthfield_preferencevalue["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.preferencevalue = obj.get("preferencevalue")
        # 偏好类型

        if mcauthfield_preferencetype["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.preferencetype = obj.get("preferencetype")
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createtime = obj.get("createtime")
        # 更新时间

        if mcauthfield_updatetime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatetime = obj.get("updatetime")
        # 是否激活

        if mcauthfield_kwkwisactive["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.kwkwisactive = obj.get("kwkwisactive")
        # 偏好描述

        if mcauthfield_description["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.description = obj.get("description")
        # 关联平台ID

        if mcauthfield_platkwkwfkwkwormid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.platkwkwfkwkwormid = obj.get("platkwkwfkwkwormid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_userpreference.objects.get(id=obj.get("_id_upd"))

        # 用户ID

        if mcauthfield_userid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.userid = str(uuid.uuid4())

            ins_table_busi.userid = str(ins_table_busi.userid)
        # 偏好名称

        if mcauthfield_preferencename["mcauthchange"]:

            # CharField

            ins_table_busi.preferencename = obj.get("preferencename")
        # 偏好值

        if mcauthfield_preferencevalue["mcauthchange"]:

            # CharField

            ins_table_busi.preferencevalue = obj.get("preferencevalue")
        # 偏好类型

        if mcauthfield_preferencetype["mcauthchange"]:

            # CharField

            ins_table_busi.preferencetype = obj.get("preferencetype")
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createtime = obj.get("createtime")
        # 更新时间

        if mcauthfield_updatetime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatetime = obj.get("updatetime")
        # 是否激活

        if mcauthfield_kwkwisactive["mcauthchange"]:

            # BooleanField

            ins_table_busi.kwkwisactive = obj.get("kwkwisactive")
        # 偏好描述

        if mcauthfield_description["mcauthchange"]:

            # TextField

            ins_table_busi.description = obj.get("description")
        # 关联平台ID

        if mcauthfield_platkwkwfkwkwormid["mcauthchange"]:

            # SelectField

            ins_table_busi.platkwkwfkwkwormid = obj.get("platkwkwfkwkwormid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_userpreference.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_userpreference.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/userpreference")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_accountbkwkwindkwkwing(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 账号绑定关系表 系统管理员(7895)

    if user_table_id == str(7895):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 账号ID

        mcauthfield_accountid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 平台ID

        mcauthfield_platkwkwfkwkwormid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 绑定类型

        mcauthfield_bkwkwindkwkwingtype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 绑定状态

        mcauthfield_bkwkwindkwkwingstatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 账号绑定关系表 用户信息表(7864)

    if user_table_id == str(7864):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 账号ID

        mcauthfield_accountid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 平台ID

        mcauthfield_platkwkwfkwkwormid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 绑定类型

        mcauthfield_bkwkwindkwkwingtype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 绑定状态

        mcauthfield_bkwkwindkwkwingstatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_accountbkwkwindkwkwing.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_accountbkwkwindkwkwing().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_accountbkwkwindkwkwing.objects.filter(**filter)
        else:
            records = mc_accountbkwkwindkwkwing.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/accountbkwkwindkwkwing.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_accountbkwkwindkwkwing()

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 账号ID

        if mcauthfield_accountid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.accountid = str(uuid.uuid4())
        # 平台ID

        if mcauthfield_platkwkwfkwkwormid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.platkwkwfkwkwormid = str(uuid.uuid4())
        # 绑定类型

        if mcauthfield_bkwkwindkwkwingtype["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.bkwkwindkwkwingtype = obj.get("bkwkwindkwkwingtype")
        # 绑定状态

        if mcauthfield_bkwkwindkwkwingstatus["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.bkwkwindkwkwingstatus = obj.get("bkwkwindkwkwingstatus")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatedat = obj.get("updatedat")
        # 用户ID

        if mcauthfield_userid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.userid = str(uuid.uuid4())
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_accountbkwkwindkwkwing.objects.get(id=obj.get("_id_upd"))

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 账号ID

        if mcauthfield_accountid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.accountid = str(uuid.uuid4())

            ins_table_busi.accountid = str(ins_table_busi.accountid)
        # 平台ID

        if mcauthfield_platkwkwfkwkwormid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.platkwkwfkwkwormid = str(uuid.uuid4())

            ins_table_busi.platkwkwfkwkwormid = str(ins_table_busi.platkwkwfkwkwormid)
        # 绑定类型

        if mcauthfield_bkwkwindkwkwingtype["mcauthchange"]:

            # CharField

            ins_table_busi.bkwkwindkwkwingtype = obj.get("bkwkwindkwkwingtype")
        # 绑定状态

        if mcauthfield_bkwkwindkwkwingstatus["mcauthchange"]:

            # CharField

            ins_table_busi.bkwkwindkwkwingstatus = obj.get("bkwkwindkwkwingstatus")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatedat = obj.get("updatedat")
        # 用户ID

        if mcauthfield_userid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.userid = str(uuid.uuid4())

            ins_table_busi.userid = str(ins_table_busi.userid)
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_accountbkwkwindkwkwing.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_accountbkwkwindkwkwing.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/accountbkwkwindkwkwing")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_messagecontentreview(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 消息内容审核表 系统管理员(7895)

    if user_table_id == str(7895):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 消息内容审核ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 消息内容

        mcauthfield_content = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 平台名称

        mcauthfield_platkwkwfkwkworm = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 审核状态

        mcauthfield_reviewstatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 审核时间

        mcauthfield_reviewtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 审核员ID

        mcauthfield_reviewerid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 拒绝原因

        mcauthfield_rejectionrekwkwason = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否敏感内容

        mcauthfield_kwkwissensitive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 消息内容审核表 用户信息表(7864)

    if user_table_id == str(7864):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 消息内容审核ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 消息内容

        mcauthfield_content = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 平台名称

        mcauthfield_platkwkwfkwkworm = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 审核状态

        mcauthfield_reviewstatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 审核时间

        mcauthfield_reviewtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 审核员ID

        mcauthfield_reviewerid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 拒绝原因

        mcauthfield_rejectionrekwkwason = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否敏感内容

        mcauthfield_kwkwissensitive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_messagecontentreview.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_messagecontentreview().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_messagecontentreview.objects.filter(**filter)
        else:
            records = mc_messagecontentreview.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/messagecontentreview.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_messagecontentreview()

        # 消息内容审核ID

        if mcauthfield_id["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 消息内容

        if mcauthfield_content["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.content = obj.get("content")
        # 用户ID

        if mcauthfield_userid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.userid = str(uuid.uuid4())
        # 平台名称

        if mcauthfield_platkwkwfkwkworm["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.platkwkwfkwkworm = obj.get("platkwkwfkwkworm")
        # 审核状态

        if mcauthfield_reviewstatus["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.reviewstatus = obj.get("reviewstatus")
        # 审核时间

        if mcauthfield_reviewtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.reviewtime = obj.get("reviewtime")
        # 审核员ID

        if mcauthfield_reviewerid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.reviewerid = str(uuid.uuid4())
        # 拒绝原因

        if mcauthfield_rejectionrekwkwason["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.rejectionrekwkwason = obj.get("rejectionrekwkwason")
        # 是否敏感内容

        if mcauthfield_kwkwissensitive["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.kwkwissensitive = obj.get("kwkwissensitive")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createdat = obj.get("createdat")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_messagecontentreview.objects.get(id=obj.get("_id_upd"))

        # 消息内容审核ID

        if mcauthfield_id["mcauthchange"]:

            # TextField

            ins_table_busi.id = obj.get("id")
        # 消息内容

        if mcauthfield_content["mcauthchange"]:

            # TextField

            ins_table_busi.content = obj.get("content")
        # 用户ID

        if mcauthfield_userid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.userid = str(uuid.uuid4())

            ins_table_busi.userid = str(ins_table_busi.userid)
        # 平台名称

        if mcauthfield_platkwkwfkwkworm["mcauthchange"]:

            # CharField

            ins_table_busi.platkwkwfkwkworm = obj.get("platkwkwfkwkworm")
        # 审核状态

        if mcauthfield_reviewstatus["mcauthchange"]:

            # CharField

            ins_table_busi.reviewstatus = obj.get("reviewstatus")
        # 审核时间

        if mcauthfield_reviewtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.reviewtime = obj.get("reviewtime")
        # 审核员ID

        if mcauthfield_reviewerid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.reviewerid = str(uuid.uuid4())

            ins_table_busi.reviewerid = str(ins_table_busi.reviewerid)
        # 拒绝原因

        if mcauthfield_rejectionrekwkwason["mcauthchange"]:

            # CharField

            ins_table_busi.rejectionrekwkwason = obj.get("rejectionrekwkwason")
        # 是否敏感内容

        if mcauthfield_kwkwissensitive["mcauthchange"]:

            # TextField

            ins_table_busi.kwkwissensitive = obj.get("kwkwissensitive")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createdat = obj.get("createdat")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_messagecontentreview.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_messagecontentreview.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/messagecontentreview")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_messagesendfailurelog(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 消息发送失败日志表 系统管理员(7895)

    if user_table_id == str(7895):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 消息ID

        mcauthfield_messageid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 平台名称

        mcauthfield_platkwkwfkwkworm = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 目标用户ID

        mcauthfield_targetuserid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 发送时间

        mcauthfield_sendtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 失败原因

        mcauthfield_failurerekwkwason = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 重试次数

        mcauthfield_rekwkwtrycount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 上次重试时间

        mcauthfield_lkwkwastrekwkwtrytime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否已解决

        mcauthfield_kwkwisresolved = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 消息发送失败日志表 用户信息表(7864)

    if user_table_id == str(7864):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 消息ID

        mcauthfield_messageid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 平台名称

        mcauthfield_platkwkwfkwkworm = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 目标用户ID

        mcauthfield_targetuserid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 发送时间

        mcauthfield_sendtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 失败原因

        mcauthfield_failurerekwkwason = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 重试次数

        mcauthfield_rekwkwtrycount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 上次重试时间

        mcauthfield_lkwkwastrekwkwtrytime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否已解决

        mcauthfield_kwkwisresolved = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_messagesendfailurelog.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_messagesendfailurelog().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_messagesendfailurelog.objects.filter(**filter)
        else:
            records = mc_messagesendfailurelog.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/messagesendfailurelog.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_messagesendfailurelog()

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 消息ID

        if mcauthfield_messageid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.messageid = str(uuid.uuid4())
        # 平台名称

        if mcauthfield_platkwkwfkwkworm["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.platkwkwfkwkworm = obj.get("platkwkwfkwkworm")
        # 用户ID

        if mcauthfield_userid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.userid = str(uuid.uuid4())
        # 目标用户ID

        if mcauthfield_targetuserid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.targetuserid = str(uuid.uuid4())
        # 发送时间

        if mcauthfield_sendtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.sendtime = obj.get("sendtime")
        # 失败原因

        if mcauthfield_failurerekwkwason["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.failurerekwkwason = obj.get("failurerekwkwason")
        # 重试次数

        if mcauthfield_rekwkwtrycount["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.rekwkwtrycount = obj.get("rekwkwtrycount")
        # 上次重试时间

        if mcauthfield_lkwkwastrekwkwtrytime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.lkwkwastrekwkwtrytime = obj.get("lkwkwastrekwkwtrytime")
        # 是否已解决

        if mcauthfield_kwkwisresolved["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.kwkwisresolved = obj.get("kwkwisresolved")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_messagesendfailurelog.objects.get(id=obj.get("_id_upd"))

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 消息ID

        if mcauthfield_messageid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.messageid = str(uuid.uuid4())

            ins_table_busi.messageid = str(ins_table_busi.messageid)
        # 平台名称

        if mcauthfield_platkwkwfkwkworm["mcauthchange"]:

            # CharField

            ins_table_busi.platkwkwfkwkworm = obj.get("platkwkwfkwkworm")
        # 用户ID

        if mcauthfield_userid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.userid = str(uuid.uuid4())

            ins_table_busi.userid = str(ins_table_busi.userid)
        # 目标用户ID

        if mcauthfield_targetuserid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.targetuserid = str(uuid.uuid4())

            ins_table_busi.targetuserid = str(ins_table_busi.targetuserid)
        # 发送时间

        if mcauthfield_sendtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.sendtime = obj.get("sendtime")
        # 失败原因

        if mcauthfield_failurerekwkwason["mcauthchange"]:

            # CharField

            ins_table_busi.failurerekwkwason = obj.get("failurerekwkwason")
        # 重试次数

        if mcauthfield_rekwkwtrycount["mcauthchange"]:

            # CharField

            ins_table_busi.rekwkwtrycount = obj.get("rekwkwtrycount")
        # 上次重试时间

        if mcauthfield_lkwkwastrekwkwtrytime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.lkwkwastrekwkwtrytime = obj.get("lkwkwastrekwkwtrytime")
        # 是否已解决

        if mcauthfield_kwkwisresolved["mcauthchange"]:

            # BooleanField

            ins_table_busi.kwkwisresolved = obj.get("kwkwisresolved")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_messagesendfailurelog.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_messagesendfailurelog.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/messagesendfailurelog")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_messagesendsuccesslog(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 消息发送成功日志表 系统管理员(7895)

    if user_table_id == str(7895):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 消息ID

        mcauthfield_messageid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 平台名称

        mcauthfield_platkwkwfkwkworm = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 接收者ID

        mcauthfield_receiverid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 发送时间

        mcauthfield_sendtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 发送内容

        mcauthfield_content = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 发送状态

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 错误信息

        mcauthfield_errkwkworkwkwinfo = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联任务ID

        mcauthfield_relatedtkwkwaskid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 消息发送成功日志表 用户信息表(7864)

    if user_table_id == str(7864):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 消息ID

        mcauthfield_messageid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 平台名称

        mcauthfield_platkwkwfkwkworm = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 接收者ID

        mcauthfield_receiverid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 发送时间

        mcauthfield_sendtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 发送内容

        mcauthfield_content = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 发送状态

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 错误信息

        mcauthfield_errkwkworkwkwinfo = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联任务ID

        mcauthfield_relatedtkwkwaskid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_messagesendsuccesslog.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_messagesendsuccesslog().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_messagesendsuccesslog.objects.filter(**filter)
        else:
            records = mc_messagesendsuccesslog.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_tkwkwaskmanagement_53201 = []
        for m in mc_tkwkwaskmanagement.objects.all():
            mobj = m.toJson()
            data_mc_tkwkwaskmanagement_53201.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("tkwkwaskname"),
                }
            )
        return render(request, "config_busi/messagesendsuccesslog.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_messagesendsuccesslog()

        # 消息ID

        if mcauthfield_messageid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.messageid = str(uuid.uuid4())
        # 平台名称

        if mcauthfield_platkwkwfkwkworm["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.platkwkwfkwkworm = obj.get("platkwkwfkwkworm")
        # 用户ID

        if mcauthfield_userid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.userid = str(uuid.uuid4())
        # 接收者ID

        if mcauthfield_receiverid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.receiverid = str(uuid.uuid4())
        # 发送时间

        if mcauthfield_sendtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.sendtime = obj.get("sendtime")
        # 发送内容

        if mcauthfield_content["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.content = obj.get("content")
        # 发送状态

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        # 错误信息

        if mcauthfield_errkwkworkwkwinfo["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.errkwkworkwkwinfo = obj.get("errkwkworkwkwinfo")
        # 关联任务ID

        if mcauthfield_relatedtkwkwaskid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.relatedtkwkwaskid = obj.get("relatedtkwkwaskid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_messagesendsuccesslog.objects.get(id=obj.get("_id_upd"))

        # 消息ID

        if mcauthfield_messageid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.messageid = str(uuid.uuid4())

            ins_table_busi.messageid = str(ins_table_busi.messageid)
        # 平台名称

        if mcauthfield_platkwkwfkwkworm["mcauthchange"]:

            # CharField

            ins_table_busi.platkwkwfkwkworm = obj.get("platkwkwfkwkworm")
        # 用户ID

        if mcauthfield_userid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.userid = str(uuid.uuid4())

            ins_table_busi.userid = str(ins_table_busi.userid)
        # 接收者ID

        if mcauthfield_receiverid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.receiverid = str(uuid.uuid4())

            ins_table_busi.receiverid = str(ins_table_busi.receiverid)
        # 发送时间

        if mcauthfield_sendtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.sendtime = obj.get("sendtime")
        # 发送内容

        if mcauthfield_content["mcauthchange"]:

            # TextField

            ins_table_busi.content = obj.get("content")
        # 发送状态

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        # 错误信息

        if mcauthfield_errkwkworkwkwinfo["mcauthchange"]:

            # CharField

            ins_table_busi.errkwkworkwkwinfo = obj.get("errkwkworkwkwinfo")
        # 关联任务ID

        if mcauthfield_relatedtkwkwaskid["mcauthchange"]:

            # SelectField

            ins_table_busi.relatedtkwkwaskid = obj.get("relatedtkwkwaskid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_messagesendsuccesslog.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_messagesendsuccesslog.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/messagesendsuccesslog")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_messagetemplatecategkwkwory(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 消息模板分类表 系统管理员(7895)

    if user_table_id == str(7895):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 分类名称

        mcauthfield_name = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 分类描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活用于控制分类是否可用

        mcauthfield_kwkwisactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 父级分类ID用于构建分类层级结构

        mcauthfield_parentid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 排序顺序用于控制分类在列中的显示顺序

        mcauthfield_skwkwortkwkworder = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 模板数量可选统计属于该分类的消息模板数量可通过触发器或应用逻辑维护

        mcauthfield_templatecount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 消息模板分类表 用户信息表(7864)

    if user_table_id == str(7864):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 分类名称

        mcauthfield_name = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 分类描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活用于控制分类是否可用

        mcauthfield_kwkwisactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 父级分类ID用于构建分类层级结构

        mcauthfield_parentid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 排序顺序用于控制分类在列中的显示顺序

        mcauthfield_skwkwortkwkworder = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 模板数量可选统计属于该分类的消息模板数量可通过触发器或应用逻辑维护

        mcauthfield_templatecount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_messagetemplatecategkwkwory.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_messagetemplatecategkwkwory().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_messagetemplatecategkwkwory.objects.filter(**filter)
        else:
            records = mc_messagetemplatecategkwkwory.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/messagetemplatecategkwkwory.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_messagetemplatecategkwkwory()

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 分类名称

        if mcauthfield_name["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.name = obj.get("name")
        # 分类描述

        if mcauthfield_description["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.description = obj.get("description")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatedat = obj.get("updatedat")
        # 是否激活用于控制分类是否可用

        if mcauthfield_kwkwisactive["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.kwkwisactive = obj.get("kwkwisactive")
        # 父级分类ID用于构建分类层级结构

        if mcauthfield_parentid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.parentid = str(uuid.uuid4())
        # 排序顺序用于控制分类在列中的显示顺序

        if mcauthfield_skwkwortkwkworder["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.skwkwortkwkworder = obj.get("skwkwortkwkworder")
        # 模板数量可选统计属于该分类的消息模板数量可通过触发器或应用逻辑维护

        if mcauthfield_templatecount["mcauthchange"]:

            # IntegerField # 其他情况/待补充

            ins_table_busi.templatecount = obj.get("templatecount")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_messagetemplatecategkwkwory.objects.get(
            id=obj.get("_id_upd")
        )

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 分类名称

        if mcauthfield_name["mcauthchange"]:

            # CharField

            ins_table_busi.name = obj.get("name")
        # 分类描述

        if mcauthfield_description["mcauthchange"]:

            # TextField

            ins_table_busi.description = obj.get("description")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatedat = obj.get("updatedat")
        # 是否激活用于控制分类是否可用

        if mcauthfield_kwkwisactive["mcauthchange"]:

            # BooleanField

            ins_table_busi.kwkwisactive = obj.get("kwkwisactive")
        # 父级分类ID用于构建分类层级结构

        if mcauthfield_parentid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.parentid = str(uuid.uuid4())

            ins_table_busi.parentid = str(ins_table_busi.parentid)
        # 排序顺序用于控制分类在列中的显示顺序

        if mcauthfield_skwkwortkwkworder["mcauthchange"]:

            # CharField

            ins_table_busi.skwkwortkwkworder = obj.get("skwkwortkwkworder")
        # 模板数量可选统计属于该分类的消息模板数量可通过触发器或应用逻辑维护

        if mcauthfield_templatecount["mcauthchange"]:

            # IntegerField

            ins_table_busi.templatecount = obj.get("templatecount")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_messagetemplatecategkwkwory.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_messagetemplatecategkwkwory.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/messagetemplatecategkwkwory")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_messagetemplatetag(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 消息模板标签表 系统管理员(7895)

    if user_table_id == str(7895):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 消息模板ID关联字段指向消息模板的ID

        mcauthfield_templateid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 标签名称

        mcauthfield_tagname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 标签描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活用于控制标签是否可用

        mcauthfield_kwkwisactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 使用次数记录该标签被用于消息模板的次数

        mcauthfield_usagecount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者ID关联字段指向用户的ID

        mcauthfield_creatkwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 消息模板标签表 用户信息表(7864)

    if user_table_id == str(7864):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 消息模板ID关联字段指向消息模板的ID

        mcauthfield_templateid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 标签名称

        mcauthfield_tagname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 标签描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活用于控制标签是否可用

        mcauthfield_kwkwisactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 使用次数记录该标签被用于消息模板的次数

        mcauthfield_usagecount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者ID关联字段指向用户的ID

        mcauthfield_creatkwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_messagetemplatetag.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_messagetemplatetag().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_messagetemplatetag.objects.filter(**filter)
        else:
            records = mc_messagetemplatetag.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_messagetemplateedithkwkwistkwkwory_53212 = []
        for m in mc_messagetemplateedithkwkwistkwkwory.objects.all():
            mobj = m.toJson()
            data_mc_messagetemplateedithkwkwistkwkwory_53212.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("version"),
                }
            )
        data_mc_userinfo_53219 = []
        for m in mc_userinfo.objects.all():
            mobj = m.toJson()
            data_mc_userinfo_53219.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        return render(request, "config_busi/messagetemplatetag.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_messagetemplatetag()

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 消息模板ID关联字段指向消息模板的ID

        if mcauthfield_templateid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.templateid = obj.get("templateid")
        # 标签名称

        if mcauthfield_tagname["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.tagname = obj.get("tagname")
        # 标签描述

        if mcauthfield_description["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.description = obj.get("description")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatedat = obj.get("updatedat")
        # 是否激活用于控制标签是否可用

        if mcauthfield_kwkwisactive["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.kwkwisactive = obj.get("kwkwisactive")
        # 使用次数记录该标签被用于消息模板的次数

        if mcauthfield_usagecount["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.usagecount = obj.get("usagecount")
        # 创建者ID关联字段指向用户的ID

        if mcauthfield_creatkwkworid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.creatkwkworid = obj.get("creatkwkworid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_messagetemplatetag.objects.get(id=obj.get("_id_upd"))

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 消息模板ID关联字段指向消息模板的ID

        if mcauthfield_templateid["mcauthchange"]:

            # SelectField

            ins_table_busi.templateid = obj.get("templateid")
        # 标签名称

        if mcauthfield_tagname["mcauthchange"]:

            # CharField

            ins_table_busi.tagname = obj.get("tagname")
        # 标签描述

        if mcauthfield_description["mcauthchange"]:

            # TextField

            ins_table_busi.description = obj.get("description")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatedat = obj.get("updatedat")
        # 是否激活用于控制标签是否可用

        if mcauthfield_kwkwisactive["mcauthchange"]:

            # BooleanField

            ins_table_busi.kwkwisactive = obj.get("kwkwisactive")
        # 使用次数记录该标签被用于消息模板的次数

        if mcauthfield_usagecount["mcauthchange"]:

            # CharField

            ins_table_busi.usagecount = obj.get("usagecount")
        # 创建者ID关联字段指向用户的ID

        if mcauthfield_creatkwkworid["mcauthchange"]:

            # SelectField

            ins_table_busi.creatkwkworid = obj.get("creatkwkworid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_messagetemplatetag.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_messagetemplatetag.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/messagetemplatetag")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_userpermkwkwission(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 用户权限表 系统管理员(7895)

    if user_table_id == str(7895):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 权限ID

        mcauthfield_permkwkwissionid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 权限名称

        mcauthfield_permkwkwissionname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 权限描述

        mcauthfield_permkwkwissiondescription = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活

        mcauthfield_isactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否删除

        mcauthfield_isdeleted = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 角色名称关联字段

        mcauthfield_rolename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 用户权限表 用户信息表(7864)

    if user_table_id == str(7864):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 权限ID

        mcauthfield_permkwkwissionid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 权限名称

        mcauthfield_permkwkwissionname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 权限描述

        mcauthfield_permkwkwissiondescription = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活

        mcauthfield_isactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否删除

        mcauthfield_isdeleted = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 角色名称关联字段

        mcauthfield_rolename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_userpermkwkwission.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_userpermkwkwission().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_userpermkwkwission.objects.filter(**filter)
        else:
            records = mc_userpermkwkwission.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_userinfo_53228 = []
        for m in mc_userinfo.objects.all():
            mobj = m.toJson()
            data_mc_userinfo_53228.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("roleid"),
                }
            )
        return render(request, "config_busi/userpermkwkwission.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_userpermkwkwission()

        # 用户ID

        if mcauthfield_userid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.userid = str(uuid.uuid4())
        # 权限ID

        if mcauthfield_permkwkwissionid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.permkwkwissionid = str(uuid.uuid4())
        # 权限名称

        if mcauthfield_permkwkwissionname["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.permkwkwissionname = obj.get("permkwkwissionname")
        # 权限描述

        if mcauthfield_permkwkwissiondescription["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.permkwkwissiondescription = obj.get(
                "permkwkwissiondescription"
            )
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createtime = obj.get("createtime")
        # 更新时间

        if mcauthfield_updatetime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatetime = obj.get("updatetime")
        # 是否激活

        if mcauthfield_isactive["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.isactive = obj.get("isactive")
        # 是否删除

        if mcauthfield_isdeleted["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.isdeleted = obj.get("isdeleted")
        # 角色名称关联字段

        if mcauthfield_rolename["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.rolename = obj.get("rolename")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_userpermkwkwission.objects.get(id=obj.get("_id_upd"))

        # 用户ID

        if mcauthfield_userid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.userid = str(uuid.uuid4())

            ins_table_busi.userid = str(ins_table_busi.userid)
        # 权限ID

        if mcauthfield_permkwkwissionid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.permkwkwissionid = str(uuid.uuid4())

            ins_table_busi.permkwkwissionid = str(ins_table_busi.permkwkwissionid)
        # 权限名称

        if mcauthfield_permkwkwissionname["mcauthchange"]:

            # CharField

            ins_table_busi.permkwkwissionname = obj.get("permkwkwissionname")
        # 权限描述

        if mcauthfield_permkwkwissiondescription["mcauthchange"]:

            # TextField

            ins_table_busi.permkwkwissiondescription = obj.get(
                "permkwkwissiondescription"
            )
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createtime = obj.get("createtime")
        # 更新时间

        if mcauthfield_updatetime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatetime = obj.get("updatetime")
        # 是否激活

        if mcauthfield_isactive["mcauthchange"]:

            # BooleanField

            ins_table_busi.isactive = obj.get("isactive")
        # 是否删除

        if mcauthfield_isdeleted["mcauthchange"]:

            # BooleanField

            ins_table_busi.isdeleted = obj.get("isdeleted")
        # 角色名称关联字段

        if mcauthfield_rolename["mcauthchange"]:

            # SelectField

            ins_table_busi.rolename = obj.get("rolename")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_userpermkwkwission.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_userpermkwkwission.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/userpermkwkwission")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_systemconfig(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 系统配置表 系统管理员(7895)

    if user_table_id == str(7895):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 系统配置ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 配置名称

        mcauthfield_configname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 配置值

        mcauthfield_configvalue = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 配置描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活1为激活0为未激活

        mcauthfield_kwkwisactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者ID

        mcauthfield_creatkwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联系统ID

        mcauthfield_relatedsystemid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 系统配置表 用户信息表(7864)

    if user_table_id == str(7864):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 系统配置ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 配置名称

        mcauthfield_configname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 配置值

        mcauthfield_configvalue = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 配置描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活1为激活0为未激活

        mcauthfield_kwkwisactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者ID

        mcauthfield_creatkwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联系统ID

        mcauthfield_relatedsystemid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_systemconfig.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_systemconfig().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_systemconfig.objects.filter(**filter)
        else:
            records = mc_systemconfig.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_systemconfig_53237 = []
        for m in mc_systemconfig.objects.all():
            mobj = m.toJson()
            data_mc_systemconfig_53237.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("relatedsystemid"),
                }
            )
        return render(request, "config_busi/systemconfig.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_systemconfig()

        # 系统配置ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 配置名称

        if mcauthfield_configname["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.configname = obj.get("configname")
        # 配置值

        if mcauthfield_configvalue["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.configvalue = obj.get("configvalue")
        # 配置描述

        if mcauthfield_description["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.description = obj.get("description")
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createtime = obj.get("createtime")
        # 更新时间

        if mcauthfield_updatetime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatetime = obj.get("updatetime")
        # 是否激活1为激活0为未激活

        if mcauthfield_kwkwisactive["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.kwkwisactive = obj.get("kwkwisactive")
        # 创建者ID

        if mcauthfield_creatkwkworid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.creatkwkworid = str(uuid.uuid4())
        # 关联系统ID

        if mcauthfield_relatedsystemid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.relatedsystemid = obj.get("relatedsystemid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_systemconfig.objects.get(id=obj.get("_id_upd"))

        # 系统配置ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 配置名称

        if mcauthfield_configname["mcauthchange"]:

            # CharField

            ins_table_busi.configname = obj.get("configname")
        # 配置值

        if mcauthfield_configvalue["mcauthchange"]:

            # CharField

            ins_table_busi.configvalue = obj.get("configvalue")
        # 配置描述

        if mcauthfield_description["mcauthchange"]:

            # TextField

            ins_table_busi.description = obj.get("description")
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createtime = obj.get("createtime")
        # 更新时间

        if mcauthfield_updatetime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatetime = obj.get("updatetime")
        # 是否激活1为激活0为未激活

        if mcauthfield_kwkwisactive["mcauthchange"]:

            # BooleanField

            ins_table_busi.kwkwisactive = obj.get("kwkwisactive")
        # 创建者ID

        if mcauthfield_creatkwkworid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.creatkwkworid = str(uuid.uuid4())

            ins_table_busi.creatkwkworid = str(ins_table_busi.creatkwkworid)
        # 关联系统ID

        if mcauthfield_relatedsystemid["mcauthchange"]:

            # SelectField

            ins_table_busi.relatedsystemid = obj.get("relatedsystemid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_systemconfig.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_systemconfig.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/systemconfig")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_notkwkwificationpush(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 通知推送表 系统管理员(7895)

    if user_table_id == str(7895):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 平台ID关联字段指向平台的ID

        mcauthfield_platkwkwfkwkwormid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户ID关联字段指向用户的ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 消息内容

        mcauthfield_messagecontent = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 推送状态例如待推送、已推送、推送失败

        mcauthfield_pushstatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 推送时间

        mcauthfield_pushtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 重试次数

        mcauthfield_rekwkwtrycount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 失败原因

        mcauthfield_failrekwkwason = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 通知推送表 用户信息表(7864)

    if user_table_id == str(7864):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 平台ID关联字段指向平台的ID

        mcauthfield_platkwkwfkwkwormid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户ID关联字段指向用户的ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 消息内容

        mcauthfield_messagecontent = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 推送状态例如待推送、已推送、推送失败

        mcauthfield_pushstatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 推送时间

        mcauthfield_pushtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 重试次数

        mcauthfield_rekwkwtrycount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 失败原因

        mcauthfield_failrekwkwason = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_notkwkwificationpush.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_notkwkwificationpush().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_notkwkwificationpush.objects.filter(**filter)
        else:
            records = mc_notkwkwificationpush.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_platkwkwfkwkwormaccount_53239 = []
        for m in mc_platkwkwfkwkwormaccount.objects.all():
            mobj = m.toJson()
            data_mc_platkwkwfkwkwormaccount_53239.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("accountname"),
                }
            )
        data_mc_userinfo_53240 = []
        for m in mc_userinfo.objects.all():
            mobj = m.toJson()
            data_mc_userinfo_53240.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        return render(request, "config_busi/notkwkwificationpush.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_notkwkwificationpush()

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 平台ID关联字段指向平台的ID

        if mcauthfield_platkwkwfkwkwormid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.platkwkwfkwkwormid = obj.get("platkwkwfkwkwormid")
        # 用户ID关联字段指向用户的ID

        if mcauthfield_userid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.userid = obj.get("userid")
        # 消息内容

        if mcauthfield_messagecontent["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.messagecontent = obj.get("messagecontent")
        # 推送状态例如待推送、已推送、推送失败

        if mcauthfield_pushstatus["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.pushstatus = obj.get("pushstatus")
        # 推送时间

        if mcauthfield_pushtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.pushtime = obj.get("pushtime")
        # 重试次数

        if mcauthfield_rekwkwtrycount["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.rekwkwtrycount = obj.get("rekwkwtrycount")
        # 失败原因

        if mcauthfield_failrekwkwason["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.failrekwkwason = obj.get("failrekwkwason")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatedat = obj.get("updatedat")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_notkwkwificationpush.objects.get(id=obj.get("_id_upd"))

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 平台ID关联字段指向平台的ID

        if mcauthfield_platkwkwfkwkwormid["mcauthchange"]:

            # SelectField

            ins_table_busi.platkwkwfkwkwormid = obj.get("platkwkwfkwkwormid")
        # 用户ID关联字段指向用户的ID

        if mcauthfield_userid["mcauthchange"]:

            # SelectField

            ins_table_busi.userid = obj.get("userid")
        # 消息内容

        if mcauthfield_messagecontent["mcauthchange"]:

            # TextField

            ins_table_busi.messagecontent = obj.get("messagecontent")
        # 推送状态例如待推送、已推送、推送失败

        if mcauthfield_pushstatus["mcauthchange"]:

            # CharField

            ins_table_busi.pushstatus = obj.get("pushstatus")
        # 推送时间

        if mcauthfield_pushtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.pushtime = obj.get("pushtime")
        # 重试次数

        if mcauthfield_rekwkwtrycount["mcauthchange"]:

            # CharField

            ins_table_busi.rekwkwtrycount = obj.get("rekwkwtrycount")
        # 失败原因

        if mcauthfield_failrekwkwason["mcauthchange"]:

            # CharField

            ins_table_busi.failrekwkwason = obj.get("failrekwkwason")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatedat = obj.get("updatedat")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_notkwkwificationpush.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_notkwkwificationpush.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/notkwkwificationpush")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_messagequeue(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 消息队列表 系统管理员(7895)

    if user_table_id == str(7895):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 消息ID唯一标识

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 平台名称记录消息需要发送的平台如微信、微博等

        mcauthfield_platkwkwfkwkworm = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户ID接收消息的用户ID用于标识消息接收者

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 消息内容需要发送的具体消息内容

        mcauthfield_messagecontent = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 消息状态如待发送、发送中、已发送、发送失败等

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间消息加入队列的时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间消息状态最后一次更新的时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 重试次数如果消息发送失败记录重试的次数

        mcauthfield_rekwkwtrycount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 下一次重试时间如果消息发送失败记录下一次尝试发送的时间

        mcauthfield_nextrekwkwtrytime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 消息队列表 用户信息表(7864)

    if user_table_id == str(7864):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 消息ID唯一标识

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 平台名称记录消息需要发送的平台如微信、微博等

        mcauthfield_platkwkwfkwkworm = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户ID接收消息的用户ID用于标识消息接收者

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 消息内容需要发送的具体消息内容

        mcauthfield_messagecontent = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 消息状态如待发送、发送中、已发送、发送失败等

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间消息加入队列的时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间消息状态最后一次更新的时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 重试次数如果消息发送失败记录重试的次数

        mcauthfield_rekwkwtrycount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 下一次重试时间如果消息发送失败记录下一次尝试发送的时间

        mcauthfield_nextrekwkwtrytime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_messagequeue.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_messagequeue().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_messagequeue.objects.filter(**filter)
        else:
            records = mc_messagequeue.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/messagequeue.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_messagequeue()

        # 消息ID唯一标识

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 平台名称记录消息需要发送的平台如微信、微博等

        if mcauthfield_platkwkwfkwkworm["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.platkwkwfkwkworm = obj.get("platkwkwfkwkworm")
        # 用户ID接收消息的用户ID用于标识消息接收者

        if mcauthfield_userid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.userid = str(uuid.uuid4())
        # 消息内容需要发送的具体消息内容

        if mcauthfield_messagecontent["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.messagecontent = obj.get("messagecontent")
        # 消息状态如待发送、发送中、已发送、发送失败等

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        # 创建时间消息加入队列的时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间消息状态最后一次更新的时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatedat = obj.get("updatedat")
        # 重试次数如果消息发送失败记录重试的次数

        if mcauthfield_rekwkwtrycount["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.rekwkwtrycount = obj.get("rekwkwtrycount")
        # 下一次重试时间如果消息发送失败记录下一次尝试发送的时间

        if mcauthfield_nextrekwkwtrytime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.nextrekwkwtrytime = obj.get("nextrekwkwtrytime")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_messagequeue.objects.get(id=obj.get("_id_upd"))

        # 消息ID唯一标识

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 平台名称记录消息需要发送的平台如微信、微博等

        if mcauthfield_platkwkwfkwkworm["mcauthchange"]:

            # CharField

            ins_table_busi.platkwkwfkwkworm = obj.get("platkwkwfkwkworm")
        # 用户ID接收消息的用户ID用于标识消息接收者

        if mcauthfield_userid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.userid = str(uuid.uuid4())

            ins_table_busi.userid = str(ins_table_busi.userid)
        # 消息内容需要发送的具体消息内容

        if mcauthfield_messagecontent["mcauthchange"]:

            # TextField

            ins_table_busi.messagecontent = obj.get("messagecontent")
        # 消息状态如待发送、发送中、已发送、发送失败等

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        # 创建时间消息加入队列的时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间消息状态最后一次更新的时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatedat = obj.get("updatedat")
        # 重试次数如果消息发送失败记录重试的次数

        if mcauthfield_rekwkwtrycount["mcauthchange"]:

            # CharField

            ins_table_busi.rekwkwtrycount = obj.get("rekwkwtrycount")
        # 下一次重试时间如果消息发送失败记录下一次尝试发送的时间

        if mcauthfield_nextrekwkwtrytime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.nextrekwkwtrytime = obj.get("nextrekwkwtrytime")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_messagequeue.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_messagequeue.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/messagequeue")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_messagequeuestatus(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 消息队列状态表 系统管理员(7895)

    if user_table_id == str(7895):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 平台ID关联字段指向不同平台的唯一标识

        mcauthfield_platkwkwfkwkwormid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 消息ID关联字段指向具体消息的唯一标识

        mcauthfield_messageid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 状态如待发送、发送中、发送成功、发送失败

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 重试次数

        mcauthfield_rekwkwtrycount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 下一次重试时间

        mcauthfield_nextrekwkwtrytime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 错误信息如果发送失败记录失败原因

        mcauthfield_errkwkwormessage = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 消息队列状态表 用户信息表(7864)

    if user_table_id == str(7864):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 平台ID关联字段指向不同平台的唯一标识

        mcauthfield_platkwkwfkwkwormid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 消息ID关联字段指向具体消息的唯一标识

        mcauthfield_messageid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 状态如待发送、发送中、发送成功、发送失败

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 重试次数

        mcauthfield_rekwkwtrycount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 下一次重试时间

        mcauthfield_nextrekwkwtrytime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 错误信息如果发送失败记录失败原因

        mcauthfield_errkwkwormessage = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_messagequeuestatus.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_messagequeuestatus().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_messagequeuestatus.objects.filter(**filter)
        else:
            records = mc_messagequeuestatus.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_platkwkwfkwkwormaccount_53258 = []
        for m in mc_platkwkwfkwkwormaccount.objects.all():
            mobj = m.toJson()
            data_mc_platkwkwfkwkwormaccount_53258.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("accountname"),
                }
            )
        data_mc_messagesendreckwkword_53259 = []
        for m in mc_messagesendreckwkword.objects.all():
            mobj = m.toJson()
            data_mc_messagesendreckwkword_53259.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("sendtime"),
                }
            )
        return render(request, "config_busi/messagequeuestatus.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_messagequeuestatus()

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 平台ID关联字段指向不同平台的唯一标识

        if mcauthfield_platkwkwfkwkwormid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.platkwkwfkwkwormid = obj.get("platkwkwfkwkwormid")
        # 消息ID关联字段指向具体消息的唯一标识

        if mcauthfield_messageid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.messageid = obj.get("messageid")
        # 状态如待发送、发送中、发送成功、发送失败

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatedat = obj.get("updatedat")
        # 重试次数

        if mcauthfield_rekwkwtrycount["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.rekwkwtrycount = obj.get("rekwkwtrycount")
        # 下一次重试时间

        if mcauthfield_nextrekwkwtrytime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.nextrekwkwtrytime = obj.get("nextrekwkwtrytime")
        # 错误信息如果发送失败记录失败原因

        if mcauthfield_errkwkwormessage["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.errkwkwormessage = obj.get("errkwkwormessage")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_messagequeuestatus.objects.get(id=obj.get("_id_upd"))

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 平台ID关联字段指向不同平台的唯一标识

        if mcauthfield_platkwkwfkwkwormid["mcauthchange"]:

            # SelectField

            ins_table_busi.platkwkwfkwkwormid = obj.get("platkwkwfkwkwormid")
        # 消息ID关联字段指向具体消息的唯一标识

        if mcauthfield_messageid["mcauthchange"]:

            # SelectField

            ins_table_busi.messageid = obj.get("messageid")
        # 状态如待发送、发送中、发送成功、发送失败

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatedat = obj.get("updatedat")
        # 重试次数

        if mcauthfield_rekwkwtrycount["mcauthchange"]:

            # CharField

            ins_table_busi.rekwkwtrycount = obj.get("rekwkwtrycount")
        # 下一次重试时间

        if mcauthfield_nextrekwkwtrytime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.nextrekwkwtrytime = obj.get("nextrekwkwtrytime")
        # 错误信息如果发送失败记录失败原因

        if mcauthfield_errkwkwormessage["mcauthchange"]:

            # CharField

            ins_table_busi.errkwkwormessage = obj.get("errkwkwormessage")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_messagequeuestatus.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_messagequeuestatus.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/messagequeuestatus")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_messagerekwkwtryreckwkword(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 消息重试记录表 系统管理员(7895)

    if user_table_id == str(7895):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 消息ID关联消息的ID

        mcauthfield_messageid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 平台名称

        mcauthfield_platkwkwfkwkworm = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 目标用户ID

        mcauthfield_targetuserid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 消息内容

        mcauthfield_content = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 重试次数

        mcauthfield_rekwkwtrycount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 上次重试时间

        mcauthfield_lkwkwastrekwkwtrytime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 下一次重试时间

        mcauthfield_nextrekwkwtrytime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 消息状态如待发送、发送中、发送成功、发送失败

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 错误信息如果发送失败记录错误信息

        mcauthfield_errkwkworkwkwinfo = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 消息重试记录表 用户信息表(7864)

    if user_table_id == str(7864):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 消息ID关联消息的ID

        mcauthfield_messageid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 平台名称

        mcauthfield_platkwkwfkwkworm = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 目标用户ID

        mcauthfield_targetuserid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 消息内容

        mcauthfield_content = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 重试次数

        mcauthfield_rekwkwtrycount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 上次重试时间

        mcauthfield_lkwkwastrekwkwtrytime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 下一次重试时间

        mcauthfield_nextrekwkwtrytime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 消息状态如待发送、发送中、发送成功、发送失败

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 错误信息如果发送失败记录错误信息

        mcauthfield_errkwkworkwkwinfo = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_messagerekwkwtryreckwkword.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_messagerekwkwtryreckwkword().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_messagerekwkwtryreckwkword.objects.filter(**filter)
        else:
            records = mc_messagerekwkwtryreckwkword.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_messagesendreckwkword_53266 = []
        for m in mc_messagesendreckwkword.objects.all():
            mobj = m.toJson()
            data_mc_messagesendreckwkword_53266.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("sendtime"),
                }
            )
        return render(request, "config_busi/messagerekwkwtryreckwkword.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_messagerekwkwtryreckwkword()

        # 消息ID关联消息的ID

        if mcauthfield_messageid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.messageid = obj.get("messageid")
        # 平台名称

        if mcauthfield_platkwkwfkwkworm["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.platkwkwfkwkworm = obj.get("platkwkwfkwkworm")
        # 目标用户ID

        if mcauthfield_targetuserid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.targetuserid = str(uuid.uuid4())
        # 消息内容

        if mcauthfield_content["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.content = obj.get("content")
        # 重试次数

        if mcauthfield_rekwkwtrycount["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.rekwkwtrycount = obj.get("rekwkwtrycount")
        # 上次重试时间

        if mcauthfield_lkwkwastrekwkwtrytime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.lkwkwastrekwkwtrytime = obj.get("lkwkwastrekwkwtrytime")
        # 下一次重试时间

        if mcauthfield_nextrekwkwtrytime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.nextrekwkwtrytime = obj.get("nextrekwkwtrytime")
        # 消息状态如待发送、发送中、发送成功、发送失败

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        # 错误信息如果发送失败记录错误信息

        if mcauthfield_errkwkworkwkwinfo["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.errkwkworkwkwinfo = obj.get("errkwkworkwkwinfo")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_messagerekwkwtryreckwkword.objects.get(
            id=obj.get("_id_upd")
        )

        # 消息ID关联消息的ID

        if mcauthfield_messageid["mcauthchange"]:

            # SelectField

            ins_table_busi.messageid = obj.get("messageid")
        # 平台名称

        if mcauthfield_platkwkwfkwkworm["mcauthchange"]:

            # CharField

            ins_table_busi.platkwkwfkwkworm = obj.get("platkwkwfkwkworm")
        # 目标用户ID

        if mcauthfield_targetuserid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.targetuserid = str(uuid.uuid4())

            ins_table_busi.targetuserid = str(ins_table_busi.targetuserid)
        # 消息内容

        if mcauthfield_content["mcauthchange"]:

            # TextField

            ins_table_busi.content = obj.get("content")
        # 重试次数

        if mcauthfield_rekwkwtrycount["mcauthchange"]:

            # CharField

            ins_table_busi.rekwkwtrycount = obj.get("rekwkwtrycount")
        # 上次重试时间

        if mcauthfield_lkwkwastrekwkwtrytime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.lkwkwastrekwkwtrytime = obj.get("lkwkwastrekwkwtrytime")
        # 下一次重试时间

        if mcauthfield_nextrekwkwtrytime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.nextrekwkwtrytime = obj.get("nextrekwkwtrytime")
        # 消息状态如待发送、发送中、发送成功、发送失败

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        # 错误信息如果发送失败记录错误信息

        if mcauthfield_errkwkworkwkwinfo["mcauthchange"]:

            # CharField

            ins_table_busi.errkwkworkwkwinfo = obj.get("errkwkworkwkwinfo")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_messagerekwkwtryreckwkword.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_messagerekwkwtryreckwkword.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/messagerekwkwtryreckwkword")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_accountblacklkwkwist(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 账号黑名单表 系统管理员(7895)

    if user_table_id == str(7895):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 账号ID

        mcauthfield_accountid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 黑名单类型

        mcauthfield_blacklkwkwisttype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 加入黑名单原因

        mcauthfield_rekwkwason = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否有效用于标记黑名单记录是否仍然有效

        mcauthfield_kwkwisactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者ID

        mcauthfield_creatkwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 相关账号ID如果黑名单与特定操作或另一账号相关

        mcauthfield_relatedaccountid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 账号黑名单表 用户信息表(7864)

    if user_table_id == str(7864):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 账号ID

        mcauthfield_accountid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 黑名单类型

        mcauthfield_blacklkwkwisttype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 加入黑名单原因

        mcauthfield_rekwkwason = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否有效用于标记黑名单记录是否仍然有效

        mcauthfield_kwkwisactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者ID

        mcauthfield_creatkwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 相关账号ID如果黑名单与特定操作或另一账号相关

        mcauthfield_relatedaccountid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_accountblacklkwkwist.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_accountblacklkwkwist().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_accountblacklkwkwist.objects.filter(**filter)
        else:
            records = mc_accountblacklkwkwist.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/accountblacklkwkwist.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_accountblacklkwkwist()

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 账号ID

        if mcauthfield_accountid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.accountid = str(uuid.uuid4())
        # 黑名单类型

        if mcauthfield_blacklkwkwisttype["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.blacklkwkwisttype = obj.get("blacklkwkwisttype")
        # 加入黑名单原因

        if mcauthfield_rekwkwason["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.rekwkwason = obj.get("rekwkwason")
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createtime = obj.get("createtime")
        # 更新时间

        if mcauthfield_updatetime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatetime = obj.get("updatetime")
        # 是否有效用于标记黑名单记录是否仍然有效

        if mcauthfield_kwkwisactive["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.kwkwisactive = obj.get("kwkwisactive")
        # 创建者ID

        if mcauthfield_creatkwkworid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.creatkwkworid = str(uuid.uuid4())
        # 相关账号ID如果黑名单与特定操作或另一账号相关

        if mcauthfield_relatedaccountid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.relatedaccountid = str(uuid.uuid4())
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_accountblacklkwkwist.objects.get(id=obj.get("_id_upd"))

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 账号ID

        if mcauthfield_accountid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.accountid = str(uuid.uuid4())

            ins_table_busi.accountid = str(ins_table_busi.accountid)
        # 黑名单类型

        if mcauthfield_blacklkwkwisttype["mcauthchange"]:

            # CharField

            ins_table_busi.blacklkwkwisttype = obj.get("blacklkwkwisttype")
        # 加入黑名单原因

        if mcauthfield_rekwkwason["mcauthchange"]:

            # CharField

            ins_table_busi.rekwkwason = obj.get("rekwkwason")
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createtime = obj.get("createtime")
        # 更新时间

        if mcauthfield_updatetime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatetime = obj.get("updatetime")
        # 是否有效用于标记黑名单记录是否仍然有效

        if mcauthfield_kwkwisactive["mcauthchange"]:

            # BooleanField

            ins_table_busi.kwkwisactive = obj.get("kwkwisactive")
        # 创建者ID

        if mcauthfield_creatkwkworid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.creatkwkworid = str(uuid.uuid4())

            ins_table_busi.creatkwkworid = str(ins_table_busi.creatkwkworid)
        # 相关账号ID如果黑名单与特定操作或另一账号相关

        if mcauthfield_relatedaccountid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.relatedaccountid = str(uuid.uuid4())

            ins_table_busi.relatedaccountid = str(ins_table_busi.relatedaccountid)
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_accountblacklkwkwist.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_accountblacklkwkwist.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/accountblacklkwkwist")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_userfeedback(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 用户反馈表 系统管理员(7895)

    if user_table_id == str(7895):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户ID关联用户

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 反馈内容

        mcauthfield_feedbackcontent = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 反馈类型如建议、投诉、咨询等

        mcauthfield_feedbacktype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 反馈创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 反馈状态如待处理、已处理、已忽略等

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 回复内容

        mcauthfield_responsecontent = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 回复时间

        mcauthfield_responseat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否已解决是否

        mcauthfield_kwkwisresolved = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 用户反馈表 用户信息表(7864)

    if user_table_id == str(7864):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户ID关联用户

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 反馈内容

        mcauthfield_feedbackcontent = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 反馈类型如建议、投诉、咨询等

        mcauthfield_feedbacktype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 反馈创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 反馈状态如待处理、已处理、已忽略等

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 回复内容

        mcauthfield_responsecontent = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 回复时间

        mcauthfield_responseat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否已解决是否

        mcauthfield_kwkwisresolved = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_userfeedback.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_userfeedback().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_userfeedback.objects.filter(**filter)
        else:
            records = mc_userfeedback.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_userinfo_53285 = []
        for m in mc_userinfo.objects.all():
            mobj = m.toJson()
            data_mc_userinfo_53285.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        return render(request, "config_busi/userfeedback.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_userfeedback()

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 用户ID关联用户

        if mcauthfield_userid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.userid = obj.get("userid")
        # 反馈内容

        if mcauthfield_feedbackcontent["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.feedbackcontent = obj.get("feedbackcontent")
        # 反馈类型如建议、投诉、咨询等

        if mcauthfield_feedbacktype["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.feedbacktype = obj.get("feedbacktype")
        # 反馈创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createdat = obj.get("createdat")
        # 反馈状态如待处理、已处理、已忽略等

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        # 回复内容

        if mcauthfield_responsecontent["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.responsecontent = obj.get("responsecontent")
        # 回复时间

        if mcauthfield_responseat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.responseat = obj.get("responseat")
        # 是否已解决是否

        if mcauthfield_kwkwisresolved["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.kwkwisresolved = obj.get("kwkwisresolved")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_userfeedback.objects.get(id=obj.get("_id_upd"))

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 用户ID关联用户

        if mcauthfield_userid["mcauthchange"]:

            # SelectField

            ins_table_busi.userid = obj.get("userid")
        # 反馈内容

        if mcauthfield_feedbackcontent["mcauthchange"]:

            # TextField

            ins_table_busi.feedbackcontent = obj.get("feedbackcontent")
        # 反馈类型如建议、投诉、咨询等

        if mcauthfield_feedbacktype["mcauthchange"]:

            # TextField

            ins_table_busi.feedbacktype = obj.get("feedbacktype")
        # 反馈创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createdat = obj.get("createdat")
        # 反馈状态如待处理、已处理、已忽略等

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        # 回复内容

        if mcauthfield_responsecontent["mcauthchange"]:

            # TextField

            ins_table_busi.responsecontent = obj.get("responsecontent")
        # 回复时间

        if mcauthfield_responseat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.responseat = obj.get("responseat")
        # 是否已解决是否

        if mcauthfield_kwkwisresolved["mcauthchange"]:

            # BooleanField

            ins_table_busi.kwkwisresolved = obj.get("kwkwisresolved")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_userfeedback.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_userfeedback.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/userfeedback")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_accountsecuritylog(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 账号安全日志表 系统管理员(7895)

    if user_table_id == str(7895):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 日志ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 账号ID

        mcauthfield_accountid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 日志类型

        mcauthfield_logtype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 动作描述

        mcauthfield_action = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 地址

        mcauthfield_ipaddressip = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 时间戳

        mcauthfield_timestamp = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 结果状态

        mcauthfield_result = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 描述信息

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联账号ID

        mcauthfield_relatedaccountid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 账号安全日志表 用户信息表(7864)

    if user_table_id == str(7864):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 日志ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 账号ID

        mcauthfield_accountid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 日志类型

        mcauthfield_logtype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 动作描述

        mcauthfield_action = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 地址

        mcauthfield_ipaddressip = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 时间戳

        mcauthfield_timestamp = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 结果状态

        mcauthfield_result = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 描述信息

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联账号ID

        mcauthfield_relatedaccountid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_accountsecuritylog.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_accountsecuritylog().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_accountsecuritylog.objects.filter(**filter)
        else:
            records = mc_accountsecuritylog.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_platkwkwfkwkwormaccount_53301 = []
        for m in mc_platkwkwfkwkwormaccount.objects.all():
            mobj = m.toJson()
            data_mc_platkwkwfkwkwormaccount_53301.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("accountname"),
                }
            )
        return render(request, "config_busi/accountsecuritylog.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_accountsecuritylog()

        # 日志ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 账号ID

        if mcauthfield_accountid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.accountid = str(uuid.uuid4())
        # 日志类型

        if mcauthfield_logtype["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.logtype = obj.get("logtype")
        # 动作描述

        if mcauthfield_action["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.action = obj.get("action")
        # 地址

        if mcauthfield_ipaddressip["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.ipaddressip = obj.get("ipaddressip")
        # 时间戳

        if mcauthfield_timestamp["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.timestamp = obj.get("timestamp")
        # 结果状态

        if mcauthfield_result["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.result = obj.get("result")
        # 描述信息

        if mcauthfield_description["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.description = obj.get("description")
        # 关联账号ID

        if mcauthfield_relatedaccountid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.relatedaccountid = obj.get("relatedaccountid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_accountsecuritylog.objects.get(id=obj.get("_id_upd"))

        # 日志ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 账号ID

        if mcauthfield_accountid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.accountid = str(uuid.uuid4())

            ins_table_busi.accountid = str(ins_table_busi.accountid)
        # 日志类型

        if mcauthfield_logtype["mcauthchange"]:

            # CharField

            ins_table_busi.logtype = obj.get("logtype")
        # 动作描述

        if mcauthfield_action["mcauthchange"]:

            # TextField

            ins_table_busi.action = obj.get("action")
        # 地址

        if mcauthfield_ipaddressip["mcauthchange"]:

            # TextField

            ins_table_busi.ipaddressip = obj.get("ipaddressip")
        # 时间戳

        if mcauthfield_timestamp["mcauthchange"]:

            # DateTimeField

            ins_table_busi.timestamp = obj.get("timestamp")
        # 结果状态

        if mcauthfield_result["mcauthchange"]:

            # CharField

            ins_table_busi.result = obj.get("result")
        # 描述信息

        if mcauthfield_description["mcauthchange"]:

            # TextField

            ins_table_busi.description = obj.get("description")
        # 关联账号ID

        if mcauthfield_relatedaccountid["mcauthchange"]:

            # SelectField

            ins_table_busi.relatedaccountid = obj.get("relatedaccountid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_accountsecuritylog.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_accountsecuritylog.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/accountsecuritylog")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_messagetemplateedithkwkwistkwkwory(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 消息模板编辑历史表 系统管理员(7895)

    if user_table_id == str(7895):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 消息模板ID关联字段指向消息模板的ID

        mcauthfield_templateid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 编辑者ID关联字段指向用户的ID

        mcauthfield_editkwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 编辑时间

        mcauthfield_edittime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 编辑内容本次编辑的具体内容或变更

        mcauthfield_editcontent = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 版本号每次编辑递增

        mcauthfield_version = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 状态如有效、已删除等

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 备注编辑时的额外说明或备注信息

        mcauthfield_remark = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否为最新版本标识当前记录是否为该模板的最新编辑版本

        mcauthfield_kwkwislatest = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 消息模板编辑历史表 用户信息表(7864)

    if user_table_id == str(7864):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 消息模板ID关联字段指向消息模板的ID

        mcauthfield_templateid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 编辑者ID关联字段指向用户的ID

        mcauthfield_editkwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 编辑时间

        mcauthfield_edittime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 编辑内容本次编辑的具体内容或变更

        mcauthfield_editcontent = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 版本号每次编辑递增

        mcauthfield_version = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 状态如有效、已删除等

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 备注编辑时的额外说明或备注信息

        mcauthfield_remark = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否为最新版本标识当前记录是否为该模板的最新编辑版本

        mcauthfield_kwkwislatest = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_messagetemplateedithkwkwistkwkwory.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_messagetemplateedithkwkwistkwkwory().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_messagetemplateedithkwkwistkwkwory.objects.filter(**filter)
        else:
            records = mc_messagetemplateedithkwkwistkwkwory.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_messagetemplatecategkwkwory_53303 = []
        for m in mc_messagetemplatecategkwkwory.objects.all():
            mobj = m.toJson()
            data_mc_messagetemplatecategkwkwory_53303.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("name"),
                }
            )
        data_mc_userinfo_53304 = []
        for m in mc_userinfo.objects.all():
            mobj = m.toJson()
            data_mc_userinfo_53304.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        return render(
            request, "config_busi/messagetemplateedithkwkwistkwkwory.html", locals()
        )
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_messagetemplateedithkwkwistkwkwory()

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 消息模板ID关联字段指向消息模板的ID

        if mcauthfield_templateid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.templateid = obj.get("templateid")
        # 编辑者ID关联字段指向用户的ID

        if mcauthfield_editkwkworid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.editkwkworid = obj.get("editkwkworid")
        # 编辑时间

        if mcauthfield_edittime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.edittime = obj.get("edittime")
        # 编辑内容本次编辑的具体内容或变更

        if mcauthfield_editcontent["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.editcontent = obj.get("editcontent")
        # 版本号每次编辑递增

        if mcauthfield_version["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.version = obj.get("version")
        # 状态如有效、已删除等

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        # 备注编辑时的额外说明或备注信息

        if mcauthfield_remark["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.remark = obj.get("remark")
        # 是否为最新版本标识当前记录是否为该模板的最新编辑版本

        if mcauthfield_kwkwislatest["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.kwkwislatest = obj.get("kwkwislatest")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_messagetemplateedithkwkwistkwkwory.objects.get(
            id=obj.get("_id_upd")
        )

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 消息模板ID关联字段指向消息模板的ID

        if mcauthfield_templateid["mcauthchange"]:

            # SelectField

            ins_table_busi.templateid = obj.get("templateid")
        # 编辑者ID关联字段指向用户的ID

        if mcauthfield_editkwkworid["mcauthchange"]:

            # SelectField

            ins_table_busi.editkwkworid = obj.get("editkwkworid")
        # 编辑时间

        if mcauthfield_edittime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.edittime = obj.get("edittime")
        # 编辑内容本次编辑的具体内容或变更

        if mcauthfield_editcontent["mcauthchange"]:

            # TextField

            ins_table_busi.editcontent = obj.get("editcontent")
        # 版本号每次编辑递增

        if mcauthfield_version["mcauthchange"]:

            # CharField

            ins_table_busi.version = obj.get("version")
        # 状态如有效、已删除等

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        # 备注编辑时的额外说明或备注信息

        if mcauthfield_remark["mcauthchange"]:

            # CharField

            ins_table_busi.remark = obj.get("remark")
        # 是否为最新版本标识当前记录是否为该模板的最新编辑版本

        if mcauthfield_kwkwislatest["mcauthchange"]:

            # BooleanField

            ins_table_busi.kwkwislatest = obj.get("kwkwislatest")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_messagetemplateedithkwkwistkwkwory.objects.get(
            id=obj.get("_id")
        )
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_messagetemplateedithkwkwistkwkwory.objects.get(
            id=obj.get("_id")
        )
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/messagetemplateedithkwkwistkwkwory")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_messagetemplatereviewreckwkword(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 消息模板审核记录表 系统管理员(7895)

    if user_table_id == str(7895):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 消息模板ID关联消息模板

        mcauthfield_templateid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 审核者ID关联用户

        mcauthfield_reviewerid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 审核时间

        mcauthfield_reviewtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 审核状态如待审核、审核通过、审核拒绝

        mcauthfield_reviewstatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 审核意见

        mcauthfield_reviewcomment = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 记录创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 记录更新时间

        mcauthfield_updatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否删除逻辑删除标记

        mcauthfield_kwkwiskwkwdeleted = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 消息模板审核记录表 用户信息表(7864)

    if user_table_id == str(7864):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 消息模板ID关联消息模板

        mcauthfield_templateid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 审核者ID关联用户

        mcauthfield_reviewerid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 审核时间

        mcauthfield_reviewtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 审核状态如待审核、审核通过、审核拒绝

        mcauthfield_reviewstatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 审核意见

        mcauthfield_reviewcomment = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 记录创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 记录更新时间

        mcauthfield_updatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否删除逻辑删除标记

        mcauthfield_kwkwiskwkwdeleted = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_messagetemplatereviewreckwkword.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_messagetemplatereviewreckwkword().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_messagetemplatereviewreckwkword.objects.filter(**filter)
        else:
            records = mc_messagetemplatereviewreckwkword.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_messagetemplatecategkwkwory_53312 = []
        for m in mc_messagetemplatecategkwkwory.objects.all():
            mobj = m.toJson()
            data_mc_messagetemplatecategkwkwory_53312.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("name"),
                }
            )
        data_mc_userinfo_53313 = []
        for m in mc_userinfo.objects.all():
            mobj = m.toJson()
            data_mc_userinfo_53313.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        return render(
            request, "config_busi/messagetemplatereviewreckwkword.html", locals()
        )
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_messagetemplatereviewreckwkword()

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 消息模板ID关联消息模板

        if mcauthfield_templateid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.templateid = obj.get("templateid")
        # 审核者ID关联用户

        if mcauthfield_reviewerid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.reviewerid = obj.get("reviewerid")
        # 审核时间

        if mcauthfield_reviewtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.reviewtime = obj.get("reviewtime")
        # 审核状态如待审核、审核通过、审核拒绝

        if mcauthfield_reviewstatus["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.reviewstatus = obj.get("reviewstatus")
        # 审核意见

        if mcauthfield_reviewcomment["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.reviewcomment = obj.get("reviewcomment")
        # 记录创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createtime = obj.get("createtime")
        # 记录更新时间

        if mcauthfield_updatetime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatetime = obj.get("updatetime")
        # 是否删除逻辑删除标记

        if mcauthfield_kwkwiskwkwdeleted["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.kwkwiskwkwdeleted = obj.get("kwkwiskwkwdeleted")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_messagetemplatereviewreckwkword.objects.get(
            id=obj.get("_id_upd")
        )

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 消息模板ID关联消息模板

        if mcauthfield_templateid["mcauthchange"]:

            # SelectField

            ins_table_busi.templateid = obj.get("templateid")
        # 审核者ID关联用户

        if mcauthfield_reviewerid["mcauthchange"]:

            # SelectField

            ins_table_busi.reviewerid = obj.get("reviewerid")
        # 审核时间

        if mcauthfield_reviewtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.reviewtime = obj.get("reviewtime")
        # 审核状态如待审核、审核通过、审核拒绝

        if mcauthfield_reviewstatus["mcauthchange"]:

            # CharField

            ins_table_busi.reviewstatus = obj.get("reviewstatus")
        # 审核意见

        if mcauthfield_reviewcomment["mcauthchange"]:

            # CharField

            ins_table_busi.reviewcomment = obj.get("reviewcomment")
        # 记录创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createtime = obj.get("createtime")
        # 记录更新时间

        if mcauthfield_updatetime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatetime = obj.get("updatetime")
        # 是否删除逻辑删除标记

        if mcauthfield_kwkwiskwkwdeleted["mcauthchange"]:

            # BooleanField

            ins_table_busi.kwkwiskwkwdeleted = obj.get("kwkwiskwkwdeleted")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_messagetemplatereviewreckwkword.objects.get(
            id=obj.get("_id")
        )
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_messagetemplatereviewreckwkword.objects.get(
            id=obj.get("_id")
        )
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/messagetemplatereviewreckwkword")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_messagesendstrategy(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 消息发送策略表 系统管理员(7895)

    if user_table_id == str(7895):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 策略ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 策略名称

        mcauthfield_name = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 策略描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 平台类型

        mcauthfield_platkwkwfkwkworm = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 目标类型

        mcauthfield_targettype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 内容模板

        mcauthfield_contenttemplate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 计划类型如一次性、周期性

        mcauthfield_scheduletype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 开始时间

        mcauthfield_starttime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 结束时间

        mcauthfield_endtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户ID关联用户

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 状态如启用、禁用

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 消息发送策略表 用户信息表(7864)

    if user_table_id == str(7864):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 策略ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 策略名称

        mcauthfield_name = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 策略描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 平台类型

        mcauthfield_platkwkwfkwkworm = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 目标类型

        mcauthfield_targettype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 内容模板

        mcauthfield_contenttemplate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 计划类型如一次性、周期性

        mcauthfield_scheduletype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 开始时间

        mcauthfield_starttime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 结束时间

        mcauthfield_endtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户ID关联用户

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 状态如启用、禁用

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_messagesendstrategy.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_messagesendstrategy().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_messagesendstrategy.objects.filter(**filter)
        else:
            records = mc_messagesendstrategy.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_userinfo_53329 = []
        for m in mc_userinfo.objects.all():
            mobj = m.toJson()
            data_mc_userinfo_53329.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        return render(request, "config_busi/messagesendstrategy.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_messagesendstrategy()

        # 策略ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 策略名称

        if mcauthfield_name["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.name = obj.get("name")
        # 策略描述

        if mcauthfield_description["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.description = obj.get("description")
        # 平台类型

        if mcauthfield_platkwkwfkwkworm["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.platkwkwfkwkworm = obj.get("platkwkwfkwkworm")
        # 目标类型

        if mcauthfield_targettype["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.targettype = obj.get("targettype")
        # 内容模板

        if mcauthfield_contenttemplate["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.contenttemplate = obj.get("contenttemplate")
        # 计划类型如一次性、周期性

        if mcauthfield_scheduletype["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.scheduletype = obj.get("scheduletype")
        # 开始时间

        if mcauthfield_starttime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.starttime = obj.get("starttime")
        # 结束时间

        if mcauthfield_endtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.endtime = obj.get("endtime")
        # 用户ID关联用户

        if mcauthfield_userid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.userid = obj.get("userid")
        # 状态如启用、禁用

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatedat = obj.get("updatedat")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_messagesendstrategy.objects.get(id=obj.get("_id_upd"))

        # 策略ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 策略名称

        if mcauthfield_name["mcauthchange"]:

            # CharField

            ins_table_busi.name = obj.get("name")
        # 策略描述

        if mcauthfield_description["mcauthchange"]:

            # TextField

            ins_table_busi.description = obj.get("description")
        # 平台类型

        if mcauthfield_platkwkwfkwkworm["mcauthchange"]:

            # CharField

            ins_table_busi.platkwkwfkwkworm = obj.get("platkwkwfkwkworm")
        # 目标类型

        if mcauthfield_targettype["mcauthchange"]:

            # CharField

            ins_table_busi.targettype = obj.get("targettype")
        # 内容模板

        if mcauthfield_contenttemplate["mcauthchange"]:

            # TextField

            ins_table_busi.contenttemplate = obj.get("contenttemplate")
        # 计划类型如一次性、周期性

        if mcauthfield_scheduletype["mcauthchange"]:

            # CharField

            ins_table_busi.scheduletype = obj.get("scheduletype")
        # 开始时间

        if mcauthfield_starttime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.starttime = obj.get("starttime")
        # 结束时间

        if mcauthfield_endtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.endtime = obj.get("endtime")
        # 用户ID关联用户

        if mcauthfield_userid["mcauthchange"]:

            # SelectField

            ins_table_busi.userid = obj.get("userid")
        # 状态如启用、禁用

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatedat = obj.get("updatedat")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_messagesendstrategy.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_messagesendstrategy.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/messagesendstrategy")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_messagesendfrequencylimit(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 消息发送频率限制表 系统管理员(7895)

    if user_table_id == str(7895):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 平台ID关联到不同平台的用于区分不同平台的发送频率限制

        mcauthfield_platkwkwfkwkwormid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户ID关联到用户示该限制是针对哪个用户的

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 消息类型如文本、图片、视频等用于区分不同类型的消息发送频率

        mcauthfield_messagetype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最大发送次数在指定时间周期内允许的最大发送次数

        mcauthfield_maxsendcount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 时间周期如每天、每小时等示上述最大发送次数的时间范围

        mcauthfield_timeperiod = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 上次发送时间记录最后一次发送消息的时间用于计算下一次发送的时间

        mcauthfield_lkwkwastsendtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 重置时间时间周期的开始时间用于重置发送次数计数器

        mcauthfield_resettime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 状态如启用、禁用示该频率限制是否生效

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 备注用于记录该频率限制的其他相关信息或说明

        mcauthfield_kwkwnote = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 消息发送频率限制表 用户信息表(7864)

    if user_table_id == str(7864):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 平台ID关联到不同平台的用于区分不同平台的发送频率限制

        mcauthfield_platkwkwfkwkwormid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户ID关联到用户示该限制是针对哪个用户的

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 消息类型如文本、图片、视频等用于区分不同类型的消息发送频率

        mcauthfield_messagetype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最大发送次数在指定时间周期内允许的最大发送次数

        mcauthfield_maxsendcount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 时间周期如每天、每小时等示上述最大发送次数的时间范围

        mcauthfield_timeperiod = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 上次发送时间记录最后一次发送消息的时间用于计算下一次发送的时间

        mcauthfield_lkwkwastsendtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 重置时间时间周期的开始时间用于重置发送次数计数器

        mcauthfield_resettime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 状态如启用、禁用示该频率限制是否生效

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 备注用于记录该频率限制的其他相关信息或说明

        mcauthfield_kwkwnote = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_messagesendfrequencylimit.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_messagesendfrequencylimit().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_messagesendfrequencylimit.objects.filter(**filter)
        else:
            records = mc_messagesendfrequencylimit.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_platkwkwfkwkwormaccount_53334 = []
        for m in mc_platkwkwfkwkwormaccount.objects.all():
            mobj = m.toJson()
            data_mc_platkwkwfkwkwormaccount_53334.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("accountname"),
                }
            )
        data_mc_userinfo_53335 = []
        for m in mc_userinfo.objects.all():
            mobj = m.toJson()
            data_mc_userinfo_53335.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        return render(request, "config_busi/messagesendfrequencylimit.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_messagesendfrequencylimit()

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 平台ID关联到不同平台的用于区分不同平台的发送频率限制

        if mcauthfield_platkwkwfkwkwormid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.platkwkwfkwkwormid = obj.get("platkwkwfkwkwormid")
        # 用户ID关联到用户示该限制是针对哪个用户的

        if mcauthfield_userid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.userid = obj.get("userid")
        # 消息类型如文本、图片、视频等用于区分不同类型的消息发送频率

        if mcauthfield_messagetype["mcauthchange"]:

            # Save FileImageField 若上传了文件

            if "messagetype" in request.FILES:
                ins_table_busi.messagetype = request.FILES["messagetype"]
        # 最大发送次数在指定时间周期内允许的最大发送次数

        if mcauthfield_maxsendcount["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.maxsendcount = obj.get("maxsendcount")
        # 时间周期如每天、每小时等示上述最大发送次数的时间范围

        if mcauthfield_timeperiod["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.timeperiod = obj.get("timeperiod")
        # 上次发送时间记录最后一次发送消息的时间用于计算下一次发送的时间

        if mcauthfield_lkwkwastsendtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.lkwkwastsendtime = obj.get("lkwkwastsendtime")
        # 重置时间时间周期的开始时间用于重置发送次数计数器

        if mcauthfield_resettime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.resettime = obj.get("resettime")
        # 状态如启用、禁用示该频率限制是否生效

        if mcauthfield_status["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        # 备注用于记录该频率限制的其他相关信息或说明

        if mcauthfield_kwkwnote["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.kwkwnote = obj.get("kwkwnote")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_messagesendfrequencylimit.objects.get(id=obj.get("_id_upd"))

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 平台ID关联到不同平台的用于区分不同平台的发送频率限制

        if mcauthfield_platkwkwfkwkwormid["mcauthchange"]:

            # SelectField

            ins_table_busi.platkwkwfkwkwormid = obj.get("platkwkwfkwkwormid")
        # 用户ID关联到用户示该限制是针对哪个用户的

        if mcauthfield_userid["mcauthchange"]:

            # SelectField

            ins_table_busi.userid = obj.get("userid")
        # 消息类型如文本、图片、视频等用于区分不同类型的消息发送频率

        if mcauthfield_messagetype["mcauthchange"]:

            # Save File ImageField

            if "messagetype" in request.FILES:
                ins_table_busi.messagetype = request.FILES["messagetype"]
        # 最大发送次数在指定时间周期内允许的最大发送次数

        if mcauthfield_maxsendcount["mcauthchange"]:

            # DateTimeField

            ins_table_busi.maxsendcount = obj.get("maxsendcount")
        # 时间周期如每天、每小时等示上述最大发送次数的时间范围

        if mcauthfield_timeperiod["mcauthchange"]:

            # DateTimeField

            ins_table_busi.timeperiod = obj.get("timeperiod")
        # 上次发送时间记录最后一次发送消息的时间用于计算下一次发送的时间

        if mcauthfield_lkwkwastsendtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.lkwkwastsendtime = obj.get("lkwkwastsendtime")
        # 重置时间时间周期的开始时间用于重置发送次数计数器

        if mcauthfield_resettime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.resettime = obj.get("resettime")
        # 状态如启用、禁用示该频率限制是否生效

        if mcauthfield_status["mcauthchange"]:

            # BooleanField

            ins_table_busi.status = obj.get("status")
        # 备注用于记录该频率限制的其他相关信息或说明

        if mcauthfield_kwkwnote["mcauthchange"]:

            # CharField

            ins_table_busi.kwkwnote = obj.get("kwkwnote")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_messagesendfrequencylimit.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_messagesendfrequencylimit.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/messagesendfrequencylimit")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_messagesendprikwkwority(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 消息发送优先级表 系统管理员(7895)

    if user_table_id == str(7895):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 自增ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 优先级等级

        mcauthfield_prikwkworitylevel = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 优先级描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活

        mcauthfield_kwkwisactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 平台ID关联字段指向平台

        mcauthfield_platkwkwfkwkwormid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 消息类型ID关联字段指向消息类型

        mcauthfield_messagetypeid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 默认延迟时间秒

        mcauthfield_kwkwdefaultkwkwdelay = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最大重试次数

        mcauthfield_maxrekwkwtrycount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 消息发送优先级表 用户信息表(7864)

    if user_table_id == str(7864):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 自增ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 优先级等级

        mcauthfield_prikwkworitylevel = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 优先级描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活

        mcauthfield_kwkwisactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 平台ID关联字段指向平台

        mcauthfield_platkwkwfkwkwormid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 消息类型ID关联字段指向消息类型

        mcauthfield_messagetypeid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 默认延迟时间秒

        mcauthfield_kwkwdefaultkwkwdelay = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最大重试次数

        mcauthfield_maxrekwkwtrycount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_messagesendprikwkwority.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_messagesendprikwkwority().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_messagesendprikwkwority.objects.filter(**filter)
        else:
            records = mc_messagesendprikwkwority.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_platkwkwfkwkwormaccount_53349 = []
        for m in mc_platkwkwfkwkwormaccount.objects.all():
            mobj = m.toJson()
            data_mc_platkwkwfkwkwormaccount_53349.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("accountname"),
                }
            )
        data_mc_messagetemplatecategkwkwory_53350 = []
        for m in mc_messagetemplatecategkwkwory.objects.all():
            mobj = m.toJson()
            data_mc_messagetemplatecategkwkwory_53350.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("name"),
                }
            )
        return render(request, "config_busi/messagesendprikwkwority.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_messagesendprikwkwority()

        # 自增ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 优先级等级

        if mcauthfield_prikwkworitylevel["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.prikwkworitylevel = obj.get("prikwkworitylevel")
        # 优先级描述

        if mcauthfield_description["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.description = obj.get("description")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatedat = obj.get("updatedat")
        # 是否激活

        if mcauthfield_kwkwisactive["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.kwkwisactive = obj.get("kwkwisactive")
        # 平台ID关联字段指向平台

        if mcauthfield_platkwkwfkwkwormid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.platkwkwfkwkwormid = obj.get("platkwkwfkwkwormid")
        # 消息类型ID关联字段指向消息类型

        if mcauthfield_messagetypeid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.messagetypeid = obj.get("messagetypeid")
        # 默认延迟时间秒

        if mcauthfield_kwkwdefaultkwkwdelay["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.kwkwdefaultkwkwdelay = obj.get("kwkwdefaultkwkwdelay")
        # 最大重试次数

        if mcauthfield_maxrekwkwtrycount["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.maxrekwkwtrycount = obj.get("maxrekwkwtrycount")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_messagesendprikwkwority.objects.get(id=obj.get("_id_upd"))

        # 自增ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 优先级等级

        if mcauthfield_prikwkworitylevel["mcauthchange"]:

            # CharField

            ins_table_busi.prikwkworitylevel = obj.get("prikwkworitylevel")
        # 优先级描述

        if mcauthfield_description["mcauthchange"]:

            # TextField

            ins_table_busi.description = obj.get("description")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatedat = obj.get("updatedat")
        # 是否激活

        if mcauthfield_kwkwisactive["mcauthchange"]:

            # BooleanField

            ins_table_busi.kwkwisactive = obj.get("kwkwisactive")
        # 平台ID关联字段指向平台

        if mcauthfield_platkwkwfkwkwormid["mcauthchange"]:

            # SelectField

            ins_table_busi.platkwkwfkwkwormid = obj.get("platkwkwfkwkwormid")
        # 消息类型ID关联字段指向消息类型

        if mcauthfield_messagetypeid["mcauthchange"]:

            # SelectField

            ins_table_busi.messagetypeid = obj.get("messagetypeid")
        # 默认延迟时间秒

        if mcauthfield_kwkwdefaultkwkwdelay["mcauthchange"]:

            # DateTimeField

            ins_table_busi.kwkwdefaultkwkwdelay = obj.get("kwkwdefaultkwkwdelay")
        # 最大重试次数

        if mcauthfield_maxrekwkwtrycount["mcauthchange"]:

            # CharField

            ins_table_busi.maxrekwkwtrycount = obj.get("maxrekwkwtrycount")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_messagesendprikwkwority.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_messagesendprikwkwority.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/messagesendprikwkwority")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_messagetemplateusagestatkwkwistics(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 消息模板使用统计表 系统管理员(7895)

    if user_table_id == str(7895):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 消息模板ID

        mcauthfield_templateid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 使用次数

        mcauthfield_usagecount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后使用时间

        mcauthfield_lkwkwastusedtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 使用平台

        mcauthfield_platkwkwfkwkworm = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 状态

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 消息模板使用统计表 用户信息表(7864)

    if user_table_id == str(7864):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 消息模板ID

        mcauthfield_templateid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 使用次数

        mcauthfield_usagecount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后使用时间

        mcauthfield_lkwkwastusedtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 使用平台

        mcauthfield_platkwkwfkwkworm = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 状态

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_messagetemplateusagestatkwkwistics.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_messagetemplateusagestatkwkwistics().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_messagetemplateusagestatkwkwistics.objects.filter(**filter)
        else:
            records = mc_messagetemplateusagestatkwkwistics.objects.all()
        # 加载界面中下拉框所需数据

        return render(
            request, "config_busi/messagetemplateusagestatkwkwistics.html", locals()
        )
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_messagetemplateusagestatkwkwistics()

        # 消息模板ID

        if mcauthfield_templateid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.templateid = str(uuid.uuid4())
        # 使用次数

        if mcauthfield_usagecount["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.usagecount = obj.get("usagecount")
        # 最后使用时间

        if mcauthfield_lkwkwastusedtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.lkwkwastusedtime = obj.get("lkwkwastusedtime")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatedat = obj.get("updatedat")
        # 使用平台

        if mcauthfield_platkwkwfkwkworm["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.platkwkwfkwkworm = obj.get("platkwkwfkwkworm")
        # 用户ID

        if mcauthfield_userid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.userid = str(uuid.uuid4())
        # 状态

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_messagetemplateusagestatkwkwistics.objects.get(
            id=obj.get("_id_upd")
        )

        # 消息模板ID

        if mcauthfield_templateid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.templateid = str(uuid.uuid4())

            ins_table_busi.templateid = str(ins_table_busi.templateid)
        # 使用次数

        if mcauthfield_usagecount["mcauthchange"]:

            # CharField

            ins_table_busi.usagecount = obj.get("usagecount")
        # 最后使用时间

        if mcauthfield_lkwkwastusedtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.lkwkwastusedtime = obj.get("lkwkwastusedtime")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatedat = obj.get("updatedat")
        # 使用平台

        if mcauthfield_platkwkwfkwkworm["mcauthchange"]:

            # CharField

            ins_table_busi.platkwkwfkwkworm = obj.get("platkwkwfkwkworm")
        # 用户ID

        if mcauthfield_userid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.userid = str(uuid.uuid4())

            ins_table_busi.userid = str(ins_table_busi.userid)
        # 状态

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_messagetemplateusagestatkwkwistics.objects.get(
            id=obj.get("_id")
        )
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_messagetemplateusagestatkwkwistics.objects.get(
            id=obj.get("_id")
        )
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/messagetemplateusagestatkwkwistics")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_supermanager(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 系统管理员 系统管理员(7895)

    if user_table_id == str(7895):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 管理员姓名

        mcauthfield_username = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 系统管理员 用户信息表(7864)

    if user_table_id == str(7864):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 管理员姓名

        mcauthfield_username = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_supermanager.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_supermanager().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_supermanager.objects.filter(**filter)
        else:
            records = mc_supermanager.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/supermanager.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_supermanager()

        # 管理员姓名

        if mcauthfield_username["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.username = obj.get("username")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_supermanager.objects.get(id=obj.get("_id_upd"))

        # 管理员姓名

        if mcauthfield_username["mcauthchange"]:

            # CharField

            ins_table_busi.username = obj.get("username")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_supermanager.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_supermanager.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/supermanager")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


def auto_detect(request):
    if request.method == "GET":
        detect = False

        return render(request, "config_algorithm/auto_detect.html", locals())
    obj = mydict(request.POST)

    if "img" not in request.FILES:
        return HttpResponse("请上传图片")
    img = request.FILES["img"]
    # mc_

    detect = True

    detect_result = "算法结果展示"

    # 保存提交的内容
    # 保存分析的结果
    # 若源码中缺少需要的表和字段.联系 qq952934650

    return render(request, "config_algorithm/auto_detect.html", locals())
