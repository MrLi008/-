from django.db import models


# Create your models here.


class MyModal(models.Model):
    class Meta:
        abstract = True

    def toParams(self):
        """
        遍历属性名
        :return:
        """
        return self._meta.fields

    def toImplement(self):
        """用于接口开发"""
        return "<br/>".join(
            [f"{field.name}, {field.verbose_name}" for field in self._meta.fields]
        )

    def toParams_zh(self):
        return [field.verbose_name for field in self._meta.fields]

    def toVue(self):
        res = {field.name: getattr(self, field.name, "") for field in self.toParams()}
        if res["id"] == "":
            del res["id"]
        return res

    def toValues(self):
        """
        遍历值
        :return:
        """
        return [getattr(self, field.name) for field in self._meta.fields]

    def toJson(self):
        return {
            field.name: value for field, value in zip(self.toParams(), self.toValues())
        }

    def toMeta(self):
        return {
            "table": {
                "mctablenameen": self._meta.db_table,
                "mctablenamezh": self._meta.verbose_name,
            },
            "field": self.toParams(),
            "field_count": len(self.toParams()),
        }


class mc_userinfo(MyModal):
    id = models.BigAutoField(primary_key=True)
    userid = models.CharField(
        max_length=200,
        verbose_name="用户ID唯一标识",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    username = models.CharField(
        verbose_name="用户名用户登录名或昵称",
        max_length=575,
        null=True,
        blank=True,
        unique=False,
    )
    pkwkwasswkwkwordhkwkwash = models.CharField(
        verbose_name="密码哈希存储加密后的密码",
        max_length=600,
        null=True,
        blank=True,
        unique=False,
    )
    email = models.TextField(
        verbose_name="电子邮件用户邮箱地址",
        null=True,
        blank=True,
        unique=False,
    )
    phonenumber = models.CharField(
        verbose_name="手机号码用户联系电话",
        max_length=715,
        null=True,
        blank=True,
        unique=False,
    )
    regkwkwistertime = models.DateTimeField(
        verbose_name="注册时间用户注册时的日期和时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    lkwkwastlogkwkwintime = models.DateTimeField(
        verbose_name="最后登录时间用户最后一次登录的日期和时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    status = models.CharField(
        verbose_name="用户状态如活跃、禁用等",
        max_length=500,
        null=True,
        blank=True,
        unique=False,
    )
    avatarurl = models.ImageField(
        verbose_name="头像URL用户头像图片的存储地址",
        upload_to="53074",
        null=True,
        blank=True,
        unique=False,
    )
    roleid = models.CharField(
        verbose_name="角色ID关联到角色的ID示用户所属的角色",
        max_length=655,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.avatarurl:
            res["avatarurl"] = {
                "name": self.avatarurl.name,
                "url": self.avatarurl.url,
            }
        else:
            res["avatarurl"] = None

        if self.userid:
            res["userid"] = str(self.userid)

        if self.regkwkwistertime:
            res["regkwkwistertime"] = str(self.regkwkwistertime)

        if self.lkwkwastlogkwkwintime:
            res["lkwkwastlogkwkwintime"] = str(self.lkwkwastlogkwkwintime)

        return res

    class Meta:
        managed = True
        db_table = "userinfo"
        verbose_name = "用户信息表"
        verbose_name_plural = verbose_name


class mc_platkwkwfkwkwormaccount(MyModal):
    id = models.BigAutoField(primary_key=True)
    platkwkwfkwkwormid = models.CharField(
        max_length=200,
        verbose_name="平台ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    accountname = models.CharField(
        verbose_name="账号名称",
        max_length=475,
        null=True,
        blank=True,
        unique=False,
    )
    accounttype = models.CharField(
        verbose_name="账号类型",
        max_length=595,
        null=True,
        blank=True,
        unique=False,
    )
    platkwkwfkwkwormname = models.CharField(
        verbose_name="所属平台名称",
        max_length=825,
        null=True,
        blank=True,
        unique=False,
    )
    username = models.CharField(
        verbose_name="用户名",
        max_length=740,
        null=True,
        blank=True,
        unique=False,
    )
    pkwkwasswkwkword = models.CharField(
        verbose_name="密码加密存储",
        max_length=990,
        null=True,
        blank=True,
        unique=False,
    )
    accesstoken = models.CharField(
        verbose_name="访问令牌",
        max_length=470,
        null=True,
        blank=True,
        unique=False,
    )
    status = models.CharField(
        verbose_name="账号状态如启用、禁用",
        max_length=475,
        null=True,
        blank=True,
        unique=False,
    )
    lkwkwastlogkwkwintime = models.DateTimeField(
        verbose_name="最后登录时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    createdat = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    updatedat = models.DateTimeField(
        verbose_name="更新时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    kwkwassociateduserid = models.CharField(
        verbose_name="关联用户ID如果有用户与账号关联",
        max_length=630,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.platkwkwfkwkwormid:
            res["platkwkwfkwkwormid"] = str(self.platkwkwfkwkwormid)

        if self.lkwkwastlogkwkwintime:
            res["lkwkwastlogkwkwintime"] = str(self.lkwkwastlogkwkwintime)

        if self.createdat:
            res["createdat"] = str(self.createdat)

        if self.updatedat:
            res["updatedat"] = str(self.updatedat)

        return res

    class Meta:
        managed = True
        db_table = "platkwkwfkwkwormaccount"
        verbose_name = "平台账号表"
        verbose_name_plural = verbose_name


class mc_messagetemplate(MyModal):
    id = models.BigAutoField(primary_key=True)
    templateid = models.CharField(
        max_length=200,
        verbose_name="模板ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    templatename = models.CharField(
        verbose_name="模板名称",
        max_length=930,
        null=True,
        blank=True,
        unique=False,
    )
    templatecontent = models.TextField(
        verbose_name="模板内容",
        null=True,
        blank=True,
        unique=False,
    )
    creatkwkworid = models.CharField(
        max_length=200,
        verbose_name="创建者ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    createtime = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    updatetime = models.DateTimeField(
        verbose_name="更新时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    kwkwisactive = models.BooleanField(
        verbose_name="是否激活",
        null=True,
        blank=True,
        unique=False,
    )
    platkwkwfkwkwormtype = models.CharField(
        verbose_name="平台类型",
        max_length=475,
        null=True,
        blank=True,
        unique=False,
    )
    targetuserid = models.CharField(
        max_length=200,
        verbose_name="目标用户ID可选用于指定特定用户",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.templateid:
            res["templateid"] = str(self.templateid)

        if self.creatkwkworid:
            res["creatkwkworid"] = str(self.creatkwkworid)

        if self.createtime:
            res["createtime"] = str(self.createtime)

        if self.updatetime:
            res["updatetime"] = str(self.updatetime)

        if self.targetuserid:
            res["targetuserid"] = str(self.targetuserid)

        return res

    class Meta:
        managed = True
        db_table = "messagetemplate"
        verbose_name = "私信模板表"
        verbose_name_plural = verbose_name


class mc_tkwkwaskmanagement(MyModal):
    id = models.BigAutoField(primary_key=True)
    tkwkwaskid = models.CharField(
        max_length=200,
        verbose_name="任务ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    tkwkwaskname = models.CharField(
        verbose_name="任务名称",
        max_length=770,
        null=True,
        blank=True,
        unique=False,
    )
    platkwkwfkwkworm = models.CharField(
        verbose_name="平台",
        max_length=985,
        null=True,
        blank=True,
        unique=False,
    )
    targetuserid = models.CharField(
        max_length=200,
        verbose_name="目标用户ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    messagecontent = models.TextField(
        verbose_name="私信内容",
        null=True,
        blank=True,
        unique=False,
    )
    scheduledtime = models.DateTimeField(
        verbose_name="计划执行时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    status = models.CharField(
        verbose_name="任务状态",
        max_length=755,
        null=True,
        blank=True,
        unique=False,
    )
    createdtime = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    updatedtime = models.DateTimeField(
        verbose_name="更新时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    kwkwassociateduserid = models.CharField(
        verbose_name="关联用户ID如任务创建者",
        max_length=765,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.tkwkwaskid:
            res["tkwkwaskid"] = str(self.tkwkwaskid)

        if self.targetuserid:
            res["targetuserid"] = str(self.targetuserid)

        if self.scheduledtime:
            res["scheduledtime"] = str(self.scheduledtime)

        if self.createdtime:
            res["createdtime"] = str(self.createdtime)

        if self.updatedtime:
            res["updatedtime"] = str(self.updatedtime)

        return res

    class Meta:
        managed = True
        db_table = "tkwkwaskmanagement"
        verbose_name = "任务管理表"
        verbose_name_plural = verbose_name


class mc_tkwkwaskexecutionreckwkword(MyModal):
    id = models.BigAutoField(primary_key=True)
    tkwkwaskid = models.CharField(
        max_length=200,
        verbose_name="任务ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    executiontime = models.DateTimeField(
        verbose_name="执行时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    status = models.CharField(
        verbose_name="执行状态",
        max_length=510,
        null=True,
        blank=True,
        unique=False,
    )
    userid = models.CharField(
        max_length=200,
        verbose_name="用户ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    platkwkwfkwkworm = models.CharField(
        verbose_name="平台",
        max_length=530,
        null=True,
        blank=True,
        unique=False,
    )
    messagecontent = models.TextField(
        verbose_name="私信内容",
        null=True,
        blank=True,
        unique=False,
    )
    recipientid = models.CharField(
        max_length=200,
        verbose_name="接收者ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    senderid = models.CharField(
        max_length=200,
        verbose_name="发送者ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    tkwkwasktemplateid = models.CharField(
        max_length=200,
        verbose_name="任务模板ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    errkwkwormessage = models.CharField(
        verbose_name="错误信息",
        max_length=515,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.tkwkwaskid:
            res["tkwkwaskid"] = str(self.tkwkwaskid)

        if self.executiontime:
            res["executiontime"] = str(self.executiontime)

        if self.userid:
            res["userid"] = str(self.userid)

        if self.recipientid:
            res["recipientid"] = str(self.recipientid)

        if self.senderid:
            res["senderid"] = str(self.senderid)

        if self.tkwkwasktemplateid:
            res["tkwkwasktemplateid"] = str(self.tkwkwasktemplateid)

        return res

    class Meta:
        managed = True
        db_table = "tkwkwaskexecutionreckwkword"
        verbose_name = "任务执行记录表"
        verbose_name_plural = verbose_name


class mc_tkwkwaskstatus(MyModal):
    id = models.BigAutoField(primary_key=True)
    tkwkwaskid = models.CharField(
        max_length=200,
        verbose_name="任务ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    statuscode = models.CharField(
        verbose_name="状态码",
        max_length=835,
        null=True,
        blank=True,
        unique=False,
    )
    statusname = models.CharField(
        verbose_name="状态名称",
        max_length=735,
        null=True,
        blank=True,
        unique=False,
    )
    createdat = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    updatedat = models.DateTimeField(
        verbose_name="更新时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    completedat = models.DateTimeField(
        verbose_name="完成时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    userid = models.CharField(
        max_length=200,
        verbose_name="用户ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    platkwkwfkwkwormid = models.CharField(
        max_length=200,
        verbose_name="平台ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    messagecontent = models.TextField(
        verbose_name="私信内容",
        null=True,
        blank=True,
        unique=False,
    )
    kwkwisactive = models.BooleanField(
        verbose_name="是否激活",
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.tkwkwaskid:
            res["tkwkwaskid"] = str(self.tkwkwaskid)

        if self.createdat:
            res["createdat"] = str(self.createdat)

        if self.updatedat:
            res["updatedat"] = str(self.updatedat)

        if self.completedat:
            res["completedat"] = str(self.completedat)

        if self.userid:
            res["userid"] = str(self.userid)

        if self.platkwkwfkwkwormid:
            res["platkwkwfkwkwormid"] = str(self.platkwkwfkwkwormid)

        return res

    class Meta:
        managed = True
        db_table = "tkwkwaskstatus"
        verbose_name = "任务状态表"
        verbose_name_plural = verbose_name


class mc_scheduledtkwkwask(MyModal):
    id = models.BigAutoField(primary_key=True)
    tkwkwaskid = models.CharField(
        max_length=200,
        verbose_name="任务ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    tkwkwaskname = models.CharField(
        verbose_name="任务名称",
        max_length=950,
        null=True,
        blank=True,
        unique=False,
    )
    targetplatkwkwfkwkworm = models.CharField(
        verbose_name="目标平台",
        max_length=890,
        null=True,
        blank=True,
        unique=False,
    )
    scheduletime = models.DateTimeField(
        verbose_name="计划执行时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    executestatus = models.CharField(
        verbose_name="执行状态",
        max_length=865,
        null=True,
        blank=True,
        unique=False,
    )
    lkwkwasterrkwkwor = models.CharField(
        verbose_name="最近一次错误信息",
        max_length=695,
        null=True,
        blank=True,
        unique=False,
    )
    creatkwkwor = models.CharField(
        verbose_name="创建者",
        max_length=525,
        null=True,
        blank=True,
        unique=False,
    )
    createtime = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    updatetime = models.DateTimeField(
        verbose_name="更新时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    relateduserid = models.CharField(
        verbose_name="关联用户ID",
        max_length=425,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.tkwkwaskid:
            res["tkwkwaskid"] = str(self.tkwkwaskid)

        if self.scheduletime:
            res["scheduletime"] = str(self.scheduletime)

        if self.createtime:
            res["createtime"] = str(self.createtime)

        if self.updatetime:
            res["updatetime"] = str(self.updatetime)

        return res

    class Meta:
        managed = True
        db_table = "scheduledtkwkwask"
        verbose_name = "定时任务表"
        verbose_name_plural = verbose_name


class mc_messagesendreckwkword(MyModal):
    id = models.BigAutoField(primary_key=True)
    platkwkwfkwkwormid = models.CharField(
        verbose_name="平台ID关联字段指向不同社交媒体或消息平台的ID",
        max_length=570,
        null=True,
        blank=True,
        unique=False,
    )
    userid = models.CharField(
        verbose_name="用户ID关联字段指向系统中用户的ID",
        max_length=660,
        null=True,
        blank=True,
        unique=False,
    )
    targetuserid = models.CharField(
        max_length=200,
        verbose_name="目标用户ID如果是私信则为目标接收者的ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    messagecontent = models.TextField(
        verbose_name="消息内容",
        null=True,
        blank=True,
        unique=False,
    )
    sendtime = models.DateTimeField(
        verbose_name="发送时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    status = models.CharField(
        verbose_name="发送状态如待发送、发送中、已发送、发送失败",
        max_length=450,
        null=True,
        blank=True,
        unique=False,
    )
    rekwkwtrycount = models.CharField(
        verbose_name="重试次数记录消息发送失败后的重试次数",
        max_length=935,
        null=True,
        blank=True,
        unique=False,
    )
    lkwkwastrekwkwtrytime = models.DateTimeField(
        verbose_name="上次重试时间记录最后一次尝试发送的时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    errkwkwormessage = models.CharField(
        verbose_name="错误信息如果发送失败记录失败的具体原因",
        max_length=925,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.id:
            res["id"] = str(self.id)

        if self.targetuserid:
            res["targetuserid"] = str(self.targetuserid)

        if self.sendtime:
            res["sendtime"] = str(self.sendtime)

        if self.lkwkwastrekwkwtrytime:
            res["lkwkwastrekwkwtrytime"] = str(self.lkwkwastrekwkwtrytime)

        return res

    class Meta:
        managed = True
        db_table = "messagesendreckwkword"
        verbose_name = "消息发送记录表"
        verbose_name_plural = verbose_name


class mc_messagereceivereckwkword(MyModal):
    id = models.BigAutoField(primary_key=True)
    userid = models.CharField(
        verbose_name="用户ID关联用户",
        max_length=480,
        null=True,
        blank=True,
        unique=False,
    )
    platkwkwfkwkwormid = models.CharField(
        verbose_name="平台ID关联平台",
        max_length=965,
        null=True,
        blank=True,
        unique=False,
    )
    messagecontent = models.TextField(
        verbose_name="消息内容",
        null=True,
        blank=True,
        unique=False,
    )
    receivetime = models.DateTimeField(
        verbose_name="接收时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    status = models.CharField(
        verbose_name="接收状态如已接收、未处理、已处理等",
        max_length=455,
        null=True,
        blank=True,
        unique=False,
    )
    responsecontent = models.TextField(
        verbose_name="回复内容",
        null=True,
        blank=True,
        unique=False,
    )
    responsetime = models.DateTimeField(
        verbose_name="回复时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    kwkwisread = models.BooleanField(
        verbose_name="是否已读示用户是否已读该消息",
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.id:
            res["id"] = str(self.id)

        if self.receivetime:
            res["receivetime"] = str(self.receivetime)

        if self.responsetime:
            res["responsetime"] = str(self.responsetime)

        return res

    class Meta:
        managed = True
        db_table = "messagereceivereckwkword"
        verbose_name = "消息接收记录表"
        verbose_name_plural = verbose_name


class mc_userpreference(MyModal):
    id = models.BigAutoField(primary_key=True)
    userid = models.CharField(
        max_length=200,
        verbose_name="用户ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    preferencename = models.CharField(
        verbose_name="偏好名称",
        max_length=430,
        null=True,
        blank=True,
        unique=False,
    )
    preferencevalue = models.CharField(
        verbose_name="偏好值",
        max_length=930,
        null=True,
        blank=True,
        unique=False,
    )
    preferencetype = models.CharField(
        verbose_name="偏好类型",
        max_length=745,
        null=True,
        blank=True,
        unique=False,
    )
    createtime = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    updatetime = models.DateTimeField(
        verbose_name="更新时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    kwkwisactive = models.BooleanField(
        verbose_name="是否激活",
        null=True,
        blank=True,
        unique=False,
    )
    description = models.TextField(
        verbose_name="偏好描述",
        null=True,
        blank=True,
        unique=False,
    )
    platkwkwfkwkwormid = models.CharField(
        verbose_name="关联平台ID",
        max_length=435,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.userid:
            res["userid"] = str(self.userid)

        if self.createtime:
            res["createtime"] = str(self.createtime)

        if self.updatetime:
            res["updatetime"] = str(self.updatetime)

        return res

    class Meta:
        managed = True
        db_table = "userpreference"
        verbose_name = "用户偏好设置表"
        verbose_name_plural = verbose_name


class mc_accountbkwkwindkwkwing(MyModal):
    id = models.BigAutoField(primary_key=True)
    accountid = models.CharField(
        max_length=200,
        verbose_name="账号ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    platkwkwfkwkwormid = models.CharField(
        max_length=200,
        verbose_name="平台ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    bkwkwindkwkwingtype = models.CharField(
        verbose_name="绑定类型",
        max_length=780,
        null=True,
        blank=True,
        unique=False,
    )
    bkwkwindkwkwingstatus = models.CharField(
        verbose_name="绑定状态",
        max_length=945,
        null=True,
        blank=True,
        unique=False,
    )
    createdat = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    updatedat = models.DateTimeField(
        verbose_name="更新时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    userid = models.CharField(
        max_length=200,
        verbose_name="用户ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.id:
            res["id"] = str(self.id)

        if self.accountid:
            res["accountid"] = str(self.accountid)

        if self.platkwkwfkwkwormid:
            res["platkwkwfkwkwormid"] = str(self.platkwkwfkwkwormid)

        if self.createdat:
            res["createdat"] = str(self.createdat)

        if self.updatedat:
            res["updatedat"] = str(self.updatedat)

        if self.userid:
            res["userid"] = str(self.userid)

        return res

    class Meta:
        managed = True
        db_table = "accountbkwkwindkwkwing"
        verbose_name = "账号绑定关系表"
        verbose_name_plural = verbose_name


class mc_messagecontentreview(MyModal):
    id = models.BigAutoField(primary_key=True)
    content = models.TextField(
        verbose_name="消息内容",
        null=True,
        blank=True,
        unique=False,
    )
    userid = models.CharField(
        max_length=200,
        verbose_name="用户ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    platkwkwfkwkworm = models.CharField(
        verbose_name="平台名称",
        max_length=720,
        null=True,
        blank=True,
        unique=False,
    )
    reviewstatus = models.CharField(
        verbose_name="审核状态",
        max_length=605,
        null=True,
        blank=True,
        unique=False,
    )
    reviewtime = models.DateTimeField(
        verbose_name="审核时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    reviewerid = models.CharField(
        max_length=200,
        verbose_name="审核员ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    rejectionrekwkwason = models.CharField(
        verbose_name="拒绝原因",
        max_length=825,
        null=True,
        blank=True,
        unique=False,
    )
    kwkwissensitive = models.TextField(
        verbose_name="是否敏感内容",
        null=True,
        blank=True,
        unique=False,
    )
    createdat = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.userid:
            res["userid"] = str(self.userid)

        if self.reviewtime:
            res["reviewtime"] = str(self.reviewtime)

        if self.reviewerid:
            res["reviewerid"] = str(self.reviewerid)

        if self.createdat:
            res["createdat"] = str(self.createdat)

        return res

    class Meta:
        managed = True
        db_table = "messagecontentreview"
        verbose_name = "消息内容审核表"
        verbose_name_plural = verbose_name


class mc_messagesendfailurelog(MyModal):
    id = models.BigAutoField(primary_key=True)
    messageid = models.CharField(
        max_length=200,
        verbose_name="消息ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    platkwkwfkwkworm = models.CharField(
        verbose_name="平台名称",
        max_length=945,
        null=True,
        blank=True,
        unique=False,
    )
    userid = models.CharField(
        max_length=200,
        verbose_name="用户ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    targetuserid = models.CharField(
        max_length=200,
        verbose_name="目标用户ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    sendtime = models.DateTimeField(
        verbose_name="发送时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    failurerekwkwason = models.CharField(
        verbose_name="失败原因",
        max_length=615,
        null=True,
        blank=True,
        unique=False,
    )
    rekwkwtrycount = models.CharField(
        verbose_name="重试次数",
        max_length=545,
        null=True,
        blank=True,
        unique=False,
    )
    lkwkwastrekwkwtrytime = models.DateTimeField(
        verbose_name="上次重试时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    kwkwisresolved = models.BooleanField(
        verbose_name="是否已解决",
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.id:
            res["id"] = str(self.id)

        if self.messageid:
            res["messageid"] = str(self.messageid)

        if self.userid:
            res["userid"] = str(self.userid)

        if self.targetuserid:
            res["targetuserid"] = str(self.targetuserid)

        if self.sendtime:
            res["sendtime"] = str(self.sendtime)

        if self.lkwkwastrekwkwtrytime:
            res["lkwkwastrekwkwtrytime"] = str(self.lkwkwastrekwkwtrytime)

        return res

    class Meta:
        managed = True
        db_table = "messagesendfailurelog"
        verbose_name = "消息发送失败日志表"
        verbose_name_plural = verbose_name


class mc_messagesendsuccesslog(MyModal):
    id = models.BigAutoField(primary_key=True)
    messageid = models.CharField(
        max_length=200,
        verbose_name="消息ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    platkwkwfkwkworm = models.CharField(
        verbose_name="平台名称",
        max_length=885,
        null=True,
        blank=True,
        unique=False,
    )
    userid = models.CharField(
        max_length=200,
        verbose_name="用户ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    receiverid = models.CharField(
        max_length=200,
        verbose_name="接收者ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    sendtime = models.DateTimeField(
        verbose_name="发送时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    content = models.TextField(
        verbose_name="发送内容",
        null=True,
        blank=True,
        unique=False,
    )
    status = models.CharField(
        verbose_name="发送状态",
        max_length=595,
        null=True,
        blank=True,
        unique=False,
    )
    errkwkworkwkwinfo = models.CharField(
        verbose_name="错误信息",
        max_length=975,
        null=True,
        blank=True,
        unique=False,
    )
    relatedtkwkwaskid = models.CharField(
        verbose_name="关联任务ID",
        max_length=725,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.messageid:
            res["messageid"] = str(self.messageid)

        if self.userid:
            res["userid"] = str(self.userid)

        if self.receiverid:
            res["receiverid"] = str(self.receiverid)

        if self.sendtime:
            res["sendtime"] = str(self.sendtime)

        return res

    class Meta:
        managed = True
        db_table = "messagesendsuccesslog"
        verbose_name = "消息发送成功日志表"
        verbose_name_plural = verbose_name


class mc_messagetemplatecategkwkwory(MyModal):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(
        verbose_name="分类名称",
        max_length=485,
        null=True,
        blank=True,
        unique=False,
    )
    description = models.TextField(
        verbose_name="分类描述",
        null=True,
        blank=True,
        unique=False,
    )
    createdat = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    updatedat = models.DateTimeField(
        verbose_name="更新时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    kwkwisactive = models.BooleanField(
        verbose_name="是否激活用于控制分类是否可用",
        null=True,
        blank=True,
        unique=False,
    )
    parentid = models.CharField(
        max_length=200,
        verbose_name="父级分类ID用于构建分类层级结构",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    skwkwortkwkworder = models.CharField(
        verbose_name="排序顺序用于控制分类在列中的显示顺序",
        max_length=690,
        null=True,
        blank=True,
        unique=False,
    )
    templatecount = models.IntegerField(
        verbose_name="模板数量可选统计属于该分类的消息模板数量可通过触发器或应用逻辑维护",
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.id:
            res["id"] = str(self.id)

        if self.createdat:
            res["createdat"] = str(self.createdat)

        if self.updatedat:
            res["updatedat"] = str(self.updatedat)

        if self.parentid:
            res["parentid"] = str(self.parentid)

        return res

    class Meta:
        managed = True
        db_table = "messagetemplatecategkwkwory"
        verbose_name = "消息模板分类表"
        verbose_name_plural = verbose_name


class mc_messagetemplatetag(MyModal):
    id = models.BigAutoField(primary_key=True)
    templateid = models.CharField(
        verbose_name="消息模板ID关联字段指向消息模板的ID",
        max_length=930,
        null=True,
        blank=True,
        unique=False,
    )
    tagname = models.CharField(
        verbose_name="标签名称",
        max_length=685,
        null=True,
        blank=True,
        unique=False,
    )
    description = models.TextField(
        verbose_name="标签描述",
        null=True,
        blank=True,
        unique=False,
    )
    createdat = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    updatedat = models.DateTimeField(
        verbose_name="更新时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    kwkwisactive = models.BooleanField(
        verbose_name="是否激活用于控制标签是否可用",
        null=True,
        blank=True,
        unique=False,
    )
    usagecount = models.CharField(
        verbose_name="使用次数记录该标签被用于消息模板的次数",
        max_length=430,
        null=True,
        blank=True,
        unique=False,
    )
    creatkwkworid = models.CharField(
        verbose_name="创建者ID关联字段指向用户的ID",
        max_length=880,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.id:
            res["id"] = str(self.id)

        if self.createdat:
            res["createdat"] = str(self.createdat)

        if self.updatedat:
            res["updatedat"] = str(self.updatedat)

        return res

    class Meta:
        managed = True
        db_table = "messagetemplatetag"
        verbose_name = "消息模板标签表"
        verbose_name_plural = verbose_name


class mc_userpermkwkwission(MyModal):
    id = models.BigAutoField(primary_key=True)
    userid = models.CharField(
        max_length=200,
        verbose_name="用户ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    permkwkwissionid = models.CharField(
        max_length=200,
        verbose_name="权限ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    permkwkwissionname = models.CharField(
        verbose_name="权限名称",
        max_length=585,
        null=True,
        blank=True,
        unique=False,
    )
    permkwkwissiondescription = models.TextField(
        verbose_name="权限描述",
        null=True,
        blank=True,
        unique=False,
    )
    createtime = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    updatetime = models.DateTimeField(
        verbose_name="更新时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    isactive = models.BooleanField(
        verbose_name="是否激活",
        null=True,
        blank=True,
        unique=False,
    )
    isdeleted = models.BooleanField(
        verbose_name="是否删除",
        null=True,
        blank=True,
        unique=False,
    )
    rolename = models.CharField(
        verbose_name="角色名称关联字段",
        max_length=815,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.userid:
            res["userid"] = str(self.userid)

        if self.permkwkwissionid:
            res["permkwkwissionid"] = str(self.permkwkwissionid)

        if self.createtime:
            res["createtime"] = str(self.createtime)

        if self.updatetime:
            res["updatetime"] = str(self.updatetime)

        return res

    class Meta:
        managed = True
        db_table = "userpermkwkwission"
        verbose_name = "用户权限表"
        verbose_name_plural = verbose_name


class mc_systemconfig(MyModal):
    id = models.BigAutoField(primary_key=True)
    configname = models.CharField(
        verbose_name="配置名称",
        max_length=515,
        null=True,
        blank=True,
        unique=False,
    )
    configvalue = models.CharField(
        verbose_name="配置值",
        max_length=735,
        null=True,
        blank=True,
        unique=False,
    )
    description = models.TextField(
        verbose_name="配置描述",
        null=True,
        blank=True,
        unique=False,
    )
    createtime = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    updatetime = models.DateTimeField(
        verbose_name="更新时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    kwkwisactive = models.BooleanField(
        verbose_name="是否激活1为激活0为未激活",
        null=True,
        blank=True,
        unique=False,
    )
    creatkwkworid = models.CharField(
        max_length=200,
        verbose_name="创建者ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    relatedsystemid = models.CharField(
        verbose_name="关联系统ID",
        max_length=990,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.id:
            res["id"] = str(self.id)

        if self.createtime:
            res["createtime"] = str(self.createtime)

        if self.updatetime:
            res["updatetime"] = str(self.updatetime)

        if self.creatkwkworid:
            res["creatkwkworid"] = str(self.creatkwkworid)

        return res

    class Meta:
        managed = True
        db_table = "systemconfig"
        verbose_name = "系统配置表"
        verbose_name_plural = verbose_name


class mc_notkwkwificationpush(MyModal):
    id = models.BigAutoField(primary_key=True)
    platkwkwfkwkwormid = models.CharField(
        verbose_name="平台ID关联字段指向平台的ID",
        max_length=840,
        null=True,
        blank=True,
        unique=False,
    )
    userid = models.CharField(
        verbose_name="用户ID关联字段指向用户的ID",
        max_length=695,
        null=True,
        blank=True,
        unique=False,
    )
    messagecontent = models.TextField(
        verbose_name="消息内容",
        null=True,
        blank=True,
        unique=False,
    )
    pushstatus = models.CharField(
        verbose_name="推送状态例如待推送、已推送、推送失败",
        max_length=495,
        null=True,
        blank=True,
        unique=False,
    )
    pushtime = models.DateTimeField(
        verbose_name="推送时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    rekwkwtrycount = models.CharField(
        verbose_name="重试次数",
        max_length=760,
        null=True,
        blank=True,
        unique=False,
    )
    failrekwkwason = models.CharField(
        verbose_name="失败原因",
        max_length=675,
        null=True,
        blank=True,
        unique=False,
    )
    createdat = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    updatedat = models.DateTimeField(
        verbose_name="更新时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.id:
            res["id"] = str(self.id)

        if self.pushtime:
            res["pushtime"] = str(self.pushtime)

        if self.createdat:
            res["createdat"] = str(self.createdat)

        if self.updatedat:
            res["updatedat"] = str(self.updatedat)

        return res

    class Meta:
        managed = True
        db_table = "notkwkwificationpush"
        verbose_name = "通知推送表"
        verbose_name_plural = verbose_name


class mc_messagequeue(MyModal):
    id = models.BigAutoField(primary_key=True)
    platkwkwfkwkworm = models.CharField(
        verbose_name="平台名称记录消息需要发送的平台如微信、微博等",
        max_length=950,
        null=True,
        blank=True,
        unique=False,
    )
    userid = models.CharField(
        max_length=200,
        verbose_name="用户ID接收消息的用户ID用于标识消息接收者",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    messagecontent = models.TextField(
        verbose_name="消息内容需要发送的具体消息内容",
        null=True,
        blank=True,
        unique=False,
    )
    status = models.CharField(
        verbose_name="消息状态如待发送、发送中、已发送、发送失败等",
        max_length=940,
        null=True,
        blank=True,
        unique=False,
    )
    createdat = models.DateTimeField(
        verbose_name="创建时间消息加入队列的时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    updatedat = models.DateTimeField(
        verbose_name="更新时间消息状态最后一次更新的时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    rekwkwtrycount = models.CharField(
        verbose_name="重试次数如果消息发送失败记录重试的次数",
        max_length=825,
        null=True,
        blank=True,
        unique=False,
    )
    nextrekwkwtrytime = models.DateTimeField(
        verbose_name="下一次重试时间如果消息发送失败记录下一次尝试发送的时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.id:
            res["id"] = str(self.id)

        if self.userid:
            res["userid"] = str(self.userid)

        if self.createdat:
            res["createdat"] = str(self.createdat)

        if self.updatedat:
            res["updatedat"] = str(self.updatedat)

        if self.nextrekwkwtrytime:
            res["nextrekwkwtrytime"] = str(self.nextrekwkwtrytime)

        return res

    class Meta:
        managed = True
        db_table = "messagequeue"
        verbose_name = "消息队列表"
        verbose_name_plural = verbose_name


class mc_messagequeuestatus(MyModal):
    id = models.BigAutoField(primary_key=True)
    platkwkwfkwkwormid = models.CharField(
        verbose_name="平台ID关联字段指向不同平台的唯一标识",
        max_length=755,
        null=True,
        blank=True,
        unique=False,
    )
    messageid = models.CharField(
        verbose_name="消息ID关联字段指向具体消息的唯一标识",
        max_length=590,
        null=True,
        blank=True,
        unique=False,
    )
    status = models.CharField(
        verbose_name="状态如待发送、发送中、发送成功、发送失败",
        max_length=765,
        null=True,
        blank=True,
        unique=False,
    )
    createdat = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    updatedat = models.DateTimeField(
        verbose_name="更新时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    rekwkwtrycount = models.CharField(
        verbose_name="重试次数",
        max_length=715,
        null=True,
        blank=True,
        unique=False,
    )
    nextrekwkwtrytime = models.DateTimeField(
        verbose_name="下一次重试时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    errkwkwormessage = models.CharField(
        verbose_name="错误信息如果发送失败记录失败原因",
        max_length=865,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.id:
            res["id"] = str(self.id)

        if self.createdat:
            res["createdat"] = str(self.createdat)

        if self.updatedat:
            res["updatedat"] = str(self.updatedat)

        if self.nextrekwkwtrytime:
            res["nextrekwkwtrytime"] = str(self.nextrekwkwtrytime)

        return res

    class Meta:
        managed = True
        db_table = "messagequeuestatus"
        verbose_name = "消息队列状态表"
        verbose_name_plural = verbose_name


class mc_messagerekwkwtryreckwkword(MyModal):
    id = models.BigAutoField(primary_key=True)
    messageid = models.CharField(
        verbose_name="消息ID关联消息的ID",
        max_length=490,
        null=True,
        blank=True,
        unique=False,
    )
    platkwkwfkwkworm = models.CharField(
        verbose_name="平台名称",
        max_length=600,
        null=True,
        blank=True,
        unique=False,
    )
    targetuserid = models.CharField(
        max_length=200,
        verbose_name="目标用户ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    content = models.TextField(
        verbose_name="消息内容",
        null=True,
        blank=True,
        unique=False,
    )
    rekwkwtrycount = models.CharField(
        verbose_name="重试次数",
        max_length=690,
        null=True,
        blank=True,
        unique=False,
    )
    lkwkwastrekwkwtrytime = models.DateTimeField(
        verbose_name="上次重试时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    nextrekwkwtrytime = models.DateTimeField(
        verbose_name="下一次重试时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    status = models.CharField(
        verbose_name="消息状态如待发送、发送中、发送成功、发送失败",
        max_length=485,
        null=True,
        blank=True,
        unique=False,
    )
    errkwkworkwkwinfo = models.CharField(
        verbose_name="错误信息如果发送失败记录错误信息",
        max_length=560,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.targetuserid:
            res["targetuserid"] = str(self.targetuserid)

        if self.lkwkwastrekwkwtrytime:
            res["lkwkwastrekwkwtrytime"] = str(self.lkwkwastrekwkwtrytime)

        if self.nextrekwkwtrytime:
            res["nextrekwkwtrytime"] = str(self.nextrekwkwtrytime)

        return res

    class Meta:
        managed = True
        db_table = "messagerekwkwtryreckwkword"
        verbose_name = "消息重试记录表"
        verbose_name_plural = verbose_name


class mc_accountblacklkwkwist(MyModal):
    id = models.BigAutoField(primary_key=True)
    accountid = models.CharField(
        max_length=200,
        verbose_name="账号ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    blacklkwkwisttype = models.CharField(
        verbose_name="黑名单类型",
        max_length=465,
        null=True,
        blank=True,
        unique=False,
    )
    rekwkwason = models.CharField(
        verbose_name="加入黑名单原因",
        max_length=820,
        null=True,
        blank=True,
        unique=False,
    )
    createtime = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    updatetime = models.DateTimeField(
        verbose_name="更新时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    kwkwisactive = models.BooleanField(
        verbose_name="是否有效用于标记黑名单记录是否仍然有效",
        null=True,
        blank=True,
        unique=False,
    )
    creatkwkworid = models.CharField(
        max_length=200,
        verbose_name="创建者ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    relatedaccountid = models.CharField(
        max_length=200,
        verbose_name="相关账号ID如果黑名单与特定操作或另一账号相关",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.id:
            res["id"] = str(self.id)

        if self.accountid:
            res["accountid"] = str(self.accountid)

        if self.createtime:
            res["createtime"] = str(self.createtime)

        if self.updatetime:
            res["updatetime"] = str(self.updatetime)

        if self.creatkwkworid:
            res["creatkwkworid"] = str(self.creatkwkworid)

        if self.relatedaccountid:
            res["relatedaccountid"] = str(self.relatedaccountid)

        return res

    class Meta:
        managed = True
        db_table = "accountblacklkwkwist"
        verbose_name = "账号黑名单表"
        verbose_name_plural = verbose_name


class mc_userfeedback(MyModal):
    id = models.BigAutoField(primary_key=True)
    userid = models.CharField(
        verbose_name="用户ID关联用户",
        max_length=500,
        null=True,
        blank=True,
        unique=False,
    )
    feedbackcontent = models.TextField(
        verbose_name="反馈内容",
        null=True,
        blank=True,
        unique=False,
    )
    feedbacktype = models.TextField(
        verbose_name="反馈类型如建议、投诉、咨询等",
        null=True,
        blank=True,
        unique=False,
    )
    createdat = models.DateTimeField(
        verbose_name="反馈创建时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    status = models.CharField(
        verbose_name="反馈状态如待处理、已处理、已忽略等",
        max_length=685,
        null=True,
        blank=True,
        unique=False,
    )
    responsecontent = models.TextField(
        verbose_name="回复内容",
        null=True,
        blank=True,
        unique=False,
    )
    responseat = models.DateTimeField(
        verbose_name="回复时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    kwkwisresolved = models.BooleanField(
        verbose_name="是否已解决是否",
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.id:
            res["id"] = str(self.id)

        if self.createdat:
            res["createdat"] = str(self.createdat)

        if self.responseat:
            res["responseat"] = str(self.responseat)

        return res

    class Meta:
        managed = True
        db_table = "userfeedback"
        verbose_name = "用户反馈表"
        verbose_name_plural = verbose_name


class mc_accountsecuritylog(MyModal):
    id = models.BigAutoField(primary_key=True)
    accountid = models.CharField(
        max_length=200,
        verbose_name="账号ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    logtype = models.CharField(
        verbose_name="日志类型",
        max_length=455,
        null=True,
        blank=True,
        unique=False,
    )
    action = models.TextField(
        verbose_name="动作描述",
        null=True,
        blank=True,
        unique=False,
    )
    ipaddressip = models.TextField(
        verbose_name="地址",
        null=True,
        blank=True,
        unique=False,
    )
    timestamp = models.DateTimeField(
        verbose_name="时间戳",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    result = models.CharField(
        verbose_name="结果状态",
        max_length=875,
        null=True,
        blank=True,
        unique=False,
    )
    description = models.TextField(
        verbose_name="描述信息",
        null=True,
        blank=True,
        unique=False,
    )
    relatedaccountid = models.CharField(
        verbose_name="关联账号ID",
        max_length=765,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.id:
            res["id"] = str(self.id)

        if self.accountid:
            res["accountid"] = str(self.accountid)

        if self.timestamp:
            res["timestamp"] = str(self.timestamp)

        return res

    class Meta:
        managed = True
        db_table = "accountsecuritylog"
        verbose_name = "账号安全日志表"
        verbose_name_plural = verbose_name


class mc_messagetemplateedithkwkwistkwkwory(MyModal):
    id = models.BigAutoField(primary_key=True)
    templateid = models.CharField(
        verbose_name="消息模板ID关联字段指向消息模板的ID",
        max_length=495,
        null=True,
        blank=True,
        unique=False,
    )
    editkwkworid = models.CharField(
        verbose_name="编辑者ID关联字段指向用户的ID",
        max_length=785,
        null=True,
        blank=True,
        unique=False,
    )
    edittime = models.DateTimeField(
        verbose_name="编辑时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    editcontent = models.TextField(
        verbose_name="编辑内容本次编辑的具体内容或变更",
        null=True,
        blank=True,
        unique=False,
    )
    version = models.CharField(
        verbose_name="版本号每次编辑递增",
        max_length=595,
        null=True,
        blank=True,
        unique=False,
    )
    status = models.CharField(
        verbose_name="状态如有效、已删除等",
        max_length=810,
        null=True,
        blank=True,
        unique=False,
    )
    remark = models.CharField(
        verbose_name="备注编辑时的额外说明或备注信息",
        max_length=610,
        null=True,
        blank=True,
        unique=False,
    )
    kwkwislatest = models.BooleanField(
        verbose_name="是否为最新版本标识当前记录是否为该模板的最新编辑版本",
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.id:
            res["id"] = str(self.id)

        if self.edittime:
            res["edittime"] = str(self.edittime)

        return res

    class Meta:
        managed = True
        db_table = "messagetemplateedithkwkwistkwkwory"
        verbose_name = "消息模板编辑历史表"
        verbose_name_plural = verbose_name


class mc_messagetemplatereviewreckwkword(MyModal):
    id = models.BigAutoField(primary_key=True)
    templateid = models.CharField(
        verbose_name="消息模板ID关联消息模板",
        max_length=610,
        null=True,
        blank=True,
        unique=False,
    )
    reviewerid = models.CharField(
        verbose_name="审核者ID关联用户",
        max_length=600,
        null=True,
        blank=True,
        unique=False,
    )
    reviewtime = models.DateTimeField(
        verbose_name="审核时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    reviewstatus = models.CharField(
        verbose_name="审核状态如待审核、审核通过、审核拒绝",
        max_length=825,
        null=True,
        blank=True,
        unique=False,
    )
    reviewcomment = models.CharField(
        verbose_name="审核意见",
        max_length=770,
        null=True,
        blank=True,
        unique=False,
    )
    createtime = models.DateTimeField(
        verbose_name="记录创建时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    updatetime = models.DateTimeField(
        verbose_name="记录更新时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    kwkwiskwkwdeleted = models.BooleanField(
        verbose_name="是否删除逻辑删除标记",
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.id:
            res["id"] = str(self.id)

        if self.reviewtime:
            res["reviewtime"] = str(self.reviewtime)

        if self.createtime:
            res["createtime"] = str(self.createtime)

        if self.updatetime:
            res["updatetime"] = str(self.updatetime)

        return res

    class Meta:
        managed = True
        db_table = "messagetemplatereviewreckwkword"
        verbose_name = "消息模板审核记录表"
        verbose_name_plural = verbose_name


class mc_messagesendstrategy(MyModal):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(
        verbose_name="策略名称",
        max_length=925,
        null=True,
        blank=True,
        unique=False,
    )
    description = models.TextField(
        verbose_name="策略描述",
        null=True,
        blank=True,
        unique=False,
    )
    platkwkwfkwkworm = models.CharField(
        verbose_name="平台类型",
        max_length=760,
        null=True,
        blank=True,
        unique=False,
    )
    targettype = models.CharField(
        verbose_name="目标类型",
        max_length=540,
        null=True,
        blank=True,
        unique=False,
    )
    contenttemplate = models.TextField(
        verbose_name="内容模板",
        null=True,
        blank=True,
        unique=False,
    )
    scheduletype = models.CharField(
        verbose_name="计划类型如一次性、周期性",
        max_length=935,
        null=True,
        blank=True,
        unique=False,
    )
    starttime = models.DateTimeField(
        verbose_name="开始时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    endtime = models.DateTimeField(
        verbose_name="结束时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    userid = models.CharField(
        verbose_name="用户ID关联用户",
        max_length=505,
        null=True,
        blank=True,
        unique=False,
    )
    status = models.CharField(
        verbose_name="状态如启用、禁用",
        max_length=520,
        null=True,
        blank=True,
        unique=False,
    )
    createdat = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    updatedat = models.DateTimeField(
        verbose_name="更新时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.id:
            res["id"] = str(self.id)

        if self.starttime:
            res["starttime"] = str(self.starttime)

        if self.endtime:
            res["endtime"] = str(self.endtime)

        if self.createdat:
            res["createdat"] = str(self.createdat)

        if self.updatedat:
            res["updatedat"] = str(self.updatedat)

        return res

    class Meta:
        managed = True
        db_table = "messagesendstrategy"
        verbose_name = "消息发送策略表"
        verbose_name_plural = verbose_name


class mc_messagesendfrequencylimit(MyModal):
    id = models.BigAutoField(primary_key=True)
    platkwkwfkwkwormid = models.CharField(
        verbose_name="平台ID关联到不同平台的用于区分不同平台的发送频率限制",
        max_length=700,
        null=True,
        blank=True,
        unique=False,
    )
    userid = models.CharField(
        verbose_name="用户ID关联到用户示该限制是针对哪个用户的",
        max_length=530,
        null=True,
        blank=True,
        unique=False,
    )
    messagetype = models.ImageField(
        verbose_name="消息类型如文本、图片、视频等用于区分不同类型的消息发送频率",
        upload_to="53336",
        null=True,
        blank=True,
        unique=False,
    )
    maxsendcount = models.DateTimeField(
        verbose_name="最大发送次数在指定时间周期内允许的最大发送次数",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    timeperiod = models.DateTimeField(
        verbose_name="时间周期如每天、每小时等示上述最大发送次数的时间范围",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    lkwkwastsendtime = models.DateTimeField(
        verbose_name="上次发送时间记录最后一次发送消息的时间用于计算下一次发送的时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    resettime = models.DateTimeField(
        verbose_name="重置时间时间周期的开始时间用于重置发送次数计数器",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    status = models.BooleanField(
        verbose_name="状态如启用、禁用示该频率限制是否生效",
        null=True,
        blank=True,
        unique=False,
    )
    kwkwnote = models.CharField(
        verbose_name="备注用于记录该频率限制的其他相关信息或说明",
        max_length=535,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.messagetype:
            res["messagetype"] = {
                "name": self.messagetype.name,
                "url": self.messagetype.url,
            }
        else:
            res["messagetype"] = None

        if self.id:
            res["id"] = str(self.id)

        if self.maxsendcount:
            res["maxsendcount"] = str(self.maxsendcount)

        if self.timeperiod:
            res["timeperiod"] = str(self.timeperiod)

        if self.lkwkwastsendtime:
            res["lkwkwastsendtime"] = str(self.lkwkwastsendtime)

        if self.resettime:
            res["resettime"] = str(self.resettime)

        return res

    class Meta:
        managed = True
        db_table = "messagesendfrequencylimit"
        verbose_name = "消息发送频率限制表"
        verbose_name_plural = verbose_name


class mc_messagesendprikwkwority(MyModal):
    id = models.BigAutoField(primary_key=True)
    prikwkworitylevel = models.CharField(
        verbose_name="优先级等级",
        max_length=440,
        null=True,
        blank=True,
        unique=False,
    )
    description = models.TextField(
        verbose_name="优先级描述",
        null=True,
        blank=True,
        unique=False,
    )
    createdat = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    updatedat = models.DateTimeField(
        verbose_name="更新时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    kwkwisactive = models.BooleanField(
        verbose_name="是否激活",
        null=True,
        blank=True,
        unique=False,
    )
    platkwkwfkwkwormid = models.CharField(
        verbose_name="平台ID关联字段指向平台",
        max_length=495,
        null=True,
        blank=True,
        unique=False,
    )
    messagetypeid = models.CharField(
        verbose_name="消息类型ID关联字段指向消息类型",
        max_length=760,
        null=True,
        blank=True,
        unique=False,
    )
    kwkwdefaultkwkwdelay = models.DateTimeField(
        verbose_name="默认延迟时间秒",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    maxrekwkwtrycount = models.CharField(
        verbose_name="最大重试次数",
        max_length=435,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.id:
            res["id"] = str(self.id)

        if self.createdat:
            res["createdat"] = str(self.createdat)

        if self.updatedat:
            res["updatedat"] = str(self.updatedat)

        if self.kwkwdefaultkwkwdelay:
            res["kwkwdefaultkwkwdelay"] = str(self.kwkwdefaultkwkwdelay)

        return res

    class Meta:
        managed = True
        db_table = "messagesendprikwkwority"
        verbose_name = "消息发送优先级表"
        verbose_name_plural = verbose_name


class mc_messagetemplateusagestatkwkwistics(MyModal):
    id = models.BigAutoField(primary_key=True)
    templateid = models.CharField(
        max_length=200,
        verbose_name="消息模板ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    usagecount = models.CharField(
        verbose_name="使用次数",
        max_length=525,
        null=True,
        blank=True,
        unique=False,
    )
    lkwkwastusedtime = models.DateTimeField(
        verbose_name="最后使用时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    createdat = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    updatedat = models.DateTimeField(
        verbose_name="更新时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    platkwkwfkwkworm = models.CharField(
        verbose_name="使用平台",
        max_length=830,
        null=True,
        blank=True,
        unique=False,
    )
    userid = models.CharField(
        max_length=200,
        verbose_name="用户ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    status = models.CharField(
        verbose_name="状态",
        max_length=460,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.templateid:
            res["templateid"] = str(self.templateid)

        if self.lkwkwastusedtime:
            res["lkwkwastusedtime"] = str(self.lkwkwastusedtime)

        if self.createdat:
            res["createdat"] = str(self.createdat)

        if self.updatedat:
            res["updatedat"] = str(self.updatedat)

        if self.userid:
            res["userid"] = str(self.userid)

        return res

    class Meta:
        managed = True
        db_table = "messagetemplateusagestatkwkwistics"
        verbose_name = "消息模板使用统计表"
        verbose_name_plural = verbose_name


class mc_supermanager(MyModal):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(
        verbose_name="管理员姓名",
        max_length=400,
        null=True,
        blank=True,
        unique=False,
    )

    class Meta:
        managed = True
        db_table = "supermanager"
        verbose_name = "系统管理员"
        verbose_name_plural = verbose_name
